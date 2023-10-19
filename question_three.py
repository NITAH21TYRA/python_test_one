#NUMBER 3 (i)
#student_marks = [78,83,90,88,75]
def student_marks(a,b,c,d,e):
    output = (a+b+c+d+e)
    print(f"The sum of the items in the list is {output}.")
student_marks(78,83,90,88,75)

#(ii)
student_marks = [78,83,90,88,75]
newList=student_marks[0::4]
print(newList)


#(iii)
#Adding 96 to the list
student_marks = [78,83,90,88,75]
new_item = 96
student_marks.append(new_item)
print(student_marks)


#(iv)
#Updating 78 to 87
student_marks = [78,83,90,88,75]
new_list = student_marks.index(78)
new_list = student_marks(87)
print(student_marks)