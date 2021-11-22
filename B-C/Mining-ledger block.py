#save and restore data in block

from Block_Transaction import Tran
from Blockchain import CBlock
from block_Signatures import generate_keys, sign
import pickle
from cryptography.hazmat.backends import default_backend

class LedgerBlock (CBlock):
    def __init__(self,previousBlock):
        super (LedgerBlock,self).__init__([],previousBlock)
        
    def AddToLedgerBlock (self,ledger_inputs):
        self.data.append(ledger_inputs)

    def validation(self):
        if not super(LedgerBlock,self).validation():
            return False
        return True

if __name__ == "__main__":
    pr1,pu1 = generate_keys()
    pr2,pu2 = generate_keys()
    pr3,pu3 = generate_keys()
    pr4,pu4 = generate_keys()
    
    message ='hi my name is ....'
    message = bytes (str(message), 'utf-8')
    Signatures = sign(message,pr1)

    Tran1 = Tran(pu1)
    Tran1.add_sender(pu1,5)
    Tran1.add_reciver(pu2,2.5)
    Tran1.SignTransaction(private=pr1)
    
    if Tran1.validation():
        print("Sucssesful ledger")
    
    SaveFile = open("Ledgerblock.dat","wb")
    pickle.dump(Tran1,SaveFile)
    SaveFile.close()
    
    LoadFile = open("LedgerBlock.dat","rb")
    new_serialize_public_key = pickle.load(LoadFile)
    if new_serialize_public_key.validation():
        print("Sucessful load")
    LoadFile.close()
    
    print(new_serialize_public_key)
    
    # mining transaction test
    root = LedgerBlock(None)
    root.AddToLedgerBlock(Tran1)
    
    #mining reward 
    Tran2 = Tran(pu2)
    Tran2.add_sender(pu2,1.5)
    Tran2.add_reciver(pu3,1.5)
    Tran2.SignTransaction(pr2)
    root.AddToLedgerBlock(Tran2)
    
    SaveFile = open("Ledgerblock.dat","wb")
    pickle.dump(Tran2,SaveFile)
    SaveFile.close()
    
    LoadFile = open("LedgerBlock.dat","rb")
    new_serialize_public_key = pickle.load(LoadFile)
    if new_serialize_public_key.validation():
        print("Sucessful load")
    LoadFile.close()
    
    print(new_serialize_public_key)
    
    if Tran2.validation():
        print( "good job! Mining reward  has been extracted " )
    else:
        print("there is something wormg with minig transaction")
    
    #mining fee
    B1 = LedgerBlock(root)
    Tran3 = Tran(pu3)
    Tran3.add_sender(pu3,1)
    Tran3.add_reciver(pu1,1)
    Tran3.SignTransaction(pr3)
    B1.AddToLedgerBlock(Tran3)
    
    SaveFile = open("Ledgerblock.dat","wb")
    pickle.dump(Tran3,SaveFile)
    SaveFile.close()
    
    LoadFile = open("LedgerBlock.dat","rb")
    new_serialize_public_key = pickle.load(LoadFile)
    if new_serialize_public_key.validation():
        print("Sucessful load")
    LoadFile.close()
    
    print(new_serialize_public_key)
    
    if Tran3.validation():
        print( "good job! fee has been extracted " )
    else:
        print("there is something wormg with minig transaction")
    
    B2 = LedgerBlock(B1)
    tran4 = Tran(pu4)
    tran4.add_sender(pu3,1)
    tran4.add_reciver(pu4,1)
    tran4.SignTransaction(pr3)
    B2.AddToLedgerBlock(tran4)
    
    SaveFile = open("Ledgerblock.dat","wb")
    pickle.dump(tran4,SaveFile)
    SaveFile.close()
    
    LoadFile = open("LedgerBlock.dat","rb")
    new_serialize_public_key = pickle.load(LoadFile)
    if new_serialize_public_key.validation():
        print("Sucessful load")
    LoadFile.close()
    
    print(new_serialize_public_key)
    
    if B2.validation():
        print( "good job! Mining reward and fee has been extracted " )
    else:
        print("there is something wormg with minig transaction")
    