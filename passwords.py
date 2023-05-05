from cryptography.fernet import Fernet

'''def write_key():
    key = Fernet.generate_key()
    with open("key.key", 'wb') as key_file:
        key_file.write(key)'''

def load_key():
    file = open("key.key", 'rb')
    key = file.read()
    file.close()
    return key

key = load_key()
fer = Fernet(key)


def add():
    user = input("please enter your user name: ")
    pwd = input("please enter the password")

    with open("password.txt", 'a') as f:
       f.write(user + "%" + fer.encrypt(pwd.encode()).decode() + '\n')

def view():
    with open("password.txt", 'r') as f:
        for line in f.readlines():
            data = line.rstrip()
            user, passwd = data.split("%")
            print("user:" + user + " password:" + fer.decrypt(passwd.encode()).decode())

while True:
    mode = input("Do you want to add a new password or view the existing ones?(add/view). Type q to quit").lower()
    if mode=="q":
        break

    if mode=="add":
        add()
    elif mode=="view":
        view()
    else:
        print("invalid mode chosen")
        continue