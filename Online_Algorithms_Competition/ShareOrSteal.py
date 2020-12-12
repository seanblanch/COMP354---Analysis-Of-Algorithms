# IMPORTS
from itertools import combinations
from random import random
import matplotlib.pyplot as plt
from enum import Enum


# GAME CONSTANTS
class CHOICE(Enum):
    SHARE = True,
    STEAL = False


SHARE_BONUS = 2
STEAL_BONUS = 3
PASSIVE_BONUS = 1


# ABSTRACTED GAME ENTITIES (DO NOT EDIT)
class AbstractPlayer:

    # Creates a Contestant
    def __init__(self):
        # set name
        self.name = self.__class__.__name__

        # fields to store the sequence of moves made by both players
        self.personal_decision_log = []
        self.opponent_decision_log = []

        # ensure that chooseMove is implemented
        self.choose_move()

    # Chooses the contestant's move (SHARE or STEAL) and returns it
    def choose_move(self):
        print("IMPLEMENT CHOOSE_MOVE")
        return CHOICE.SHARE

    def choose_and_validate_move(self):
        choice = self.choose_move()
        if choice not in CHOICE.__members__.values():
            print("Player " + self.__class__.__name__ + " couldn't make a decision...")
            return CHOICE.SHARE
        return choice

    # Updates the move histories with a specified values
    def update_move_logs(self, personal_move, opponent_move):
        self.personal_decision_log.append(personal_move)
        self.opponent_decision_log.append(opponent_move)

    # Resets move logs between rounds
    def reset(self):
        self.personal_decision_log = []
        self.opponent_decision_log = []


# PLAYER CREATION

# How to create your player:
#   1. Read the description in the README to be sure you understand the game.
#   2. Run this, see what the output should look like before you start.
#   3. Change the identifier of the YourPlayerName class below
#       - this should be something you'll recognize; you'll use it to identify your player in the results
#       - this doesn't mean it actually has to be your name, just something you'll recognize
#   4. Fill out the choose_move function. It:
#       - can view your player's moves made (so far, against this opponent)
#           - self.personal_decision_log is a list of your moves so far
#       - can view your opponent's moves made (so far, against you)
#           - self.opponent_decision_log
#       - must return Choice.SHARE or Choice.STEAL
#       - must run in O(n^2) time, where n is the length of self.personal_decision_log and self.opponent_decision_log
#       - may not declare new non-local variables
#   5. Add an instance of your player to the players list in the main (near the bottom, search for Gandhi).
#   6. Test run :)
#   7. Create and submit a new .py file consisting of only your player.
#
#   YOU MAY NOT:
#   1. Declare any variables outside of the choose_move scope.
#   2. Use any additional dependencies (imports).
#   3. Call or modify any of the functions defined in AbstractPlayer.
#   4. Modify the personal_decision_log or opponent_decision_log.

# When you are done, put your player class in a separate file and submit that file on Canvas.
# You may work in teams of up to 4 students; each team shoud ONLY submit once, and should put
# all 4 names in their submitted file in Python comments.


class Sean(AbstractPlayer):
    def choose_move(self):
        # We'll start you out as Gandhi, but there are tons of other examples below
        # start here
        # If no moves have been made, I've done equal parts share and steal

        if len(self.opponent_decision_log) == 0:
            return CHOICE.SHARE

        if CHOICE.STEAL in self.opponent_decision_log:
            return CHOICE.STEAL
        return CHOICE.SHARE


# EXAMPLE PLAYERS
class Gandhi(AbstractPlayer):
    def choose_move(self):
        # be nice
        return CHOICE.SHARE


class Hitler(AbstractPlayer):
    def choose_move(self):
        # be mean
        return CHOICE.STEAL


class UniformRandom(AbstractPlayer):
    def choose_move(self):
        # choose STEAL or SHARE, 50/50
        # become chaos
        sample = random()  # random float from 0 to 1
        if sample >= 0.5:
            return CHOICE.SHARE
        return CHOICE.STEAL


class BigStick(AbstractPlayer):
    def choose_move(self):
        # never forgive. never forget.
        if CHOICE.STEAL in self.opponent_decision_log:
            return CHOICE.STEAL
        return CHOICE.SHARE


class TitForTat(AbstractPlayer):
    def choose_move(self):
        # if it's the first move, be nice
        if len(self.opponent_decision_log) == 0:
            return CHOICE.SHARE
        # if the opponent was nice on the last move, be nice on this move
        if self.opponent_decision_log[-1] == CHOICE.SHARE:
            return CHOICE.SHARE
        # the opponent was mean last time, take your revenge, be mean back
        return CHOICE.STEAL


