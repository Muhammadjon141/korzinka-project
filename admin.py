import classes
import first_page
def admin_page():
    data = input(f"""
                 1. SELECT
                 2. INSERT
                 3. CREATE
                 4. UPDATE
                 0. Back
                    >>> """)
    if data == "1":
        return classes.Korzinka.admin_select()
    elif data == "0":
        return first_page.main()
    else:
        print("Hatolik")
        return admin_page()