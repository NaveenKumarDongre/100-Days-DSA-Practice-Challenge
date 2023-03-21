class MyHash:
    
    def __init__(self, size):
        self.table = [[] for x in range(size)]
        self.BUCKET = size
        
    def hashFxn(self, data):
        return data % self.BUCKET
        
    def insert(self, data):
        index = self.hashFxn(data)
        self.table[index].append(data)

    def search(self, data):
        index = self.hashFxn(data)
        if data in self.table[index]:
            return True 
        return False
    
    def __str__(self):
        return f"{self.table}"
     
    def remove(self, data):
        index = self.hashFxn(data)
        if data in self.table[index]:
            self.table[index].remove(data)
            
            
if __name__ == "__main__":
    h = MyHash(7)
    h.insert(70)
    h.insert(71)
    h.insert(9)
    h.insert(56)
    h.insert(72)
    print(h.search(56))
    h.remove(56)
    print(h.search(56))
    
    print(h)
        
            