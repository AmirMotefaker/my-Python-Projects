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


def ask_if_change_settings(settings):
    while True:
        user_answer = input('Do you want to change default settings? (y: yes, n: no, enter: yes): ')

        if user_answer in ['y', 'n','']:
            if user_answer in ['y','']:
                print('-'*5, 'Change Settings', '-'*5, sep='')
                get_settings_from_user(settings)
            break
        else:
            print('Invalid input.')
            print('Please try again.')


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


def ask_user_to_generate_another_password():
    while True:
        user_answer = input('Regenerate? (y: yes, n: no, enter: yes): ')

        if user_answer in ['y', 'n','']:
            if user_answer == 'n':
                return False
            return True
        else:
            print('Invalid input.')
            print('Please try again.')


def password_generator_loop(settings):
    while True:
        print('-'*20)
        print(f'Generated Password: {password_generator(settings)}')
   
        if ask_user_to_generate_another_password() == False:
            break

        
def run():
    clear_screen()
    ask_if_change_settings(settings)
    password_generator_loop(settings)
    print('Thank you for choosing us.')
  

run()
