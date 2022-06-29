# Code by @AmirMotefaker

# Random Password Generator

import random
import string
import os

settings = {
    'lower': True,
    'upper': True,
    'symbol': True,
    'number': True,
    'space': False,
    'length': 8,
}

PASSWORD_MIN_LENGTH = 4
PASSWORD_MAX_LENGTH = 30


def clear_screen():
    os.system('cls')


def get_user_password_length(option, default, pw_min_length=PASSWORD_MIN_LENGTH, pw_max_length=PASSWORD_MAX_LENGTH):
    while True:
        user_input = input('Enter password length. '
                          f'(Defualt is {default}) (enter: default): ')

        if user_input == '':
            return default
        
        if user_input.isdigit():
            user_password_length = int(user_input)
            if pw_min_length <= user_password_length <= pw_max_length:
                return(int(user_input))
            print('Invalid input.')
            print('Password length should be '
                 f' between {pw_min_length} and {pw_max_length}.')
        else:
            print('Invalid input. You should enter a number.')

        print('Please try again.')


def get_yes_or_no_for_settings(option, default):
    while True:
        user_input = input(f'Include {option}? '
                           f' (Defualt is {default}) '
                            ' (y: yes, n:no, enter: default): ' )

        if user_input == '':
            return default

        if user_input in ['y', 'n']:
            return user_input == 'y'
            
        print('Invalid input. Please try again.')
          

def get_settings_from_user(settings):
    
    for option, default in settings.items():
        if option != 'length':
            user_choice = get_yes_or_no_for_settings(option, default)
            settings[option] = user_choice
        else:
            user_password_length = get_user_password_length(option, default)
            settings[option] = user_password_length


def get_random_upper_case():
    return random.choice(string.ascii_uppercase)

def get_random_lower_case():
    return random.choice(string.ascii_lowercase)
    
def get_random_number():
    return random.choice('0123456789')

def get_random_symbol():
    return random.choice("""~`!@#$%^&*()_+-=|\}]{["':;?/>.<,""")


def generate_random_char(choices):
    choice = random.choice(choices)

    if choice == 'upper':
        return get_random_upper_case()
    if choice == 'lower': 
        return get_random_lower_case()
    if choice == 'symbol':
        return get_random_symbol()
    if choice == 'number':
        return get_random_number()
    if choice == 'space':
        return ' '
 

def password_generator(settings):
    final_password = ''
    password_length = settings['length']

    choices = list(filter(lambda x: settings[x], ['lower', 'upper', 'symbol','number', 'space']))
    for i in range(password_length):
        final_password += generate_random_char(choices)

    return final_password


def password_generator_loop(settings):
    while True:
        print('-'*20)
        print(f'Generated Password: {password_generator(settings)}')
   
        while True:
            want_another_password = input('Do you want another password? (y: yes, n: no, enter: yes): ')
            if want_another_password in ['y', 'n','']:
                if want_another_password == 'n':
                    return
                break
            else:
                print('Invalid input. (Choose from y: yes, n: no, enter: yes).')
                print('Please try again.')


def run():
    clear_screen()
    get_settings_from_user(settings)
    password_generator_loop(settings)
  

run()
