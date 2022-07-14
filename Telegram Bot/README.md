# Telegram Bot

>> Requirements:

      A Telegram Account: If you don’t have the Telegram app installed just download it from the play store.
      After downloading create an account using your mobile number just like WhatsApp.
    
     .python-telegram-bot module: Here we will need a module called python-telegram-bot, This library provides
     a pure Python interface for the Telegram Bot API. It’s compatible with Python versions 3.6.8+. In addition
     to the pure API implementation, this library features a number of high-level classes to make the development
     of bots easy and straightforward. These classes are contained in the “telegram.ext” submodule.
     
     
 >> Step by Step:

      After opening an account on Telegram, in the search bar at the top search for “BotFather”

      Click on the ‘BotFather’ (first result) and type /newbot
      
      Give a unique name to your bot. After naming it, Botfather will ask for its username. 
      Then also give a unique name BUT remember the username of your bot must end with the bot, like my_bot, hellobot etc.
      
      After giving a unique name and if it gets accepted you will get a message something
      
      
      
 >> Step by Step implementation:
 
 
      1- Importing required libraries:
      
                  Updater: This will contain the API key we got from BotFather to specify in which bot we are adding functionalities to using our python code.
                  
                  Update: This will invoke every time a bot receives an update i.e. message or command and will send the user a message.
                  
                  CallbackContext: We will not use its functionality directly in our code but when we will be adding the dispatcher it is required (and it will work                            internally)
                  
                  CommandHandler: This Handler class is used to handle any command sent by the user to the bot, a command always starts with “/” i.e “/start”,”/help”                            etc.
                  
                  MessageHandler: This Handler class is used to handle any normal message sent by the user to the bot,
                  
                  FIlters: This will filter normal text, commands, images, etc from a sent message.
                  
                  
       2- Define functions for operation:
       
                  Start function
                  
                  Help function
                  
                  Adding some more functionalities to the Bot. like Gmail, YouTube, LinkedIn,...
                  
                  
                  
       3- Adding the Handlers to handle our messages and commands      
       
       
       4- Running the bot
                  
            
      
      
    
    
