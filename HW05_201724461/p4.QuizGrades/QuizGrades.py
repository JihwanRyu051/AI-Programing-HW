class Quizzes:
    def __init__(self, gradelist):
        self._gradelist = gradelist

    def average(self):
        total = 0
        self._gradelist.sort()
        self._gradelist.pop(0)
        for grade in self._gradelist:
            total += grade
        return total/len(self._gradelist)

    def __str__(self):
        return ("Quiz average: {0:.1f}".format(self.average()))


def main():
    for index in range(3):
        print("case {}\n".format(index+1))
        list = []
        for index in range(6):
            score = int(input("Enter grade on quiz {}: ".format(index+1)))
            list.append(score)
        quiz = Quizzes(list)
        print(quiz,end = "\n\n")


main()
