#To do
#2's complement range




base_64_binary_dict = {'A':0, 'B':1, 'C':2, 'D':3, 'E':4, 'F':5, 'G':6, 'H':7, 'I':8, 'J':9, 'K':10, 'L':11, 'M':12, 'N':13,
                       'O':14, 'P':15, 'Q':16, 'R':17, 'S':18, 'T':19, 'U':20, 'V':21, 'W':22, 'X':23, 'Y':24, 'Z':25,
                       'a':26, 'b':27, 'c':28, 'd':29, 'e':30, 'f':31, 'g':32, 'h':33, 'i':34, 'j':35, 'k':36, 'l':37,
                       'm':38, 'n':39, 'o':40, 'p':41, 'q':42, 'r':43, 's':44, 't':45, 'u':46, 'v':47, 'w':48, 'x':49,
                       'y':50, 'z':51, '0':52, '1':53, '2':54, '3':55, '4':56, '5':57, '6':58, '7':59, '8':60, '9':61,
                       '+':62, '/':63, '=':000000}



base_64_dict = {0: 'A', 1: 'B', 2: 'C', 3: 'D', 4: 'E', 5: 'F', 6: 'G', 7: 'H', 8: 'I', 9: 'J', 10: 'K', 11: 'L',
                12: 'M', 13: 'N',
                14: 'O', 15: 'P', 16: 'Q', 17: 'R', 18: 'S', 19: 'T', 20: 'U', 21: 'V', 22: 'W', 23: 'X', 24: 'Y',
                25: 'Z', 26: 'a',
                27: 'b', 28: 'c', 29: 'd', 30: 'e', 31: 'f', 32: 'g', 33: 'h', 34: 'i', 35: 'j', 36: 'k', 37: 'l',
                38: 'm', 39: 'n',
                40: 'o', 41: 'p', 42: 'q', 43: 'r', 44: 's', 45: 't', 46: 'u', 47: 'v', 48: 'w', 49: 'x', 50: 'y',
                51: 'z', 52: '0',
                53: '1', 54: '2', 55: '3', 56: '4', 57: '5', 58: '6', 59: '7', 60: '8', 61: '9', 62: '+', 63: '/'
                }


unreadable_ASCII_dict = {1: '~START OF HEADING~',
              2: '~START OF TEXT~', 3: '~END OF TEXT~', 4: '~END OF TRANSMISSION~', 5: '~ENQUIRY~', 6: '~ACKNOWLEDGE~',
              7: '~BELL~',
              8: '~BACKSPACE~', 9: '    ', 10: '~NEW LINE~', 11: '~VERTICAL TAB~', 12: '~NEW PAG~',
              13: '~CARRIAGE RETURN~',
              14: '~SHIFT OUT~', 15: '~SHIFT IN~', 16: '~DATA LINK ESCAPE~', 17: '~DEVICE CONTROL 1~',
              18: '~DEVICE CONTROL 2~',
              19: '~DEVICE CONTROL 3~', 20: '~DEVICE CONTROL 4~', 21: '~NEGATIVE ACKNOLWLEDGE~',
              22: '~SYNCHRONOUS IDLE~',
              23: '~END OF TRANS. BLOCK~', 24: '~CANCEL~', 25: '~END OF MEDIUM~', 26: '~SUBSTITUTE~', 27: '~ESCAPE~',
              28: '~FILE SEPARATOR~', 29: '~GROUP SEPARATOR~', 30: '~RECORD SEPARATOR~', 31: '~UNIT SEPARATOR~', 32: '~space~',
              127: '~DEL~'}


def char_to_ASCII(letter):
    #input letter (char) -> output ASCII value (int)
    try:
        return ord(letter)

    except:
            return '#'


def ASCII_to_char(ASCIIcode):
    #input ASCII value (int) -> output letter (char)
    try:
        if ASCIIcode > 32 and ASCIIcode != 127:
            return chr(ASCIIcode)
            
        else:
            return unreadable_ASCII_dict[ASCIIcode]

    except:
        return '#'


