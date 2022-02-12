#Password Generator Project
import random, sys
import pandas as pd

# standard letters, symbols and numbers
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

# get details of password required
print("Welcome to the Password Memory Generator and Viewer!")

# make password
def password_generator(): 
    list_password = []
    for n in range(0,nr_letters - (nr_symbols+nr_numbers)):
      a = random.choice(letters)
      list_password += a
    for n in range(0,nr_symbols):
      b = random.choice(symbols)
      list_password += b
    for n in range(0,nr_numbers):
      c = random.choice(numbers)
      list_password += c
    
    random.shuffle(list_password)

    readable_password = ""
    return (readable_password.join(list_password))


option = input("Do you wish to make new password or see the old ones? Type 'new' to make new password or 'view' to view old ones: ")
if (option == 'view'):
    # print the password list
    result = pd.read_csv('PasswordMemory.csv')
    print(result)

elif (option == 'new') :

    nr_letters= int(input("How many letters would you like in your password?\n")) 
    nr_symbols = int(input(f"How many symbols would you like?\n"))
    nr_numbers = int(input(f"How many numbers would you like?\n"))
    # get the desired row data into a list
    row_data = []
    row_data.append(input('If you wish please enter the common name of the website else hit enter key :'))
    row_data.append(input('If you wish please enter the username else hit enter key :'))
    password = password_generator()
    row_data.append(password)
    row_data.append(input('If you wish please copy paste the website link/url else hit enter key :'))


    #header = ("SNo","Common_Name", "Username", "Password", "Weblink")

    # make data
    data = {
            "Common Name": [row_data[0]],
            "Username": [row_data[1]],
            "Password": [row_data[2]],
            "Weblink": [row_data[3]]
            }

    # Make data frame of above data
    df = pd.DataFrame(data)

    # append data frame to CSV file
    df.to_csv('PasswordMemory.csv', mode='a', index=False, header=False)

    print(f"Your password is:- \n {password}")

else:
    print('There is a spelling mistake. Please run the program again. Make sure that only view or new is typed in all  small letters')
