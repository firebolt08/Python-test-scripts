def message ():
    print("Enter a value: ")
print("We start here.")
message()
print("We end here.")
def message_1(number):
    print("Enter a number: ", number)
message_1(1)
# positional argument passing
def introduction(first_name, last_name):
    print("Hello, my name is", first_name, last_name)
introduction("Skywalker", "Luke")
introduction("Quick", "Jesse")
introduction("Kent", "Clark")
# Keyword argument passing
introduction(first_name = "James", last_name = "Bond")
def adding(a, b, c):print(a, "+", b, "+", c, "=", a + b + c)# Call the adding function here.
adding()