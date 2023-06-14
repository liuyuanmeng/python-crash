

# answer = "4"
# guess = input("Guess what number I'm thinking of (1-10): ")
# while guess != answer:
#  guess = input("Nope, try again: ")
# print("You got it!")
    
# answer = "5"
# guess = input("Guess the number: ")

# while guess != answer:
#     if guess.lower() == "quit":
#         break
#     guess = input("Wrong guess! Try again: ")

# if guess == answer:
#     print("You did it!")
# else:
#     print("You quit. The answer was:", answer)

# my_list = ["apple","banana","cherry"]

def capitalize_list(lst):
    for i in range(len(lst)):
        lst[i] = lst[i].capitalize()

words = ["apple", "banana", "cherry"]
capitalize_list(words)
print(words)
