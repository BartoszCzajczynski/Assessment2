class Contact:

    def __init__(self, name, address, phone_number, dob):
        self.__name = name
        self.__address = address
        self.__phone_number = phone_number
        self.__dob = dob

    def get_name(self):
        return self.__name

    def get_address(self):
        return self.__address

    def get_phone_number(self):
        return self.__phone_number

    def get_dob(self):
        return self.__dob

    def get_details(self):
        return [self.__name, self.__address, self.__phone_number, self.__dob]

    def set_name(self, new_name):
        if not any(char.isdigit() for char in str(new_name)):
            print("Success")
            self.__name = new_name
        else:
            print("Incorrect Entry")
            print("(Only Alphabet Characters)")
            print("(To cancel input 'cancel')")
            retry = input("Input: ")#Incorrect Entry (Needs to be a string) (To cancel input 'cancel') Input:
            if retry == "cancel":
                print("Cancelled")
            else:
                self.set_name(retry)


    def set_address(self, new_address):
        separated_address = new_address.split(",")
        if len(separated_address) == 4:
            print("Success")
            self.__address = new_address
        else:
            print("Incorrect Entry")
            print("(Needs to be, 'Name/Number,Street,Town,Postcode')")
            print("(To cancel input 'cancel')")
            retry = input("Input: ")  # Incorrect Entry (Needs to be a string) (To cancel input 'cancel') Input:
            if retry == "cancel":
                print("Cancelled")
            else:
                self.set_address(retry)

    # number,street,town,postcode

    def set_phone_number(self, new_phone_number):
        if str(new_phone_number).isdigit() and len(new_phone_number) == 11:
            print("Success")
            self.__phone_number = new_phone_number
        else:
            print("Incorrect Entry")
            print("(Needs to be an 11 Digit Number)")
            print("(To cancel input 'cancel')")
            retry = input("Input: ")  # Incorrect Entry (Needs to be a string) (To cancel input 'cancel') Input:
            if retry == "cancel":
                print("Cancelled")
            else:
                self.set_phone_number(retry)

    def set_dob(self, new_dob):
        separated_dob = new_dob.split("/")
        if len(separated_dob) == 3 and len(separated_dob[0]) == 2 and len(separated_dob[1]) == 2 and len(separated_dob[2]) == 4:
            print("Success")
            self.__dob = new_dob
        else:
            print("Incorrect Entry")
            print("(Needs to be Day/Month/Year, 'XX/XX/XXXX')")
            print("(To cancel input 'cancel')")
            retry = input("Input: ")  # Incorrect Entry (Needs to be a string) (To cancel input 'cancel') Input:
            if retry == "cancel":
                print("Cancelled")
            else:
                self.set_dob(retry)

