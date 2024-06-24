from random import randint,choice
import sys
def main():
    tiles={}
    playertiles={"Player 1":[],
                 "Player 2":[]}
    with open('tiles.txt', 'r') as file:
        while True:
            line = file.readline()
            if not line:
                break
            line=line.split(',')
            tiles[line[0]]={"quantity": int(line[1]), "value": (line[2].strip("\n"))}
    def dealtiles(player1tiles,player2tiles,round=2):
        tilesremaining1 = len(player1tiles)
        tilesremaining2=len(player2tiles)
        ongoing=True
        if round==1:
            
            for i in range(2):
                vowel=choice('AEIOU')
                player1tiles.append(vowel)
                tiles[vowel]['quantity']-=1
            for i in range(5):
                consonant=choice('BCDFGHJKLMNPQRSTVWXYZ')
                player1tiles.append(consonant)
                tiles[consonant]['quantity']-=1
            for i in range(2):
                vowel=choice('AEIOU')
                player2tiles.append(vowel)
                tiles[vowel]['quantity']-=1
            for i in range(5):
                consonant=choice('BCDFGHJKLMNPQRSTVWXYZ')
                player2tiles.append(consonant)
                tiles[consonant]['quantity']-=1
            
        else:
            for i in range(7-tilesremaining1):
                while True:
                 tile = choice(list(tiles.keys()))
                 if tiles[tile]['quantity'] > 0:
                      player1tiles.append(tile)
                      tiles[tile]['quantity'] -= 1
                      break
                 

            for i in range(7-tilesremaining2):
                while True:
                 tile = choice(list(tiles.keys()))
                 if tiles[tile]['quantity'] > 0:
                      player2tiles.append(tile)
                      tiles[tile]['quantity'] -= 1
                      break
                 
        playertiles["Player 1"]=playertiles["Player 1"]+player1tiles
        playertiles["Player 2"]=playertiles["Player 2"]+player2tiles
        






        


if __name__ == "__main__":
    main()