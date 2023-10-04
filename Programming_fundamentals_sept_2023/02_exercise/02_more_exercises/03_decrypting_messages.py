key = int(input())
n = int(input())
message = ""

for _ in range(n):
    line = input()
    encrypted_line = ""
    for char in line:
        if 'a' <= char <= 'z':
            encrypted_char = chr(((ord(char) - ord('a') + key) % 26) + ord('a'))
        elif 'A' <= char <= 'Z':
            encrypted_char = chr(((ord(char) - ord('A') + key) % 26) + ord('A'))
        else:
            encrypted_char = char

        encrypted_line += encrypted_char

    message += encrypted_line

print(message)
