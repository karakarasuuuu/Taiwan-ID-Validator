import validator

if __name__ == '__main__':

    while True:

        input_string = input('Enter an ID to validate.\nEnter "exit" to exit.\n(case-insensitive): ').upper()

        if input_string == 'EXIT': break
        else: validator.id_validator(input_string)
        