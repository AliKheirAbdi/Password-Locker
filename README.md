# Password-Vault :closed_lock_with_key:


## Project pre-discription
It becomes really hard to remember all those passwords and create new ones for all apps we use.
This app helps a user save and generate passwords.
# Author
[Ali Kheir](https://github.com/AliKheirAbdi)

## Author details
* Email: akheirali(@)gmail.com

# Description 
This project lets a user save login credentials for any application.
Once they create a username and password they can add an app and the program saves the credentials.
One has the choice to either input their own password or opt for a system generated one.
A user can also delete an existing entry.
## Screenshot
![image](https://github.com/AliKheirAbdi/Password-Locker/blob/master/DeepinScreenshot_select-area_20191006112629.png)
# User stories
The user would like to.... :

1) create a password locker account with my details, a login username and password.
2) store my already existing account credentials in the application. Assuming I already have a twitter account, I want to store my already existing twitter username and password in the application.
3) create new account credentials in the application. For example, if I have not yet signed up for Instagram, I would want to create a credentials account for Instagram in the application and the application generates a password for me to use when I sign up for Instagram.
4) have the option of putting in a password that I want to use for the new credential account. For example, when creating my Instagram credential account, I want to have an option of putting in the password I want to use instead of having the application generate a password for me.
5) view my various account credentials and their passwords in the application.
6) Delete a credentials account that I no longer need in the application.
# Set-up and installation instructions
 ### You need to have the following installed
  * Python3.7
  * Pip
  * x-clip
  * Pyfiglet
  * Pyperclip
  
 ### Cloning
 
Open Terminal {Ctrl+Alt+T}

git clone https://github.com/AliKheirAbdi/Password-Locker.git

cd Password-Locker

code . or atom . based on the text editor you have.
 ### Running the Application
  To run the application, open the cloned file in terminal and run the following commands:

    $ chmod +x run.py
    $ ./run.py
  To run test for the application $ python3.7 user-test.py
# Behaviour driven development
| Behaviour                          | Input                               | Output  |
| ---:                               | ---:                                | ---:    |
| Run the application in the terminal| chmod +x run.py followed by ./run.py | App runs |
| App asks for user name             | Enter user name | App asks for password |
| App prompts password or use user customized| Enter password | App displays a welcome note |
| App proceeds to list an option for user interactions| select short code | prompts generated |
| Short code NC - create new account | app name and password | user app and password displayed |
| Short code VC-view user accounts | - | Displays a list of accounts created and their passwords|| Short code DEL - delete accounts | account and password of app to be deleted| deletes app | 

## Known bugs
- currently the app does not display saved credentials
- Does not reject duplicate entries

## Technologies used
* Python

# Development
Do you wish to contribute to this App,
* Fork the repo
* Create a new branch 
* Navigate to the branch
* Make appropriate changes to the files
* Add changes to reflect changes made.
* Commit your changes
* Push to the chosen git branch
* Create a pull request
* Request is reviewed and published once approved

# License
MIT license
Copyright 2019 -- Ali Kheir
