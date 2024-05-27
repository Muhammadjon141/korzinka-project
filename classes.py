import psycopg2 as psql
import first_page
import service
import products
import savdo
import admin
import register
import datetime
import json
 
class Online_market:
    def __init__(self, market_name, market_address, olchami) -> None:
        self.market_name = market_name
        self.market_address = market_address
        self.__olchami = olchami

    @property
    def get_olcham(self):
        return self.__olchami

    def __str__(self) -> str:
        return f"{self.market_name} {self.market_address} {self.get_olcham}"
    


class Korzinka(Online_market):
    def __init__(self, market_name, market_address, olchami, hisob_raqami) -> None:
        super().__init__(market_name, market_address, olchami)
        self.hisob_raqami = hisob_raqami

    @staticmethod
    def check_new_user(card_number, phone_number):
        query = "SELECT card_number, phone_number from users;"
        data = Korzinka.select(query)
        try:
            card_numbers = []
            phone_numbers = []
            for i in data:
                card_numbers.append(i[0])
                phone_numbers.append(i[1])
            if not int(card_number) in card_numbers and not int(phone_number) in card_numbers:
                return True
            else: 
             print("Bunday foydalanuchi mavjud !!")
             return register.register_page()    
        except:
            print("Bunday foydalanuchi mavjud !!")
            return register.register_page()


    @staticmethod
    def insert_new_user(first_name, last_name, card_number, phone_number):
        query1 = f"INSERT INTO users(first_name, last_name, card_number, phone_number, balanc, status) values('{first_name}', '{last_name}', '{card_number}', '{phone_number}', 10000, False)"
        if Korzinka.commit(query1):
            print("Muvaffaqiyatli ro'yhatdan o'tdingiz")
            return service.service(card_number, phone_number, first_name)

    @staticmethod
    def admin_select():
        table_name = input("Ko'rmoqchi bo'lgan jadvalingizni nomini kiriting: ")
        Table_name = table_name.lower()
        print(Korzinka.admin_select1(Table_name))

    @staticmethod
    def admin_select1(Table_name):
        try:
            query1 = f" SELECT column_name FROM information_schema.columns WHERE table_schema = 'public' AND table_name = '{Table_name}';"
            query = f"SELECT * FROM {Table_name};"
            data1 = Korzinka.select(query1)
            data2 = Korzinka.select(query)
            if data2 and data1:
                print(data1)
                # print(data2)
                for i in data2:
                    print(i)
                return admin.admin_page()
            else:
                print("Bunday jadval mavjud emas:")
                return Korzinka.admin_select()
        except:
            print("Bunday jadval mavjud emas!")
            return Korzinka.admin_select1(Table_name)

    @staticmethod
    def select(query):
        with open("parol.json", encoding="utf-8") as file:
            parol = json.load(file)
        try:
            db_connect = psql.connect(
                database = 'korzinka',
                user = 'postgres',
                host = 'localhost',
                password = f'{parol["password"]}',
                port = f'{parol["port"]}'
            )

            cursor = db_connect.cursor()
            cursor.execute(query)
            data = cursor.fetchall()
            return data
        except:
            return "Kod xato kiritildi !!!"

    @staticmethod
    def commit(query):
        try:
            db_connect = psql.connect(
                database = 'korzinka',
                user = 'postgres',
                host = 'localhost',
                password = '7982',
                port = '5432'
            )

            cursor = db_connect.cursor()
            cursor.execute(query)
            db_connect.commit()
            return True
        except:
            print("Kod xato kiritildi !!!")

    @staticmethod
    def check_users(card_number, phone_number):
        query = f"SELECT card_number, phone_number, first_name, status FROM users"
        data = Korzinka.select(query)
        for card_phone in data:
            if card_phone[0] == int(card_number):
                if card_phone[1] == int(phone_number):
                    first_name = card_phone[2]
                    if card_phone[3] is True:
                        return admin.admin_page()
                    else:
                        return service.service(card_phone, phone_number, first_name)
                else:
                     continue
            else:
                    continue
        else:
                print("Bunday foydalanuvchi mavjud emas!")
                return(first_page.login())
        
    @staticmethod
    def xizmatlar(card_number, phone_number, first_name):
        query = f"SELECT product_type FROM product_type"
        data = Korzinka.select(query)
        soni = []
        for i,j in zip(range(1, (len(data)+1)), data):
            soni.append(i)
            print(f"""{i}. {j[0]}""")
        print(f"""{i+1}. Qidirish""")
        print(f"""0. Orqaga qaytish""")
        try:    
            product_type = input("""
                          >>> """)
            if int(product_type) in soni:
                return products.product1(card_number, phone_number, first_name, product_type)
            elif int(product_type) == i+1:
                return Korzinka.search_product_type(card_number, phone_number, first_name)
            elif product_type == "0":
                return first_page.main()
            else:
                print("Bor bo'limlarni tanlang: ")
                return Korzinka.xizmatlar(card_number, phone_number, first_name)
        except:
            print("Bor bo'limlarni tanlang: ")
            return Korzinka.xizmatlar(card_number, phone_number, first_name)  

    @staticmethod
    def product(card_number, phone_number, first_name, product_type):
            query = f"SELECT PRODUCT_NAME, description, price, amount FROM products where product_type = {product_type};"
            data = Korzinka.select(query)
            soni = []
            for i,j in zip(range(1, (len(data)+1)), data):
                soni.append(i)
                print(f"""{i}. {j[0]} 
                    Mahsulot haqida ma'lumot: {j[1]}
                    Narxi: {j[2]}
                    Do'konda mavjud: {j[3]}""")
            print(f"""{i+1}.  Mahsulot qidirish""")
            print(f"""0. Orqaga qaytish""")   
            product = input("""     >>> """)
            try:
                if int(product) in soni:
                    return savdo.savdo1(card_number, phone_number, first_name, data, product, product_type)
                elif int(product) == i+1:
                    return Korzinka.search_product(card_number, phone_number, first_name, product_type)
                elif product == "0":
                    return Korzinka.xizmatlar(card_number, phone_number, first_name)
                else:
                    return Korzinka.product(card_number, phone_number, first_name, product_type)
            except:
                print("Son kiriting! ")
                return products.product1(card_number, phone_number, first_name, product_type)
            # except:
                # print("Xatolik")
                # return (products.products(a))

    @staticmethod
    def one_user_balanc(card_number, phone_number):
        query = f"select balanc from users where card_number = {card_number} and  phone_number = {phone_number};"
        user_balanc = Korzinka.select(query)
        return user_balanc

    @staticmethod
    def update_mahsulot(new_user_balanc, new_son_products, mahsulot_nomi, card_number, phone_number, first_name):
        card_number1 = card_number[0]
        query1 = f"update users set balanc = {new_user_balanc} where card_number = {card_number1} and phone_number = {phone_number};"
        query = f"update products set amount = {new_son_products} where product_name = '{mahsulot_nomi}';"
        if Korzinka.commit(query1):
            if Korzinka.commit(query):
                yana = input("""
                             1. Yana tanlash
                             2. Toxtatish
                                >>> """)
                if yana == "1":
                    print("To'lov muvaffaqiyatli amalga oshirildi")
                    return service.service(card_number, phone_number, first_name)
                else:
                    c1 = (str(card_number1)[:4])
                    c2 = (str(card_number1)[12:])
                    print(f"""
                            Karta raqam:        {c1}****{c2}
                            Check date:         {datetime.datetime.now()}
                              Savdoingiz uchun rahmat""")
        else:
            print("Hisobingizda yetarlik mablag mavjud emas")

    @staticmethod
    def search_product(card_number, phone_number, first_name, product_type):
            text = input("""
                         Qidirmoqchi bo'lgan mahsulotingizni kiritng: 
                         0. Back
                              >>> """)
            text.lower()
            query = f"SELECT PRODUCT_NAME, description, price, amount FROM products where product_type = {product_type} AND product_name LIKE '%{text}%';"
            data = Korzinka.select(query)
            for i,j in zip(range(1, len(data)), data):
                print(f"""{i}. {j[0]} 
                    Mahsulot haqida ma'lumot: {j[1]}
                    Narxi: {j[2]}
                    Do'konda mavjud: {j[3]}""")
            temp = input("     >>> ")
            if temp <= i and temp != "0":
                return savdo.savdo2(card_number, phone_number, first_name, data, product_type)
            elif text == "0":
                    return Korzinka.xizmatlar(card_number, phone_number, first_name)
            else:
                    return Korzinka.product(card_number, phone_number, first_name, product_type)
        # except:
        #     print("Son kiriting! ")
        #     return products.product1(card_number, phone_number, first_name, product_type)
        
    @staticmethod
    def search_product_type(card_number, phone_number, first_name):
        try:
            text = input("""
                         Qidirmoqchi bo'lgan bo'limingizni kiritng: 
                              >>> """)
            text.lower()
            try:
                query = f"SELECT product_type FROM product_type where product_type LIKE '%{text}%';"
                product_type1 = Korzinka.select(query)
            except:
                print("Bunday ma'lumot topilmadi! ")
                return Korzinka.search_product_type(card_number, phone_number, first_name)
            if len(product_type1) == 0:
                print("Bunday bo'lim topilmadi!")
                return Korzinka.search_product_type(card_number, phone_number, first_name)
            else:
                soni = []
                for i,j in zip(range(1, (len(product_type1)+1)), product_type1):
                    soni.append(i)
                    print(f"""{i}. {j[0]}""")
                print(f"""0. Orqaga qaytish""")
                temp = input("      >>> ")
                for k, f in zip(range(1, len(product_type1)+1), product_type1):
                    print(soni, k, f"{f}", product_type1)
                    if int(temp) == k:
                        product_type = f"{f[0]}"
                        return Korzinka.product(card_number, phone_number, first_name, product_type)
                    elif temp == "0":
                        return first_page.main()
                    else:
                        print("Bunday bo'lim mavjud emas!")
                        # return Korzinka.search_product_type(card_number, phone_number, first_name)
                        continue
                # except:
                #     print("Bor bo'limni tenlang! ")
                #     return Korzinka.search_product_type(card_number, phone_number, first_name)
        except:
            print("Son kiriting! ")
            return Korzinka.search_product_type(card_number, phone_number, first_name)