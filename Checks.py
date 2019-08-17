debug = False

from TileGenerate import *

def formatTile(tile):
    return tile.suit + " " + str(tile.value)

def checkFlowers(player, game):
    done = False
    while not done:
        for tile in player.handTiles:
            if tile.suit in ("Flowers", "Seasons"):
                flowerDraw = game.availableTiles.pop()
                player.tableTiles.append(player.handTiles.pop(player.handTiles.index(tile)))
                player.handTiles.append(flowerDraw)
                if player.seat == 1:
                    print("Flower draw:", formatTile(flowerDraw))
        if "Flowers" not in getSuits(player) and "Seasons" not in getSuits(player):
            done = True

def checkKong(player, game):
    lastPlay = game.playedTiles[-1]
    tileCount = player.getTiles().count(formatTile(lastPlay))
    if tileCount == 3:
        action = input("Kong " + formatTile(lastPlay) + "? ")
        if action.lower() == "yes":
            game.currentPlayer = 1
            player.tableTiles.append(game.playedTiles.pop())
            tilesAdded = 0
            for tile in player.handTiles:
                if formatTile(lastPlay) == formatTile(tile) and tilesAdded < 3:
                    player.handTiles.remove(tile)
                    player.tableTiles.append(tile)
                    tilesAdded += 1
            playerRound(player)

def checkPong(player, game):
    lastPlay = game.playedTiles[-1]
    tileCount = player.getTiles().count(formatTile(lastPlay))
    if tileCount >= 2:
        action = input("Pong " + formatTile(lastPlay) + "? ")
        if action.lower() == "yes":
            game.currentPlayer = 1
            player.tableTiles.append(game.playedTiles.pop())
            tilesAdded = 0
            for tile in player.handTiles:
                if formatTile(lastPlay) == formatTile(tile) and tilesAdded < 2:
                    player.handTiles.remove(tile)
                    player.tableTiles.append(tile)
                    tilesAdded += 1
            playerRound(player, game)

def checkChow(player, game):
    lastPlay = game.playedTiles[-1]
    if formatTile(lastPlay).split(" ")[0] != "Word":
        filteredTiles = [tile for tile in player.getTiles() if formatTile(lastPlay).split(" ")[0] == tile.split(" ")[0]]
        filteredTiles.append(formatTile(lastPlay))
        filteredTiles = sorted(list(set(filteredTiles)))
        lastPlayIndex = filteredTiles.index(formatTile(lastPlay))

        if len(filteredTiles) >= 3:
            indecies = [[lastPlayIndex, lastPlayIndex-1, lastPlayIndex-2],
                        [lastPlayIndex+1, lastPlayIndex, lastPlayIndex-1],
                        [lastPlayIndex+2, lastPlayIndex+1, lastPlayIndex]]

            for indexSet in indecies:
                try:
                    firstTile = filteredTiles[indexSet[0]].split(" ")
                    secondTile = filteredTiles[indexSet[1]].split(" ")
                    thirdTile = filteredTiles[indexSet[2]].split(" ")
                    tileSet = [firstTile, secondTile, thirdTile]

                    if int(firstTile[1])-int(secondTile[1]) == 1 and int(secondTile[1])-int(thirdTile[1]) == 1:
                        action = input("Chow " + formatTile(lastPlay) + "? ")
                        if action.lower() == "yes":
                            game.currentPlayer = 1
                            player.tableTiles.append(game.playedTiles.pop())
                            for tile in tileSet:
                                moved = False
                                i = 0
                                while not moved and i < len(player.handTiles):
                                    handTile = player.handTiles[i]
                                    if " ".join(tile) == formatTile(handTile):
                                        player.handTiles.remove(handTile)
                                        player.tableTiles.append(handTile)
                                        moved = True
                                    i += 1
                            playerRound(player, game)
                            break
                except:
                    pass


def getSuits(player):
    return [tile.suit for tile in player.handTiles]

def playerRound(player, game):
    if len(player.handTiles) % 3 == 1:
        if debug:
            drawInput = input("DEBUG ONLY: Enter a tile to draw: ").split(" ")
            drawTile = Tile(drawInput[0], drawInput[1])
        else:
            drawTile = game.availableTiles.pop(0)
        player.handTiles.append(drawTile)
        print("\n\nYou drew", formatTile(drawTile))
        checkFlowers(player, game)

    print("\nYour tiles:")
    print(player)
    print()

    played = False
    while not played:
        play = input("Please play a tile: ")
        for tile in player.handTiles:
            if play == formatTile(tile):
                played = True
                game.playedTiles.append(player.handTiles.pop(player.handTiles.index(tile)))
                break
    game.currentPlayer += 1

def computerRound(player, game):
    if len(player.handTiles) % 3 == 1:
        player.handTiles.append(game.availableTiles.pop(0))
        checkFlowers(player, game)

    if debug:
        playInput = input("DEBUG ONLY: Enter a tile for the computer the play: ").split(" ")
        play = Tile(playInput[0], playInput[1])
    else:
        play = player.handTiles.pop(0)
        
    game.playedTiles.append(play)
    print("Player", player.seat, "played", formatTile(play))
    if game.currentPlayer == 4:
        game.currentPlayer = 1
    else:
        game.currentPlayer += 1
                     
