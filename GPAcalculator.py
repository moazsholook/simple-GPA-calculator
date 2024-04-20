creditvaltotal = 0
gradepointtotal = 0

//I take 5 courses a semester, I'm currently completing my 4th semester. I added an extra 5 iterations to see what grades I would need to get next semester to hit my target GPA. this number can be changed to fit however many courses you need. 
for i in range(25):
    creditvaltotal += float(input("Credit value: "))
    gradepointtotal += float(input("Gradepoint: "))

gpa = float(gradepointtotal/creditvaltotal)
print(gpa)
