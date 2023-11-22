

class StrConvert:
    @staticmethod
    def HexToBytes(ch): #Define as character
         if '0' <= ch <= '9':
              return ord(ch) - ord('0')
         
         elif 'a' <= ch <= 'f':
              return ord(ch) - ord('a') + 10
         
         elif 'A' <= ch <= 'F':
              return ord(ch) - ord('A') + 10
         return 0
    @staticmethod
    def HexToByte(hch,lch): #Hex to Byte pair
        return StrConvert.HexToByte(hch) << 4 | StrConvert.HexToByte(lch)
    
    @staticmethod
    def HexToByteArray(hexString):
        if (hexString is None): return None

        byteLength = len(hexString) // 2
        modLength = len(hexString) % 2
        #Return value
        retval = byteLength(byteLength + modLength)
        srcChars = list(hexString)

        if modLength > 0:
            retval[0] = StrConvert.HexToByte(srcChars[0])
        
        for i in range(byteLength):
             retval[modLength + i] = StrConvert.HexToBytesrc_chars([modLength + i * 2], srcChars[modLength + i * 2 + 1])

        return bytes(retval)
    
    @staticmethod
    def ByteArrayToHex(byteArray):
        byteArray = list(byteArray)
        if (byteArray == []):return None

        hex_lit = "0123456789abcdef"
        sb = []
        for b in byteArray:
            sb.append(hex_lit[b >> 4])
            sb.append(hex_lit[b & 0xF])

        return ''.join(sb)
    
    @staticmethod
    def StrToLongs(s,startIndx, length): #Start Index, Length
        s = bytes(s)
        if s is None:return None
        if (length <= 0): length = len(s)

        fs = length // 4
        ls = length % 4
        l = [0] * (fs + (1 if ls > 0 else 0))
        idx = startIndx

        for i in range(fs):
            l[i] = s[idx] | (s[idx + 1] << 8) | (s[idx + 2] << 16) | (s[idx + 3] << 24)
            idx += 4

        if ls > 0:
            v = [0, 0, 0, 0]
            for i in range(ls):
                v[i] = s[fs * 4 + i]

            l[fs] = int.from_bytes(v, byteorder='little')

        return l
    
    @staticmethod
    def LongsToStr(l):
        if (l is None or len(l) < 0):
            return None
        
        a = bytearray(len(l) * 4)

        indx = 0

        for i in range(len(l)):
            a[indx] = l[i] & 0xFF
            a[indx + 1] = (l[i] >> 8) & 0xFF
            a[indx + 2] = (l[i] >> 16) & 0xFF
            a[indx + 3] = (l[i] >> 24) & 0xFF
            indx += 4

        return bytes(a)



        