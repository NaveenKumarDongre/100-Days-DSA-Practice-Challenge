class DirectAddressTable:
    
    def __init__(self):
        self.table = [0]*1000
    
    def insert(self, num):
        self.table[num] = 1
    
    def search(self, num):
        return self.table[i]
            
    def delete(self, num):
        self.table[num] = 0