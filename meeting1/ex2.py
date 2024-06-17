input_num = input("Insert a number:")
# if input_num.isdigit() == False:
# if input_num.isdigit() != True:
if not input_num.isdigit():
    print("The input must be a digit")
elif len(input_num) != 1:
    print("Yhe input should be 1 digit")
else:
    num = int(input_num)
    for i in range(1, 11):
        # 1 x 5 = 5
        # 2 x 5 = 10
        print(f"{i} x {num} = {i*num}")