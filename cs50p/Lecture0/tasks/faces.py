def main():
    user_input = input("Please let me know how you feel today by using the :) or :( expression: \n)")
    result = convert(user_input)
    if result:
        print(result)

def convert(user_input):
    conversion_happy = user_input.replace(":)", "🙂")
    conversion_sad = user_input.replace(":(", "🙁")

    if ":)" in user_input and ":(" not in user_input:
        return conversion_happy
    elif ":(" in user_input and ":)" not in user_input:
        return conversion_sad
    elif ":(" and ":)" in user_input:
        print("So you feel... nothing? Try again!")
        return None
    else:
        return user_input

main()
