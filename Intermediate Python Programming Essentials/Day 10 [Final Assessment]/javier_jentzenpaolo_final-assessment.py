import os


class RestaurantReservationSystem:
    reservation_list = [['#', 'Date', 'Time', 'Name', 'Adults', 'Children']]
    report_list = [['#', 'Date', 'Time', 'Name', 'Adults', 'Children', 'Subtotal']]
    adultRate = 500
    childrenRate = 300

    def makeReservation(self, indexCtr, name, date, time, adults, children):
        self.reservation_list.append([indexCtr, date, time, name, adults, children])
        subTotal = float((adults * self.adultRate) + (children * self.childrenRate))
        self.report_list.append([indexCtr, date, time, name, adults, children, subTotal])
        self.saveReservationsToFile() #save to file
        self.saveReportsToFile() #save to file

    def saveReservationsToFile(self):
        file = open("reservation.txt", "w")  # clear file first
        file.close()

        for i in range(len(self.reservation_list)):
            for j in range(len(self.reservation_list[i])):
                file = open("reservation.txt", "a")
                space = ""
                toWrite = str(self.reservation_list[i][j])
                file.writelines([toWrite, space.rjust(20, " ")])
                file.close()
            file = open("reservation.txt", "a")
            file.write("\n")
            file.close()

    def saveReportsToFile(self):
        file = open("report.txt", "w")  # clear file first
        file.close()

        for i in range(len(self.report_list)):
            for j in range(len(self.report_list[i])):
                file = open("report.txt", "a")
                space = ""
                toWrite = str(self.report_list[i][j])
                file.writelines([toWrite, space.rjust(20, " ")])
                file.close()
            file = open("report.txt", "a")
            file.write("\n")

            file.close()

    def viewReservations(self):
        for i in range(len(self.reservation_list)):
            for j in range(len(self.reservation_list[i])):
                space = ""
                print(self.reservation_list[i][j], space.rjust(20, " "), end=" ")
            print()

    def viewReport(self):
        for i in range(len(self.report_list)):
            for j in range(len(self.report_list[i])):
                space = ""
                print(self.report_list[i][j], space.rjust(20, " "), end=" ")
            print()

    def sumReports(self):
        sumAdults = 0
        sumKids = 0
        sumSubTotal = 0
        ctr = len(self.report_list) - 1
        ctr2 = 1
        while ctr != 0:
            sumAdults += self.report_list[ctr2][4]
            sumKids += self.report_list[ctr2][5]
            sumSubTotal += self.report_list[ctr2][6]
            ctr -= 1
            ctr2 += 1

        print("\nTotal number of adults:", sumAdults)
        print("Total number of kids:", sumKids)
        print("Grand Total: PHP", sumSubTotal)

    def deleteReservation(self, numToDelete):
        del self.reservation_list[numToDelete]
        del self.report_list[numToDelete]
        self.viewReservations()
        self.saveReservationsToFile() #update the file
        self.saveReportsToFile() #update the file


indexCtr = 1
try:
    while True:
        rss = RestaurantReservationSystem()
        choice = str(input("""\nRESTAURANT RESERVATION SYSTEM

            System Menu

                        a. View all Reservations
                        b. Make Reservation
                        c. Delete Reservation
                        d. Generate Report
                        e. Exit

            Enter choice >>> """))

        if choice.lower() == 'a':
            print("---------------------------------------------------------------RESERVATIONS"
                  "---------------------------------------------------------------")
            rss.viewReservations()
            print("--------------------------------------------------------------NOTHING FOLLOWS"
                  "--------------------------------------------------------------")
            continue
        elif choice.lower() == 'b':
            name = str(input("Name: "))
            date = str(input("Date: "))
            time = str(input("Time: "))
            adults = int(input("No. of Adults: "))
            children = int(input("No. of Children: "))
            rss.makeReservation(indexCtr, name, date, time, adults, children)
            indexCtr += 1
        elif choice.lower() == 'c':
            numToDelete = int(input("Enter Reservation # to cancel >>> "))
            if numToDelete > 0:
                rss.deleteReservation(numToDelete)
            elif numToDelete == 0:
                print("NO BOOKING FOUND. PLEASE TRY AGAIN.")
                continue
            else:
                print("PLEASE TRY AGAIN.")
                continue
        elif choice.lower() == 'd':
            print("--------------------------------------------------------------------------------REPORTS"
                  "--------------------------------------------------------------------------------")
            rss.viewReport()
            rss.sumReports()
            print("----------------------------------------------------------------------------NOTHING FOLLOWS"
                  "----------------------------------------------------------------------------")
            continue
        elif choice.lower() == 'e':
            print("THANK YOU!")
            quit()
            break
        else:
            raise Exception
            continue
except Exception:
    print("""\nPLEASE TRY AGAIN WITH APPROPRIATE ENTRIES.
        Possible fix:
        -Use the appropriate choice.
        -Don't use alphabets to fields requiring numbers.
        -Cancel reservations only if it exists.
        -Generate report if reservations exists.
    """)
