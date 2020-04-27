from sqlalchemy import *
from sqlalchemy.sql import select
import pytest


engine = create_engine('sqlite:///heroes.db')
CONECCTION = engine.connect()
metadata = MetaData()

HEROES_TABLE = Table('heroes', metadata,
    Column('hero_id', Integer, nullable=False, primary_key=True),
    Column('name', String(20), nullable=False, unique=True),
)

BATTLE_EVENTS_TABLE = Table('battle_events', metadata,
    Column('battle_event_id', Integer, nullable=False, primary_key=True),
    Column('battle_participant_id', Integer, nullable=False),
    Column('rubies_gained', Integer, nullable=False),
    Column('timestamp', Integer, nullable=False),
)


@pytest.mark.parametrize("query",
                          [(select([HEROES_TABLE])),
                            (select([HEROES_TABLE.columns.name])),
                            (select([HEROES_TABLE]).limit(5)),
                            (select([HEROES_TABLE]).offset(5)),
                            (select([HEROES_TABLE]).order_by(HEROES_TABLE.columns.name)),
                            (select([HEROES_TABLE]).offset(5).limit(5).order_by(HEROES_TABLE.columns.name)),
                            (select([HEROES_TABLE.columns.hero_id]).where(HEROES_TABLE.columns.name == 'Jade')),
                            (select([HEROES_TABLE.columns.name]).where(HEROES_TABLE.columns.name.like('A%'))),
                            ])
def test_simple_query(query):
    assert show_comands_on_db(query) == True


def test_sum_battle_events():
    query = select([func.sum(BATTLE_EVENTS_TABLE.columns.rubies_gained)])
    assert show_comands_on_db(query, battle_event=True) == 72847


def test_max_battle_events():
    query = select([func.max(BATTLE_EVENTS_TABLE.columns.rubies_gained)])
    assert show_comands_on_db(query, battle_event=True) == 15


def test_min_battle_events():
    query = select([func.min(BATTLE_EVENTS_TABLE.columns.rubies_gained)])
    assert show_comands_on_db(query, battle_event=True) == 1


def test_most_battle_events():
    query = select([
        BATTLE_EVENTS_TABLE.columns.battle_participant_id,\
        func.count(BATTLE_EVENTS_TABLE.columns.battle_event_id).label('total_events')
    ])\
    .group_by(BATTLE_EVENTS_TABLE.columns.battle_participant_id)\
    .order_by(Column('total_events').desc())
    assert show_comands_on_db(query) == True


def show_comands_on_db(query, battle_event=None):
    _assert = False
    results = CONECCTION.execute(query)

    if battle_event:
        return results.scalar()


    if results.fetchall():
        _assert = True

    return _assert
