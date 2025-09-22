"""
This module defines the different kinds of moves, for the different kinds of
players.
"""

def possible_moves(Player):
  moves=[]
  if (Player.color!=BLACK): #check if the player is an inspector
    for c in CONNECTIONS :
      if c[0]==Player.position:
        if (c[2] Player.hand  ):
          moves.append[(c[1],c[2])]
  else():
  return moves
