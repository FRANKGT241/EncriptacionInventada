
import binascii
from sympy import isprime
import base64
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
character_no=0

def rotated_array(gram_array, rotacion):#Funcion para generar las rotacoines del arreglo
    if(rotacion>=88):
        rotacion-=88
    rotated_array = gram_array[rotacion:]
    without_f_l=rotated_array[:-rotacion]
    without_first=gram_array[-rotacion:]
    without_last=gram_array[:rotacion]
    gram_array=without_first+without_last+without_f_l
    return gram_array

def select_character_in_gram_rotated(passw_without_codify):#Genera la contraseña a partir de la primera rotacion
    global gram_array  
    global character_no
    number_of_rotates = len(passw_without_codify)
    character_no=number_of_rotates
    rotated = rotated_array(gram_array, number_of_rotates)  
    gram_array = rotated  
    new_password = ""  
    for array_input in passw_without_codify:
        index = gram_array_no_changes.index(array_input)#Toma la posicion letra por letra de la gramatica inicial
        new_password = new_password + "" + rotated[index]#Genera una nueva contraseña a bas de las posiciones de la gramtica anterior para generar una contraseña totalmente nueva
    return new_password

def select_character_in_gram_rotated_with_primes(passw_without_codify):#Genera la contraseña nueva a base de una rotacion condicional
    global gram_array  
    number_of_rotates = count_primes_in_length(passw_without_codify)
    rotated = rotated_array(gram_array, number_of_rotates)  
    new_password =""  
    for array_input in passw_without_codify:
        index = gram_array.index(array_input)#Toma la posicion letra por letra de la gramatica ya rotada
        new_password = new_password + "" + rotated[index]#Genera una nueva contraseña a bas de las posiciones de la gramtica anterior para generar una contraseña totalmente nueva
    with open("PimosKey.txt", "w") as f:#Guarda la cantidad de rotaciones en numeros primos
        f.write(str(number_of_rotates))
    return new_password


def count_primes_in_length(passw_without_codify):#Cuentas los numeros primos
    length = len(passw_without_codify)
    count = sum(1 for i in range(2, length+1) if isprime(i))
    return count

def generate_hexa(password):
    newpasword=select_character_in_gram_rotated(password)
    password_with_hexa  = binascii.hexlify(newpasword.encode()).decode()
    newpasword=select_character_in_gram_rotated_with_primes(password_with_hexa)
    password_with_hexa  = binascii.hexlify(newpasword.encode()).decode()
    return password_with_hexa

def generate_base64(password_with_hexa):#Generacion a Base64
    bytes_word = password_with_hexa.encode('utf-8')
    word_in_base64 = base64.b64encode(bytes_word)
    prepass=word_in_base64.decode('utf-8')
    
    return prepass

def save_key_N_characters(pre_final_password, character_no):#Funcion para concatenar los digitos de rotacion
    character_no_str = str(character_no)
    final_concat=str(len(character_no_str))#Cantidad de digitos de rotacion incial
    final_password = pre_final_password[:len(pre_final_password) // 2] + character_no_str + pre_final_password[len(pre_final_password) // 2:]+final_concat #donde se concatena
    return final_password




def password_codify(password):
    hexa=generate_hexa(password)
    pref=generate_base64(hexa)
    final_passowrd=save_key_N_characters(pref,character_no)
    return final_passowrd

password = "FranciscoMnauelperezdeleonmariobladimirgalvezvelazquesmendelsshonalessandrotambriztorres1234142334112daFranciscoMnauelperezdeleonmariobladimirgalvezvelazquesmendelsshonalessandrotambriztorres1234142334112daFranciscoMnauelperezdeleonmariobladimirgalvezvelazquesmendelsshonalessandrotambriztorres1234142334112daFranciscoMnauelperezdeleonmariobladimirgalvezvelazquesmendelsshonalessandrotambriztorres1234142334112daFranciscoMnauelperezdeleonmariobladimirgalvezvelazquesmendelsshonalessandrotambriztorres1234142334112daFranciscoMnauelperezdeleonmariobladimirgalvezvelazquesmendelsshonalessandrotambriztorres1234142334112daFranciscoMnauelperezdeleonmariobladimirgalvezvelazquesmendelsshonalessandrotambriztorres1234142334112daFranciscoMnauelperezdeleonmariobladimirgalvezvelazquesmendelsshonalessandrotambriztorres1234142334112daFranciscoMnauelperezdeleonmariobladimirgalvezvelazquesmendelsshonalessandrotambriztorres1234142334112da"

print(password_codify(password))


