
import hashlib

# files
def create_files():
    try:
        f = open("data_base.txt", "r")
        f.close()
    except:
        f = open("data_base.txt", "w")
        f.close()
        rewrite_config(False, "None")
    
    try:
        f = open("configure.txt", "r")
        f.close()
    except:
        f = open("configure.txt", "w")
        f.close()
        rewrite_config(False, "None")

def check_login(login, file_name = "data_base.txt"):
    f = open(file_name, "r")
   
    for i in f:
        if i[1:i.find(":")] == login:
            f.close()
            return False
    f.close()
    return True

def write_new_user(login, password, file_name = "data_base.txt"):
    f = open(file_name, "a")
    f.write("{" + str(login) + ":" + str(password) + "}" + "\n")
    f.close()

def rewrite_config(autorized, login, file_name = "configure.txt"):
    f = open(file_name, "w")
    f.write(f"AUTORISED {autorized}\n")
    f.write(f"LOGIN {login}\n")
    f.close()

def get_login(file_name = "configure.txt"):
    f = open(file_name, "r")
    for i in f:
        if i[:i.find(" ")] == "LOGIN":
            return i[i.find(" ") + 1 : i.find("\n")]
    return "None"

def try_entrance(login, password, file_name = "data_base.txt"):
    f = open(file_name, "r")
    password = hash_string(password)
    for i in f:
        cur_login = i[1:i.find(':')]
        cur_password = i[i.find(':')+1:i.find('}')]
        if cur_login == login and cur_password == password:
            f.close()
            return True
    f.close()
    return False

def get_autorised(file_name = "configure.txt"):
    f = open(file_name, "r")
    line = f.readline()
    f.close()
    if line[line.find(' ') + 1:line.find("\n")] == 'True':
        return True
    return False

def change_autorised(autorised, file_name = "configure.txt"):
    login = "None"
    f = open(file_name, "r")
    for i in f:
        if i[:i.find(" ")] == "LOGIN":
            login = i[i.find(" ") + 1 : i.find("\n")]

    rewrite_config(autorised, login)   

def change_login_conf(login, file_name = "configure.txt"):
    autorised = ""
    f = open(file_name, "r")
    for i in f:
        if i[:i.find(" ")] == "AUTORISED":
            autorised = i[i.find(" ") + 1 : i.find("\n")]

    rewrite_config(autorised, login)   

def change_password(login, new_password, file_name = "data_base.txt"):
    f = open(file_name, "r")
    lines = f.readlines()
    f.close()

    f = open(file_name, "w")
    for i in lines:
        if i[1:i.find(":")] == login:
            i = "{" + login + ":" + hash_string(new_password) + "}\n"
        f.write(i)
    f.close()


# hash
def hash_string(string):
    return hashlib.sha256(string.encode()).hexdigest()


# check
def check_symbols(string):
    if ":" in string or "}" in string or "{" in string:
        return False
    return True
