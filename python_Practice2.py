#What is the score?
score = int(input("What is your test score?"))

#Determine the grade
if score >= 90:
    print("Your Grade is an A.")
elif score >= 80:
    print("your grade is a B.")
elif score >= 70:
    print("Your score is a C.")
elif score >= 60:
    print("Your score is a D")
else:
    print("Your score is an F. Loser.")