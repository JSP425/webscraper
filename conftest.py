import pytest
import random
import string

@pytest.fixture
def random_name():
    rName = "".join(random.choice(string.ascii_letters) for _ in range(10))
    return rName

@pytest.fixture
def random_number():
    num=random.random()
    # print(f"randomnum={num}")

    return num

@pytest.fixture
def random_choice(list):
    choice = random.choice(list)
    return choice

# print(random_name())