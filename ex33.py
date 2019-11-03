
def topbottom(min ,max, step=1):
    numbers = []
    for i in range(min, max, step):
        # print(f"At the top i is {i}")
        numbers.append(i)
        # print("numbers now:", numbers)
        # print(f"At the bottom i is {i}\n") 
    return numbers

print("the numbers:")
numbers = topbottom(1, 6)
for num in numbers:
    print(num)
