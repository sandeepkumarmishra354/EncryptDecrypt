# EncryptDecrypt
# python3 required

Python script for text encryption and decryption
it generates truely random keys for every session

ex-
```
import encrypt
en = encrypt.Encrypt()
en.setText("abc")
txt = en.startEncryption()
print("Encrypted: {}".format(txt))
txt = en.startDecryption()
print("Decrypted: {}".format(txt))
```
## output
*Encrypted: 1#4d%3df&*

*Decrypted: abc*
