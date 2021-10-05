from admin import admin

if __name__ == "__main__":
    while(True):
        choice = input("1. Admin\n2. User\n")
        if choice == '1':
            ad = admin()

        else:
            break
