import os

class PhilSysStep2DARCalculator:
    dar_list = [['RKO', 'ARN', 'ONLINE', 'WI', 'I-ARN', 'I-OL', 'I-WI', 'TOTAL']]
    age_list = [['Q', '5-14', '15-59', '60+', 'TOTAL']]
    bio_list = [['Q', 'F-05+', 'F-15+', 'F-60+', 'I-05+', 'I-15+', 'I-60+', 'TOTAL']]

    def addRKO(self, rkoCtr, assistedStep1, onlineRegistrant, walkinRegistrant, instAssistedStep1, instOnline, instWalkIn, totalRKO):
        # self.rkoCtr = rkoCtr
        # self.assistedStep1 = assistedStep1
        # self.onlineRegistrant = onlineRegistrant
        # self.walkinRegistrant = walkinRegistrant
        # self.instAssistedStep1 = instAssistedStep1
        # self.instOnline = instOnline
        # self.instWalkIn = instWalkIn
        self.dar_list.append([rkoCtr, assistedStep1, onlineRegistrant, walkinRegistrant, instAssistedStep1, instOnline, instWalkIn, totalRKO])

    def ageGroup(self, ageCtr, age_fivefourteen, age_fifteenfiftynine, age_sixtyplus, totalAge):
        # self.age_fivefourteen = age_fivefourteen
        # self.age_fifteenfiftynine = age_fifteenfiftynine
        # self.age_sixtyplus = age_sixtyplus
        self.age_list.append([ageCtr, age_fivefourteen, age_fifteenfiftynine, age_sixtyplus, totalAge])

    def bioExemption(self, bioCtr, finger_fivefourteen, finger_fifteenfiftynine, finger_sixtyplus, iris_fivefourteen, iris_fifteenfiftynine, iris_sixtyplus, totalBio):
        # self.finger_fivefourteen = finger_fivefourteen
        # self.finger_fifteenfiftynine = finger_fifteenfiftynine
        # self.finger_sixtyplus = finger_sixtyplus
        # self.iris_fivefourteen = iris_fivefourteen
        # self.iris_fifteenfiftynine = iris_fifteenfiftynine
        # self.iris_sixtyplus = iris_sixtyplus
        self.bio_list.append([bioCtr, finger_fivefourteen, finger_fifteenfiftynine, finger_sixtyplus, iris_fivefourteen, iris_fifteenfiftynine, iris_sixtyplus, totalBio])

    def viewTable(self):
        print("\n******DAR\n")
        for i in range(len(self.dar_list)):
            for j in range(len(self.dar_list[i])):
                space = ""
                print(self.dar_list[i][j], space.rjust(5, " "), end=" ")
            print()
        self.sumDAR()
        print ("\n******AGE GROUP\n")

        for i in range(len(self.age_list)):
            for j in range(len(self.age_list[i])):
                space = ""
                print(self.age_list[i][j], space.rjust(5, " "), end=" ")
            print()
        self.sumAge()
        print("\n******BIO EXEMPTIONS\n")

        for i in range(len(self.bio_list)):
            for j in range(len(self.bio_list[i])):
                space = ""
                print(self.bio_list[i][j], space.rjust(5, " "), end=" ")
            print()
        self.sumBio()

    def deleteRKO(self, rkoToDelete):
        del self.dar_list[rkoToDelete]
        self.viewTable()

    def sumDAR(self):
        sumRKO = 0
        ctr = len(self.dar_list) - 1
        ctr2 = 1
        while ctr != 0:
            sumRKO += int(self.dar_list[ctr2][7])
            ctr -= 1
            ctr2 += 1

        print("\nTotal for all RKO:", sumRKO)

    def sumAge(self):
        sumAge = 0
        ctr = len(self.age_list) - 1
        ctr2 = 1
        while ctr != 0:
            sumAge += int(self.age_list[ctr2][4])
            ctr -= 1
            ctr2 += 1

        print("\nTotal Age Group:", sumAge)

    def sumBio(self):
        sumBio = 0
        ctr = len(self.bio_list) - 1
        ctr2 = 1
        while ctr != 0:
            sumBio += int(self.bio_list[ctr2][7])
            ctr -= 1
            ctr2 += 1

        print("\nTotal Bio Exemption:", sumBio)

