#Signatures.py
from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.asymmetric import padding
from cryptography.exceptions import InvalidSignature
from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.backends import default_backend


def generate_keys():    
    private = rsa.generate_private_key(
        public_exponent=65537,
        key_size=2048,
     )
    
    public = private.public_key()
    pu_serialize  = public.public_bytes(
        encoding = serialization.Encoding.PEM,
        format = serialization.PublicFormat.SubjectPublicKeyInfo
   )
    return private, pu_serialize

def sign(message, private):

   
    sig = private.sign(
        message,
        padding.PSS(
            mgf=padding.MGF1(hashes.SHA256()),
            salt_length=padding.PSS.MAX_LENGTH
        ),
        hashes.SHA256()
    )
    return sig

def verify(message, sig, pu_serialize):
    public = serialization.load_pem_public_key(
        pu_serialize,
        backend = default_backend()
    )
    message = bytes (str(message), 'utf-8')
    try:
        public.verify(
            sig,
            message,
            padding.PSS(
                mgf=padding.MGF1(hashes.SHA256()),
                salt_length=padding.PSS.MAX_LENGTH
            ),
            hashes.SHA256()
        )
        return True
    except InvalidSignature:
        return False 
    except :
        print("someting is Wrong with key verification")
        return False

        
if __name__ == '__main__':

    pr,pu = generate_keys()
    message = b"This is a secret message"
    sig = sign(message, pr)
    
    try:
        verify(message, sig, pu)
        print("Success! Good Signature")
    except:
        print ("ERROR! Signature is bad")