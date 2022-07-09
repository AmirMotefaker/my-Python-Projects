# Address Book

>> prerequisite:

    pip install tkinter
    
## Step by Step:

  1. Importing module
  

  2. Initializing window:

      Tk() use to initialized tkinter
      
      geometry() sets the window width and height
      
      title() used to set window’s tiltle
      
      resizable(0,0) this command stop window to resize
      
      bg use to set the background color of the window
      
      Contacts’ information is stored in contactlist
      
      Frame is like a container that is used to organized widgets
      
      Here Scrollbar widget and Listbox widget is used to allow users to select from many options
      
      
  3. Define functions:

      Selected() function used to return selected value
      
      Addcontact() function used to add new contact
      
      EDIT() function will edit existing contact
      
      DELETE() function will delete selected contact
      
      VIEW() function will view selected contact
      
      EXIT() used to destroy mainloop
      
      RESET() will set the name and number field to empty string
      
      Select_set() will sort the manage the contactlist and also used in other functions
      
      
 4. Define buttons and labels:
 
      Label() widget used when we want to display text
      
      Entry() widget used when we want to create an input text field.
      
      Button() widget used to display button
      
          root is the name of our window
          
          text which display on the label as title of that label
          
          font in which form the text will be write
          
          textvariable used to retrieve the text to entry widget
          
          place() – place widgets at specific position
          
          command called the specific function when the button will clicked
