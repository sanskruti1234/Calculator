import math
import statistics
from itertools import permutations
from itertools import combinations


class calculator:
    def __init__(self):
        print("welcome to my Calculator")

    # function to addition two numbers
    def add(self,num1,num2):
        print(num1,"+",num2,'=',num1 + num2)

    # function to subtraction two numbers
    def sub(self,num1,num2):
        print(num1,"-",num2,"=",num1 - num2)

    # function to multiply two numbers
    def multiply(self,num1,num2):
        print(num1,"*",num2,"=",num1 * num2)

    # method to perform division of two numbers
    def division(self,num1,num2):
        print(num1, "/", num2, "=", num1 / num2)

    # method to perform floor division of two numbers
    def floor_division(self,num1,num2):
        print(num1, "//", num2, "=", num1 // num2)

    # method to perform AND operation
    def andOperation(self,num1,num2):
        print(num1,"AND",num2,"=",num1 and num2)

    # method to perform OR operation
    def orOperation(self,num1,num2):
        print(num1,"OR",num2,"=",num1 or num2)

    # method to perform NOR operation
    def NorOperation(self,num1,num2):
        if num1 == 1 and num2 == 1:
            print(num1,"NOR",num2,"=",0)
        elif num1 == 1 and num2 == 0:
            print(num1,"NOR",num2,"=",0)
        elif num1 == 0 and num2 == 1:
            print(num1,"NOR",num2,"=",0)
        elif num1 == 0 and num2 == 0:
            print(num1,"NOR",num2,"=",1)
        else:
            print("invaild number")


    #method to perform FACTORIAL of number
    def fact(self,num):
        print("factorial of",num,"=",math.factorial(num))

    # method to write fibonacci sequence for given number
    def fibonacci_series(self,n):
        a=0
        b=1
        print(a)
        for i in range(n):
            print(b)
            a,b = b,a+b

    # method to return permutations of given data
    def permutation(self,data):
        perm = permutations(data, 2)
        print("permutations are as:\n")
        for i in list(perm):
            print(i)

    # method to reverse the given integer
    def reverse(self,n):
        rev = 0
        while (n > 0):
            a = n % 10
            rev = rev * 10 + a
            n = n // 10

        print("Reverse of no:","is",rev)

    # method to return combinations of given data
    def combination(self,data):
        comb = combinations(data, 2)
        print("combinations are as:\n")
        for i in list(comb):
            print(i)

    # method to return mean,median,mode,variance
    # and standard deviation of given data
    def statistic(self,data):
        x = statistics.mean(data)
        print("Mean is",x,"\n")
        y = statistics.mode(data)
        print("Mode is",y,"\n")
        z = statistics.median(data)
        print("Median is",z,"\n")
        v = statistics.variance(data)
        print("variance is", v,"\n")
        std = statistics.sqrt(v)
        print("Standard Deviation is",std)


# Testing all operations of calculator

student = calculator()               # creating an object(student) of an calculator class

student.add(23,56)
student.sub(45,20)
student.multiply(3,10)
student.division(30,6)
student.floor_division(25,6)
student.andOperation(1,0)
student.orOperation(0,0)
student.NorOperation(0,0)
student.fact(3)
student.fibonacci_series(5)
student.reverse(2583)

data=[1,5,7,8,1,4]
student.permutation(data)
student.combination(data)
student.statistic(data)