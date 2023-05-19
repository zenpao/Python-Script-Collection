#Day 3 Activitity1

StudName = str(input("Student Name: "))

markOne = int(input("\nMath Grade: "))
markTwo = int(input("Science Grade: "))
markThree = int(input("English Grade: "))

avg = round((markOne + markTwo + markThree) / 3)

if avg>=75 and markOne<=74 and markTwo>=75 and markThree>=75:
    print("\nStatus: Congratulations! You PASSED!")
    print("\nAdditional Condition(s): BUT, You have to re-enroll MATH subject!")
elif avg>=75 and markOne>=75 and markTwo<=74 and markThree>=75:
    print("\nStatus: Congratulations! You PASSED!")
    print("\nAdditional Condition(s): BUT, You have to re-enroll SCIENCE subject!")
elif avg>=75 and markOne>=75 and markTwo>=75 and markThree<=74:
    print("\nStatus: Congratulations! You PASSED!")
    print("\nAdditional Condition(s): BUT, You have to re-enroll ENGLISH subject!")
elif avg>=75 and markOne<=74 and markTwo<=74 and markThree>=75:
    print("\nStatus: Congratulations! You PASSED!")
    print("\nAdditional Condition(s): BUT, You have to re-enroll subjects of MATH and SCIENCE!")
elif avg>=75 and markOne<=74 and markTwo>=75 and markThree<=74:
    print("\nStatus: Congratulations! You PASSED!")
    print("\nAdditional Condition(s): BUT, You have to re-enroll the subjects of MATH and ENGLISH!")
elif avg>=75 and markOne>=75 and markTwo<=74 and markThree<=74:
    print("\nStatus: Congratulations! You PASSED!")
    print("\nAdditional Condition(s): BUT, You have to re-enroll the subjects of SCIENCE and ENGLISH!")
elif avg>=75 and markOne>=75 and markTwo>=75 and markThree>=75:
    print("\nStatus: Congratulations! You PASSED!")
    print("\nYou can enroll next semester without any concern!")
elif avg<=74:
    print("\nStatus: Apologies for you FAILED the semester!")