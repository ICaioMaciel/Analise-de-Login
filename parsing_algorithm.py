import_file = "login_list.txt"

with open("Projetos Python\parsing algorithm\login_list.txt") as file:
    file_text = file.read()

usernames = file_text.splitlines()

def login_check(login_list, current_user):
    counter = 0
    for i in login_list:
        if i in current_user:
            counter += 1

    if counter >= 3:
        print('You have tried to login more than three times, your account is blocked...')
    else:
        print("Successful Login")
        
login_check(usernames, "joao.silva")