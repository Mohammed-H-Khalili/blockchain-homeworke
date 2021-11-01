from cryptography.hazmat.primitives import hashes

class someClass:
    def __init__(self,mystring):
        self.string = mystring
    def __repr__(self):
        return self.string

class CBlock:
    data = None
    previousHash = None
    def __init__(self,data,previousBlock):
        self.data = data
        self.previousBlock = previousBlock
        if previousBlock != None:
            self.previousHash = previousBlock.computeHash()
    def computeHash(self):
        digest =hashes.Hash(hashes.SHA256())
        digest.update(bytes(str(self.data),'utf8'))
        digest.update(bytes(str(self.previousHash),'utf8'))
        hash =digest.finalize()

    def validation(self):
        if self.previousBlock == None:
            return True
        return self.previousBlock.computeHash() == self.previousHash

if __name__ == '__main__':
    root = CBlock('its block zero',None)
    B1 = CBlock('its block number 1', root)
    B2 = CBlock('its block number 2',B1)
    B3 = CBlock('its block number 3',B2)
    B4 = CBlock('its block number 4',B3)
    B5 = CBlock('its block number 5',B4)

    for b in [B1,B2,B3,B4,B5]:
        if b.previousBlock.computeHash() == b.previousHash:
            print("Success! u did great")
        else:
            print ("Error! something is wrong")