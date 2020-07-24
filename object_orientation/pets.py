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
    def create_without_details(cls, name):
        return cls(name, details={})

    @classmethod
    def create(cls, name, details):
        return cls(name, details)

    def __init__(self, name, details):
        self.name = name
        self.details = details
        self.identifier = self._create_id(
            name=name,
            identifier=Pets._generate_id()
        )


class PetOwner(Pets):

    @staticmethod
    def _create_id(name, identifier):
        return f'owner - {name} - {identifier}'


if __name__ == "__main__":
    dog1 = Pets("nega", {"color": "black"})
    dog2 = Pets.create("filo", {"color": "brown", "fur": "short"})
    dog3 = Pets.create_without_details('max')

    print(dog1.name, dog2.name, dog3.name)
    print(dog1.details, dog2.details, dog3.details)
    print(dog1.identifier, dog2.identifier, dog3.identifier)

    person = PetOwner('nega', 1)
    print(person.identifier)
