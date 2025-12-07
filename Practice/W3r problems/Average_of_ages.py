i = 1
sum = 0
counter = 0
while(i <= 5):
    age = int(input("Enter an age: ").strip())
    if(age > 0):
        sum= sum + age
        counter += 1
    i += 1
average = float(sum/counter)
print(average)