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
        user_input = input(f'Include {option}? (Defualt is {default}) (y: yes, n:no, enter: default): ' )

        if user_input == '':
            return default

        if user_input in ['y', 'n']:
            return user_input == 'y'
            
        print('Invalid input. Please try again.')
          

def get_settings_from_user(settings):
    
    for option, default in settings.items():
        if option != 'length':
            user_choice = get_yes_or_no_for_settings(option, default)
            print(user_choice)
           

get_settings_from_user(settings)
