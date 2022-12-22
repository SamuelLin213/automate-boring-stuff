import random #  imports random module

print("Hello. What is your name?")
name = input()
right = random.randint(1, 20)

print("Well, " + name + ", I'm thinking of a num between 1 and 20")

# Ask player for 6 guesses
for guesses in range(1, 7):
	print("Take a guess:")
	guess = int(input())
	if guess < right:
		print("Your guess is too low!")
	elif guess > right:
		print("Your guess is too high!")
	else:
		break # found the right ans

if guess == right:
	print("You guessed the right number!")
else:
	print("Nope. I was thinking of the number " + str(right))

