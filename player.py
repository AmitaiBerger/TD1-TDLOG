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
    def __init__(self,main:list[Cards]):
        self.main=main

class Player:
    def __init__(self,position:int,hand:Hand,color,name):
        assert 0<position<200
        self.position=position
        self.hand=hand
        self.color=color

class Mister_X(Player):
    def __init__(self,position,hand):


class Inspectors(Player):
    def __init__()