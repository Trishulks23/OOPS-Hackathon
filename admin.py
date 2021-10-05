import getpass
import sys
import csv
from colorama import Fore, Style


class admin:
    def __init__(self):
        if(self.__verify_cred()):
            print(Fore.GREEN + "Authentication successful!" + Style.RESET_ALL)
            self.__do_operations(True)

        else:
            print(Fore.LIGHTRED_EX +
                  "Authentication unsuccessful!" + Style.RESET_ALL)

    #  private verify cred method
    def __verify_cred(self):
        username = input("Username: ")
        pass1 = getpass.getpass("Password: ")
        # delete username and password input from stdout
        sys.stdout.write("\033[F \033[F")
        if(username.lower() == "trishul" and pass1 == "pass1"):
            return True
        else:
            return False

    def __do_operations(self, authorized=False):
        if((authorized) or self.__verify_cred()):
            print("Operations: \n" + Fore.YELLOW + "1" + Style.RESET_ALL + ". Add Donation Camps\n" + Fore.YELLOW + "2" + Style.RESET_ALL + ". View Donation Camps\n" + Fore.YELLOW + "3" + Style.RESET_ALL +
                  ". Add Hospitals\n" + Fore.YELLOW + "4" + Style.RESET_ALL + ". View Hospitals\n" + Fore.YELLOW + "5" + Style.RESET_ALL + ". View Donors\n" + Fore.YELLOW + "6" + Style.RESET_ALL + ". View Requests")
            while(True):
                choice = input(
                    "Choose an operation: ")
                if choice == '1':
                    self.__add_bloodCamp()
                elif choice == '2':
                    self.__view_bloodCamps()
                elif choice == '3':
                    self.__add_hospital()
                elif choice == '4':
                    self.__view_hospitals()
                elif choice == '5':
                    self.__view_donors()
                elif choice == '6':
                    self.__view_requests()
                else:
                    print("Exiting Admin access.")
                    break

    def __add_bloodCamp(self):
        name = input("Name of Blood Donation Camp: ")
        loc = input(f"Location of {name}: ")
        with open('bloodCamps.csv', 'a', newline='') as csvfile:
            writer = csv.writer(csvfile, delimiter=' ',
                                quotechar='|', quoting=csv.QUOTE_MINIMAL)
            writer.writerow([name, loc])

    def __view_bloodCamps(self):
        with open('bloodCamps.csv', newline='') as csvfile:
            reader = csv.reader(csvfile, delimiter=' ', quotechar='|')
            print("Blood Donation camps:")
            c = 0
            for row in reader:
                print("\t" + str(c := c+1) + f". {row[0]}, {row[1]}")

    def __add_hospital(self):
        name = input("Name of Hospital: ")
        loc = input(f"Location of {name}: ")
        with open('hospitals.csv', 'a', newline='') as csvfile:
            writer = csv.writer(csvfile, delimiter=' ',
                                quotechar='|', quoting=csv.QUOTE_MINIMAL)
            writer.writerow([name, loc])

    def __view_hospitals(self):
        with open('hospitals.csv', newline='') as csvfile:
            reader = csv.reader(csvfile, delimiter=' ', quotechar='|')
            print("Hospitals:")
            c = 0
            for row in reader:
                print("\t" + str(c := c+1) + f". {row[0]} {row[1]}")

    def __view_donors(self):
        with open('donors.csv', newline='') as csvfile:
            reader = csv.reader(csvfile, delimiter=' ', quotechar='|')
            c = 0
            for row in reader:
                print("\t" + str(c := c+1) +
                      f". {row[1]}, {row[3]}, {row[0]}, {row[2]} years old, Contact: {row[4]}")

    def __view_requests(self):
        with open('requests.csv', newline='') as csvfile:
            reader = csv.reader(csvfile, delimiter=' ', quotechar='|')
            c = 0
            for row in reader:
                print("\t" + str(c := c+1) +
                      f". {row[1]}, Required: {row[0]} litres, Contact: {row[2]}, Emergency: {row[3]}")
