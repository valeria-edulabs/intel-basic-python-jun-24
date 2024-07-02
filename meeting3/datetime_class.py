import datetime

# datetime.date.

today = datetime.datetime.now()
print(today)
# print(type(d))
# print(d.weekday())

bday = datetime.datetime(2025, 2, 11)
print(bday)

result = bday - today
print(type(result))
print(result)

past_bday = datetime.datetime(1987, 2, 11, 16, 30)
td = today - past_bday

print(today - past_bday)
# print(td.)

print(today + datetime.timedelta(days=10))

# datetime.timedelta()