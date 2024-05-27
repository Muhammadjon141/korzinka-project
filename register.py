import classes

def register_page():
    first_name = input("Ismingizni kiriting: ")
    last_name = input("Familiyangizni kiriting: ")
    card_number = input("Karta raqamingizni kiriting: ")
    phone_number = input("Telefon raqamingizni kiriting: ")
    try:
        if card_number.isdigit() and phone_number.isdigit():
            if len(card_number) == 16:
                if len(phone_number) == 9:
                    if classes.Korzinka.check_new_user(card_number, phone_number):
                        return classes.Korzinka.insert_new_user(first_name, last_name, card_number, phone_number)
                    else:
                        print("Bunday foydalanuvchi mavjud! ")
                        return register_page()
                else:
                    print("Telefon raqam 9 xonalik raqam bo'lishi kerak!")
                    return register_page()
            else:
                print("Karta raqam 16 xonalik raqam bo'lishi kerak!")
                return register_page()
        else:
            print("Faqat son kiriting!")
            return register_page()
    except:
        print("No'to'g'ri ma'lumotlar kiritildi! ")
        return register_page()