# Code by @AmirMotefaker
# Random Password Generator


settings = {
    'lower': True,
    'upper': True,
    'symbol': True,
    'number': True,
    'space': False,
    'length': 8
}

def get_yes_or_no_for_settings(option, default):
    while True:
        user_input = input(f'Include {option}? (Defualt is {default}) (y: yes, n:no): ' )

        if user_input == 'y' or user_input == 'n':
            if user_input == 'y':
                return True
            else:
                return False
        else:
            print('Invalid input. Please try again.')



def get_settings_from_user(settings):
    
    for option, default in settings.items():
        if option != 'length':
            get_yes_or_no_for_settings(option, default)
           

get_settings_from_user(settings)

print(settings)
