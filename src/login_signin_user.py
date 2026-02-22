import pandas as pd
import openpyxl

excel_file = f"C:\\Users\\hp\\OneDrive\\Desktop\\python_rel\\finance_tracking_sheet.xlsx"

df = pd.read_excel(excel_file,sheet_name='Sheet1')
#print(df)
usr_list= list(df["username"])
print(usr_list)

def sign_up():
    print("Enter details for sign up")

def login_usr(usr,pwd):
    usr = usr
    pwd = pwd
    if usr in usr_list:
        if pwd == 'Msk123':
            print("login successful")
        else:
            print("login failed due to invalid password ")
    else:
        print("user not available please sign in")
        sign_up()



def main():
    usr = input("Please enter username:")
    pwd = input("Please enter password:")

    login_usr(usr,pwd)


main()

