#print  Patricia ,faith, phionah and anitah.(slicing)
#add Masha at the 4th position .
# update the name phionah to Phionah Aladinah.
#Display the length of the students lists.
#print all the students names using a for loop
# calculate the total marks for the students marks variable. ans 304


#solutions
student_name = ["sandra","Patricia","Phionah","Anitah"]#strings
student_marks=[80, 56,78,90]#integers

#appending (adding new items in the list.)
student_name.append("Michelle")
print(student_name)

# At a particular position
student_name.insert(2,"Faith")
print(student_name)

#Printing(Patricia, faith,phionah and Anitah.)
print(student_name[1])#patricia
print(student_name[2])#Faith
print(student_name[3])#Phionah
print(student_name[4])#Anitah

#adding masha to the 4th position
student_name.insert(3,"Masha")
print(student_name)

#updating the name Phionah to Phionah Aladinah.
student_name[student_name.index("Phionah")]="Phionah Aladinah"

#displaying the length
length = len(student_name)
print(length)



#printing the members in the list using a for loop.
for items in student_name:
    print(items)

#Total marks
total_marks = sum(student_marks)
print(total_marks)


