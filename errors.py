# a = 1
# b = "2"
# c = 3
# print(int(2.5))
# print(str(a) + b)
# print(c/0)

# mylist = ["John", "Jack", "Jim"]
# print(mylist)

def divide(a,b):
    try:
        return a/b
    except ZeroDivisionError:
        return("Zero division is meaningless")

print(divide(1,0))
print("End of program")