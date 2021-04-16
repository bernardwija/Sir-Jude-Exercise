print('Welcome to ROT-13 Encoder and Decoder!')
def rotup(asn,key):
    print('Here is your sentence: ', asn)
    print('Here is your encoded sentence:')
    new=''
    for i in asn:
        if i in key.keys():
            new+=key[i]
        elif i not in key.keys():
            new+=i
    return new

def data():
	asn=list(input('Please Input your sentence: '))
	key = {'a':'n', 'b':'o', 'c':'p', 'd':'q', 'e':'r', 'f':'s', 'g':'t', 'h':'u','i':'v', 'j':'w', 'k':'x', 'l':'y', 'm':'z', 'n':'a', 'o':'b', 'p':'c','q':'d', 'r':'e', 's':'f', 't':'g', 'u':'h', 'v':'i', 'w':'j', 'x':'k', 'y':'l', 'z':'m', 'A':'N', 'B':'O', 'C':'P', 'D':'Q', 'E':'R', 'F':'S', 'G':'T', 'H':'U', 'I':'V', 'J':'W', 'K':'X', 'L':'Y', 'M':'Z', 'N':'A', 'O':'B', 'P':'C', 'Q':'D', 'R':'E', 'S':'F', 'T':'G', 'U':'H', 'V':'I', 'W':'J', 'X':'K', 'Y':'L', 'Z':'M', ' ':' ','?':'?','!':'!','.':'.'}
	print(rotup(asn,key))
data()
print('Thankyou for using our service!')