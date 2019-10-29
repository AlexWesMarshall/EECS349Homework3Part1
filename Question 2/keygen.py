while (True):
    username = input("enter username: ")
    username = username.upper()
    bitsum = 0
    for c in username:
        bitsum += ord(c)
    bitsum = bitsum^4660
    bitsum = bitsum^22136
    print(bitsum)