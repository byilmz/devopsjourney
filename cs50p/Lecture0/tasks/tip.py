def main():
    dollars = dollars_to_float(input("How much was the meal? "))
    percent = percent_to_float(input("How much would you like to tip? "))
    tip = dollars * percent
    print(f"Leave: ${tip:.2f}")

def dollars_to_float(dollars):
    dollars_float = float(dollars.replace("$", ""))
    dollars_formatted = float("{:.1f}".format(dollars_float))
    return dollars_formatted

def percent_to_float(percent):
    percent_float = float(percent.replace("%", ""))
    percent_formatted = percent_float / 100
    return percent_formatted

main()



