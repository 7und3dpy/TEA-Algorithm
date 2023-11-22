from src.convertstr import StrConvert

from datetime import datetime, timezone
import random

class TEA:
    DELTA = 0x9E3779B9
    teaKeyArr = []
    
    def generateTeaKey():
        now = datetime.now(timezone.utc) #Get current time
        #Calculate time in miliseconds 
        time = int((now - datetime(1970, 1, 1, 0, 0, 0, tzinfo=timezone.utc)).total_seconds() * 1000)
        random_value = int(random.random() * 65536) #generate random integer
        key_value = time * random_value #calculate key value
        return "{:016d}".format(key_value) #Format result as 16 digit 
    
    def Encrypt(self,v,k,_sum):
        if (v is None or k is None):return 0
        v0 = v[0], v1 = v[1]
        k0 = k[0], k1 = k[1], k2 = k[2], k3 = k[3]   
        for i in range(32):
            _sum += self.DELTA 
            v0 += ((v1 << 4) + k0) ^ (v1 + _sum) ^ ((v1 >> 5) + k1)
            v1 += ((v0 << 4) + k2) ^ (v0 + _sum) ^ ((v0 >> 5) + k3)
        
        v[0] = v0, v[1] = v1

        return _sum
    
    def Decrypt(self,v,k,_sum):
        if (v is None or k is None):return 0
        v0 = v[0], v1 = v[1]
        k0 = k[0], k1 = k[1], k2 = k[2], k3 = k[3]   
        for i in range(32):
            v1 -= ((v0 << 4) + k2) ^ (v0 + _sum) ^ ((v0 >> 5) + k3)
            v0 -= ((v1 << 4) + k0) ^ (v1 + _sum) ^ ((v1 >> 5) + k1)
            _sum -= self.DELTA
        
        v[0] = v0, v[1] = v1

        return _sum       

    def EncryptBlock(self,v,k):
        if (v is None or k is None):return None
        if (len(k) < 4):return None

        n = len(v)

        if (n == 0):return None
        if (n <= 1):return  

