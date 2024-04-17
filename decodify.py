import binascii
import base64

# Gramática original
gram_array = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k','l', 'm', 'n', 'ñ','o', 
              'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z','A', 'B', 'C', 
              'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'Ñ','O', 'P', 'Q',
              'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z','_', '{', '}','0','1','2','3','4','5','6','7','8','9',
              '+','/','=']


gram_array_no_changes=['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k','l', 'm', 'n', 'ñ','o', 
              'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z','A', 'B', 'C', 
              'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'Ñ','O', 'P', 'Q',
              'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z','_', '{', '}','0','1','2','3','4','5','6','7','8','9',
              '+','/','=']

def get_initial_rotations(encrypted_password):
    last_char = encrypted_password[-1]
    encrypted_password = encrypted_password[:-1]  
    
    mid_index = round(len(encrypted_password) / 2)
    first_part = encrypted_password[:mid_index]
    second_part = encrypted_password[mid_index:]
    
    if last_char == '1':
        longer_part = first_part if len(first_part) > len(second_part) else second_part
        initial_rotations = int(longer_part[0])
        encrypted_password = encrypted_password[:mid_index] + encrypted_password[mid_index + 1:]
    elif last_char == '2':
        initial_rotations = int(first_part[-1] + second_part[0])
        encrypted_password = first_part[:-1] + second_part[1:]
    elif last_char == '3':
        initial_rotations = int(first_part[-2] + first_part[-1] + second_part[0])
        encrypted_password = first_part[:-2] + second_part[1:]
    else:
        raise ValueError("Carácter final inválido")
    return initial_rotations, encrypted_password


def reverse_base64(password_with_hexa):
    bytes_word = base64.b64decode(password_with_hexa.encode('utf-8'))
    return bytes_word

def reverse_rotation(hex_password, rotations):
    hex_password = binascii.unhexlify(hex_password).decode('utf-8')
    rotationsP=0
    with open("PimosKey.txt", "r") as file:
        rotationsP= int(file.readline())

    allrotations=rotationsP+rotations
    rotated=rotated_array(gram_array,allrotations)
    rotated2=rotated_array(gram_array,rotations)
    new_password = ""  
    for array_input in hex_password:
        index = rotated.index(array_input)
        new_password = new_password + "" + rotated2[index]#
    return new_password

def reverseHex(password_hex):
    hex_password = binascii.unhexlify(password_hex).decode('utf-8')
    return hex_password


def rotated_array(gram_array, rotacion):
    if(rotacion>=88):
        rotacion-=88
    rotated_array = gram_array[rotacion:]
    without_f_l=rotated_array[:-rotacion]
    without_first=gram_array[-rotacion:]
    without_last=gram_array[:rotacion]
    gram_array=without_first+without_last+without_f_l
    return gram_array

def inverse_rotated(password_with_rotations,initial_rotations):
    rotated = rotated_array(gram_array, initial_rotations)  
    new_password = ""  
    for array_input in password_with_rotations:
        index = rotated.index(array_input)
        new_password = new_password + "" + gram_array_no_changes[index]
    return new_password


def decodify(input):
    initial_rotations, cleaned_password = get_initial_rotations(input)
    hex_password = reverse_base64(cleaned_password)
    rotated_password = reverse_rotation(hex_password, initial_rotations)
    wihtout_rotations_primes=reverseHex(rotated_password)
    passowrd=inverse_rotated(wihtout_rotations_primes,initial_rotations)
    return passowrd


