import re
import random

# The Taiwan ID contains 1 English letter and 9 arabic numerals.
pattern_string = '[A-Z][0-9]{9}'
pattern = re.compile(pattern_string)
multiplier = '19876543211'

def check_born_place(input_string):
    """
    To check where he or she was born.\n
    The return value is a tuple containing a string and a integer.\n
    The string indicates the birthplace.\n
    The integer is used for validation.\n
    Return 'None' if not matched.
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
        return None

def check_gender(input_string):
    """
    To check the gender.\n
    Return 'None' if failed.
    """
    n = input_string[1]
    if n == '1':
        return 'male'
    elif n == '2':
        return 'female'
    else:
        return None

def compute(input_num):
    s = 0
    for i in range(11):
        s += int(input_num[i]) * int(multiplier[i])
    
    return True if s % 10 == 0 else False

if __name__ == '__main__':
    input_string = input('Enter your ID (case-sensitive): ')
    # The following content is for educational purposes only.
    # Do not use it for illegal activities.
    # It might takes much time.
    if input_string == 'Make me one!':
        fake = str()

        fake += random.choice('ABCDEFGHIJKLMNOPQRSTUVWXYZ')
        fake += random.choice('12')
        for i in range(7):
            fake += random.choice('0123456789')

        fake += str(0)
        place, place_num = check_born_place(fake)
        gender = check_gender(fake)
        fake_num = str(place_num) + fake[1:10]
        while not compute(fake_num):
            fake_num[10] = str(int(fake_num[10]) + 1)
        
        print('As you wish.')
        print(fake)
        print('This person was born in ' + place + ', and is ' + gender + '.')
    else:
        # To check if the string is valid.
        result = re.match(pattern, input_string)
        if result == None:  
            print('Invalid!')
        else:
            place, place_num = check_born_place(input_string)
            gender = check_gender(input_string)

            if place == None or gender == None:
                print('Invalid!')
            else:
                input_num = str(place_num) + input_string[1:10]
                result = compute(input_num)
                
                if result:
                    print('Valid!')
                    print('This person was born in ' + place + ', and is ' + gender + '.')
                else:
                    print('Invalid!')
