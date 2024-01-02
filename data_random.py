import random


class DataRandom:
    name = f"name{random.randint(1, 999)}"
    email = f"nelly{random.randint(1, 999)}@ya.ru"
    password = f"100{random.randint(100, 999)}"
    invalid_password = f"001{random.randint(10, 99)}"
