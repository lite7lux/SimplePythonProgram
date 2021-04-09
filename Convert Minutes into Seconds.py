#Convert Minutes into Seconds
#Write a function that takes an integer minutes and converts it to seconds.

# minutes to seconds convert function
def convert(minutes):
    seconds = minutes*60	
    return seconds

#printing and testing 
print(convert(5))
print(convert(3))
print(convert(2))