#save and restore data in block

from Block_Transaction import Tran
from Blockchain import CBlock
from block_Signatures import generate_keys, sign
import pickle
from cryptography.hazmat.backends import default_backend

class LedgerBlock (CBlock):
    def __init__(self,previousBlock):
        hash = self.previousBlock
        
    def AddToLedgerBlock (self):
        pass
    
    def validation(self):
        return False

if __name__ == "__main__":
    pr2,pu2 = generate_keys()
    pr3,pu3 = generate_keys()

    Tran2 = Tran(pu2)
    Tran2.add_sender(pu2,1)
    Tran2.add_reciver(pu3,1)
    Tran2.SignTransaction(private=pr2)
    
    if Tran2.validation():
        print("Sucssesful ledger")
    #print(Tran2.validation())

    message ='hi my name is ....'
    message = bytes (str(message), 'utf-8')
    Signatures = sign(message,pr2)

    SaveFile = open("save.dat","wb")
    pickle.dump(pu2,SaveFile)
    SaveFile.close()
    
    LoadFile = open("save.dat","rb")
    new_serialize_public_key = pickle.load(LoadFile)

    print(new_serialize_public_key)