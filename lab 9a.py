#Akshar Niranjan Katariya

# Create a rock-paper-scissors game!
# - Play once and report the result
# - Play in a loop and record how many wins and losses happen?
# - Allow choosing how many human players there are, from 0-2?
# - Organize everything into functions?
# - Organize everything into classes??

from numpy import random

choices = ['rock', 'paper', 'scissors']

p1 = input('Pick one of rock, paper or scissors: ')
p2 = random.choice(choices)

if p1 == p2:
    print(f"Both players selected the same. It's a tie!")
elif p2 == "rock":
    if p1 == "scissors":
        print("You lose.")
    else:
        print("You win!")
elif p2 == "paper":
    if p1 == "rock":
        print("You lose.")
    else:
        print("You win!")
elif p2 == "scissors":
    if p1 == "paper":
        print("You lose.")
    else:
        print("You win!")

# LOOP for repeated games

wins = 0
losses = 0
rounds = 0

while rounds < 20:
    p1 = 'rock'
    p2 = random.choice(choices)

    if p1 == p2:
        print(f"Both players selected the same. It's a tie!")
    elif p2 == "rock":
        print("Both players selected rock. It's a tie!")
    elif p2 == "paper":
        print("Paper covers rock! You lose.")
        losses += 1
    elif p2 == "scissors":
        print("Rock smashes scissors! You win!")
        wins += 1
    rounds += 1

print(wins)
print(losses)
