print("ROCK-PAPER-SCISSORS")

choice01 = str(input("Which will you choose; Rock, Paper, or Scissors?: ").upper())
choice02 = str(input("{} will be pinned against; Rock, Paper or Scissors?: ".format(choice01)).upper())

if choice01 == "ROCK":
        if choice02 == "ROCK":
                print("It's a draw!")
        elif choice02 == "PAPER":
                print("Rock lose!")
        else:
                print("Rock wins!")
elif choice01 == "PAPER":
        if choice02 == "ROCK":
                print("Paper wins!")
        elif choice02 == "PAPER":
                print("It's a draw!")
        else:
                print("Paper lose!")
elif choice01 == "SCISSORS":
        if choice02 == "ROCK":
                print("Scissors lose!")
        elif choice02 == "PAPER":
                print("Scissors win!")
        else:
                print("It's a draw!")
else:
        print("Please enter from the given choices.")
