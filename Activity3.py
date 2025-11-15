#Raj scored 40, 70, 50 and 60 out of 100 in maths, science, Hindi and English. Find the percentage he got?

# take marks as input from user
print("Enter Marks Obtained in 4 Subjects: ")
math = int(input("Maths : "))
english = int(input("English :"))
science = int(input("Science: "))
hindi = int(input("Hindi: "))

# Let's calculate the percentage of marks
sum = math+english+science+hindi
print("sum of math, english, science, and hindi")

perc = (sum/400)*100

print(end="Percentage Mark = ")
print(perc)
