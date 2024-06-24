alice_path = "/Users/valeria/src/intel/intel-basic-python-jun-24/meeting2/data/alice_in_wonderland.txt"

# file_handler = open(alice_path, 'r', encoding="utf-8")
# print(file_handler)
#
# file_content = file_handler.read()
#
# # file_handler.close()
#
# print(file_content)

# with open(alice_path, 'r', encoding="utf-8") as file_handler:
#     file_content = file_handler.read()

# print(file_content)
# print(len(file_content), 'words:', len(file_content.split()))

with open(alice_path, 'r', encoding="utf-8") as file_handler:
    for line in file_handler:
        print(len(line))
    # file_content = file_handler.read(20)
    # print(file_content)
    # file_content = file_handler.read(20)
    # print(file_content)
    # c = file_handler.readline()
    # print(c)
    # c = file_handler.readline()
    # print(c)
    # c = file_handler.readline()
    # print(c)