rkoCtr = 1
ageCtr = 1
bioCtr = 1
while True:
    dar = PhilSysStep2DARCalculator()
    choice = str(input("""\nPHILSYS STEP 2 DAR CALCULATOR

        System Menu

                    a. Check table
                    b. Add a RKO
                    c. Add Total Age Group
                    d. Add Total Biometric Exemption
                    e. Delete RKO Output
                    f. Exit

        Enter choice >>> """))

    if choice.lower() == 'a':
       dar.viewTable()
    elif choice.lower() == 'b':
        assistedStep1 = int(input("Assisted Step 1: "))
        onlineRegistrant = int(input("Online: "))
        walkinRegistrant = int(input("Walk-In: "))
        instAssistedStep1 = int(input("Institutional-Assisted Step 1: "))
        instOnline = int(input("Institutional-Online: "))
        instWalkIn = int(input("Institutional-Walk-In: "))
        totalRKO = assistedStep1 + onlineRegistrant + walkinRegistrant + instAssistedStep1 + instOnline + instWalkIn
        dar.addRKO(rkoCtr, '{:004}'.format(assistedStep1), '{:004}'.format(onlineRegistrant),
                   '{:004}'.format(walkinRegistrant), '{:004}'.format(instAssistedStep1), '{:004}'.format(instOnline),
                   '{:004}'.format(instWalkIn), '{:004}'.format(totalRKO))
        rkoCtr += 1
    elif choice.lower() == 'c':
        age_fivefourteen = int(input("5-14: "))
        age_fifteenfiftynine = int(input("15-59: "))
        age_sixtyplus = int(input("60+: "))
        totalAge = age_fivefourteen + age_fifteenfiftynine + age_sixtyplus
        dar.ageGroup(ageCtr, '{:004}'.format(age_fivefourteen), '{:004}'.format(age_fifteenfiftynine),
                   '{:004}'.format(age_sixtyplus), '{:004}'.format(totalAge))
        ageCtr += 1
    elif choice.lower() == 'd':
        finger_fivefourteen = int(input("Finger 5-14: "))
        finger_fifteenfiftynine = int(input("Finger 15-59: "))
        finger_sixtyplus = int(input("Finger 60+: "))
        iris_fivefourteen = int(input("Iris 5-14: "))
        iris_fifteenfiftynine = int(input("Iris 15-59: "))
        iris_sixtyplus = int(input("Iris 60+: "))
        totalBio = finger_fivefourteen + finger_fifteenfiftynine + finger_sixtyplus + iris_fivefourteen + iris_fifteenfiftynine + iris_sixtyplus
        dar.bioExemption(bioCtr, '{:004}'.format(finger_fivefourteen), '{:004}'.format(finger_fifteenfiftynine),
                     '{:004}'.format(finger_sixtyplus), '{:004}'.format(iris_fivefourteen), '{:004}'.format(iris_fifteenfiftynine),
                     '{:004}'.format(iris_sixtyplus), '{:004}'.format(totalBio))
        bioCtr += 1
    elif choice.lower() == 'e':
        rkoToDelete = int(input("Enter RKO # to remove >>> "))
        if rkoToDelete > 0:
            dar.deleteRKO(rkoToDelete)
        elif rkoToDelete == 0:
            print("NO RKO FOUND. PLEASE TRY AGAIN.")
            continue
        else:
            print("PLEASE TRY AGAIN.")
            continue
        continue
    elif choice.lower() == 'f':
        print("THANK YOU!")
        quit()
        break
    else:
        #raise Exception
        continue
# except Exception:
#     print("""\nPLEASE TRY AGAIN WITH APPROPRIATE ENTRIES.
#         Possible fix:
#         -Use the appropriate choice.
#         -Don't use alphabets to fields requiring numbers..
#         -Generate report if reservations exists.
#     """)
