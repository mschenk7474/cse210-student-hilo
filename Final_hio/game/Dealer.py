import random

class Dealer:
    """
    Attributes: 
        first_card (int): The first card of the game and then the previous card the player guesses against. 
        Second_card (int): The current card
        score (int): The Total score 
    """

    def __init__(self):
        """The class constructor.

        Args:
            self (Director): an instance of Director.
        """
        self.first_card = 0 
        self.second_card = 0
        self.score = 300

    def First_card():
        """
        Creates the first random card and becomes the previous card. 
        """
        options = [i for i in range(1, 14)]
        return random.choice(options)

    def Second_card():
        """
        Creates the current card. 
        """
        options = [i for i in range(1, 14)]
        return random.choice(options)


    def get_points(card_1, card_2, score, play):
        """
        Gets the score of the current play and adds it to score. 

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


    def get_probability(self, card1):
        """
        Gets the probability of the current or next card being higher or lower than the previous card.

        """
        card_prod = float((100/12)/100)
        lower_prod = (card1 - 1) * card_prod
        
        return round(lower_prod,2)
