
stars = "***"
def print_stars():
    print("********************")
    print("********************")
    print("********************")

# print(type(stars))
# print(type(print_stars))
# print(stars)

# print_stars()

# print_stars()
# print("INTEL")
# print_stars()

age = 10
def get_age(year, name):
    age = 2024-year
    print(f"{name}, you are {age} years old")
    return age, name.upper()

# print(year)
# year = int(input("Insert year: "))
# name = input("Insert name:")
# get_age(year, name)
# print(age)

persons = [
    {"name": "VAleria", "year": 1987},
    {"name": "yarden", "year": 2000}
]

def convert_dictionary(
        persons_list: list[dict[str, str | int]],
        how="c"):
    for person in persons_list:
        if how == "u":
            person["name"] = person["name"].upper()
        else:
            person["name"] = person["name"].capitalize()
        person["age"] = 2024 - person["year"]
    return persons_list

l = convert_dictionary(persons)
l = convert_dictionary(persons_list=persons, how="u")
print(l)

def sum_numbers(*nums):
    my_sum = 0
    for num in nums:
        my_sum += num
    return my_sum

sum_numbers(1,2,3,4,6,8,0)

print("hello", "world", sep="\n")

sum([2,3,4,56])

# a, b = get_age(1999, "fff")
# print(a)

