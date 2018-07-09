#!/usr/bin/python
class Encrypt:
    def __init__(self):
        self.key = ({'a':'1#4', 'b':'d%3', 'c':'df&', 'd':'@34', 'e':'f61', 'f':'dfq', 'g':'@1@', 'h':'fg4','i':'d4d',
        'j':'**5', 'k':'d33', 'l':'=+0', 'm':'%$$', 'n':'~`^', 'o':'!!(', 'p':')^(', 'q':'#-)', 'r':'s^f', 's':'0%6',
        't':'ff#', 'u':'$dd', 'v':'<?%', 'w':'d+x', 'x':'vv)', 'y':'$gQ', 'z':'5^b', ' ':'spc', '`':'QZX', '~':'{R)',
        '1':'4$]', '2':'fDf', '3':'%^G', '4':'[F]', '5':'~1W', '6':'GH&', '7':'|\Y', '8':'F4Z', '9':'0O{', '0':'AQA',
        '!':'_+#', '@':'DD<', '#':'!@!', '$':'iYF', '%':'FqQ', '^':'FLF', '&':'$$$', '*':'~Q~', '(':'(((', ')':')))',
        '-':'+++', '_':'D~~', '=':'Brb', '+':'PLs', '[':'BRI', ']':'BLE', '{':'MRI', '}':'MLE', ';':'SMC', ':':'onc',
        "'":'Scl', '"':'Dcl', '<':'RAL', '>':'LAL', ',':'COM', '.':'DOT', '/':'SLS', '?':'qeS', '|':'ORC'})
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

    
