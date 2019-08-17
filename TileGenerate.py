class Tile(object):
    def __init__(self, suit, value):
        self.suit = suit
        self.value = value

def generateTiles():
    tiles = []

    valueSuits = ("Dot", "Bamboo", "Thousands")
    for suit in valueSuits:
        for i in range(4):
            for j in range(1, 10):
                tiles.append(Tile(suit, j))
                

    otherSuits = ("Word", "Seasons", "Flowers")
    for suit in otherSuits:
        if suit == "Word":
            for i in range(4):
                words = ("East", "South", "West", "North", "Red", "Green", "White")
                for word in words:
                    tiles.append(Tile("Word", word))
        else:
            for i in range(1,5):
                tiles.append(Tile(suit, i))

    return tiles
