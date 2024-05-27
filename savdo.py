import classes

def savdo1(card_number, phone_number, first_name, data, product, product_type):
    for i,j in zip(range(1, (len(data)+1)), data):
                    if int(product) == i:
                        data1 = j
                        print(f"""
                                Siz tanlagan mahsulot: {data1[0]}
                                Mahsulot narxi: {data1[2]} so'm
                                Do'konda mavjud: {data1[3]}""")
                        miqdor = input("Qancha olmoqchi bo'lgan  miqdoringizni kiriting: ")
                        card_number1 = card_number[0]
                        if int(miqdor) < data1[3]:
                            old_user_balanc = classes.Korzinka.one_user_balanc(card_number1, phone_number)
                            int_old_user_balanc = old_user_balanc[0][0]
                            a = data1[2]*int(miqdor)
                            new_user_balanc = int_old_user_balanc - data1[2]*int(miqdor)
                            new_son_products = data1[3] - int(miqdor)
                            mahsulot_nomi = data1[0]
                            print(f"Siz to'lashingiz kerak miqdor: {a}")
                            return classes.Korzinka.update_mahsulot(new_user_balanc, new_son_products, mahsulot_nomi, card_number, phone_number, first_name)
                        else:
                            print("Buncha mahsulot mavjud emas! ")
                            return savdo1(card_number, phone_number, first_name, data, product, product_type)

                    
def savdo2(card_number, phone_number, first_name, data, product_type):
    for data1 in data:
        print(f"""
                Siz tanlagan mahsulot: {data1[0]}
                Mahsulot narxi: {data1[2]} so'm
                Do'konda mavjud: {data1[3]}""")
        miqdor = input("Qancha olmoqchi bo'lgan  miqdoringizni kiriting: ")
        card_number1 = card_number[0]
        if int(miqdor) < data1[3]:
            old_user_balanc = classes.Korzinka.one_user_balanc(card_number1, phone_number)
            int_old_user_balanc = old_user_balanc[0][0]
            a = data1[2]*int(miqdor)
            new_user_balanc = int_old_user_balanc - data1[2]*int(miqdor)
            new_son_products = data1[3] - int(miqdor)
            mahsulot_nomi = data1[0]
            print(f"Siz to'lashingiz kerak miqdor: {a}")
            return classes.Korzinka.update_mahsulot(new_user_balanc, new_son_products, mahsulot_nomi, card_number, phone_number, first_name)
        else:
            print("Buncha mahsulot mavjud emas! ")
            return savdo2(card_number, phone_number, first_name, data, product_type)