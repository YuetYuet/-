#!/usr/bin/env python
# coding: utf-8

# In[6]:


import tkinter as tk
from tkinter import *
import tkinter.ttk as ttk
from tkcalendar import Calendar
from tkinterhtml import HtmlFrame
import webbrowser
from tkinter import messagebox
import pymongo
import pandas as pd
import time

client=pymongo.MongoClient("mongodb+srv://s972192006:leeyuet841120@cluster0.jcgpz.mongodb.net/myFirstDatabase?retryWrites=true&w=majority")

#取所有條件的值      
def choose_value():
    date=cal.selection_get()
    if date== None:
        error2()
        return
    else:
        year=date=cal.selection_get().year
        month=date=cal.selection_get().month
        day=date=cal.selection_get().day        
        if day==10:
            date_info=str(year)+"-0"+str(month)+"-"+str(day)
        else:
            date_info=str(year)+"-0"+str(month)+"-0"+str(day)
    
    city=place_r.get()
    if city=="台北市":
        city_info="Taipei"
    elif city=="新北市":
        city_info="New_Taipei"
    elif city=="桃園市":
        city_info="Taoyuan"
    elif city=="台中市":
        city_info="Taichung"
    elif city=="台南市":
        city_info="Tainan"
    elif city=="高雄市":
        city_info="Kaohsiung"        
    
    people_num=people_r.get()
    if people_num=="2人":
        db_name="Two_p"
    elif people_num=="4人":
        db_name="Four_p"
    
    factor=rates_r.get()
    if factor=="住宿地點":
        factor="Location"
    elif factor=="清潔程度":
        factor="Cleanliness"
    elif factor=="舒適程度":
        factor="Comfort"
    
    car_p=v.get()
    if car_p==1:
        car_p="Yes"
    elif car_p==0:
        db_name="No"
        
    price_low=int(dollar_low.get())
    price_hight=int(dollar_hight.get())
    
    if date_info==None or city =="地區" or people_num=="住宿人數" or factor=="選項" or car_p==0 or int(price_low)<1 or int(price_hight)< int(price_low) :
        error()
        return
    
    lb1.config(bg="#FFFFFF",fg="#1C1C1C",font=('微軟正黑體',13),text="搜尋中，請稍後")
        
    
    return date_info,city,city_info,db_name,factor,car_p,price_low,price_hight
              
#get 選擇日期       
def grad_date():
    date_info=cal.selection_get().day
    #判斷日期是否超過可選範圍
    if int(date_info)>10:
        error2()
    else:
        day.config(text=cal.selection_get())


#提醒-條件缺少
def error():
    messagebox.showwarning("錯誤","條件不全，請重新確認")

#提醒-日期超過
def error2():
    messagebox.showwarning("日期錯誤","可選擇的日期為6/1-6/10，請重新選擇")

#提醒-日期超過
def error3():
    messagebox.showinfo("錯誤","當日無空房飯店")


def factor(num):
    
    date_info,city,city_info,db_name,factor,car_p,price_low,price_hight=choose_value()
    
    client=pymongo.MongoClient("mongodb+srv://s972192006:leeyuet841120@cluster0.jcgpz.mongodb.net/myFirstDatabase?retryWrites=true&w=majority")
    db=client[db_name][city_info]
    

    result=db.find({"Checkin_day":date_info,"Car_Park_State":car_p,"Price":{"$gte":price_low,"$lte":price_hight}}).sort(factor,-1).limit(3)
    content_list=[]
    
    for result_info in result:
        content_list.append(result_info)
        print(result_info)
        print(result_info[factor])
        
    if content_list ==[]:
        lb1.config(bg="#FFFFFF",fg="#1C1C1C",font=('微軟正黑體',13),text="當日無空房飯店")
        error3()
        return
    canvas.delete(reslut_bg) #刪除遮擋畫布
    
    #筆數資訊
    if len(content_list)==2:
        lb1.config(bg="#FFFFFF",fg="#1C1C1C",font=('微軟正黑體',13),text="為您推薦以下2間飯店")
    elif len(content_list)==1:
        lb1.config(bg="#FFFFFF",fg="#1C1C1C",font=('微軟正黑體',13),text="為您推薦以下1間飯店")
    elif len(content_list)==3:
        lb1.config(bg="#FFFFFF",fg="#1C1C1C",font=('微軟正黑體',13),text="為您推薦以下3間飯店")
    
    
    google_link=content_list[0]["Map_link"]
    link=content_list[0]["Link"]

    #名稱資訊
    hotel_name_info.config(bg="#FFFFFF",fg="#1C1C1C", font=('微軟正黑體',13),text=content_list[0]["Name"])

    #地址
    hotel_address_info.config(bg="#FFFFFF",fg="#1C1C1C", font=('微軟正黑體',13),text=city +content_list[0]["District"])
    #Google Map位置
    google_map.config(image=img,bg="#E8EEFF",width=64,command=lambda : map_browser(google_link))
    google_map.place(x=920,y=255)

    #入住日期
    check_date_info.config(bg="#FFFFFF",fg="#1C1C1C", font=('微軟正黑體',13),text=content_list[0]["Checkin_day"])

    #房型資訊
    roomtype_info.config(bg="#FFFFFF",fg="#1C1C1C", font=('微軟正黑體',13),text=content_list[0]["Roomtype"])

    #停車資訊
    car_park_info.config(bg="#FFFFFF",fg="#1C1C1C", font=('微軟正黑體',13),text=content_list[0]["Car_Park"])

    #價錢
    price_info.config(bg="#FFFFFF",fg="#1C1C1C", font=('微軟正黑體',13),text=str(content_list[0]["Price"])+" 元")
    
    #booking連結位置
    booking_link.config(image=img3,bg="#E8EEFF",width=64,command=lambda :booking_browser(link))
    booking_link.place(x=1150,y=195)
    
    num=0
    
    #切換上一筆
    btn1=tk.Button(text='上一筆')
    btn1.config(bg="#FFFFFF",width=6,font=('微軟正黑體',13),command=lambda :switch_item_up(content_list,num,city))
    btn1.place(x=1040,y=600)
    
    
    #該筆數:
    lb2.config(bg="#E8EEFF",fg="#1C1C1C", font=('微軟正黑體',12),text="第%d筆"%(num+1))

    #切換下一筆
    btn2=tk.Button(text='下一筆')
    btn2.config(bg="#FFFFFF",width=6,font=('微軟正黑體',13),command=lambda :switch_item(content_list,num,city),textvariable=num)
    btn2.place(x=1180,y=600)
    
    return 

    
