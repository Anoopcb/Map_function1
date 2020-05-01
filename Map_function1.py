## map() function



numbers = [1, 2, 3, 4]
#def square(a):
    #return  a**2

squares = list(map(lambda a: a**2, numbers))
print(squares)
## by list comprehension

squares1 = [i**2 for i in numbers]
print(squares1)


name =["abc", "abcd", "abcde"]
length = map(len, name)
for i in length:
    print(i)