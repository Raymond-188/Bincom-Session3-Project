# fibonacci series
n = int(input('Enter Any Number => '))
n1, n2 = 0, 1
sum_n = 0

if n <= 0:
    print("Please Enter Number Greater Than 0 ")
else:
    for i in range(0, n):
        print(sum_n, end='')
        n1 = n2
        n2 = sum_n
        sum_n = n1 + n2
