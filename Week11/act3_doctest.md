Error: The answer for the test factorial(34) was wrong. 
Should be 295232799039604140847618609643520000000

Doctest is used to test if functions within the code are running correctly
by writing example calculations directly in quoted description texts.
Python detects this and automatically runs the examples to make sure the 
function returns the correct answers.

What is being tested: The factorial function where the function multiplies all the numbers
below a given number until it reaches 1. Also does data validation checks to make sure
errors are caught and handled properly.

The first check stops the user from using negative numbers
The second check makes sure user is using whole numbers and no decimals greater than zero
The third check prevents the program from crashing if user enters a very large number
