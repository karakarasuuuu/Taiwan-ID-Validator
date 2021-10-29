import re
import random

# The Taiwan ID contains 1 English letter and 9 arabic numerals.
pattern_string = '[A-Z][0-9]{9}'
pattern = re.compile(pattern_string)
multiplier = '19876543211'

def check_born_place(input_string: str) -> tuple:
    """
    To check where he or she was born.\n
    The return value is a tuple containing a string and a integer.\n
    The string indicates the birthplace.\n
    The integer is used for validation.\n
    Return None if not matched.
    """
    c = input_string[0]
    if c == 'A':
        return 'Taipei City', 10
    elif c == 'B':
        return 'Taichung City', 11
    elif c == 'C':
        return 'Keelung City', 12
    elif c == 'D':
        return 'Tainan City', 13
    elif c == 'E':
        return 'Kaohsiung City', 14
    elif c == 'F':
        return 'New Taipei City', 15
    elif c == 'G':
        return 'Yilan County', 16
    elif c == 'H':
        return 'Taoyuan City', 17
    elif c == 'I':
        return 'Chiayi City', 34
    elif c == 'J':
        return 'Hsinchu County', 18
    elif c == 'K':
        return 'Miaoli County', 19
    elif c == 'L':
        return 'Taichung County', 20
    elif c == 'M':
        return 'Nantou County', 21
    elif c == 'N':
        return 'Changhua County', 22
    elif c == 'O':
        return 'Hsinchu City', 35
    elif c == 'P':
        return 'Yunlin County', 23
    elif c == 'Q':
        return 'Chiayi County', 24
    elif c == 'R':
        return 'Tainan County', 25
    elif c == 'S':
        return 'Kaohsiung County', 26
    elif c == 'T':
        return 'Pingtung County', 27
    elif c == 'U':
        return 'Hualien County', 28
    elif c == 'V':
        return 'Taitung County', 29
    elif c == 'W':
        return 'Kinmen County', 32
    elif c == 'X':
        return 'Penghu County', 30
    elif c == 'Y':
        return 'Yangmingshan Management Bureau', 31
    elif c == 'Z':
        return 'Lienchiang County', 33
    else:
        # Should not happen
        return None, None # The return value is a tuple containing two values

def check_gender(input_string: str) -> str:
    """
    To check the gender.\n
    Return None if failed.
    """
    n = input_string[1]
    if n == '1':
        return 'male'
    elif n == '2':
        return 'female'
    else:
        return None

def check_identity(input_string: str) -> str:
    """
    To check the identity.\n
    Return None if failed.
    """
    n = input_string[2]
    if n == '6':
        return 'a foreigner with nationality'
    elif n == '7':
        return 'a national without household registration'
    elif n == '8':
        return 'from Hong Kong or Macau'
    elif n == '9':
        return 'from China'
    elif n == '0' \
      or n == '1' \
      or n == '2' \
      or n == '3' \
      or n == '4' \
      or n == '5':
        return 'a normal national'
    else:
        # Should not happen
        return None

def compute_checksum(input_num: list) -> bool:
    s = 0
    for i in range(11):
        s += int(input_num[i]) * int(multiplier[i])
    
    return True if s % 10 == 0 else False

def id_validator(input_string: str):

    # The following content is for educational purposes only.
    # Do not use it for illegal activities.
    # It might takes much time.
    if input_string == 'MAKE ME ONE!':

        fake = str()

        fake += random.choice('ABCDEFGHIJKLMNOPQRSTUVWXYZ')
        fake += random.choice('12')
        fake += random.choice('0123456789')
        for i in range(6):
            fake += random.choice('0123456789')

        i = 0
        fake += str(i)
        place, place_num = check_born_place(fake)
        gender = check_gender(fake)
        identity = check_identity(fake)
        fake_num = str(place_num) + fake[1:10]
        while not compute_checksum(fake_num):
            i += 1
            fake_num = list(fake_num)
            fake_num.pop()
            fake_num = ''.join(fake_num) + str(i)
        
        fake = list(fake)
        fake.pop()
        fake = ''.join(fake) + str(i)
        
        # Printing result
        print() # A blank line for typesetting.
        print('As you wish.')
        print() # A blank line for typesetting.
        print(fake + ', this ' + gender + ' person was registered in ' + place + ', and is ' + identity + '.')
        print() # A blank line for typesetting.

    else:
        # To check if the string is valid.
        result = re.fullmatch(pattern, input_string) # Use fullmatch instead of match to avoid cases that are more than 10 characters
        
        if result == None:  
            print() # A blank line for typesetting.
            print('Invalid! Does not match the format!')
            print() # A blank line for typesetting.
        
        else:
            place, place_num = check_born_place(input_string)
            gender = check_gender(input_string)
            identity = check_identity(input_string)

            if place == None:
                print() # A blank line for typesetting.
                print('Invalid birthplace! Please try again.')
                print() # A blank line for typesetting.
                return

            if gender == None:
                print() # A blank line for typesetting.
                print('Invalid gender! Please try again.')
                print() # A blank line for typesetting.
                return

            if identity == None:
                print() # A blank line for typesetting.
                print('Invalid identity! Please try again.')
                print() # A blank line for typesetting.
                return

            input_num = str(place_num) + input_string[1:10]
            result = compute_checksum(input_num)
            
            if result:
                print() # A blank line for typesetting.
                print('Valid!')
                print(input_string + ', this ' + gender + ' person was registered in ' + place + ', and is ' + identity + '.')
                print() # A blank line for typesetting.
            else:
                print() # A blank line for typesetting.
                print('Invalid!')
                print() # A blank line for typesetting.

