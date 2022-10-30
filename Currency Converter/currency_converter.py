# Code by @AmirMotefaker

# Currency Converter - Advanced

# # Solution 1
import requests
from tkinter import *
import tkinter as tk
from tkinter import ttk

class RealTimeCurrencyConverter():
    def __init__(self,url):
        self.data= requests.get(url).json()
        self.currencies = self.data['rates']


def convert(self, from_currency, to_currency, amount): 
    initial_amount = amount 
    #first convert it into USD if it is not in USD.
    # because our base currency is USD
    if from_currency != 'USD' : 
        amount = amount / self.currencies[from_currency] 
  
    # limiting the precision to 4 decimal places 
    amount = round(amount * self.currencies[to_currency], 4) 
    return amount


def __init__(self, converter):
    tk.Tk.__init__(self)
    self.title = 'Currency Converter'
    self.currency_converter = converter


    self.geometry("500x200")
    #Label
    self.intro_label = Label(self, text = 'Welcome to Real Time Currency Convertor',  fg = 'blue', relief = tk.RAISED, borderwidth = 3)
    self.intro_label.config(font = ('Courier',15,'bold'))
    self.date_label = Label(self, text = f"1 Indian Rupee equals = {self.currency_converter.convert('INR','USD',1)} USD \n Date : {self.currency_converter.data['date']}", relief = tk.GROOVE, borderwidth = 5)
    self.intro_label.place(x = 10 , y = 5)
    self.date_label.place(x = 170, y= 50)

    # Entry box
    valid = (self.register(self.restrictNumberOnly), '%d', '%P')
    # restricNumberOnly function will restrict thes user to enter invavalid number in Amount field. We will define it later in code
    self.amount_field = Entry(self,bd = 3, relief = tk.RIDGE, justify = tk.CENTER,validate='key', validatecommand=valid)
    self.converted_amount_field_label = Label(self, text = '', fg = 'black', bg = 'white', relief = tk.RIDGE, justify = tk.CENTER, width = 17, borderwidth = 3)
    
    # dropdown
    self.from_currency_variable = StringVar(self)
    self.from_currency_variable.set("INR") # default value
    self.to_currency_variable = StringVar(self)
    self.to_currency_variable.set("USD") # default value
    
    font = ("Courier", 12, "bold")
    self.option_add('*TCombobox*Listbox.font', font)
    self.from_currency_dropdown = ttk.Combobox(self, textvariable=self.from_currency_variable,values=list(self.currency_converter.currencies.keys()), font = font, state = 'readonly', width = 12, justify = tk.CENTER)
    self.to_currency_dropdown = ttk.Combobox(self, textvariable=self.to_currency_variable,values=list(self.currency_converter.currencies.keys()), font = font, state = 'readonly', width = 12, justify = tk.CENTER)
    
    # placing
    self.from_currency_dropdown.place(x = 30, y= 120)
    self.amount_field.place(x = 36, y = 150)
    self.to_currency_dropdown.place(x = 340, y= 120)
    #self.converted_amount_field.place(x = 346, y = 150)
    self.converted_amount_field_label.place(x = 346, y = 150)

    # Convert button
    self.convert_button = Button(self, text = "Convert", fg = "black", command = self.perform) 
    self.convert_button.config(font=('Courier', 10, 'bold'))
    self.convert_button.place(x = 225, y = 135)

def perform(self,):
        amount = float(self.amount_field.get())
        from_curr = self.from_currency_variable.get()
        to_curr = self.to_currency_variable.get()
 
        converted_amount= self.currency_converter.convert(from_curr,to_curr,amount)
        converted_amount = round(converted_amount, 2)
     
        self.converted_amount_field_label.config(text = str(converted_amount))

def restrictNumberOnly(self, action, string):
        regex = re.compile(r"[0-9,]*?(\.)?[0-9,]*$")
        result = regex.match(string)
        return (string == "" or (string.count('.') <= 1 and result is not None))

if __name__ == '__main__':
    url = 'https://api.exchangerate-api.com/v4/latest/USD'
    converter = RealTimeCurrencyConverter(url)
 
    App(converter)
    mainloop()



-------------------------------------------------------
# Solution 2
# import all functions from the tkinter 
from tkinter import *
  
# Create a GUI window
root = Tk()
  
# create a global variables 
variable1 = StringVar(root)
variable2 = StringVar(root)
  
