from Objects.Fighter import Fighter
from Objects.Fight import Fight

if __name__ == '__main__':

    # Fight Simulation
    number_of_fights = 10

    for i in range(number_of_fights):

        # First Fighter
        f1 = Fighter('Fighter #1', [1, 55], [1, 36], [1, 44], [1, 26])

        # Second Fighter
        f2 = Fighter('Fighter #2', [1, 55], [1, 36], [1, 44], [1, 26])

        # Create Fight
        f = Fight(i+1, f1, f2)

        # Publish Results
        print(f1.name, f1.scores)
        print(f2.name, f2.scores)
        print("Fight #%i (%i rounds)" % (i+1, f.number_of_rounds))
        if f.tie:
            print("The fight ended in a tie.")
        else:
            print("The winner is " + f.winner.name)
            print(f.winner.__str__())
            print("The loser is " + f.loser.name)
            print(f.loser.__str__())
