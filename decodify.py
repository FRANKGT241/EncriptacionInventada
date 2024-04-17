import base64
import binascii

gram_array = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k','l', 'm', 'n', 'ñ','o', 
              'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z','A', 'B', 'C', 
              'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'Ñ','O', 'P', 'Q',
              'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z','_', '{', '}','0','1','2','3','4','5','6','7','8','9',
              '+','/','=']

def reverse_base64(password_with_hexa):
    bytes_word = base64.b64decode(password_with_hexa.encode('utf-8'))
    new_password = binascii.unhexlify(bytes_word).decode('utf-8')
    return new_password




hexa="MzczNzM2NjU="

reverse_base64(hexa)