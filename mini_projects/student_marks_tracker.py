# tracking one students marks in a dictionary
marks = []

for i in range(5):
    mark = int(input("Enter a subject mark: "))
    marks.append(mark)

total = 0

for mark in marks:
    total += mark

average = total / len(marks)

print("Marks:", marks)
print("Total:", total)
print("Average:", average)

# tracking multiple students marks in a dictionary
students = {
    "Riya": [85, 90, 92],
    "Aman": [78, 82, 80],
    "Kabir": [95, 91, 97]
}

for name, marks in students.items():
    total = 0

    for mark in marks:
        total += mark

    average = total / len(marks)

    print(name)
    print("Marks:", marks)
    print("Total:", total)
    print("Average:", average)
    print()