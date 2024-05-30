from faker import Faker


def get_names_to_file(count: int = 10) -> None:
    fake = Faker()
    with open('data/faker/names.csv') as file:
        for t in range(count):
            file.write(fake.name())
            file.write("\n")


range_100 = [t for t in range(100)]
