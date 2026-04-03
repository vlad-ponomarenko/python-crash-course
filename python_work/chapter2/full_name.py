first_name = "ada"
last_name = "lovelace"
full_name=f"{first_name} {last_name}"
print(full_name)
print(f"Hello, {full_name.title()}!")
print("\tPython")
print("Languages:\nPython\nC\nJavaScript")
print("Languages:\n\tPython\n\tC\n\tJavaScript")
favourite_language = ' python '
print(favourite_language.lstrip())
print(favourite_language.rstrip())
print(favourite_language.strip())


# This code is responsible for assigning a website to a variable, then creating new variable for a link wtihout prefix. 
nostarch_url = 'https://nostarch.com'
simple_url = nostarch_url.removeprefix('https://')
# Print link without prefix 
print(simple_url)


# This represents a message that contains a syntax error 
message = 'One of Python's strengths is its diverse community.'
print(message)