import re
text = """Contact us on support@gmail.com or help123@yahoo.com
Call us on 9906898630,8082187958 
meeting date : 13/1/2026

"""
email_pattern = r'.+@.+'
phone_pattern = r'\d{10}'
date_pattern = r'\d+/\d+/\d+'


emails = re.findall(email_pattern,text)
phone_no = re.findall(phone_pattern,text)
dates = re.findall(date_pattern,text)
print("Emails found",emails)
print(" phone_no's found",phone_no )
print("dates found", dates) 