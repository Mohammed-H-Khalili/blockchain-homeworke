#Transaction
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.asymmetric import padding, rsa
import block_Signatures
import hashModule

class Tran:

    sender = None
    reciver = None
    sig = None
    puK = puK

    def __init__(self,puK) :
        self.puK = puK
        self.sender = []
        self.reciver = []
        self.sig = []

    def add_sender(self,from_address,quantity):
        self.sender.append((from_address,quantity))

    def add_reciver(self,to_address,quantity):
        self.reciver.append((to_address,quantity)) 

    def SignTransaction(self):
        message = self.__gather()
        signature = block_Signatures.sig(message,self.puK)
        self.sig.append(signature)       

    def __gather(self):
        data = []
        data.append(self.sender)
        data.append(self.reciver)
        data.append(self.puK)
        return data

    def validation(self):
        Input_balance = 0
        Output_balance = 0
        message = self.__gather()
        for address,quantity in self.sender:
            found = False
            for S in self.sig:
                if block_Signatures.verify(message,S,address):
                    found = True
            if not found:
                print ("Correct signature not found " + str(message))
                return False
            if quantity < 0 :
                return False
            Input_balance = Input_balance + quantity
        for address in self.puK:
            found = False
            for s in self.sig:
                if block_Signatures.verify(message,S,address) :
                    found = True
            if not found:
                return False
        for address,quantity in self.outputs:
            if quantity < 0:
                return False
            Output_balance = Output_balance + quantity

        if Output_balance > Input_balance:
            print('output balance is more than input balance')
            return False
        
        return True

#In-Module Trial Transaction
if __name__ == "__main__":
    pr1 , pu1 = block_Signatures.generate_keys()
    pr2 , pu2 = block_Signatures.generate_keys()
    Tran1 = Tran()
    Tran1.add_input(pu1, 1)
    Tran1.add_output(pu2, 1)
    Tran1.sign(pr1)
    if Tran1.is_valid():
        print("Success! Tran is valid")
    else:
        print("ERROR! Tran is invalid")
