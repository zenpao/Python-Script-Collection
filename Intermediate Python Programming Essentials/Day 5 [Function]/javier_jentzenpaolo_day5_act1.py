def user(name, mathGrade, scienceGrade, englishGrade):
    averageGrade = round((mathGrade + scienceGrade + englishGrade) / 3)
    print(f"{name}'s grade (Math={mathGrade}, Science={scienceGrade}, English={englishGrade}) and the average is {averageGrade}")

user("John",89,89,75)
user("Ana",85,79,75)
user("Frank",84,98,75)