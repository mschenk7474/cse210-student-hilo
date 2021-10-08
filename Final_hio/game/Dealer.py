import random
class Dealer:
    def __init__(self):
        self.first_card = 0 
        self.second_card = 0
        self.score = 300
        self.card_1 = 0
        self.card_2 = 0
        self.score = 0
        self.play = ""

    def First_card():
        """
        This is where we will create the first random card
        """
        options = [i for i in range(13)]
        return random.choice(options)

    def Second_card():
        """
        This is where we will create the second random card
        """
        options = [i for i in range(13)]
        return random.choice(options)


    def get_points(card_1, card_2, score, play):
        """
        Returns:
        If the second card is bigger than the first, return score + 100. If not, 
        return score -75
        """

        if (card_1 > card_2) & (play == "l"):
            print("You are right")
            return  (score + 100)
        elif (card_2 > card_1) & (play == "h"):
            print("You are right")
            return (score + 100)
        else:
            print("You are wrong")
            return (score -75)

    def can_deal(self):
        """
        This function tells the user if they can get dealt another card or not,
        and that is based on the score they get. If the score is equal to or below 
        zero, they can't play again. Other than that, they can continue to play as
        they wish.

        Returns:
        Boolean. True if the score is greater than 0. False if otherwise.
        """
        return (self.score > 0)
