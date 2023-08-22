import re
_, time_passed = map(int, input().split(" "))
students = str(input())
for i in range(time_passed):
    for m in re.finditer("BG", students):
        students = list(students)
        students[m.start()] = "G"
        students[m.end()-1] = "B"
        students = "".join(students)
print(students)