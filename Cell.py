class Cell():
    def __init__(self):
        self.num_surrounding = 0
        self.is_clicked = False
        self.flagged = False
        self.checked = False

    def make_bomb(self):
        if self.num_surrounding == -1:
            return False
        self.num_surrounding = -1
        return True

    def set_num_surrounding(self, num):
        self.num_surrounding = num

    def is_bomb(self):
        return self.num_surrounding == -1
    
    def open(self):
        self.is_clicked = not self.is_clicked

    def is_opened(self):
        return self.is_clicked
    
    def num_surrounding(self):
        return self.num_surrounding
    
    def flag(self):
        self.flagged = not self.flagged


    