class ExpectedValue(AbstractPlayer):
    def choose_move(self):
        # If no moves have been made, your opponent has done equal parts steal and share.
        if len(self.opponent_decision_log) == 0:
            opponent_share_probability = 0.5
            opponent_steal_proportion = 0.5
        # otherwise, get proportions of steals and shares from opponent so far
        else:
            opponent_share_probability = sum(1 for x in self.opponent_decision_log if x == CHOICE.SHARE) / len(
                self.opponent_decision_log)
            opponent_steal_proportion = sum(1 for x in self.opponent_decision_log if x == CHOICE.STEAL) / len(
                self.opponent_decision_log)

        # calculate expected value of your reward if sharing or stealing based on probability
        share_ev = SHARE_BONUS * opponent_share_probability + PASSIVE_BONUS * opponent_steal_proportion
        steal_ev = STEAL_BONUS * opponent_share_probability

        # return the move with the higher expected value (or share, if all else is the same)
        if share_ev >= steal_ev:
            return CHOICE.SHARE
        return CHOICE.STEAL


class CounterExpectedValue(AbstractPlayer):
    def choose_move(self):
        # If no moves have been made, I've done equal parts share and steal
        if len(self.personal_decision_log) == 0:
            personal_share_probability = 0.5
            personal_steal_probability = 0.5
        # otherwise, get proportions of steals and shares from self so far
        else:
            personal_share_probability = sum(1 for x in self.personal_decision_log if x == CHOICE.SHARE) / len(
                self.personal_decision_log)
            personal_steal_probability = sum(1 for x in self.personal_decision_log if x == CHOICE.STEAL) / len(
                self.personal_decision_log)

        # calculate the opponent's expectations (assuming they're an expected value player)
        share_ev = SHARE_BONUS * personal_share_probability + PASSIVE_BONUS * personal_steal_probability
        steal_ev = STEAL_BONUS * personal_share_probability

        # counter your opponents expectations
        if share_ev >= steal_ev:
            return CHOICE.STEAL
        return CHOICE.SHARE


class ExpectedValueWeightedRandom(AbstractPlayer):
    def choose_move(self):
        # If no moves have been made, my opponent has done equal parts share and steal
        if len(self.opponent_decision_log) == 0:
            opponent_share_probability = 0.5
            opponent_steal_probability = 0.5
        # otherwise, get proportions of steals and shares from opponent so far
        else:
            opponent_share_probability = sum(
                1 for x in self.opponent_decision_log if x == CHOICE.SHARE) / len(self.opponent_decision_log)
            opponent_steal_probability = sum(1 for x in self.opponent_decision_log if x == CHOICE.STEAL) / len(
                self.opponent_decision_log)

        # calculate expected value of your reward if sharing or stealing based on probability
        share_ev = SHARE_BONUS * opponent_share_probability + PASSIVE_BONUS * opponent_steal_probability
        steal_ev = STEAL_BONUS * opponent_share_probability

        # choose randomly, with chance proportional to expected value
        likelihood_share = share_ev / (share_ev + steal_ev)
        if random() <= likelihood_share:
            return CHOICE.SHARE
        return CHOICE.STEAL


# MAIN
if __name__ == "__main__":

    players = [
        Sean(),
        Gandhi(),
        Hitler(),
        UniformRandom(),
        BigStick(),
        TitForTat(),
        ExpectedValue(),
        CounterExpectedValue(),
        ExpectedValueWeightedRandom()
    ]

    players = {player.name: player for player in players}
    scores = {player: 0 for player in players}
    scores["THE VOID (normalized)"] = 0

    moves_per_round = 1000
    for name_1, name_2 in combinations(players, 2):

        # get players
        player_1 = players[name_1]
        player_2 = players[name_2]

        # play a round
        for r in range(moves_per_round):

            # get player moves
            player_1_move = player_1.choose_and_validate_move()
            player_2_move = player_2.choose_and_validate_move()

            # adjust scores
            if player_1_move == CHOICE.SHARE and player_2_move == CHOICE.SHARE:
                scores[name_1] += SHARE_BONUS
                scores[name_2] += SHARE_BONUS
            elif player_1_move == CHOICE.SHARE:
                scores[name_2] += STEAL_BONUS
                scores[name_1] += PASSIVE_BONUS
            elif player_2_move == CHOICE.SHARE:
                scores[name_1] += STEAL_BONUS
                scores[name_2] += PASSIVE_BONUS
            else:
                scores["THE VOID (normalized)"] += 2 * SHARE_BONUS

            # update logs
            player_1.update_move_logs(personal_move=player_1_move, opponent_move=player_2_move)
            player_2.update_move_logs(personal_move=player_2_move, opponent_move=player_1_move)

        # reset logs
        player_1.reset()
        player_2.reset()

    scores["THE VOID (normalized)"] /= len(scores) - 1
    for name in sorted(scores, key=lambda x: scores[x]):
        print(name + " : " + str(scores[name]))

    fig = plt.figure()
    fig.suptitle("Share Or Steal Results")
    fig.subplots_adjust(bottom=0.5)

    ax = plt.subplot(1, 1, 1)

    X_Labels = sorted(scores, key=lambda x: scores[x], reverse=True)
    X = [i for i in range(len(X_Labels))]
    Y = [scores[name] for name in X_Labels]
    C = [(random(), random(), random()) for i in X_Labels]

    ax.bar(X_Labels, Y, color=C)
    plt.xticks(rotation=90)
    plt.ylabel("$")

    plt.show()
