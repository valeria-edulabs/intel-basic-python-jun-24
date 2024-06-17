words_list = []
length = 0
words_num = int(input("Insert words num: "))
for i in range(1, words_num+1):
    word = input(f"Insert word number {i}:")
    words_list.append(word)
    length = length + len(word)
print(f"The words are: {words_list}, total length: {length}")

s1 = "apple"
s2 = 'apple'
s = 'app"lle'
s3 = f"""
Hello
Good bye
"""
print(s3)


