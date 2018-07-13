import sys
try:
    import secrets
except ImportError:
    print("python v3.5 or greater required..")
    sys.exit(0)

class Encrypt:
    def __init__(self):

        lkey = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s',
        't','u','v','w','x','y','z']
        ukey = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S',
        'T','U','V','W','X','Y','Z']
        numKey = ['1','2','3','4','5','6','7','8','9','0']
        splKey = ['`','~','!','@','#','$','%','^','&','*','(',')','-','_','=','+','[',']',
        '{','}',';',':',"'",'"',',','<','.','>','/','?','|',' ']

        self.key = {}
        for k in lkey:
            self.key[k] = secrets.token_hex(nbytes=3)
        for k in ukey:
            self.key[k] = secrets.token_hex(nbytes=3)
        for k in numKey:
            self.key[k] = secrets.token_hex(nbytes=3)
        for k in splKey:
            self.key[k] = secrets.token_hex(nbytes=3)

        self.txtForEncrypt = None

    def startEncryption(self):
        encryptedText = ""
        if self.txtForEncrypt != None or "":
            for ch in self.txtForEncrypt:
                if ch in self.key:
                    encryptedText += self.key[ch]
        return encryptedText

    def startDecryption(self, enTxt=""):
        decryptedText = ""
        data = []
        ini = 0
        lst = 3
        if enTxt == "":
            return self.txtForEncrypt
        else:
            for i in range(len(enTxt)//3):
                data.append(enTxt[ini:lst])
                ini = lst
                lst += 3
            for dt in data:
                for ch in self.key:
                    if self.key[ch] == dt:
                        decryptedText += ch
        return decryptedText


    def setText(self, txt):
        self.txtForEncrypt = txt

    