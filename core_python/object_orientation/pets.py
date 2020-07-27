import uuid


class Pets:

    id = 0

    @classmethod
    def _generate_id(cls):
        cls.id += 1
        return cls.id

    @staticmethod
    def _create_id(name, identifier):
        return f'{name} - {identifier}'

    @classmethod
    def create_without_details(cls, name, **kwargs):
        return cls(name, details={}, **kwargs)

    @classmethod
    def create(cls, name, details, **kwargs):
        return cls(name, details, **kwargs)

    def __init__(self, name, details):
        self.name = name
        self.details = details
        self.identifier = self._create_id(
            name=name,
            identifier=Pets._generate_id()
        )


class PetOwner(Pets):

    def __init__(self, name, identifier, *, owner, **kwargs):
        super().__init__(name, identifier)
        self.owner = owner

    @property
    def owner(self):
        return self._owner

    @owner.setter
    def owner(self, owner):
        self._owner = PetOwner.check_owner(owner)

    @staticmethod
    def check_owner(owner):
        if not owner:
            raise ValueError('Hey! Needs a Owner')
        if type(owner) != str:
            raise ValueError('Hey! Owner Needs be a str')
        return owner

    @staticmethod
    def _create_id(*args, **kwargs):
        return str(uuid.uuid4())


if __name__ == "__main__":
    dog1 = Pets("nega", {"color": "black"})
    dog2 = Pets.create("filo", {"color": "brown", "fur": "short"})
    dog3 = Pets.create_without_details('max')

    print(dog1.name, dog1.details, dog1.identifier)
    print(dog2.name, dog2.details, dog2.identifier)
    print(dog3.name, dog3.details, dog3.identifier)

    po = PetOwner.create_without_details('dog', owner='me', identifier=1)
    print(po.identifier, po.owner)