def switch_item(content_list,num,city):
    
    num+=1
    if num==3:
        return
    content_list[num]
    google_link=content_list[num]["Map_link"]
    link=content_list[num]["Link"]

    #名稱資訊
    hotel_name_info.config(bg="#FFFFFF",fg="#1C1C1C", font=('微軟正黑體',13),text=content_list[num]["Name"])

    #地址
    hotel_address_info.config(bg="#FFFFFF",fg="#1C1C1C", font=('微軟正黑體',13),text=city +content_list[num]["District"])
    #Google Map位置
    google_map.config(image=img,bg="#E8EEFF",width=64,command=lambda : map_browser(google_link))
    google_map.place(x=920,y=255)

    #入住日期
    check_date_info.config(bg="#FFFFFF",fg="#1C1C1C", font=('微軟正黑體',13),text=content_list[num]["Checkin_day"])

    #房型資訊
    roomtype_info.config(bg="#FFFFFF",fg="#1C1C1C", font=('微軟正黑體',13),text=content_list[num]["Roomtype"])

    #停車資訊
    car_park_info.config(bg="#FFFFFF",fg="#1C1C1C", font=('微軟正黑體',13),text=content_list[num]["Car_Park"])

    #價錢
    price_info.config(bg="#FFFFFF",fg="#1C1C1C", font=('微軟正黑體',13),text=str(content_list[num]["Price"])+" 元")
    
    #booking連結位置
    booking_link.config(image=img3,bg="#E8EEFF",width=64,command=lambda :booking_browser(link))
    booking_link.place(x=1150,y=195)
    
     #切換上一筆
    btn1=tk.Button(text='上一筆')
    btn1.config(bg="#FFFFFF",width=6,font=('微軟正黑體',13),command=lambda :switch_item_up(content_list,num,city))
    btn1.place(x=1040,y=600)
    
    
    #該筆數:
    lb2.config(text="第%d筆"%(num+1))

    #切換下一筆
    btn2=tk.Button(text='下一筆')
    btn2.config(bg="#FFFFFF",width=6,font=('微軟正黑體',13),command=lambda :switch_item(content_list,num,city))
    btn2.place(x=1180,y=600)
    
    return num

