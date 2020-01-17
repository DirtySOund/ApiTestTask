from faker import Faker

faker = Faker()


def random_user():
    return {
        "name": faker.first_name(),
        "salary": faker.pyint(min_value=100, max_value=10000, step=100),
        "age": faker.pyint(min_value=21, max_value=80, step=1),
    }
