def match(pattern, sub):
    return sub == pattern

#takes in a char to be subtracted,value is the previous value, string is the current window
def rabin_fingerprint(string, val, char):
    d = 256
    length = len(string)
    # if no previous val was calculated 
    if(val == 0):
        #calculate inital val
        for i in range(0, length):  
            val += ord(string[i]) * pow(d, length - i -1)
    else:
        # subtract the original 
        val -= (ord(char) * pow(d, length-1))
        val *= d
        val += ord(string[length-1])

   
    return val

def rabin_karp(string, pattern):
    #get length of the pattern and pattern's hash value
    length = len(pattern)
    hash_val = rabin_fingerprint(pattern,0, '')
    index = []
    val =0
    # iterate through string utilizing a sliding window
    for i in range(0, len(string) - length+1):
        # get the substring and calculate its hash value
        sub = string[i: i + length]
        val = rabin_fingerprint(sub, val, string[i-1])
        #if same hash values then check if it is a match and add to index
        if(val == hash_val):
            if(match(sub, pattern)):
                index.append(i)
    return index

