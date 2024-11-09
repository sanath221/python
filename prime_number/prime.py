def prime_checker(n):
    if (n%2!=0) or (n%3!=0) or (n%4!=0) or (n%5!=0) or (n%6!=0) or (n%7!=0) or (n%8!=0) or (n%9!=0):
        print(f"given number is prime number : {n}")
    else: 
        print(f"{n} is not a prime number")

num=int(input("enter the number to check if it is prime number or not :"))
prime_checker(n=num)