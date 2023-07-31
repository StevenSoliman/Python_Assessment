print("Hello there player")
print("Who are you?")
print("I am.... I am the guy who is going to test you")
player_name = input("What's your name player?")
print(f"Hello there {player_name}")

# Ask the user if they have played before
show_instructions = input("Have you played this game before? ").lower()

# If they say yes , output 'program continues'
if show_instructions == "yes" or show_instructions == "y":
    print("program continues")

# If they say no, output 'display instructions'
elif show_instructions == "no" or show_instructions == "n":
    print("display instructions")

else:
    print("Please answer yes / no")

display_instruction = input("To play the game, there will be 3 answer if front of you and two of them is wrong while the other is right. "
"You must answer one in each question of the subject that they give you and if you failed three times you’ll lose.")