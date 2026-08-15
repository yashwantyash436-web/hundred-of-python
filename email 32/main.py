##################### Extra Hard Starting Project ######################
import smtplib
import pandas
import random
from datetime import datetime


my_email = "4vm24is048@gmail.com"
password = "pzkpyuklywkwvfnd"

today=datetime.now()
today_tuple=(today.month,today.day)
print(today_tuple)
# 1. Update the birthdays.csv



# 2. Check if today matches a birthday in the birthdays.csv
data=pandas.read_csv("birthdays.csv")
birthday_dict={(data_row["month"] , data_row["day"]) : data_row for (index,data_row) in data.iterrows()}
if today_tuple in birthday_dict:
    birthday_person=birthday_dict[today_tuple]
    file_path=f"letter_templates/letter_{random.randint(1,3)}.txt"
    with open(file_path) as file:
        details=file.read()
        details=details.replace("[NAME]", birthday_person["name"])
        
    with smtplib.SMTP("smtp.gmail.com",587) as connection:
        connection.starttls()
        connection.login(my_email,password)
        connection.sendmail(from_addr=my_email,to_addrs=birthday_person["email"],msg=f"Subject:Happy Birthday!\n\n{details}")

        
        


# 3. If step 2 is true, pick a random letter from letter templates and replace the [NAME] with the person's actual name from birthdays.csv

# 4. Send the letter generated in step 3 to that person's email address.




