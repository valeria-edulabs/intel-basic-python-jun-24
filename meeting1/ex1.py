minutes = input("Insert the movie length: ")
minutes = int(minutes)
# hours = minutes // 60
# minutes_left = minutes % 60
# print(hours, ":", minutes_left, sep="")
# print(f"{hours:02d}:{minutes_left:02d}")
h, m = divmod(minutes, 60)
result = divmod(minutes, 60)
# print(result[0])
# print(result, type(result))
print(f"{h:02d}:{m:02d}")