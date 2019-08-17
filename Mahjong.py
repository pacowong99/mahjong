

## Import statements
import random
from TileGenerate import *
from Checks import *

## Object definition 
class Player(object):
    def __init__(self, handTiles, tableTiles, balance, seat):
        self.handTiles = handTiles
        self.tableTiles = tableTiles
        self.balance = balance
        self.seat = seat

    def __str__(self):
        playerTiles = sorted([formatTile(tile) for tile in self.handTiles])
        playerTableTiles = sorted([formatTile(tile) for tile in self.tableTiles])

        message = "Player " + str(self.seat) + " hand tiles:\n"
        message += ", ".join(playerTiles)
        message += "\n\nMelds:\n"
        message += ", ".join(playerTableTiles)

        return message

    def getTiles(self):
        return sorted([formatTile(tile) for tile in self.handTiles])

class Game(object):
    def __init__(self, wind, dealer, playedTiles, currentPlayer, availableTiles):
        self.wind = wind
        self.dealer = dealer
        self.playedTiles = playedTiles
        self.currentPlayer = currentPlayer
        self.availableTiles = availableTiles

    def __str__(self):
        playedTiles = [formatTile(tile) for tile in self.playedTiles]
        
        message = "Current game: " + self.wind + " " + str(self.dealer)
        message += "\nPlayed tiles: " + ", ".join(playedTiles)

        return message

## Function definition


## Tile generation and shuffling
tiles = generateTiles()
random.shuffle(tiles)

## Players setup
players = [Player([], [], 0, i+1) for i in range(4)]

## Game Start
print("Game start! Drawing tiles...")
game = Game("East", 1, [], 1, tiles)

## Players draw tiles
for player in players:
    player.handTiles = [game.availableTiles.pop(0) for i in range(13)]
    if player.seat == game.dealer:
        player.handTiles.append(game.availableTiles.pop(0))

## Players draw flowers
for player in players:
    checkFlowers(player, game)


ended = False
while not ended:
    while True:
        if game.currentPlayer == 1:
            print()
            print()
            print("-"*40)
            print(game)
            playerRound(players[0], game)
        else:
            computerRound(players[game.currentPlayer-1], game)
            checkKong(players[0], game)
            checkPong(players[0], game)
            if game.currentPlayer == 1:
                checkChow(players[0], game)


    
