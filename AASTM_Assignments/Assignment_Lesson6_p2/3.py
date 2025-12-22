Major = ("e-commerce", "multimedia", "databases", "programming", "networks")
Minor = ("multimedia", "databases", "business intelligence")
course = input("Enter the name of your registered course: ").lower()

if course in Major and course in Minor:
    print(f"{course} is a major/minor course")
elif course in Major and not(course in Minor):
    print(f"{course} is a major course")
elif course in Minor and not(course in Minor):
    print(f"{course} is a minor course")
else:
    print(f"{course} is neither a major nor a minor course")
