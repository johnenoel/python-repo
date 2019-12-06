# Ask the user fo rname

name= input("What is your name?:")

# Ask the user for age
age = input("What is your age?:")

# Ask the user for city
city = input("where city do you live in?:")

# Ask the user for what he/she enjoys
love = input("what do you enjoy or love doing?:")

# Create output text
string = "Your name is {} and you are {} years old. You live in {} and you love {}"
output = string.format(name,age,city,love)

# Print output to screen
print(output)
