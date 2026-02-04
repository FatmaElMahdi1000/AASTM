seconds = 10000
seconds_leftovers = seconds % 60  #40 seconds
min = (seconds - seconds_leftovers) / 60
remaining_min = 166 % 60 #remaining min.
Actual_hrs = (166 -  remaining_min) / 60
print(seconds_leftovers)
print(remaining_min)
print(Actual_hrs)