secret_number = 777
print("""+================================+| Welcome to my game, muggle! || Enter an integer number || and guess what number I've || picked for you. || So, what is the secret number? |+================================+""")
secret_number = input("Enter an integer number: ")
while (int(secret_number) < 777):
    print("Ha ha! You're stuck in my loop!")
    secret_number = input("Enter an integer number: ")
print(str(secret_number)+"Well done, muggle! You are free now.")