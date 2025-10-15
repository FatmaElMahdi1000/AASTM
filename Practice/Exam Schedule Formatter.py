def  Formatter(exam_date):
    Final_format = ""
    Updated_Format = list(exam_date)
    for num in exam_date:
        Final_format = Final_format + str(num) +"/"
        Cleaned = Final_format[:-1]
    return Cleaned

exam_date = (11, 12, 2014)
Final_format = Formatter(exam_date)
print(Final_format)

print("-------- Another Cleaner Way! --------- ")

#Note about join:
print(""" join() is a string method that takes a list
(or any iterable) of strings and joins them into a single 
string, using the string you call it on as the separator.""")

def formatter(exam_date):
    return "/".join(map(str, exam_date))

exam_date = (11, 12, 2014) #Tuple
Cleaned_Format = formatter(exam_date)
print(Cleaned_Format)