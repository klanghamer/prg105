"""
In this programming exercise, you will create a simple trivia game for two players. The program will work like this:

Starting with player 1, each player gets a turn at answering 5 trivia questions.
(There should be a total of 10 questions.) When a question is displayed, 4 possible answers are
 also displayed. Only one of the answers is correct, and if the player selects the correct answer,
 he or she earns a point. After answers have been selected for all the questions, the program displays
  the number of points earned by each player and declares the player with the highest number of points the winner.
To create this program, write a Question class to hold the data for the trivia question. The question
class should have attributes for the following data:

A trivia question
Possible answer 1
Possible answer 2
Possible answer 3
Possible answer 4
The number of the correct answer (1, 2, 3, or 4)
The Question class should also have an appropriate __init__ method, accessors, and mutators.

The program should have a list or a dictionary containing 10
Question Objects, one for each trivia question. Make up your own trivia question on
the subject or subjects of your choice for the objects.

"""


class Question:

    def __init__(self, question, a1, a2, a3, a4, answer):
        self.__question = question
        self.__a1 = a1
        self.__a2 = a2
        self.__a3 = a3
        self.__a4 = a4
        self.__answer = answer

    def set_question(self, question):
        self.__question = question

    def set_a1(self, a1):
        self.__a1 = a1

    def set_a2(self, a2):
        self.__a2 = a2

    def set_a3(self, a3):
        self.__a3 = a3

    def set_a4(self, a4):
        self.__a4 = a4

    def set_answer(self, answer):
        self.__answer = answer

    def get_question(self):
        return self.__question

    def get_a1(self):
        return self.__a1

    def get_a2(self):
        return self.__a2

    def get_a3(self):
        return self.__a3

    def get_a4(self):
        return self.__a4

    def get_answer(self):
        return self.__answer


def main():
    q1 = Question("How long is New Zealand's 90 mile beach? ", "A. 90 miles", "B. 55 miles", "C. 91 miles",
                  "D. 67 miles", "B")

    q2 = Question("Which country was Caesar salad invented in? ", "A. Italy", "B. Greece", "C. Mexico", "D. Brazil",
                  "C")

    q3 = Question("Which animal is the Canary Islands named after? ", "A. Dogs", "B. Canary", "C. Cats", "D. Tortise",
                  "A")

    q4 = Question("Which country does kiwi fruit originate from? ", "A. Chile", "B. Canada", "C. New Zealand",
                  "D. China", "D")

    q5 = Question("How many months have 28 days? ", "A. 2", "B. 1", "C. All", "D. Depends on leap year.", "C")

    q6 = Question("How many more ridges does a quarter have than a dime? ", "A. 1", "B. 10", "C. 7", "D. 23", "A")

    q7 = Question("How long can a cockroach live off of a toothbrush that has been used only once? ", "A. 1 Day",
                  "B. 1 Week", "C. 1 Month", "D. 1 Year", "B")

    q8 = Question("What is the name of a group of narwhals? ", "A. Group", "B. Blessing", "C. Herd", "D. School", "B")

    q9 = Question("What country does Greenland belong to? ", "A. Iceland", "B. England", "C. Sweden", "D. Denmark", "D")

    q10 = Question("Which state is at the center of North America? ", "A. Nevada", "B. Nebraska",
                   "C. North Dakota", "D. New Mexico", "C")

    player1 = 0
    player2 = 0

    set_1 = [q1, q3, q5, q7, q9]
    set_2 = [q2, q4, q6, q8, q10]

    print("Player 1: ")
    for query in set_1:
        print("\n")
        print(query.get_question())
        print(query.get_a1())
        print(query.get_a2())
        print(query.get_a3())
        print(query.get_a4())
        guess = input("Please enter the letter of the correct answer: ")
        if guess.upper() == query.get_answer():
            print("You are correct!")
            player1 += 1
        else:
            print("That was not correct. Too bad, so sad.")

    print("Player 1 earned " + str(player1) + " points.")

    print("Player 2: ")
    for query in set_2:
        print("\n")
        print(query.get_question())
        print(query.get_a1())
        print(query.get_a2())
        print(query.get_a3())
        print(query.get_a4())
        guess = input("Please enter the letter of the correct answer: ")
        if guess.upper() == query.get_answer():
            print("You are correct!")
            player2 += 1
        else:
            print("That was not correct. Too bad, so sad.")

    print("Player 2 earned " + str(player2) + " points.")


main()
