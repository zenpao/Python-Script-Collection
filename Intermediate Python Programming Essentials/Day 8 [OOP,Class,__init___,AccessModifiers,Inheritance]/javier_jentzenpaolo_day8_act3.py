class Students:
    def __init__(self, name, math, science, english):
        self.myname = name
        self.mymath = math
        self.myscience = science
        self.myenglish = english

    def average(self):
        averageGrade = round((self.mymath + self.myscience + self.myenglish) / 3)
        return averageGrade

    def printResult(self):
        if self.average() <= 74:
            remarks = "Failed"
        elif self.average() >= 75:
            remarks = "Passed"
        print(f"""
        a. Name: {self.myname}
        b. Math: {round(self.mymath)}
        c. Science: {round(self.myscience)}
        d. English: {round(self.myenglish)}
        e. Average: {self.average()} ({remarks})
        """)

name = str(input("Enter name: "))
math = float(input("Enter Math grade: "))
science = float(input("Enter Science grade: "))
english = float(input("Enter English grade: "))

computeAverage = Students(name, math, science, english)
average = computeAverage.average()
print(average)
computeAverage.printResult()