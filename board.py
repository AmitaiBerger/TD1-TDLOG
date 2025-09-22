import enum

"""
This module contains the classes used to represent a board.
"""


# Type synonym, used for better readability
StationNumber = int


class StationKind(enum.Enum):
    """
    The possible station kinds (used for display, and thus excluding ferries).
    """

    BUS = "bus"
    TAXI = "taxi"
    UNDERGROUND = "underground"


class ConnectionMode(enum.Enum):
    """
    The possible transportation modes, for connections between stations.
    """

    BUS = "bus"
    TAXI = "taxi"
    UNDERGROUND = "underground"
    FERRY = "ferry"


class InvalidBoard:
    """
    The exception raised when board data is invalid.
    """
    pass


class Board:
    def __init__(
        self,
        stations: list[tuple[StationNumber, list[StationKind]]],
        connections: list[tuple[StationNumber, StationNumber, ConnectionMode]],
    ) -> None:
        if not f(stations,connections):
            raise InvalidBoard
        else:
            self.stations=stations
            self.connections=connections


def f(stations,connections):
    """
    We check if the stations are in the connections list and if the connection mode matches 
    """
    bool=True
    for i in range(len(connections)):
        if not connections[i][0]!=connections[i][1] and 0<connections[i][0]< 200 and 0<connections[i][1]<200 and connections[i][2] in stations[i][0][1] and connections[i][2] in stations[i][1][1]:
            bool= False
            break
    return bool
        


