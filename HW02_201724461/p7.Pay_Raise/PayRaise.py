def NewSalary(salary):
    if salary < 40000:
        return salary * 1.05
    else:
        raised = 2000 + (salary-40000) * 0.02
        return salary + raised


def main():
    people = int(input("How many people? "))
    data = [["first", "last", 0] for i in range(0, people)]

    for index in range(0, people):
        print("Person {}".format(index+1))
        data[index][0] = input("Enter first name: ")
        data[index][1] = input("Enter last name: ")
        data[index][2] = float(input("Enter current salary: "))

    for person in range(0, people):
        print("{index:3}  {first:10} {last:10}  ${current:,.2f}   ${new:,.2f}"
              .format(index=person+1, first=data[person][0], last=data[person][1],
                      current=data[person][2], new=NewSalary(data[person][2])))


main()






