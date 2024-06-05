def main():
    msg = input("Enter the plaintext: ").strip()
    key = input("Enter the key: ").strip()
    
    #Ensure the key length matches the plaintext length
    mod = len(key)
    j = 0
    for i in range(len(key), len(msg)):
        key += key[j % mod]
        j += 1

    res = ""
    for i in range(len(msg)):
        res += chr((ord(msg[i]) + ord(key[i]) - 2 * ord('A')) % 26 + ord('A'))

    print("Encrypted message:", res)

if __name__ == "__main__":
    main()
