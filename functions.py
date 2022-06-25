#To do
#2's complement range
#binary_to_hex conversions error



from numpy import real


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

    index = 0
    sentence = []

    if len(binary) % 7 == 0:
    
        while(index + 6 < len(binary) - 1):    #21  0 - 6, 7 - 13 , 14 - 20
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


if __name__ == "__main__" :
    print(string_to_binary('hello'))
    
    print(binary_to_string('0110100001100101011011000110110001101111'))
    
    
    