def switch_item_up(content_list,num,city):
    
    num-=1
    if num==-1:
        return
    content_list[num]
    google_link=content_list[num]["Map_link"]
    link=content_list[num]["Link"]

    #名稱資訊
    hotel_name_info.config(bg="#FFFFFF",fg="#1C1C1C", font=('微軟正黑體',13),text=content_list[num]["Name"])

    #地址
    hotel_address_info.config(bg="#FFFFFF",fg="#1C1C1C", font=('微軟正黑體',13),text=city +content_list[num]["District"])
    #Google Map位置
    google_map.config(image=img,bg="#E8EEFF",width=64,command=lambda : map_browser(google_link))
    google_map.place(x=920,y=255)

    #入住日期
    check_date_info.config(bg="#FFFFFF",fg="#1C1C1C", font=('微軟正黑體',13),text=content_list[num]["Checkin_day"])

    #房型資訊
    roomtype_info.config(bg="#FFFFFF",fg="#1C1C1C", font=('微軟正黑體',13),text=content_list[num]["Roomtype"])

    #停車資訊
    car_park_info.config(bg="#FFFFFF",fg="#1C1C1C", font=('微軟正黑體',13),text=content_list[num]["Car_Park"])

    #價錢
    price_info.config(bg="#FFFFFF",fg="#1C1C1C", font=('微軟正黑體',13),text=str(content_list[num]["Price"])+" 元")
    
    #booking連結位置
    booking_link.config(image=img3,bg="#E8EEFF",width=64,command=lambda :booking_browser(link))
    booking_link.place(x=1150,y=195)
    
     #切換上一筆
    btn1=tk.Button(text='上一筆')
    btn1.config(bg="#FFFFFF",width=6,font=('微軟正黑體',13),command=lambda :switch_item_up(content_list,num,city))
    btn1.place(x=1040,y=600)
    
    
    #該筆數:
    lb2.config(text="第%d筆"%(num+1))

    #切換下一筆
    btn2=tk.Button(text='下一筆')
    btn2.config(bg="#FFFFFF",width=6,font=('微軟正黑體',13),command=lambda :switch_item(content_list,num,city))
    btn2.place(x=1180,y=600)
    
    return num
        

#連到google map
def map_browser(google_link):
    webbrowser.open(google_link)

#連到booking
def booking_browser(link):
    webbrowser.open(link)



# 主視窗
win=tk.Tk()
#視窗屬性設定
win.title('菈蠂芮')
win.geometry('1350x700')
win.iconbitmap('luxury.ico')
win.config(bg="#E8E8E8")
win.attributes('-alpha',1)
# win.attributes('-topmost',True) #把畫面放在最前面，可以選擇不要
win.maxsize

#添加背景

canvas= Canvas(width=1350, height=700, highlightthickness=0, borderwidth=0)
canvas.place(x=0, y=0)
bg = PhotoImage(file='COVER2.png')
bgid = canvas.create_image(0, 0, image=bg, anchor='nw')

reslut_bg =canvas.create_rectangle(650,195,1280,645,fill="#E8EEFF",width = 0)


#標示
title=tk.Label(text='請設定需求條件，將為您提供高CP值飯店 ^^')
title.config(bg="#E8F1FF",fg="#000000", font=('微軟正黑體',13))
title.place(x=100,y=45)

#建立日曆
cal = Calendar(win, selectmode = 'day',cursor="hand1",
               year = 2022, month = 6,
               day = 0)
cal.config(selectbackground="#FFC8B4",selectforeground="#000000")
cal.place(x=80,y=95)


#確認按鈕
Button(win, text = "click",bg="#FFFFFF",fg="#1C1C1C", font=('微軟正黑體',13),
       command = grad_date).place(x=310,y=215)

#顯示已選擇的日期
day_t=tk.Label(text="已選擇的日期")
day_t.config(bg="#E8F8FF",fg="#1C1C1C", font=('微軟正黑體',12))
day_t.place(x=420,y=152)
day=tk.Label(text=" ")
day.config(bg="#E8F8FF",fg="#FF0000", font=('微軟正黑體',12))
day.place(x=420,y=180)


#篩選條件:城市
place_t=tk.Label(text="選擇居住地區")
place_t.config(bg="#E8F8FF",fg="#1C1C1C", font=('微軟正黑體',12))#FFF8EC
place_t.place(x=130,y=330)
place = ["地區",
         "台北市",
         "新北市",
         "桃園市",
         "台中市",
         "台南市",
         "高雄市"]                      
place_r = ttk.Combobox(win, width=8,state="readonly", font=('微軟正黑體',13))
place_r["values"] = place
place_r.place(x=135,y=360)
place_r.current(0)
combostyle = ttk.Style()
#設定下拉選單顏色
combostyle.theme_create('combostyle', parent='alt',
settings={'TCombobox':
{'configure':
{
'foreground': '#000000', # 字顏色
'selectforeground': '#FF0000', # 被選擇的字顏色
'selectbackground': '#FFFFFF', # 被選擇的背景顏色
'fieldbackground': '#FFFFFF', # 下拉框颜色
'background': '#E8F8FF', # 下拉按钮颜色

}}}
)
combostyle.theme_use('combostyle')


#篩選條件:人數
people= ["住宿人數",
         "2人",
         "4人"]                      
people_r = ttk.Combobox(win, width=8, state="readonly", font=('微軟正黑體',13))
people_r["values"] =people
people_r.place(x=135,y=415)
people_r.current(0)


#篩選條件:考量因素
rates_t=tk.Label(text="優先考量因素")
rates_t.config(bg="#E8F8FF",fg="#1C1C1C", font=('微軟正黑體',12))
rates_t.place(x=130,y=465)
rates= ["選項",
         "住宿地點",
         "清潔程度",
         "舒適程度"]                      
