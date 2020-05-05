
from pyckbwallet.wallet import CKBWallet


if __name__ == "__main__":
    seed = "comfort rough close flame uniform chapter unique announce miracle debris space like"
    passwd = "This is a passwd"
    cw1 = CKBWallet(seed)
    ekey = cw1.dumpMasterKey(passwd)
    cw2 = CKBWallet.fromEncryptedKey(passwd, ekey)
    for i in range(10):
        print(cw1.getChildAddress(0, i))
        print(cw2.getChildAddress(0, i))

    