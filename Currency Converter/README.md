# Currency Converter 

>> Prerequisites:

    tkinter – For User Interface (UI)

    requests – to get url
    
## Step by Step:

1. Real-time Exchange rates:

    To get real-time exchange rates, we will use: https://api.exchangerate-api.com/v4/latest/USD
    
    Base – USD: It means we have our base currency USD. which means to convert any currency we have to first convert it to USD then from USD, we will convert it in whichever currency we want.
    
    Date and time: It shows the last updated date and time.
    
    Rates: It is the exchange rate of currencies with base currency USD.
    
   
2. Import the libraries


3. Create the CurrencyConverter class:

    create the constructor of class.
  
    Convert() method:
  
        From_currency: currency from which you want to convert.
    
        to _currency: currency in which you want to convert.
    
        Amount: how much amount you want to convert.
    
    Example:

        url = 'https://api.exchangerate-api.com/v4/latest/USD'
        
        converter = RealTimeCurrencyConverter(url)
        
        print(converter.convert('INR','USD',100))
        
      OUTPUT: 1.33
      
      
4. Now let’s create a UI for the currency converter

    Converter: Currency Converter object which we will use to convert currencies. Above code will create a Frame.
    
    add the CONVERT button
    
      perform() method:
      
        The perform method will take the user input and convert the amount into the desired currency and display it on the converted_amount entry box.
        
       
5. Let’s create the main function.

     First, we will create the Converter. Second, Create the UI for Converter
    
    