rates_r = ttk.Combobox(win, width=8, state="readonly", font=('微軟正黑體',13))
rates_r["values"] =rates
rates_r.place(x=135,y=500)
rates_r.current(0)

#篩選條件:停車需求
park=tk.Label(win, text="停車需求", bg="#E8F8FF",fg="#1C1C1C",width=6, font=('微軟正黑體',13)).place(x=330,y=470)
v= tk.IntVar()
tk.Radiobutton(win, text="需要",variable=v, value=1,bg="#E8F8FF",fg="#1C1C1C", font=('微軟正黑體',13)).place(x=320,y=495)
tk.Radiobutton(win, text="不用",variable=v, value=2,bg="#E8F8FF",fg="#1C1C1C", font=('微軟正黑體',13)).place(x=390,y=495)


#篩選條件:價格
dollar=tk.Label(text='預算範圍 : 低~高')
dollar.config(bg="#E8F8FF",fg="#1C1C1C", font=('微軟正黑體',13))
dollar.place(x=130,y=550)

#篩選條件:價格範圍-低
dollar_low=tk.Entry()
dollar_low.delete(0,"end")
dollar_low.insert(0,1000)
dollar_low.config(width=6)
dollar_low.place(x=135,y=580)

#to
to=tk.Label(text="元 ~")
to.config(fg="#000000",bg="#E8F8FF", font=('微軟正黑體',13),width=3)
to.place(x=190,y=575)

#篩選條件:價格範圍-高
dollar_hight=tk.Entry()
dollar_hight.delete(0,"end")
dollar_hight.config(width=6)
dollar_hight.place(x=230,y=580)
#元
to=tk.Label(text="元")
to.config(fg="#000000",bg="#E8F8FF", font=('微軟正黑體',13),width=3)
to.place(x=275,y=575)

num=0

#查詢
btn=tk.Button(text='查詢')
img2=tk.PhotoImage(file="Icon_button.png") 
btn.config(image=img2,bg="#E8EEFF",width=64,command=lambda :factor(num))
btn.place(x=470,y=550)


#-----------輸出-----------------------------------------------------------------


#結果標示
title=tk.Label(text='推薦飯店資訊')
title.config(bg="#FFFFFF",fg="#000000", font=('微軟正黑體',13))
title.place(x=745,y=42)

#推薦筆數
hotel_info=tk.Label()
hotel_info.config(bg="#E8EEFF",fg="#1C1C1C", font=('微軟正黑體',13),text="")
hotel_info.place(x=760,y=140)

#名稱資訊
hotel_name_info=tk.Label()
hotel_name_info.config(bg="#E8EEFF",fg="#1C1C1C", font=('微軟正黑體',13),text="")
hotel_name_info.place(x=760,y=210)

#地址資訊
hotel_address_info=tk.Label()
hotel_address_info.config(bg="#E8EEFF",fg="#1C1C1C", font=('微軟正黑體',13),text="")
hotel_address_info.place(x=760,y=277)

#Google Map
img=tk.PhotoImage(file="Google_Maps_logo.png")
google_map = tk.Button()
google_map.config(image=img,bg="#E8EEFF",width=64)
google_map.place(x=1200,y=120)


#入住日期
check_date_info=tk.Label()
check_date_info.config(bg="#E8EEFF",fg="#FF0000", font=('微軟正黑體',13),text="")
check_date_info.place(x=760,y=345)

#房型資訊
roomtype_info=tk.Label()
roomtype_info.config(bg="#E8EEFF",fg="#1C1C1C", font=('微軟正黑體',13),text="")
roomtype_info.place(x=760,y=410)

#停車資訊
car_park_info=tk.Label()
car_park_info.config(bg="#E8EEFF",fg="#1C1C1C", font=('微軟正黑體',13),text="")
car_park_info.place(x=760,y=475)

#價錢資訊
price_info=tk.Label()
price_info.config(bg="#E8EEFF",fg="#1C1C1C", font=('微軟正黑體',13),text="")
price_info.place(x=760,y=540)

#booking連結
img3=tk.PhotoImage(file="booking-logo.png")
booking_link = tk.Button()
booking_link.config(image=img3,bg="#E8EEFF",width=64)
booking_link.place(x=1100,y=120)



#搜尋公告:
lb1=tk.Label()
lb1.config(bg="#FFFFFF",fg="#1C1C1C",font=('微軟正黑體',13),text="設定好條件，我將為您服務 ^ ^")
lb1.place(x=760,y=140)



#該筆數:
lb2=tk.Label()
lb2.config(bg="#E8EEFF",fg="#1C1C1C", font=('微軟正黑體',12))
lb2.place(x=1120,y=607)

    




win.mainloop()

