class Mine:
    
    def __init__(self, mine):
        #space attributes, mine, if the tile is flagged, if the tile has been revealed already
        self.mine = mine
        self.flag = False
        self.revealed = False
    
    def flag(self):
        if (self.revealed):
            return
        
        #invert the flag state
        self.flag = not self.flag

    #when the space is clicked on, return true if tile has mine
    def interact(self):
        if (self.mine):
            return True
            
        return False
    