# initialise the variables
variable1.set("currency")
variable2.set("currency")
  
      
# Function to perform real time conversion
# from one currency to another currency
def RealTimeCurrencyConversion():
  
    # importing required libraries
    import requests, json
  
    # currency code
    from_currency = variable1.get()
    to_currency = variable2.get()
  
    # enter your api key here 
    api_key = "6P33X446S50O8F86"  # https://www.alphavantage.co/support/#api-key
      
    # base_url variable store base url 
    #base_url = "https://api.exchangerate-api.com/v4/latest/"
    base_url = r"https://www.alphavantage.co/query?function=CURRENCY_EXCHANGE_RATE"
  
    # main_url variable store complete url
    main_url = base_url + "&from_currency=" + from_currency + "&to_currency=" + to_currency + "&apikey=" + api_key 
    req_ob = requests.get(main_url)
  
    # get method of requests module 
    # return response object 
    req_ob = requests.get(main_url)
  
    # json method converts json data type
    #into python dictionary data type
      
    # result contains list of nested dictionaries
    result = req_ob.json()
  
    # parsing the required information
    Exchange_Rate = float(result["Realtime Currency Exchange Rate"]
                                ['5. Exchange Rate'])
  
    # get method of Entry widget
    # returns current text  as a
    # string from text entry box.
    amount = float(Amount1_field.get())
  
    # calculation for the conversion
    new_amount = round(amount * Exchange_Rate, 3)
  
    # insert method inserting the 
    # value in the text entry box. 
    Amount2_field.insert(0, str(new_amount))
  
  
# Function for clearing the Entry field
def clear_all(): 
  Amount1_field.delete(0, END) 
  Amount2_field.delete(0, END)
     
  
# Driver code
if __name__ == "__main__" :
  
    # Set the background colour of GUI window 
    root.configure(background = 'light green') 
    
    # Set the configuration of GUI window (WidthxHeight)
    root.geometry("400x175") 
    
    # Create "welcome to Real Time Currency Convertor" label 
    headlabel = Label(root, text = 'welcome to Real Time Currency Convertor', 
                      fg = 'black', bg = "red") 
  
    # Create a "Amount :" label 
    label1 = Label(root, text = "Amount :",
                 fg = 'black', bg = 'dark green')
      
    # Create a "From Currency :" label 
    label2 = Label(root, text = "From Currency", 
                   fg = 'black', bg = 'dark green') 
    
    # Create a "To Currency: " label 
    label3 = Label(root, text = "To Currency :", 
                   fg = 'black', bg = 'dark green')
  
    # Create a "Converted Amount :" label 
    label4 = Label(root, text = "Converted Amount :", 
                   fg = 'black', bg = 'dark green')
  
    # grid method is used for placing 
    # the widgets at respective positions 
    # in table like structure.  
    headlabel.grid(row = 0, column = 1) 
    label1.grid(row = 1, column = 0) 
    label2.grid(row = 2, column = 0)
    label3.grid(row = 3, column = 0)
    label4.grid(row = 5, column = 0)
      
    # Create a text entry box 
    # for filling or typing the information. 
    Amount1_field = Entry(root) 
    Amount2_field = Entry(root)
       
    # ipadx keyword argument set width of entry space. 
    Amount1_field.grid(row = 1, column = 1, ipadx ="25") 
    Amount2_field.grid(row = 5, column = 1, ipadx ="25")
  
    # list of currency codes
    CurrenyCode_list = ["INR", "USD", "CAD", "CNY", "DKK", "EUR"]
  
    # create a drop down menu using OptionMenu function
    # which takes window name, variable and choices as
    # an argument. use * before the name of the list,
    # to unpack the values
    FromCurrency_option = OptionMenu(root, variable1, *CurrenyCode_list)
    ToCurrency_option = OptionMenu(root, variable2, *CurrenyCode_list)
      
    FromCurrency_option.grid(row = 2, column = 1, ipadx = 10)
    ToCurrency_option.grid(row = 3, column = 1, ipadx = 10)
      
    # Create a Convert Button and attach 
    # with RealTimeCurrencyExchangeRate function 
    button1 = Button(root, text = "Convert", bg = "red", fg = "black",
                                command = RealTimeCurrencyConversion)
      
    button1.grid(row = 4, column = 1)
  
    # Create a Clear Button and attach 
    # with delete function 
    button2 = Button(root, text = "Clear", bg = "red", 
                     fg = "black", command = clear_all)
    button2.grid(row = 6, column = 1)
    
    # Start the GUI 
    root.mainloop()
