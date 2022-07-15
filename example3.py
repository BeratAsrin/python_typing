from typing import NewType

name_of_customer = NewType("NameOfCustomer", str)


def get_name(full_name: name_of_customer) -> str:
    return full_name.split(" ")[0]


def get_surname(full_name: name_of_customer) -> str:
    return full_name.split(" ")[1]


customer = name_of_customer("Asrin CAFEROGLU")

print("Name of customer: " + get_name(customer))
print("Surname of customer: " + get_surname(customer))
