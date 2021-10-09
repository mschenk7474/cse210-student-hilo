from game.Dealer import Dealer

class Director:
    """A code template for a person who directs the game. The responsibility of 
    this class of objects is to keep track of the score and control the 
    sequence of play.

    Attributes:
        keep_playing (string): Whether or not the player wants to keep playing.
        score (number): The total number of points earned.
        dealer (Dealer): An instance of the class of objects known as Dealer.
    """

    def __init__(self):
        """The class constructor.
        
        Args:
            self (Director): an instance of Director.
        """
        self.keep_playing = ""
        # self.score = 300
        self.dealer = Dealer()


    def My_Attempt(self):
        again = ""
        score = 300
        card1 = Dealer.First_card()
        card2 = Dealer.Second_card()
        while True:
            # print("\nThe card is: {}".format(card1))
            print(f"\nThe card is: {card1}")
            # call the probability function to give them there chances. 
            print(f"\nChances of a higher card {round(1-self.dealer.get_probability(card1),2)}\nChances of a lower card {self.dealer.get_probability(card1)}.\n")
            self.keep_playing = str(input("Higher of lower? [h/l]: "))
            print("Next card is: {}".format(card2))
            score = Dealer.get_points(card1, card2, score, self.keep_playing)
            print(f"Your score is: {score}")
            again = str(input("Keep playing? [y/n]: "))
            print("")
            card1 = card2
            card2 = Dealer.Second_card()
            if card1 == card2:
                card2 = Dealer.Second_card()
            if again == "n":
                print("Thanks for playing!")
                break
            


    
