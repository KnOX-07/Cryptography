def main():
    msg = input("Enter the encrypted message: ").strip()
    key = input("Enter the key: ").strip()

    mod = len(key)
    j = 0
    for i in range(len(key), len(msg)):
        key += key[j % mod]
        j += 1

    res = ""
    for i in range(len(msg)):
        res += chr((ord(msg[i]) - ord(key[i]) + 26) % 26 + ord('A'))

    print("Decrypted message:", res)

if __name__ == "__main__":
    main()
