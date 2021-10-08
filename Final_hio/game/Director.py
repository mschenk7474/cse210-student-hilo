from game.Dealer import Dealer

class Director:
    """A code template for a person who directs the game. The responsibility of 
    this class of objects is to keep track of the score and control the 
    sequence of play.
    
    Attributes:
        keep_playing (boolean): Whether or not the player wants to keep playing.
        score (number): The total number of points earned.
        thrower (Thrower): An instance of the class of objects known as Thrower.
    """

    def __init__(self):
        """The class constructor.
        
        Args:
            self (Director): an instance of Director.
        """
        self.keep_playing = ""
        self.score = 0
        self.dealer = Dealer()


    def My_Attempt(self):
        play = ""
        again = ""
        score = 300
        card1 = Dealer.First_card()
        card2 = Dealer.Second_card()
        while True:
            print("The first card is {}".format(card1))
            play = str(input("Higher of lower: [h/l]: "))
            print("The scond card is {}".format(card2))
            print("")
            score = Dealer.get_points(card1, card2, score, play)
            print(score)
            again = str(input("Do you want to play again [y/n]: "))
            card1 = card2
            card2 = Dealer.Second_card()
            if again == "n":
                print("Thanks for playing!")
                break
            


    