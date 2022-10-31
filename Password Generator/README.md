# Password Generator

## Random Password Generator

>> User settings:

     Password length: 6

     Existence of upper case characters: Yes  (example: A,X,Z,...)

     Existence of lower case characters: Yes   (example: a,x,z,...)

     Existence of symbols: Yes   (example: %,&,*,...)

     Existence of numbers: Yes   (example: 3,9,1,...)

     Existence of empty space: No

> Program implementation process:

     1- Ask the user about the settings they want to apply
     
     2- The user changes the settings if desired
     
     3- We will create and display the password according to the said settings for him.
     
     4- If the user wants, we will create another password with the same settings.






## Password Generator - 2

>> Sep-by-Step

 1- Store all the characters as a list. We can use the string module of Python or type all of them.
 
 2- Ask the user to enter the length of the password.
 
 3- Shuffle the characters using the random.shuffle method.
 
 4- Initialize an empty list to store the password.
 
 5- Write a loop that iterates length times.
 
 6- Pick a random character from all the characters using the random.choice method.
 
 7- Append the random character to the password.
 
 8- Shuffle the resultant password list to make it more random.
 
 9- Convert the password list to string using the join method.
