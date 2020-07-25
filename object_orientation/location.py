import dataclasses
import inspect

import position


def auto_repr(cls):
    print(f"Decoratin {cls.__name__} with auto_repr")
    members = vars(cls)
    for name, member in members.items():
        print(name, member)

    if "__repr__" in members:
        raise TypeError(f"{cls.__name__} alredy defines __repr__")

    if "__init__" not in members:
        raise TypeError(f"{cls.__name__} does not override __init___")

    sig = inspect.signature(cls.__init__)
    parameter_names = list(sig.parameters)[1:]
    print("__init__ parameter names: ", parameter_names)

    if not all(
        isinstance(members.get(name, None), property)
        for name in parameter_names
    ):
        raise TypeError(
            f"Cannot apply auto_repr to {cls.__name__} because not all "
            "__init__ parameter have matching properties"
        )

    def synthesized_repr(self):
        return "{typename}({args})".format(
            typename=position.typename(self),
            args=", ".join(
                "{name}={value!r}".format(
                    name=name,
                    value=getattr(self, name)
                ) for name in parameter_names
            )
        )

    setattr(cls, "__repr__", synthesized_repr)

    return cls


@auto_repr
class Location:

    def __init__(self, name, position):
        self._name = name
        self._position = position

    @property
    def name(self):
        return self._name

    @property
    def position(self):
        return self._position

    def __str__(self):
        return self.name

    def __eq__(self, other):
        if not isinstance(other, type(self)):
            return NotImplemented
        return (self.name == other.name) and (self.position == other.position)

    def __hash__(self):
        return hash((self.name, self.position))


@dataclasses.dataclass(eq=True, frozen=True)
class Localization:
    name: str
    location: position.Position


if __name__ == '__main__':
    somewhere = Location('SOMEWHERE', position.EarthPosition(1.22, 44.5))
    print(somewhere.__repr__())

    sw2 = Localization('AnyWhere', position.Position(1.22, -55.22))
    sw3 = Localization('AnyWhere', position.Position(1.22, -55.22))
    cites = {sw2, sw3}
    print(cites)
