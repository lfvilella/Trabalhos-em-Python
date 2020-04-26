# $ python3 -m pytest <file-name-or-nothing>
# Plugin HTML: $ python3 -m pytest <file-name-or-nothing> --html=report.html
from phonebook import PhoneBook
import pytest


@pytest.fixture
def phonebook(tmpdir):
    """ Provides a empty phonebook """
    phonebook = PhoneBook(tmpdir)
    return phonebook


def test_lookup_by_name(phonebook):
    phonebook.add('Luis', '12345')
    assert '12345' == phonebook.lookup('Luis')


def test_phonebook_contains_all_names(phonebook):
    phonebook.add('Luis', '12345')
    phonebook.add('Vilella', '9925')
    assert phonebook.names() == {'Vilella', 'Luis'}


# @pytest.mark.skip
def test_missing_name_raises_error(phonebook):
    with pytest.raises(KeyError):
        phonebook.lookup('Felipe')
