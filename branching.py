# A time traveler has suddenly appeared in your classroom!

# Create a variable representing the traveler's
# year of origin (e.g., year = 2000)
# and greet our strange visitor with a different message
# if he is from the distant past (before 1900),
# the present era (1900-2020) or from the far future (beyond 2020).

year = int(input("Greetings! What is your year of origin?"))

if year <= 1900:
    print ("Woah, that's the past!")
elif year > 1900 and year < 2020:
    print ("That's totally the present!")
else:
    print ("Far out, that's the future!!")

#Removed "=" on line 9
#Added parenthesis after "int" on line 9
#Replaced signle quote with double quote at the end of line 9
#Added ":" to line 11
#Added double quotes on line 12
#Removed a single & on line 13
#Changed elif to else on line 15
