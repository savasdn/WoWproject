from character import Character
from random import randrange

class Arena:

    def __init__(self, team_A, team_B):
        self.team_A = team_A
        self.team_B = team_B

    def print_state(self):
        print("-" * 10)
        print("TEAM_A")
        for character in self.team_A:
            character.print()
        print("-" * 10 + "\nTEAM_B" )
        for character in self.team_B:
            character.print()
        print("-" * 10)

    def play(self):
        time = -1
        while True:
            time += 1
            print("=" * 15)
            print("Time = " + str(time))
            print("=" * 15)
            self.print_state()

            #CREATE LIST OF CHARACTERS TO PLAY

            char_to_play = []
            for character in self.team_A:
                if character.delay == 0:
                    char_to_play.append(("A", character))
            for character in self.team_B:
                if character.delay == 0:
                    char_to_play.append(("B", character))

            #ACTIVATE CHARACTER ATTACK

            for character in char_to_play:
                attacking = character[1]
                if character[0] == "A":
                    defending = self.team_B[randrange(len(self.team_B))]
                else:
                    defending = self.team_A[randrange(len(self.team_A))]

                damage = attacking.attack()
                defending.health -= damage
                print(f"{attacking.name} dealt {damage} to {defending.name}")

            #CHECK FOR DEAD CHARACTERS
                ##REVERVE FOR BECAUSE WE DON'T WANT TO AFFECT OUR FOR LOOP

            for pos in range(len(self.team_A)-1, -1, -1):
                if self.team_A[pos].is_dead():
                    print(f"{self.team_A[pos].name} is dead!")
                    self.team_A.pop(pos)

            for pos in range(len(self.team_B)-1, -1, -1):
                if self.team_A[pos].is_dead():
                    print(f"{self.team_B[pos].name} is dead!")
                    self.team_B.pop(pos)

            #CHECK IF GAME ENDED

            if len(self.team_A) == 0:
                print("Team_B wins!")
                return False
            elif len(self.team_B) == 0:
                print("Team_A wins!")
                return False

            # END ROUND
            for character in self.team_A:
                character.end_round()

            for character in self.team_B:
                character.end_round()

            input("Press enter to continue")

