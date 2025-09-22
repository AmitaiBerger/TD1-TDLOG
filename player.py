"""
This module defines the different kinds of players.
"""
import enum
class Color(enum.ENUM):
    BLACK="black"
    ORANGE="orange"
    BLUE="blue"
    GREEN="green"
    RED="red"
    PURPLE="purple"

class Cards(enum.ENUM):
    BUS= "bus"
    TAXI="taxi"
    UNDERGROUND = "underground"
    DOUBLE="double"
    BLACK="black"

class Pioche:
    def __init__(self,number_metro_tickets,number_taxi_tickets,number_bus_tickets):
        self.number_metro_tickets=number_metro_tickets
        self.number_taxi_tickets=number_taxi_tickets
        self.number_bus_tickets=number_bus_tickets

class Hand:
    def __init__(self,hand:list[Cards]):
        for i in hand:
            assert type(i)==Cards
        self.hand=hand

class Player:
    """
    We create a general Player class and we define by heritage the class of the player Mister_X and the class of the Inspectors who will have different methods
    """
    def __init__(self,position:int,hand:Hand,color:Color,name:str):
        assert type(hand)==Hand
        assert type(color)==Color
        assert 0<position<200
        self.position=position
        self.hand=hand
        self.color=color
        self.name=name

class Mister_X(Player):
    def __init__(self,position,hand,color,name):
        super().__init__(position,hand,color,name)
        self.color=Color.BLACK

class Inspectors(Player):
    def __init__(position,hand,color,name):
        super().__init__(position,hand,color,name)