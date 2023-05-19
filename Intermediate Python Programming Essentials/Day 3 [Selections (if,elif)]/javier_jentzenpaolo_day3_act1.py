# inputs
name = str(input("Name: "))
mathGrade = float(input("Math: "))
scienceGrade = float(input("Science: "))
englishGrade = float(input("English: "))
average = round((mathGrade + scienceGrade + englishGrade) / 3)

# strings
subjMath = "Math"
subjScience = "Science"
subjEnglish = "English"
justAnd = "and"
displayPerfect = """
Congratulations! You passed the semester.
"""
displayPass1 = """
Congratulations! You passed the semester.
But you need to re-enroll {} subject.
"""
displayPass2 = """
Congratulations! You passed the semester.
But you need to re-enroll {} and {} 
subjects.
"""
displayFail = """
Sorry, you failed the semester.
"""

# grade checker
if mathGrade >= 75:
    mathGradeStatus = True
elif mathGrade <= 74:
    mathGradeStatus = False

if scienceGrade >= 75:
    scienceGradeStatus = True
elif scienceGrade <= 74:
    scienceGradeStatus = False

if englishGrade >= 75:
    englishGradeStatus = True
elif englishGrade <= 74:
    englishGradeStatus = False

# average checker
if average >= 75:
    if (mathGradeStatus == True) and (scienceGradeStatus == True) and (englishGradeStatus == True): #if all pass
        print(displayPerfect)
    elif (mathGradeStatus == False) and (scienceGradeStatus == True) and (englishGradeStatus == True): #if math only failed
        print(displayPass1.format(subjMath))
    elif (mathGradeStatus == True) and (scienceGradeStatus == False) and (englishGradeStatus == True): #if science only failed
        print(displayPass1.format(subjScience))
    elif (mathGradeStatus == True) and (scienceGradeStatus == True) and (englishGradeStatus == False): #if english only failed
        print(displayPass1.format(subjEnglish))
    elif (mathGradeStatus == False) and (scienceGradeStatus == False) and (englishGradeStatus == True): #if english passed
        print(displayPass2.format(subjMath, subjScience))
    elif (mathGradeStatus == True) and (scienceGradeStatus == False) and (englishGradeStatus == False): #if math only passed
        print(displayPass2.format(subjScience, subjEnglish))
    elif (mathGradeStatus == False) and (scienceGradeStatus == True) and (englishGradeStatus == False): #if science only passed
        print(displayPass2.format(subjMath, subjEnglish))
elif average <= 74: #if all fail OR the average did not meet 75
    print(displayFail)