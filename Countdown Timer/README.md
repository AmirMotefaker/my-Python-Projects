# Countdown Timer

## Prerequisites:

    sudo apt-get install python3-tkinter
    
    pip install plyer
    
    
 >> Project Structure:
 
    1- Importing modules: time, tkinter, and plyer:
      
      from plyer import notification: Plyer is a library that provides us with features to access bluetooth, wifi, battery details, send emails, gps and so on. Here we         use notification to provide desktop notifications that get displayed on completion of python countdown timer.
      
      from tkinter import messagebox: To display prompts, we use messagebox. It can create messageboxes for errors, to display information, ask questions etc.
      
      From tkinter import *: We make use of Tkinter to create the user interface for the application. Tkinter is suitable for beginners and contains many widgets.
      
      Import time: To create a delay between every second, we use time module
      
    
    2- Initializing the window and declaring the dimensions
    
        Window = Tk(): Tkinter class, Tk() is assigned to an object window. We use this python countdown timer window to set components on the object such as text             boxes, buttons etc
        
        window.geometry(): Specify the length and the breadth of the application window of the application using geometry.
        
        window.title(): Specify the title of the application. It is optional
        
                
    
    3- Defining functions for timer and placeholders
    
        def h_click(event): We add a placeholder in the hours, minutes and seconds entry widgets. Hence when the user selects an entry widget, the placeholder is               removed by deleting using entry_widget.entry(0,’end’), where 0 is the start of the placeholder character and ‘end’ denotes the end of the placeholder string.           Similarly we extend this for minutes and seconds entry widget mouse clicks
        
        def show_entry_fields(): Declaration of function to invoke the timer.
        
        timer_time: Set timer variable to contain the duration of the user timer in seconds. An hour contains 3600 seconds and a minute contains 60 seconds                     respectively. Thus we multiply hours with 3600 and minutes with 60, sum them up with the seconds
        
        try…except : If a user enters an integer, the try block will not pass into the except block. This is because we set the hour, minute and second variables to           integer data type. If the user gives a float number or it is left empty, a warning will pop up
        
        If timer_time > 0: A timer can start only when the user enters a minimum of 1 second
        
        hour =0, min =0, sec =0: Declaration and initialisation of variables
        
        while timer_time >= 0: The loop decrements timer_time until it reaches 0 which marks the end of the time delay.
        
        min, sec: Converting timer_time to minutes and seconds to display on the app. divmod(value, divisor) is a function that returns 2 values. The first value is           the quotient of the division of timer_time by 60 and the second value is the remainder obtained during the division.
        
        if min > 60: If minutes is greater than 60, it is converted to hours and minutes using hour, min = divmod(min,60)
        
        hours.set(hour), mins.set(min), secs.set(sec): Set the obtained hours, minutes and seconds to the integer variables declared outside the function.
        
        time.sleep(1): Creates a delay of 1 second
        
        timer_time -= 1: Decrement the timer_time by 1 to simulate the countdown timer
        
        notification.notify(): Creates a desktop notification. It takes the parameters: title – title of the alert, message – message of the notification, app_icon –           (optional), a picture or icon, timeout – the duration after which the notification elapses. Replace the path for app_icon with your icon’s absolute path.
        
        messagebox.showinfo(): A prompt box which serves as a notification in the python countdown timer app.
        
            
    4- Creating the user input interface
    
       title_label: To display non-editable text in the countdown timer window, we use labels. Label() has 2 mandatory parameters: window and text to display. Position        the label or any widget using pack().
       
       IntVar(): Declaring integer variables for hours, minutes and seconds. A prompt, in the try..except of the timer function, is raised if the user gives decimals          or other characters.
       
       Entry(): To take user input, we use Entry widget. The parameters are window, width of the entry field, textvariable which denotes the integer variable declared        previously. Font styling is optional.
       
       hour_entry.insert(): To insert a placeholder of 00 starting with the index 0. We extend the same for minutes and seconds entry widgets.
       
       hour_entry.place(): Similar to pack(), place() is another positioning function. This function takes 2 parameters which is the distances from the left margin and        the top margin as coordinates (x,y)
       
       hour_entry.bind(): Removal of the placeholder when the mouse clicks on the entry fields. <1> indicates mouse button 1 which is the left click.
       
           
    5- Addition of a button to activate the timer
    
       Button(): When the user selects or clicks on a button, a function is called. Thus to call functions or a specific task based on user input (interaction), we            make use of buttons.
