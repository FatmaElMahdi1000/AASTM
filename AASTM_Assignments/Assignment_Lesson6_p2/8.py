job1 = {"Job number": 1222, "Job title" : "Embedded Engineer", "Organization": "YC", "Salary": 122322, "Exp": 7}
job2 = {"Job number": 1223, "Job title" : "Embedded Engineer", "Organization": "YC", "Salary": 1234, "Exp": 3}

if job1["Salary"] > job2["Salary"]:
    print(f"Job 1 offers the highest salary. Details below: ")
    for key, value in job1.items():
        print(f"{key} : {value}")
else:
    print(f"Job 2 offers the highest salary. Details below: ")
    for key, value in job2.items():
        print(f"{key} : {value}")


