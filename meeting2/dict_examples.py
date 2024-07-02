# my_dict = {
#     1: "jan",
#     2: "feb",
#     3: "mar",
#     "aaa": "123",
#     "b": True,
#     "c": [1, 20, 30],
# }

# print(my_dict)
# print(my_dict[1])
# print(my_dict["aaa"])

# my_dict["d"] = "Intel"
# print(my_dict)
# my_dict[1] = [10, 20, 30]
# print(my_dict)

stocks = {
    "AAPL": 250,
    "INTEL": 1000,
    "NVDA": 30,
    "TSLA": 200
}
#
# print(stocks["INTEL"])

person = {
    "id": 111111111,
    "first_name": "Valeria",
    "last_name": "Aynbinder",

}

print(person["last_name"])

persons = [
    {
        "id": 111111111,
        "first_name": "Valeria",
        "last_name": "Aynbinder",
    },
    {
        "id": 222222222,
        "first_name": "Yizhar",
        "last_name": "Peled",
    },
]

for p in persons:
    print(p["first_name"])


for i in range(0, len(persons)):
    print(persons[i]["first_name"])


new_persons = {
    111111111: {
        "first_name": "Valeria",
        "last_name": "Aynbinder",
        "year": 1987
    },
    222222222: {
        "first_name": "Yizhar",
        "last_name": "Peled",
        "year": 2005
    },
    333333333: {
        "first_name": "Sagi",
        "last_name": "Zeltzer",
        "year": 1994
    }
}

print(new_persons[222222222])
print(new_persons[222222222]["first_name"])

for person_id in new_persons:
    print(person_id, new_persons[person_id])

# l = "17:05:34".split(":")
# print(l)
# h, m, s = "17:05:34".split(":")
# print(m)

# a = (5, 6)
# b,c = a


for item in new_persons.items():
    print(item)

for key, value in new_persons.items():
    if value["year"] < 2000:
        print(value["first_name"])


new_stocks = {
    "APPL": {
        "company": {
            "addresses": {
                "USA": {
                    "AL": "dfgdfg",
                    "NY": "DFDfgdfg"
                },
                "Israel": {

                }
            },
            "CEO": {
                "name": "sddfg",
                "age": "dfgdfgh"
            }
        }
    }
}

print(111111111 in new_persons)


eq = {
    'eq1': [

    ]
}