Values = input("Input a Number Separated with Comma: ")
Input = Values.split(",")
total = 0

# for i in Input:
#     g = float(Input)
#     total += g**2

for i in range(len(Input)):
    Sum = float(Input[i])
    total += Sum * Sum

print("Total: " total)