def no_to_binary(number):
    #input number (int / float) output binary(string)
    
    try:
        if number - int(number) == 0:
            return str(bin(number))[2:]
        else:
            
            realPart = str(int(float(number)))
            lengthReal = len(realPart)
            realPart = int(realPart)

            fractionPart = str(number)[lengthReal+1 : ]
            fractionPart = int(fractionPart)

            return str(bin(realPart))[2:] + '.' + str(bin(fractionPart))[2:]
    except:
        return '#'


def binary_to_no(binary):
    #input binary stream (int / float) -> output int / float 
    
    try:
        binary = str(binary)
        binary = binary.split('.')

        if len(binary) == 1:

            return int(binary[0], 2)

        elif len(binary) == 2:
            
            realPart = binary[0]
            fractionPart = binary[1]

            realPart = int(realPart,2)
            fractionPart = '0.' + str(int(fractionPart,2))

            fractionPart = float(fractionPart)
        
            return int(realPart) + fractionPart

        
    except:
        return '#'
   
    
def char_to_binary(letter):
    #input char -> output binry (string)
    try:
        
        ASCII_code = char_to_ASCII(letter)

        return no_to_binary(ASCII_code)
    
    except:
        return '#'

def binary_to_char(binary):
    #input binary (string) -> output char 
    try:
        ASCII_code = binary_to_no(binary)

        return ASCII_to_char(ASCII_code)

    except:
            return '#'
    



def binary_to_hex(binary):
     #input binary -> output hex (string)

    try:

    
        decimal = str(binary_to_no(binary))
        decimal = decimal.split('.')

        if len(decimal) == 1:
            return hex(int(decimal[0]))[2:]
        
        elif len(decimal) == 2:

            realPart = decimal[0]
            fractionPart = decimal[1]

            realPart = hex(int(realPart))[2:]
            fractionPart =  hex(int(fractionPart))[2:]

            

            return realPart + '.' + fractionPart

    except:
        return '#'


def hex_to_binary(hexNo):
    #input hex (string) -> output binary (string)
    try:

        hexNo = hexNo.split('.')

        if len(hexNo) == 1:
            decimal = int(hexNo[0], 16)
            binary = no_to_binary(decimal)
            while len(binary) < 4:
                binary = '0' + binary

            return binary

        elif len(hexNo) ==2 :
            realPart = int(hexNo[0], 16)
            fractionPart = int(hexNo[1], 16)

            realPart = no_to_binary(realPart)
            fractionPart = no_to_binary(fractionPart)

            

            while len(realPart) % 4 != 0:
            
                realPart = '0' + realPart

            while len(fractionPart) % 4 != 0:
                fractionPart =  '0' + fractionPart 

            
            return realPart + '.' + fractionPart
            

    except:
        return '#'
    

def string_to_binary(sentence):
    #input string -> output binary (string)
    try:

        binarySentence = []

        for letter in sentence:
            binaryChar = char_to_binary(letter)

            while len(binaryChar) < 8:
                binaryChar = '0' + binaryChar

            binarySentence.append(binaryChar)
        
        return binarySentence
        
    except:
        return '#'


        
def binary_to_string(binary):
    #input 7-bit or 8-bit binary (string) -> output equivalent string

    try:
        index = 0
        sentence = []

        if len(binary) % 7 == 0:
        
            while(index  < len(binary) - 1):    #21  0 - 6, 7 - 13 , 14 - 20
                letter = binary[index: index + 7]
                sentence.append(binary_to_char(letter))
                index += 7

            return sentence

        elif len(binary) % 8 == 0:
            while(index < len(binary) - 1):    #24  0 - 7, 8 - 15 , 16 - 23
                letter = binary[index: index + 8]  #we don't counter last boundary with us
                sentence.append(binary_to_char(letter))
                index += 8

            return sentence

        else:
            return '#'

    except:
        return '#'
    
'''
def binary_to_base64(binary):
    #input binary -> output base64
    try:    
        index = 0
        sentence = []

        if len(sentence) % 6 == 0:
            
            while(index  < len(binary) - 1):    
                letter = binary[index: index + 6] #we don't take last boundary
                sentence.append(binary_to_base64[binary_to_no(letter)])
                index += 6  

            return sentence

        else:
            return '#'

    except:
        return '#'

'''



    
    
