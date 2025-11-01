print("""Would you like to have:
1. Sandwich
2. Main dish
""")

payment = 0
drink_fries = 20
service_charge = 0.12
cheese_burger = 20
double = 25
Fish_Fillet = 30
Chicken_Fillet = 35
Grilled_Chicken = 70
Mixed = 120
Fish_shrimp = 180

while True:
    ans1 = int(input("Enter your choice: "))
    if ans1 == 1:
        print("""Please choose a Sandwich from below list, then:
        1. Cheese burger - 20 pounds
        2. Double Cheese burger - 25 pounds
        3. Fish Fillet  - 30 pounds
        4. Chiken Fillet - 35 pounds
        """)
        while True:
            S = int(input("Enter your sandwich choice: "))
            if S == 1:
                print("Would you like to have drink or fries?(Yes, No) ")
                while True:
                    drinkorfries = input("Enter (Yes or No): ")
                    if drinkorfries.lower() == "yes":
                        payment = payment + cheese_burger + drink_fries
                        break
                    elif drinkorfries.lower() == "no":
                        payment = payment + cheese_burger
                        break
                    else:
                        print("You did not choose!")
            elif S == 2:
                print("Would you like to have drink or fries?(Yes, No) ")
                while True:
                    drinkorfries = input("Enter (Yes or No): ")
                    if drinkorfries.lower() == "yes":
                        payment = payment + double + drink_fries
                        break
                    elif drinkorfries.lower() == "no":
                        payment = payment + double
                        break
                    else:
                        print("You did not choose!")
            elif S == 3:
                print("Would you like to have drink or fries?(Yes, No) ")
                while True:
                    drinkorfries = input("Enter (Yes or No): ")
                    if drinkorfries.lower() == "yes":
                        payment = payment + Fish_Fillet + drink_fries
                        break
                    elif drinkorfries.lower() == "no":
                        payment = payment + Fish_Fillet
                        break
                    else:
                        print("You did not choose!")
            else:
                print("Would you like to have drink or fries?(Yes, No) ")
                while True:
                    drinkorfries = input("Enter (Yes or No): ")
                    if drinkorfries.lower() == "yes":
                        payment = payment + Chicken_Fillet + drink_fries
                        break
                    elif drinkorfries.lower() == "no":
                        payment = payment + Chicken_Fillet
                        break
                    else:
                        print("You did not choose!")
            break
        break
    elif ans1 == 2:
        print("""Please choose a main dish from below list, then:
                1. Grilled chicken - 70 pounds
                2. Mixed Grill  - 120 pounds
                3. Fish & Shrimp  - 180 pounds
                """)
        while True:
            M = int(input("Enter main dish choice: "))
            if M == 1:
                while True:
                    drinkorfries = input("Enter (Yes or No): ")
                    if drinkorfries.lower() == "yes":
                        payment = payment + Grilled_Chicken + drink_fries
                        break
                    elif drinkorfries.lower() == "no":
                        payment = payment + Grilled_Chicken
                        break
                    else:
                        print("You did not choose!")
            elif M == 2:
                while True:
                    drinkorfries = input("Enter (Yes or No): ")
                    if drinkorfries.lower() == "yes":
                        payment = payment + Mixed + drink_fries
                        break
                    elif drinkorfries.lower() == "no":
                        payment = payment + Mixed
                        break
                    else:
                        print("You did not choose!")
            else:
                while True:
                    drinkorfries = input("Enter (Yes or No): ")
                    if drinkorfries.lower() == "yes":
                        payment = payment + Fish_shrimp + drink_fries
                        break
                    elif drinkorfries.lower() == "no":
                        payment = payment + Fish_shrimp
                        break
                    else:
                        print("You did not choose!")
            break
        break
    else:
        print("Invalid choice!")

print("Will you eat in cafe?")

while True:
    cafe = input("(Yes or No): ")
    if cafe:
        if cafe.lower() == "yes":
            payment = payment + (payment * 0.12)
            print(f"Your total payment is = {payment}")
            break
        else:
            print(f"Your total payment is = {payment}")
            break
    else:
        print("You did not choose!")
        cafe = input("Please enter (Yes or No): ")
