def square_number(number):
    squareNumber=[]
    for n in number:
        squareNumber.append(n*n)
    return squareNumber
number=[2,3,5,4,6,7,8]
num=square_number(number)
print(num)