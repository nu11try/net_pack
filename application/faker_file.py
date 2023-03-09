from faker import Faker

fake = Faker()


class FakerTest:
    def __init__(self):
        self.__name = fake.name()
        self.__address = fake.address()

    def get_who(self):
        print(self.__name)

    def get_address(self):
        print(self.__address)
