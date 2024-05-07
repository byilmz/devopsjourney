def space_replace():
    user_input = input("Gimme a string!! NOW!!! \n")
    space_replaced = user_input.replace(" ", "...")
    return space_replaced

result = space_replace()
print(result)