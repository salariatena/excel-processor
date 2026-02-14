import pandas as pd
import re

cities = ["تهران","مشهد","اصفهان","شیراز","تبریز","کرج","قم","اهواز","رشت","یزد","کرمانشاه","همدان","ارومیه","قائمشهر","زاهدان","سمنان","زنجان","شهرکرد","گرگان","اراک","خرم اباد","خرم آباد","سنندج","کرمان","ساری"]

services = [
"بینی",
"بلفاروپلاستی",
"دندانپزشک",
"ایمپلنت",
"پروتز دندان",
"ارتودنسی",
"کاشت",
"کامپوزیت",
"زنان",
"پوست و مو",
"پلک",
"پوست",
"بوتاکس"
]

df = pd.read_excel("input.xlsx")
text_column = df.columns[7]

def extract_city(text):
    for city in cities:
        if city in str(text):
            return city
    return ""

def extract_service(text):
    found = []
    for service in services:
        if service in str(text):
            found.append(service)
    return " ، ".join(found)




new_df = pd.DataFrame()

new_df["عنوان صفحه"] = df[text_column]
new_df["شهر"] = df[text_column].apply(extract_city)
new_df["خدمت مورد نیاز"] = df[text_column].apply(extract_service)
new_df["نام و نام خانوادگی"] = df["نام و نام خانوادگی"]
new_df["شماره تماس"] = df["شماره تماس"]
new_df["تاریخ و ساعت"] = df["تاریخ و ساعت"]
new_df["شهر کاربر"]=df["شهر"]
new_df["خدمات درخواستی کاربر"]=df["خدمات درخواستی"]

new_df["شهر"] = new_df["شهر"].replace("", pd.NA).fillna(new_df["شهر کاربر"])


new_df.to_excel("output.xlsx", index=False)

print("فایل خروجی ساخته شد ✅")

