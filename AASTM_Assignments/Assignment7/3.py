def Month_name(num):
    Month_list = ["jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]
    for idx in range(0, len(Month_list)):
        if num == idx:
            print(Month_list[idx-1])

num = int(input("Enter a number: "))
Month_name(num)