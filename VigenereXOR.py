# vigenere cipher berbasis bit dengan fungsi XOR
def generate_key_bits(message, key):
    key_bits = ''.join(format(ord(k), '08b') for k in key)
    if len(message) == len(key_bits):
        return key_bits
    elif len(message) < len(key_bits):
        return key_bits[:len(message)]
    else:
        key_bits = key_bits * (len(message) // len(key_bits)) + key_bits[:len(message) % len(key_bits)]
        return key_bits

def vigenere_encrypt_bits(message, key):
    result_bits = ""
    message_bits = ''.join(format(ord(m), '08b') if m != ' ' else ' ' for m in message.upper())
    key_bits = generate_key_bits(message_bits, key.upper())
    
    for i in range(len(message_bits)):
        if message_bits[i] == ' ':
            result_bits += ' '
        else:
            result_bits += '1' if message_bits[i] != key_bits[i] else '0'
    
    result_bits = result_bits[:len(message_bits)] 
    
    return result_bits

def vigenere_decrypt_bits(ciphertext_bits, key):
    result = ""
    key_bits = generate_key_bits(ciphertext_bits, key.upper())
    
    for i in range(0, len(ciphertext_bits), 8):
        if ciphertext_bits[i:i+8] == ' ':
            result += ' '
        else:
            char = chr(int(ciphertext_bits[i:i+8], 2) ^ int(key_bits[i:i+8], 2))
            result += char
    
    return result

message = "FRIDASUKMA"
key = "NUSANTARA"
encrypted_message_bits = vigenere_encrypt_bits(message, key)
decrypted_message = vigenere_decrypt_bits(encrypted_message_bits, key)

print("Pesan asli:", message)
print("Pesan terenkripsi berupa bits:", encrypted_message_bits)
print("Pesan terdekripsi:", decrypted_message)
