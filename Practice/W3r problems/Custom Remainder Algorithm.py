a = 2
b = 5
remainder = b #3  #copy of B to manipulate


for i in range(1, b + 1):
    if remainder >= a:
        remainder = remainder - a  #as soon as remainder became less than or equal to a 1 > 2, for will break
print(remainder)
