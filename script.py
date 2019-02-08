class Encode4Bits:
    def __init__(self):
        self._mappingTable = ['\0', \
                              '0','1','2','3','4','5','6','7','8','9', \
                              '-','','','','']

    def _encodeCharacter(self,char):
        for p in range(len(self._mappingTable)):
            if(char == self._mappingTable[p]):
                return p
        return None

    def encode(self, string):
        strLen = len(string)

        mappingIndices = []
        for i in range(strLen):
            char = string[i]
            index = self._encodeCharacter(char)
            if(index is None):
                raise("ERROR: Could not encode '" + char + "'.")
            mappingIndices.append(index)
        mappingIndices.append(0)
        
        if(len(mappingIndices) % 2 != 0):
            mappingIndices.append(0)

        ret = ""
        i = 0
        while True:
            if(i >= len(mappingIndices)):
                break
            val1 = mappingIndices[i]
            val2 = mappingIndices[i+1]
            val1 = val1 << 4           
            mixed = val1 | val2
            char = chr(mixed)
            ret += str(char)
            i += 2

        return ret

    def decode(self, string):
        ret = ""
        for char in string:
            index1 = (ord(char) & 120) >> 4
            index2 = (ord(char) & 15)            
            ret += self._mappingTable[index1]
            ret += self._mappingTable[index2]
        
        return ret

def test_operation():
    numberCompressor = Encode4Bits()
    encoded = numberCompressor.encode("067-845-512")
    decoded = numberCompressor.decode(encoded)

    print(encoded,len(encoded))
    print(decoded,len(decoded))


if __name__ == "__main__":
    test_operation()
