import classes
import register
def main():
    temp = input(f"""
                 1. Login
                 2. Register
                   >>> """)
    if temp == "1":
        return login()
    elif temp == "2":
        return register.register_page()
    else:
        print("Bunday xizmat mavjud emas! ")
        return main()


def login():
    card_number = input("Karta raqamingizni kiriting: ")
    phone_number = input("Telefon raqamingizni kiriting: +998 >>> ")
    try:
        if card_number.isdigit() and phone_number.isdigit():
            if len(card_number) == 16:
                if len(phone_number) == 9:
                    return classes.Korzinka.check_users(card_number, phone_number)
                else:
                    print("Telefon raqam 9 xonalik raqam bo'lishi kerak!")
                    return login()
            else:
                print("Karta raqam 16 xonalik raqam bo'lishi kerak!")
                return login()
        else:
            print("Faqat son kiriting!")
            return login()
    except:
        print("No'to'g'ri ma'lumotlar kiritildi! ")
        return login()


if __name__ == "__main__":
    main()