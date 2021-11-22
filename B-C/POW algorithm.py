import random
import string
import hashlib
from cryptography.hazmat.primitives import hashes
        
def Hash_generator (prev_block_hash, new_block_data, size = 16):
    NonceHash = bytes(str(''.join(random.choice(string.ascii_lowercase
                                    + string.ascii_uppercase
                                    + string.digits) for x in range(size))), 'utf-8')

    # -------------------
    hash_machine = hashes.Hash(hashes.SHA256())
    hash_machine.update(prev_block_hash)
    hash_machine.update(new_block_data)
    hash_machine.update(NonceHash)
    return hash_machine.finalize().hex()
    # -------------------


    #NewBlockHash = hashes + NonceHash
    #return NonceHash , NewBlockHash

hashcash = hashlib.sha256()

# just a test for NonceHash
def HashTest(NewBlockHash):
    if NewBlockHash.startswith('00'):
        return True

if __name__ == '__main__':
    
    prev_block_hash = b'111'
    new_block_data = b'222'

    Founde = False
    while Founde is False:
        new_block_hash = Hash_generator(prev_block_hash=prev_block_hash, new_block_data=new_block_data, size = 8)
        if HashTest(new_block_hash):
            print(new_block_hash)
            Founde = True
    
