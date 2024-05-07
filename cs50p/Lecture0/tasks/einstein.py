def physics_stuff():
    user_input = input("m: ")
    c = 300000000 ** 2
    m = int(user_input)
    E = (m * c)
    return E
   
result = physics_stuff()
print("E:", result)


