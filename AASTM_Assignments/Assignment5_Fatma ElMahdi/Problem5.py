st_num = int(input("Enter the number of students: "))
print("Please enter their marks...")

grades = []
sum = 0
for n in range(1, st_num+1):
    mark = int(input(f"Student ({n}): "))
    grades.append(mark)
    sum += mark
avg = sum / st_num
print(f"The average is: {avg}")

Above_avg = 0
for s in grades:
    if s > avg:
        Above_avg += 1
below_avg = st_num - Above_avg
print(f"The number of students above average is: {Above_avg}")
print(f"The number of students who failed is: {below_avg}")

#if the number of the students with grades above avg is 4, isn't the num of students who
#failed is 4? since the entered total num of students is 8
#in the assignment: The number of students who failed is: 1, when the entered number of students is 8,