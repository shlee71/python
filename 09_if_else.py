input_id = input('Name : ')
input_pass = input('Pass : ')
my_name = 'shlee'
my_pass = 'password'
if input_id == my_name and input_pass == my_pass:
    print('Welcome Mr. '+input_id+' !!! ')
elif input_id == my_name and input_pass != my_pass:
    print('Your password is not correct, Mr. '+input_id)
else:
    print('Who are you, mr. '+input_id)
