#QUESTION 2 (i)
def average_of_numbers(x,y):
    output= (x+y)/2
    print(output)
#Choosing 6 and 4 as numbers of my choice.
average_of_numbers(6,4)

#(ii)
#Let the three numbers be 70,55 and 85
a = 70
b = 55
c = 85
if a<b and a<c:
    print("{a} is the minimum number")
elif b<a and b<c:
    print(f"{b} is the minimum number")
else:
    print(f"{c} is the minimum number")