print(decodify("MzQzNjM3MzIzNjMxMzY2NTM2MzMzNjM5MzczMzM2MzMzNjY2MzQ2NDM2NjUzNjMxMzczNTM2MzUzNjYzMzczMDM2MzUzNzMyMzYzNTM3NjEzNjM0MzYzNTM2NjMzNjM1MzY2NjM2NjUzNjY0MzYzMTM3MzIzNjM5MzY2NjM2MzIzNjYzMzYzMTM2MzQzNjM5MzY2NDM2MzkzNzMyMzYzNzM2MzEzNjYzMzczNjM2MzUzNzYxMzczNjM2MzUzNjYzMzYzMTM3NjEzNzMxMzczNTM2MzUzNzMzMzY2NDM2MzUzNjY1MzYzNDM2MzUzNjYzMzczMzM3MzMzNjM4MzY2NjM2NjUzNjMxMzY2MzM2MzUzNzMzMzczMzM2MzEzNjY1MzYzNDM3MzIzNjY2MzczNDM2MzEzNjY0MzYzMjM3MzIzNjM5Mzc2MTM3MzQzNjY2MzczMjM3MzIzNjM1MzczMzMzMzEzMzMyMzMzMzMzMzQzMzMxMzMzNDMzMzIzMzMzMzMzMzMzMzQzMzMxMzMzMTMzMzIzNjM0MzYzMTM0MzYzNzMyMzYzMTM2NjUzNjMzMzYzOTM3MzMzNjMzMzY2NjM0NjQzNjY1MzYzMTM3MzUzNjM1MzY2MzM3MzAzNjM1MzczMjM2MzUzNzYxMzYzNDM2MzUzNjYzMzYzNTM2NjYzNjY1MzY2NDM2MzEzNzMyMzYzOTM2NjYzNjMyMzY2MzM2MzEzNjM0MzYzOTM2NjQzNjM5MzczMjM2MzczNjMxMzY2MzM3MzYzNjM1Mzc2MTM3MzYzNjM1MzY2MzM2MzEzNzYxMzczMTM3MzUzNjM1MzczMzM2NjQzNjM1MzY2NTM2MzQzNjM1MzY2MzM3MzMzNzMzMzYzODM2NjYzNjY1MzYzMTM2NjMzNjM1MzczMzM3MzMzNjMxMzY2NTM2MzQzNzMyMzY2NjM3MzQzNjMxMzY2NDM2MzIzNzMyMzYzOTM3NjEzNzM0MzY2NjM3MzIzNzMyMzYzNTM3MzMzMzMxMzMzMjMzMzMzMzM0MzMzMTMzMzQzMzMyMzMzMzMzMzMzMzM0MzMzMTMzMzEzMzMyMzYzNDM2MzEzNDM2MzczMjM2MzEzNjY1MzYzMzM2MzkzNzMzMzYzMzM2NjYzNDY0MzY2NTM2MzEzNzM1MzYzNTM2NjMzNzMwMzYzNTM3MzIzNjM1Mzc2MTM2MzQzNjM1MzY2MzM2MzUzNjY2MzY2NTM2NjQzNjMxMzczMjM2MzkzNjY2MzYzMjM2NjMzNjMxMzYzNDM2MzkzNjY0MzYzOTM3MzIzNjM3MzYzMTM2NjMzNzM2MzYzNTM3NjEzNzM2MzYzNTM2NjMzNjMxMzc2MTM3MzEzNzM1MzYzNTM3MzMzNjY0MzYzNTM2NjUzNjM0MzYzNTM2NjMzNzMzMzczMzM2MzgzNjY2MzY2NTM2MzEzNjYzMzYzNTM3MzMzNzMzMzYzMTM2NjUzNjM0MzczMjM2NjYzNzM0MzYzMTM2NjQzNjMyMzczMjM2MzkzNzYxMzczNDM2NjYzNzMyMzczMjM2MzUzNzMzMzMzMTMzMzIzMzMzMzMzNDMzMzEzMzM0MzMzMjMzMzMzMzMzMzMzNDMzMzEzMzMxMzMzMjM2MzQzNjMxMzQzNjM3MzIzNjMxMzY2NTM2MzMzNjM5MzczMzM2MzMzNjY2MzQ2NDM2NjUzNjMxMzczNTM2MzUzNjYzMzczMDM2MzUzNzMyMzYzNTM3NjEzNjM0MzYzNTM2NjMzNjM1MzY2NjM2NjUzNjY0MzYzMTM3MzIzNjM5MzY2NjM2MzIzNjYzMzYzMTM2MzQzNjM5MzY2NDM2MzkzNzMyMzYzNzM2MzEzNjYzMzczNjM2MzUzNzYxMzczNjM2MzUzNjYzMzYzMTM3NjEzNzMxMzczNTM2MzUzNzMzMzY2NDM2MzUzNjY1MzYzNDM2MzUzNjYzMzczMzM3MzMzNjM4MzY2NjM2NjUzNjMxMzY2MzM2MzUzNzMzMzczMzM2MzEzNjY1MzYzNDM3MzIzNjY2MzczNDM2MzEzNjY0MzYzMjM3MzIzNjM5Mzc2MTM3MzQzNjY2MzczMjM3MzIzNjM1MzczMzMzMzEzMzMyMzMzMzMzMzQzMzMxMzMzNDMzMzIzMzMzMzMzMzMzMzQzMzMxMzMzMTMzMzIzNjM0MzYzMTM0MzYzNzMyMzYzMTM2NjUzNjMzMzYzOTM3MzMzNjMzMzY2NjM0NjQzNjY1MzYzMTM3MzUzNjM1MzY2MzM3MzAzNjM1MzczMjM2MzUzNzYxMzYzNDM2MzUzNjYzMzYzNTM2NjYzNjY1MzY2NDM2MzEzNzMyMzYzOTM2NjYzNjMyMzY2MzM2MzEzNjM0MzYzOTM2NjQzNjM5MzczMjM2MzczNjMxMzY2MzM3MzYzNjM1Mzc2MTM3MzYzNjM1MzY2MzM2MzEzNzYxMzczMTM3927MzUzNjM1MzczMzM2NjQzNjM1MzY2NTM2MzQzNjM1MzY2MzM3MzMzNzMzMzYzODM2NjYzNjY1MzYzMTM2NjMzNjM1MzczMzM3MzMzNjMxMzY2NTM2MzQzNzMyMzY2NjM3MzQzNjMxMzY2NDM2MzIzNzMyMzYzOTM3NjEzNzM0MzY2NjM3MzIzNzMyMzYzNTM3MzMzMzMxMzMzMjMzMzMzMzM0MzMzMTMzMzQzMzMyMzMzMzMzMzMzMzM0MzMzMTMzMzEzMzMyMzYzNDM2MzEzNDM2MzczMjM2MzEzNjY1MzYzMzM2MzkzNzMzMzYzMzM2NjYzNDY0MzY2NTM2MzEzNzM1MzYzNTM2NjMzNzMwMzYzNTM3MzIzNjM1Mzc2MTM2MzQzNjM1MzY2MzM2MzUzNjY2MzY2NTM2NjQzNjMxMzczMjM2MzkzNjY2MzYzMjM2NjMzNjMxMzYzNDM2MzkzNjY0MzYzOTM3MzIzNjM3MzYzMTM2NjMzNzM2MzYzNTM3NjEzNzM2MzYzNTM2NjMzNjMxMzc2MTM3MzEzNzM1MzYzNTM3MzMzNjY0MzYzNTM2NjUzNjM0MzYzNTM2NjMzNzMzMzczMzM2MzgzNjY2MzY2NTM2MzEzNjYzMzYzNTM3MzMzNzMzMzYzMTM2NjUzNjM0MzczMjM2NjYzNzM0MzYzMTM2NjQzNjMyMzczMjM2MzkzNzYxMzczNDM2NjYzNzMyMzczMjM2MzUzNzMzMzMzMTMzMzIzMzMzMzMzNDMzMzEzMzM0MzMzMjMzMzMzMzMzMzMzNDMzMzEzMzMxMzMzMjM2MzQzNjMxMzQzNjM3MzIzNjMxMzY2NTM2MzMzNjM5MzczMzM2MzMzNjY2MzQ2NDM2NjUzNjMxMzczNTM2MzUzNjYzMzczMDM2MzUzNzMyMzYzNTM3NjEzNjM0MzYzNTM2NjMzNjM1MzY2NjM2NjUzNjY0MzYzMTM3MzIzNjM5MzY2NjM2MzIzNjYzMzYzMTM2MzQzNjM5MzY2NDM2MzkzNzMyMzYzNzM2MzEzNjYzMzczNjM2MzUzNzYxMzczNjM2MzUzNjYzMzYzMTM3NjEzNzMxMzczNTM2MzUzNzMzMzY2NDM2MzUzNjY1MzYzNDM2MzUzNjYzMzczMzM3MzMzNjM4MzY2NjM2NjUzNjMxMzY2MzM2MzUzNzMzMzczMzM2MzEzNjY1MzYzNDM3MzIzNjY2MzczNDM2MzEzNjY0MzYzMjM3MzIzNjM5Mzc2MTM3MzQzNjY2MzczMjM3MzIzNjM1MzczMzMzMzEzMzMyMzMzMzMzMzQzMzMxMzMzNDMzMzIzMzMzMzMzMzMzMzQzMzMxMzMzMTMzMzIzNjM0MzYzMTM0MzYzNzMyMzYzMTM2NjUzNjMzMzYzOTM3MzMzNjMzMzY2NjM0NjQzNjY1MzYzMTM3MzUzNjM1MzY2MzM3MzAzNjM1MzczMjM2MzUzNzYxMzYzNDM2MzUzNjYzMzYzNTM2NjYzNjY1MzY2NDM2MzEzNzMyMzYzOTM2NjYzNjMyMzY2MzM2MzEzNjM0MzYzOTM2NjQzNjM5MzczMjM2MzczNjMxMzY2MzM3MzYzNjM1Mzc2MTM3MzYzNjM1MzY2MzM2MzEzNzYxMzczMTM3MzUzNjM1MzczMzM2NjQzNjM1MzY2NTM2MzQzNjM1MzY2MzM3MzMzNzMzMzYzODM2NjYzNjY1MzYzMTM2NjMzNjM1MzczMzM3MzMzNjMxMzY2NTM2MzQzNzMyMzY2NjM3MzQzNjMxMzY2NDM2MzIzNzMyMzYzOTM3NjEzNzM0MzY2NjM3MzIzNzMyMzYzNTM3MzMzMzMxMzMzMjMzMzMzMzM0MzMzMTMzMzQzMzMyMzMzMzMzMzMzMzM0MzMzMTMzMzEzMzMyMzYzNDM2MzEzNDM2MzczMjM2MzEzNjY1MzYzMzM2MzkzNzMzMzYzMzM2NjYzNDY0MzY2NTM2MzEzNzM1MzYzNTM2NjMzNzMwMzYzNTM3MzIzNjM1Mzc2MTM2MzQzNjM1MzY2MzM2MzUzNjY2MzY2NTM2NjQzNjMxMzczMjM2MzkzNjY2MzYzMjM2NjMzNjMxMzYzNDM2MzkzNjY0MzYzOTM3MzIzNjM3MzYzMTM2NjMzNzM2MzYzNTM3NjEzNzM2MzYzNTM2NjMzNjMxMzc2MTM3MzEzNzM1MzYzNTM3MzMzNjY0MzYzNTM2NjUzNjM0MzYzNTM2NjMzNzMzMzczMzM2MzgzNjY2MzY2NTM2MzEzNjYzMzYzNTM3MzMzNzMzMzYzMTM2NjUzNjM0MzczMjM2NjYzNzM0MzYzMTM2NjQzNjMyMzczMjM2MzkzNzYxMzczNDM2NjYzNzMyMzczMjM2MzUzNzMzMzMzMTMzMzIzMzMzMzMzNDMzMzEzMzM0MzMzMjMzMzMzMzMzMzMzNDMzMzEzMzMxMzMzMjM2MzQzNjMx3"))



