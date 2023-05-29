import tweepy
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
import time
import json
import threading
from tkinter import *
from tkinter import ttk
import tkinter as tk 
from tkinter import filedialog
from PIL import ImageTk,Image
import webbrowser
import os
from tkinter import messagebox
import random
import math
import socket
# start the app GUI 
me=tk.Tk()
me.title("Twitter FullBot")
me.geometry("1000x600")
me.maxsize(1000,600)
me.minsize(1000,600)
# to stop thread
stop_event = threading.Event()
# tabs of our program
tabControl = ttk.Notebook(me)
Welcome = ttk.Frame(tabControl,width=1000,height=600)
Add_accounts = ttk.Frame(tabControl,width=1000,height=600)
Operations = ttk.Frame(tabControl,width=1000,height=600)
others = ttk.Frame(tabControl,width=1000,height=600)
others2 = ttk.Frame(tabControl,width=1000,height=600)
tabControl.add(Welcome, text ='  Welcome  ')
tabControl.add(Add_accounts, text ='  Add Accounts  ')
tabControl.add(Operations, text ='  Operations  ')
tabControl.add(others, text ='  Another Functions  ')
tabControl.add(others2, text ='  Another Functions 2  ')
tabControl.pack(expand = 1, fill ="both") 

# background imgs
bg_img= ImageTk.PhotoImage(Image.open("./my files/main/Ful.png")) 
# welcome pag2
canvas1 = Canvas(Welcome, width = 100, height = 1000)
canvas1.pack(fill = "both", expand = True)
canvas1.create_image( 0, 0, image = bg_img, anchor = "nw")
# functions to go to links
def go_face():
    webbrowser.open_new_tab("https://www.facebook.com/profile.php?id=100041132805569")
def go_linked():
    webbrowser.open_new_tab("https://www.linkedin.com/in/mahmoud-ismail-1910b1109/")    
# add the text and contact us 

wel_lbl1 = Label(me,text="Welcome to FullBot",bg="#1B9DF0",font="FangSong 18 italic bold",fg="black")
wel_lbl2=Label(me,text="by this bot you will have the ability to: ",bg="#1B9DF0",font="FangSong 18 italic bold",fg="white")
task1 = Label(me,text = "Like tweets ",bg="#ccd7e4",font="FangSong 18 italic bold",fg="#1B9DF0")
task2 = Label(me,text = "reply to tweets ",bg="#ccd7e4",font="FangSong 18 italic bold",fg="#1B9DF0")
task3 = Label(me,text = "Use number of accounts ",bg="#ccd7e4",font="FangSong 18 italic bold",fg="#1B9DF0")
task4 = Label(me,text = "Tweet ",bg="#ccd7e4",font="FangSong 18 italic bold",fg="#1B9DF0")
task5 = Label(me,text = "Retweet ",bg="#ccd7e4",font="FangSong 18 italic bold",fg="#1B9DF0")
task6 = Label(me,text = "Follow ",bg="#ccd7e4",font="FangSong 18 italic bold",fg="#1B9DF0")
task7 = Label(me,text = "Qoute",bg="#ccd7e4",font="FangSong 18 italic bold",fg="#1B9DF0",padx=23)
task8 = Label(me,text = "Schedule Tasks ",bg="#ccd7e4",font="FangSong 18 italic bold",fg="#1B9DF0")
contact = Label(me,text="Contact Us ",bg="#1B9DF0",fg="black",font = "FangSong 18 italic bold",anchor="center",width=59)
whats = Label(me,text="WhatsApp: +201020634063 ",bg="#1B9DF0",font="FangSong 18 italic bold",fg="white")
facebook = Button(me,text="Facebook",bg="#1B9DF0",font="FangSong 18 italic bold",fg="white",command=go_face)
linked = Button(me,text="LinkedIn",bg="#1B9DF0",font="FangSong 18 italic bold",fg="white",command=go_linked)
note=Label(me,text=" Note: Follow the instructions of each function in the bot to avoid errors",bg="#1B9DF0",fg="black",font = "FangSong 16 bold",anchor="w",width=60)
canvas1.create_window(365,50,anchor="nw",window=wel_lbl1)
canvas1.create_window(250,155,anchor="nw",window=wel_lbl2)


canvas1.create_window(150,200,anchor="nw",window=task1)
canvas1.create_window(320,200,anchor="nw",window=task2)
canvas1.create_window(540,200,anchor="nw",window=task3)
canvas1.create_window(165,240,anchor="nw",window=task4)
canvas1.create_window(265,240,anchor="nw",window=task5)
canvas1.create_window(395,240,anchor="nw",window=task6)
canvas1.create_window(500,240,anchor="nw",window=task7)
canvas1.create_window(635,240,anchor="nw",window=task8)
canvas1.create_window(0,320,anchor="nw",window=contact)
canvas1.create_window(115,370,anchor="nw",window=whats)
canvas1.create_window(520,362,anchor="nw",window=facebook)
canvas1.create_window(695,362,anchor="nw",window=linked)
canvas1.create_window(2,540,anchor="nw",window=note)

######################################################################################################################################################################################################
#add accounts page
logo1=Label(me,text="FullBot",bg="#1B9DF0",font="FangSong 18 italic bold",fg="black")
canvas2 = Canvas(Add_accounts, width = 100, height = 1000)
canvas2.pack(fill = "both", expand = True)
canvas2.create_image( 0, 0, image = bg_img, anchor = "nw")
#functions of add accounts page
# function to display top level with the instructions 
def add_inst():
    top = Toplevel()
    top.title("Instructions")
    l2 = Label(top,font="FangSong 14 italic ", text = "Follow the instructions to avoid errors\n this function is to get the access from your accounts\nwe will use 2 APIs access to have more request in the future\n you must add file that contains your accounts details in this form:\nuser1:pass1:mail or phone:pass\nuser2:pass2:mail or phone:pass\nrecommend to use visible mode to see the process\n don't close the browser while the program working")
    l2.pack() 
# get the id of the API
# open and read file of APIs

api_lbl=Label(me,text="Choose the number of API ",bg="#1B9DF0",font="FangSong 12 italic bold",fg="white")
   
inst1 = Button(me,text="Instructions",bg="white",fg="#1B9DF0",font="FangSong 16 italic bold",command=add_inst)
add_lbl1=Label(me,text="Choose the browser mode: ",bg="#1B9DF0",font="FangSong 18 italic bold",fg="white")
v = StringVar(me,"Visible")
radio1=Radiobutton(me,text="Headless",indicator = 0,bg="#1B9DF0",fg="black",font="FangSong 16",variable=v,value="Headless",width=20)
radio2=Radiobutton(me,text="Visible(recommended) ",bg="#1B9DF0",fg="black",font="FangSong 16",variable=v,value="Visible",indicator = 0,width=20)
text_area = Text(me,width=50,height=25)
# to browse the accounts file
def browseFiles():
    filename = filedialog.askopenfilename(initialdir = "./",title = "Select a File",filetypes = (("Text files","*.txt*"),("all files","*.*")))
    file_ent.configure(text=f"{filename}")
# Display image
canvas1.create_image( 0, 0, image = bg_img, anchor = "nw")
file_btn = Button(me,text="choose a file",bg="black",fg="white",font="FangSong 16",command=browseFiles,width=20,padx=0)
file_ent= Label(me,text="",fg="white",bg="#1B9DF0",wraplength=320)
# def to start login and add files
def start_login():
    ## getting the hostname by socket.gethostname() method
    hostname = socket.gethostname()
    ## getting the IP address using socket.gethostbyname() method
    ip_address = socket.gethostbyname(hostname)
    text_area.delete("1.0","end")
    text_area.insert("end",f"your IP Address:{ip_address}\n")
    text_area.insert("end",f"you choosed API {clicked.get()}\n")
    me.update()
    text_area.see("end")
    my_inputs = []
    try:                
        #open the file and get data
        if file_ent.cget("text")!= "":
            with open(file_ent.cget("text"),"r",encoding="utf-8") as my_file:
                my_lines = my_file.readlines()
                for i in my_lines:
                    my_inputs.append(i.split(":"))
            # loop in our dtat to get access token and secret  
            if v.get() == "Headless":
                chrome_options = Options()
                chrome_options.add_argument("--headless")
            else:
                chrome_options = Options()     
            with open(f"./my files/keys and APIs/logged API {clicked.get()}.txt","a") as logged_file:   
                text_area.insert(END,f"start logging to accounts with API {clicked.get()}\n")      
                for i in my_inputs:
                    all_logged=[]
                    my_obj ={}
                    driver = webdriver.Chrome("./my files/main/chromedriver.exe",options=chrome_options)  
                    driver.set_window_size(600,1000)
                    driver.implicitly_wait(20)
                    oauth1_user_handler = tweepy.OAuth1UserHandler(keys[clicked.get()-1][0].strip(), keys[clicked.get()-1][1].strip(),callback="oob")
                    me.update()        
                    text_area.see("end")
                    my_link = oauth1_user_handler.get_authorization_url()
                    driver.get("https://twitter.com/i/flow/login")
                    try:
                        time.sleep(3)
                        driver.find_element("xpath",'/html/body/div/div/div/div/main/div/div/div/div[2]/div[2]/div/div[5]/label/div/div[2]/div/input').send_keys(i[0].strip())
                        time.sleep(3)
                        driver.find_element("xpath","/html/body/div/div/div/div/main/div/div/div/div[2]/div[2]/div/div[6]/div/span/span").click()
                        time.sleep(3)
                        driver.find_element("xpath",'/html/body/div/div/div/div/main/div/div/div/div[2]/div[2]/div[1]/div/div/div/div[3]/div/label/div/div[2]/div[1]/input').send_keys(i[1].strip())
                        time.sleep(3)
                        driver.find_element("xpath","/html/body/div/div/div/div/main/div/div/div/div[2]/div[2]/div[2]/div/div/div[1]/div/div/div/div/span/span").click()
                        time.sleep(3)
                        try:
                            driver.find_element("xpath","/html/body/div[1]/div/div/div/main/div/div/div/div[2]/div[2]/div[1]/div/div/div[2]/label/div/div[2]/div/input").send_keys(i[2].strip())
                            time.sleep(3)
                            driver.find_element("xpath","/html/body/div[1]/div/div/div/main/div/div/div/div[2]/div[2]/div[2]/div/div/div/div/div/div/span/span").click()
                            time.sleep(3)
                        except Exception as e:
                            text_area.see("end")
                        driver.get(my_link)
                        driver.find_element("xpath","/html/body/div[2]/div/form/fieldset/input[1]").click()
                        verifier = driver.find_element("xpath","/html/body/div[2]/div/p/kbd/code").text
                        time.sleep(3)
                        access_token, access_token_secret = oauth1_user_handler.get_access_token(verifier)
                        my_obj["ID"]=clicked.get()
                        my_obj["Name"]=i[0]
                        my_obj["pass"] = i[1]
                        my_obj[f"token"] = access_token
                        my_obj[f"secret"] = access_token_secret
                        my_obj[f"Cookies"] = driver.get_cookies()
                        text_area.insert(END,f"{i[0]} logged successfully\n")
                        all_logged.append(my_obj)
                    except:
                        text_area.insert(END,f"error in the account:{i[0]}\n") 
                        text_area.see("end")
                    me.update()        
                    text_area.see("end")
                    for l in all_logged:
                        logged_file.write(f"{json.dumps(l)}\n")
            text_area.insert(END,f"Finished,see you later")             
        else:
            messagebox.showwarning("warning","you must add the path of the file")
    except Exception as e:
        text_area.insert(END,f"{e}") 
def thread_start_login():
    threading.Thread(target=start_login).start()

start_btn=Button(me,text="Start",width=20,font="FangSong 16",padx=0,command=thread_start_login)
canvas2.create_window(450,50,anchor="nw",window=logo1)
canvas2.create_window(35,480,anchor="nw",window=start_btn)
canvas2.create_window(35,375,anchor="nw",window=file_btn)
canvas2.create_window(35,425,anchor="nw",window=file_ent)
canvas2.create_window(810,10,anchor="nw",window=inst1)
canvas2.create_window(30,110,anchor="nw",window=add_lbl1)
canvas2.create_window(30,150,anchor="nw",window=radio1)
canvas2.create_window(30,190,anchor="nw",window=radio2)
canvas2.create_window(500,100,anchor="nw",window=text_area)
canvas2.create_window(40,302,anchor="nw",window=api_lbl)
canvas2.create_window(255,300,anchor="nw",window=drop)
canvas2.create_rectangle(25,255,330,550,width=2,outline="white")


######################################################################################################################################################################################################
#Opertaions page 
def add_inst2():
    top = Toplevel()
    top.title("Instructions")
    l2 = Label(top,font="FangSong 14 italic bold ", text = "Welcome to the operations instructions page")
    accounts = Label(top,font="FangSong 14 italic ", text = "Accounts file: must be the accounts file that created by the add accounts page\n it's name: 'Logged API 1' must be added before any task")
    like_follow_retweet = Label(top,font="FangSong 14 italic bold ", text = "Like/Follow/Retweet")
    like_follow_retweet_inst = Label(top,font="FangSong 14 italic ", text = "You have two ways to Like/Follow/Retweet:- like one tweet or more than one tweet\n for one tweet: add the tweet ID/username to the entry field\n for more than one tweet: Add a IDs file\n the file must be in this form:\ntweet ID1/username\ntweet ID2/username\ntweet ID3/username")
    reply_head = Label(top,font="FangSong 14 italic bold ", text = "Reply")
    reply_inst = Label(top,font="FangSong 14 italic ", text ="You must add the tweet ID and the username of the tweet author\n you must add files that contains replys and the form of the file must be:\nreply1\nreply2\nreply3\n Note that the program will reply randomly so you don't need to add too many replys ")
    tweet_head = Label(top,font="FangSong 14 italic bold ", text = "Tweet")
    tweet_inst=Label(top,font="FangSong 14 italic ", text ="you have to options to tweet:-\n1-tweet without media (just text)\nyou must add file with text, note that you must add number of lines equal to number of logged accounts\nThe form of the file:\ntext1\ntext2\ntext3\n2-tweet with media:-\nthe smae instructions of tweet without media but the file must contains the media you want to tweet with\nThe form of the file must be:\n text1|image full path1\n text2|image full path2")
    qoute_head = Label(top,font="FangSong 14 italic bold ", text = "Qoute")
    qoute_inst = Label(top,font="FangSong 14 italic ", text = "You must add file that contains the Qoute and the link of the tweet in this form\nqoute1|link1\nqoute2|link2")
    l2.pack() 
    accounts.pack()
    like_follow_retweet.pack()
    like_follow_retweet_inst.pack()
    reply_head.pack()
    reply_inst.pack()
    tweet_head.pack()
    tweet_inst.pack()
    qoute_head.pack()
    qoute_inst.pack()

logo2=Label(me,text="FullBot",bg="#1B9DF0",font="FangSong 18 italic bold",fg="black")
canvas3 = Canvas(Operations, width = 100, height = 1000)
canvas3.pack(fill = "both", expand = True)
canvas3.create_image( 0, 0, image = bg_img, anchor = "nw")
text_area2 = Text(me,width=34,height=23)
inst2 = Button(me,text="Instructions",bg="white",fg="#1B9DF0",font="FangSong 16 italic bold",command=add_inst2)
time_lbl = Label(me,bg="#1B9DF0",font="FangSong 11 italic bold",fg="black",text=5)
time_lbl1 = Label(me,bg="#1B9DF0",font="FangSong 11 italic bold",fg="black",text="Time between each task:")

# function to set time
def schedule_time():
    def set_time():
        time_minutes=float(e1.get())
        t_in_s.configure(text=f"{time_minutes*60} seconds, time sat\nexit the window")   
        time_lbl.configure(text=f"{time_minutes*60}") 
    top = Toplevel()
    top.title("Set time")
    l1 = Label(top,font="FangSong 14 italic ", text = "Enter time in minutes",pady=2)
    e1 = Entry(top,width=20)
    b1=Button(top,text="Enter",font="FangSong 14 italic",command=set_time,pady=10)
    t_in_s = Label(top,text="",font="FangSong 14 italic",padx=2)
    l1.pack()
    e1.pack() 
    b1.pack()
    t_in_s.pack()
    
schedule_btn=Button(me,text="Schedule a Task",bg="white",fg="#1B9DF0",font="FangSong 15 italic bold",width=18,command=schedule_time)
# add accounts file
my_tokens1=[]
api_num=[]
def browseFiles1():
    my_tokens1.clear()
    api_num.clear()
    filename = filedialog.askopenfilename(initialdir = "./",title = "Select a File",filetypes = (("Text files","*.txt*"),("all files","*.*")))
    file_ent2.configure(text=f"{filename}")
    try:
        with open(file_ent2.cget("text"),"r",encoding="utf-8") as api_file:
            my_lines = api_file.readlines()
            for i in my_lines:
                dic = json.loads(i)
                my_tokens1.append(dic) 
            api_num.append(my_tokens1[0]["ID"]-1)  
    except:
        messagebox.showwarning("warning","you must add the path of the file")
    
    
file_btn2 = Button(me,text="Add accounts file",bg="black",fg="white",font="FangSong 16",command=browseFiles1,width=16,padx=0)
file_ent2= Label(me,text="",fg="white",bg="#1B9DF0",wraplength=310)

######################################################################################################################################################################################################
# like tweets
like = Label(me,text=" Like ",fg="white",bg="#1B9DF0",font="FangSong 16 italic bold")
like_id_lbl = Label(me,text="Tweet Id:",fg="white",bg="#1B9DF0",font="FangSong 10 italic bold")
like_id_ent = Entry(me,width=16)
like_separator= Label(me,text="More than one tweet: ",fg="white",bg="#1B9DF0",font="FangSong 10 italic bold")
# add ids file
def browseFiles2():
    filename = filedialog.askopenfilename(initialdir = "./",title = "Select a File",filetypes = (("Text files","*.txt*"),("all files","*.*")))
    ids_file_lbl.configure(text=f"{filename}")
ids_file = Button(me,text="Add IDs file",bg="black",fg="white",font="FangSong 12",command=browseFiles2,width=16,padx=0)
ids_file_lbl= Label(me,text="",fg="white",bg="#1B9DF0",wraplength=200,padx=0,pady=0)
# function to start liking
def like_tweet():
    my_time=float(time_lbl.cget("text"))
    text_area2.delete("1.0","end")
    if ids_file_lbl.cget("text") != "" and like_id_ent.get() != "":
        messagebox.showwarning("warning","You must add tweet ID or file with tweets IDs not both")
        
    elif ids_file_lbl.cget("text") == "" and like_id_ent.get() == "":
        messagebox.showwarning("warning","You must add tweet ID or file with tweets IDs")
    else:
        try:
            if like_id_ent.get() != "":
                for i in my_tokens1:
                    try:
                        auth = tweepy.OAuth1UserHandler(
                        keys[api_num[0]][0].strip(),keys[api_num[0]][1].strip(),
                        i["token"], i["secret"] )
                        api = tweepy.API(auth,wait_on_rate_limit=True)
                        api.create_favorite(id=like_id_ent.get())
                        text_area2.insert("end",f"{i['Name']} liked {like_id_ent.get()}\n")
                        me.update()
                        text_area2.see("end")
                        time.sleep(my_time)
                    except Exception as e:
                        text_area2.insert("end",f"{e}\n")

            elif ids_file_lbl.cget("text") != "" and ids_file_lbl.cget("text") != "()":
                with open(ids_file_lbl.cget("text"),"r",encoding="utf-8") as ids_file:
                    reader = ids_file.readlines()
                for i in reader:
                    for j in my_tokens1:
                        try:
                            auth = tweepy.OAuth1UserHandler(
                            keys[api_num[0]][0].strip(),keys[api_num[0]][1].strip(),
                            j["token"], j["secret"] )
                            api = tweepy.API(auth,wait_on_rate_limit=True)
                            api.create_favorite(id=int(i.strip()))
                            text_area2.insert("end",f"{j['Name']} liked {i.strip()}\n")
                            me.update()
                            text_area2.see("end")
                            time.sleep(my_time)
                        except Exception as e:
                            text_area2.insert("end",f"{e}\n")    
        except Exception as e:
            text_area2.insert("end",f"{e}\n") 
def thread_start_like():
    threading.Thread(target=like_tweet).start()            
start_like_btn = Button(me,text="Start",bg="black",fg="white",font="FangSong 14",command=thread_start_like,width=14,padx=0)
#like layout
canvas3.create_window(30,105,anchor="nw",window=like)
canvas3.create_window(20,140,anchor="nw",window=like_id_lbl)
canvas3.create_window(100,140,anchor="nw",window=like_id_ent)
canvas3.create_window(45,170,anchor="nw",window=like_separator)
canvas3.create_window(45,190,anchor="nw",window=ids_file)
canvas3.create_window(28,230,anchor="nw",window=ids_file_lbl)
canvas3.create_window(40,285,anchor="nw",window=start_like_btn)

######################################################################################################################################################################################################
#follow
follow = Label(me,text=" Follow ",fg="white",bg="#1B9DF0",font="FangSong 16 italic bold")
follow_usr_lbl = Label(me,text="Username:",fg="white",bg="#1B9DF0",font="FangSong 10 italic bold")
follow_usr_ent = Entry(me,width=16)
follow_separator= Label(me,text="More than one user: ",fg="white",bg="#1B9DF0",font="FangSong 10 italic bold")
# add username file
def browseFiles3():
    filename = filedialog.askopenfilename(initialdir = "./",title = "Select a File",filetypes = (("Text files","*.txt*"),("all files","*.*")))
    users_file_lbl.configure(text=f"{filename}")
users_file = Button(me,text="Add users file",bg="black",fg="white",font="FangSong 12",command=browseFiles3,width=16,padx=0)
users_file_lbl= Label(me,text="",fg="white",bg="#1B9DF0",wraplength=200,padx=0,pady=0)
# function to start liking
def follow_someone():
    my_time=float(time_lbl.cget("text"))
    text_area2.delete("1.0","end")
    if users_file_lbl.cget("text") != "" and follow_usr_ent.get() != "":
        messagebox.showwarning("warning","You must add user name or file with usernames not both")
    elif users_file_lbl.cget("text") == "" and follow_usr_ent.get() == "":
        messagebox.showwarning("warning","You must add user name or file with usernames")
    else:
        try:
            if follow_usr_ent.get() != "":
                for i in my_tokens1:
                    try:
                        auth = tweepy.OAuth1UserHandler(
                        keys[api_num[0]][0].strip(),keys[api_num[0]][1].strip(),
                        i["token"], i["secret"] )
                        api = tweepy.API(auth,wait_on_rate_limit=True)
                        api.create_friendship(screen_name=follow_usr_ent.get())
                        text_area2.insert("end",f"{i['Name']} followed {follow_usr_ent.get()}\n")
                        me.update()
                        text_area2.see("end")
                        time.sleep(my_time)
                    except Exception as e:
                        text_area2.insert("end",f"{e}\n")    
            elif users_file_lbl.cget("text") != "" and users_file_lbl.cget("text") != "()":
                with open(users_file_lbl.cget("text"),"r",encoding="utf-8") as users_file:
                    reader = users_file.readlines()
                for i in reader:
                    for j in my_tokens1:
                        try:
                            auth = tweepy.OAuth1UserHandler(
                            keys[api_num[0]][0].strip(),keys[api_num[0]][1].strip(),
                            j["token"], j["secret"] )
                            api = tweepy.API(auth,wait_on_rate_limit=True)
                            api.create_friendship(screen_name=i.strip())
                            text_area2.insert("end",f"{j['Name']} followed {i.strip()}\n")
                            me.update()
                            text_area2.see("end")
                            time.sleep(my_time)
                        except Exception as e:
                            text_area2.insert(END,f"{e}\n")    
        except Exception as e:
            text_area2.insert(END,f"{e}\n")    
def thread_start_follow():
    threading.Thread(target=follow_someone).start()    
start_follow_btn = Button(me,text="Start",bg="black",fg="white",font="FangSong 14",command=thread_start_follow,width=14,padx=0)
#follow layout
canvas3.create_window(30,335,anchor="nw",window=follow)
canvas3.create_window(17,370,anchor="nw",window=follow_usr_lbl)
canvas3.create_window(102,370,anchor="nw",window=follow_usr_ent)
canvas3.create_window(45,400,anchor="nw",window=follow_separator)
canvas3.create_window(45,420,anchor="nw",window=users_file)
canvas3.create_window(28,460,anchor="nw",window=users_file_lbl)
canvas3.create_window(40,515,anchor="nw",window=start_follow_btn)
######################################################################################################################################################################################################
#reply
reply = Label(me,text=" Reply ",fg="white",bg="#1B9DF0",font="FangSong 16 italic bold")
tweet_id_lbl = Label(me,text="Tweet Id: ",fg="white",bg="#1B9DF0",font="FangSong 10 italic bold")
tweet_id_ent= Entry(me,width=16)
username_reply = Label(me,text="Username:",fg="white",bg="#1B9DF0",font="FangSong 10 italic bold")
usr_reply_ent= Entry(me,width=16)
def browseFiles4():
    filename = filedialog.askopenfilename(initialdir = "./",title = "Select a File",filetypes = (("Text files","*.txt*"),("all files","*.*")))
    replys_file_lbl.configure(text=f"{filename}")
replys_file = Button(me,text="Add replys file",bg="black",fg="white",font="FangSong 12",command=browseFiles4,width=16,padx=0)
replys_file_lbl= Label(me,text="",fg="white",bg="#1B9DF0",wraplength=200,padx=0,pady=0)
#reply function
def reply_to_tweet():
    text_area2.delete("1.0","end")
    my_time=float(time_lbl.cget("text"))
    if replys_file_lbl.cget("text") != "" and usr_reply_ent.get()!="" and tweet_id_ent.get() !="":
        with open(replys_file_lbl.cget("text"),"r",encoding="utf-8") as rply_file:
            reader = rply_file.readlines()
            for i in my_tokens1:
                try:
                    reply_txt = reader[math.floor(random.randint(0,len(reader)-1))].strip()
                    auth = tweepy.OAuth1UserHandler(
                    keys[api_num[0]][0].strip(),keys[api_num[0]][1].strip(),
                    i["token"], i["secret"] )
                    api = tweepy.API(auth,wait_on_rate_limit=True)
                    api.update_status(status=f"@{usr_reply_ent.get()} {reply_txt}",in_reply_to_status_id=tweet_id_ent.get())
                    text_area2.insert("end",f"{i['Name']} replyed to {tweet_id_ent.get()} with {reply_txt}\n")
                    me.update()
                    text_area2.see("end")
                    time.sleep(my_time)
                except Exception as e:
                    text_area2.insert("end",f"{e}\n")       
    else:
        messagebox.showwarning("warning","you must fill all enteries(username,tweet id, replys file)")        
def thread_start_reply_to_tweet():
    threading.Thread(target=reply_to_tweet).start()                  
start_reply_btn = Button(me,text="Start",bg="black",fg="white",font="FangSong 14",command=thread_start_reply_to_tweet,width=14,padx=0)
#reply layout
canvas3.create_window(265,105,anchor="nw",window=reply)
canvas3.create_window(255,140,anchor="nw",window=tweet_id_lbl)
canvas3.create_window(330,140,anchor="nw",window=tweet_id_ent)
canvas3.create_window(252,170,anchor="nw",window=username_reply)
canvas3.create_window(332,170,anchor="nw",window=usr_reply_ent)
canvas3.create_window(280,195,anchor="nw",window=replys_file)
canvas3.create_window(263,230,anchor="nw",window=replys_file_lbl)
canvas3.create_window(275,285,anchor="nw",window=start_reply_btn)

######################################################################################################################################################################################################
#tweet
tweet = Label(me,text=" Tweet ",fg="white",bg="#1B9DF0",font="FangSong 16 italic bold")
# text box for the text of the tweet
msg_area = Text(me,width=25,height=5)
# browse media
def browse_media():
    filename = filedialog.askopenfilename(initialdir = "./",title = "Select a File")
    media_file_lbl.configure(text=f"{filename}")
media_file = Button(me,text="Add media file ",bg="black",fg="white",font="FangSong 10",command=browse_media,width=16,padx=0)
media_file_lbl= Label(me,text="",fg="white",bg="#1B9DF0",wraplength=200,padx=0,pady=0)
def start_tweet():
    text_area2.delete("1.0","end")
    my_time=float(time_lbl.cget("text"))
    try:
        my_caption = msg_area.get("1.0","end")
        my_media = media_file_lbl.cget("text")
        for i in my_tokens1:
            try:
                auth = tweepy.OAuth1UserHandler(
                keys[api_num[0]][0].strip(),keys[api_num[0]][1].strip(),
                i["token"], i["secret"] )
                api = tweepy.API(auth,wait_on_rate_limit=True)
                if my_media != "":
                    api.update_status_with_media(my_caption,filename=my_media)
                    text_area2.insert(END,f"{i['Name']} tweeted with {my_caption} and {my_media}\n")
                    me.update()
                    text_area2.see("end")
                    time.sleep(my_time)
                else:
                    api.update_status(my_caption)
                    text_area2.insert(END,f"{i['Name']} tweeted with {my_caption}\n")
                    me.update()
                    text_area2.see("end")
                    time.sleep(my_time)
            except Exception as e:    
                text_area2.insert(END,f"{e}\n")
                me.update()
                text_area2.see("end")        
    except Exception as e:
        text_area2.insert("end",f"{e}\n")
        me.update()


    
def thread_start_tweet():
    threading.Thread(target=start_tweet).start()

start_tweet_btn = Button(me,text="Start",bg="black",fg="white",font="FangSong 14",command=thread_start_tweet,width=14,padx=0)
#tweet layout
canvas3.create_window(265,335,anchor="nw",window=tweet)
canvas3.create_window(260,365,anchor="nw",window=msg_area)
canvas3.create_window(260,452,anchor="nw",window=media_file)
canvas3.create_window(260,480,anchor="nw",window=media_file_lbl)
canvas3.create_window(275,515,anchor="nw",window=start_tweet_btn)

######################################################################################################################################################################################################
#retweet
retweet = Label(me,text=" Retweet ",fg="white",bg="#1B9DF0",font="FangSong 16 italic bold")
retweet_id_lbl = Label(me,text="Tweet Id: ",fg="white",bg="#1B9DF0",font="FangSong 10 italic bold")
retweet_id_ent = Entry(me,width=16)
retweet_separator= Label(me,text="More than one tweet: ",fg="white",bg="#1B9DF0",font="FangSong 10 italic bold")
# add ids file
def browseFiles1_retweet():
    filename = filedialog.askopenfilename(initialdir = "./",title = "Select a File",filetypes = (("Text files","*.txt*"),("all files","*.*")))
    ids_file_lbl1.configure(text=f"{filename}")
ids_file1 = Button(me,text="Add IDs file",bg="black",fg="white",font="FangSong 12",command=browseFiles1_retweet,width=16,padx=0)
ids_file_lbl1= Label(me,text="",fg="white",bg="#1B9DF0",wraplength=200,padx=0,pady=0)
# function to start liking
def retweet_tweet():
    my_time=float(time_lbl.cget("text"))
    text_area2.delete("1.0","end")
    if ids_file_lbl1.cget("text") != "" and retweet_id_ent.get() != "":
        messagebox.showwarning("warning","You must add tweet ID or file with tweets IDs not both")
        
    elif ids_file_lbl1.cget("text") == "" and retweet_id_ent.get() == "":
        messagebox.showwarning("warning","You must add tweet ID or file with tweets IDs")
    else:
        try:
            if retweet_id_ent.get() != "":
                for i in my_tokens1:
                    try:
                        auth = tweepy.OAuth1UserHandler(
                        keys[api_num[0]][0].strip(),keys[api_num[0]][1].strip(),
                        i["token"], i["secret"] )
                        api = tweepy.API(auth,wait_on_rate_limit=True)
                        api.retweet(id=retweet_id_ent.get())
                        text_area2.insert("end",f"{i['Name']} retweeted {retweet_id_ent.get()}\n")
                        me.update()
                        text_area2.see("end")
                        time.sleep(my_time)
                    except Exception as e:
                        text_area2.insert(END,f"{e}\n")                        
            elif ids_file_lbl1.cget("text") != "" and ids_file_lbl1.cget("text") != "()":
                with open(ids_file_lbl1.cget("text"),"r",encoding="utf-8") as ids_file1:
                    reader = ids_file1.readlines()
                for i in reader:
                    for j in my_tokens1:
                        try:
                            auth = tweepy.OAuth1UserHandler(
                            keys[api_num[0]][0].strip(),keys[api_num[0]][1].strip(),
                            j["token"], j["secret"] )
                            api = tweepy.API(auth,wait_on_rate_limit=True)
                            api.retweet(id=int(i.strip()))
                            text_area2.insert("end",f"{j['Name']} retweeted {i.strip()}\n")
                            me.update()
                            text_area2.see("end")
                            time.sleep(my_time)
                        except Exception as e:
                            text_area2.insert(END,f"{e}\n")                            
        except Exception as e:
            text_area2.insert("end",f"{e}\n")    
def thread_start_retweet():
    threading.Thread(target=retweet_tweet).start()
start_retweet_btn = Button(me,text="Start",bg="black",fg="white",font="FangSong 14",command=thread_start_retweet,width=14,padx=0)

#retweet layout
canvas3.create_window(495,105,anchor="nw",window=retweet)
canvas3.create_window(490,140,anchor="nw",window=retweet_id_lbl)
canvas3.create_window(565,140,anchor="nw",window=retweet_id_ent)
canvas3.create_window(510,170,anchor="nw",window=retweet_separator)
canvas3.create_window(510,190,anchor="nw",window=ids_file1)
canvas3.create_window(493,230,anchor="nw",window=ids_file_lbl1)
canvas3.create_window(505,285,anchor="nw",window=start_retweet_btn)
######################################################################################################################################################################################################
#qoute
def browseFiles_to_qoute():
    filename = filedialog.askopenfilename(initialdir = "./",title = "Select a File",filetypes = (("Text files","*.txt*"),("all files","*.*")))
    qoutes_file_lbl.configure(text=f"{filename}")
qoutes_file = Button(me,text="Add qoutes file",bg="black",fg="white",font="FangSong 12",command=browseFiles_to_qoute,width=16,padx=0)
qoutes_file_lbl= Label(me,text="",fg="white",bg="#1B9DF0",wraplength=200,padx=0,pady=0)
def qoute_tweet():
    text_area2.delete("1.0","end")
    my_time=float(time_lbl.cget("text"))
    try:
        with open(qoutes_file_lbl.cget("text"),"r",encoding="utf-8") as my_file:
            reader = my_file.readlines() 
        data=[]    
        for j in reader:
            data.append(j.split("|"))

        n=0
        for i in my_tokens1:
            try:
                auth = tweepy.OAuth1UserHandler(
                keys[api_num[0]][0].strip(),keys[api_num[0]][1].strip(),
                i["token"], i["secret"] )
                api = tweepy.API(auth,wait_on_rate_limit=True)
                api.update_status(data[n][0].strip(),attachment_url=data[n][1].strip())
                time.sleep(my_time)
                text_area2.insert(END,f"{i['Name']} tweeted with {data[n][1]} with {data[n][0]}\n")
                me.update()
                text_area2.see("end")
                n=n+1
            except Exception as e:
                text_area2.insert(END,f"{e}\n")   
                me.update()
                text_area2.see("end")            
    except Exception as e:
        text_area2.insert(END,f"{e}\n")
def thread_start_qoute():
    threading.Thread(target=qoute_tweet).start()    

quote = Label(me,text=" Qoute ",fg="white",bg="#1B9DF0",font="FangSong 16 italic bold")
start_qoute_btn = Button(me,text="Start",bg="black",fg="white",font="FangSong 14",command=thread_start_qoute,width=14,padx=0)

#qoute layout
canvas3.create_window(512,370,anchor="nw",window=qoutes_file)
canvas3.create_window(493,410,anchor="nw",window=qoutes_file_lbl)
canvas3.create_window(495,335,anchor="nw",window=quote)
canvas3.create_window(505,515,anchor="nw",window=start_qoute_btn)
######################################################################################################################################################################################################
# Rectangles
canvas3.create_rectangle(15,120,240,330,width=2,outline="white")
canvas3.create_rectangle(250,120,475,330,width=2,outline="white")
canvas3.create_rectangle(485,120,710,330,width=2,outline="white")
canvas3.create_rectangle(15,350,240,560,width=2,outline="white")
canvas3.create_rectangle(250,350,475,560,width=2,outline="white")
canvas3.create_rectangle(485,350,710,560,width=2,outline="white")
# other components
canvas3.create_window(715,90,anchor="nw",window=time_lbl1)
canvas3.create_window(925,90,anchor="nw",window=time_lbl)
canvas3.create_window(715,120,anchor="nw",window=schedule_btn)
canvas3.create_window(450,50,anchor="nw",window=logo2)
canvas3.create_window(715,163,anchor="nw",window=text_area2)
canvas3.create_window(810,10,anchor="nw",window=inst2)
canvas3.create_window(15,10,anchor="nw",window=file_btn2)
canvas3.create_window(15,60,anchor="nw",window=file_ent2)

######################################################################################################################################################################################################
#another functions page
logo3=Label(me,text="FullBot",bg="#1B9DF0",font="FangSong 18 italic bold",fg="black")
canvas4 = Canvas(others, width = 100, height = 1000)
canvas4.pack(fill = "both", expand = True)
canvas4.create_image( 0, 0, image = bg_img, anchor = "nw")
#other functions accounts file 
my_tokens_2=[]
api_num2=[]
def browseFiles_others():
    my_tokens_2.clear()
    api_num2.clear()
    filename = filedialog.askopenfilename(initialdir = "./",title = "Select a File",filetypes = (("Text files","*.txt*"),("all files","*.*")))
    file_ent3.configure(text=f"{filename}")
    try:
        with open(file_ent3.cget("text"),"r",encoding="utf-8") as api_file:
            my_lines = api_file.readlines()
            for i in my_lines:
                dic = json.loads(i)
                my_tokens_2.append(dic) 
            api_num2.append(my_tokens_2[0]["ID"]-1)    
    except:
        messagebox.showwarning("warning","you must add the path of the file")

file_btn3 = Button(me,text="Add accounts file",bg="black",fg="white",font="FangSong 16",command=browseFiles_others,width=16,padx=0)
file_ent3= Label(me,text="",fg="white",bg="#1B9DF0",wraplength=310)
def add_inst3():
    top = Toplevel()
    top.title("Instructions")
    l2 = Label(top,font="FangSong 14 italic bold ", text = "Welcome to the another functions instructions page\n here you must use logged api 2 file")
    checker_inst = Label(top,font="FangSong 12 italic bold ", text = "Checker\n Put txt file that contains accounts you need to check in this form:\n name1:pass1\n name2:pass2")
    get_followers_inst = Label(top,font="FangSong 12 italic bold ", text = "Get Followers\n Put txt file that contains accounts you need to scrape their followers in this form:\n username1\n username2")
    bio_name_inst= Label(top,font="FangSong 12 italic bold ", text = "Change Bio, Name\n Put txt file that contains names and bios and the program will choose from them randomly\n name1:bio1 \n name2:bio2")
    send_message_inst = Label(top,font="FangSong 12 italic bold ", text = "Send Message\n you must put text file that contains IDs and text file that contain the message")
    l2.pack() 
    checker_inst.pack()
    get_followers_inst.pack()
    bio_name_inst.pack()
    send_message_inst.pack()

text_area3 = Text(me,width=122,height=13)
inst3 = Button(me,text="Instructions",bg="white",fg="#1B9DF0",font="FangSong 16 italic bold",command=add_inst3)
#################################################################
# checker
checker = Label(me,text=" Checker ",fg="white",bg="#1B9DF0",font="FangSong 16 italic bold")
def browseFiles_checker():
    filename = filedialog.askopenfilename(initialdir = "./",title = "Select a File",filetypes = (("Text files","*.txt*"),("all files","*.*")))
    file_ent_check.configure(text=f"{filename}")
file_btn_check = Button(me,text="Choose file",bg="black",fg="white",font="FangSong 12",command=browseFiles_checker,width=16,padx=0)
file_ent_check= Label(me,text="",fg="white",bg="#1B9DF0",wraplength=240)
def check():
    my_time=float(time_lbl.cget("text"))
    try:    
        text_area3.delete("1.0","end")
        chrome_options = Options()
        chrome_options.add_argument("--headless")
        driver=webdriver.Chrome("./my files/main/chromedriver.exe",options=chrome_options)
        driver.implicitly_wait(5) 
        with open(file_ent_check.cget("text"),"r",encoding="utf-8") as my_file:
            my_file_reader = my_file.readlines()
            accounts=[]
            active=[]
            inactive=[]
            restricted=[]
            for i in my_file_reader:
                accounts.append(i.strip().split(":"))
            for i in accounts:
                text_area3.insert(END,f" start checking {i[0]} state....\n")
                me.update()
                text_area3.see("end")
                driver.get(f"https://twitter.com/{i[0]}")   
                try:
                    try:
                        state=driver.find_element("xpath","/html/body/div[1]/div/div/div[2]/main/div/div/div/div/div/div[3]/div/div/div[2]/div/div[1]/span").text
                        if state.count("restricted") == 1:
                            restricted.append(i)
                            text_area3.insert(END,f"{i[0]} is restricted\n")
                        elif state.count("suspended") == 1:
                            inactive.append(i)
                            text_area3.insert(END,f"{i[0]} is suspended\n")
                        else:
                            active.append(i) 
                            text_area3.insert(END,f"{i[0]} is active\n")   
                    except:
                        active.append(i)
                        text_area3.insert(END,f"{i[0]} is active\n")   
                except Exception as e:
                    text_area3.insert(END,e)     
                me.update() 
                text_area3.see("end")
            with open("./my files/checker/active.txt","w",encoding="utf-8") as active_file:
                for i in active:
                    active_file.writelines(f"{':'.join(i)}\n")
            with open("./my files/checker/restricted.txt","w",encoding="utf-8") as restricted_file:
                for i in restricted:
                    restricted_file.writelines(f"{':'.join(i)}\n")
            with open("./my files/checker/suspended.txt","w",encoding="utf-8") as suspended_file:
                for i in inactive:
                    suspended_file.writelines(f"{':'.join(i)}\n")
            text_area3.insert(END,"Finished,see you soon\n") 
            me.update()    
            text_area3.see("end")
    except Exception as e:
        text_area3.insert(END,e)
        me.update() 
        text_area3.see("end")
def thread_start_check():
    threading.Thread(target=check).start()    
start_check_btn = Button(me,text="Start",bg="black",fg="white",font="FangSong 14",command=thread_start_check,width=14,padx=0)
# layout
canvas4.create_window(30,105,anchor="nw",window=checker)
canvas4.create_window(45,140,anchor="nw",window=file_btn_check)
canvas4.create_window(20,185,anchor="nw",window=file_ent_check)
canvas4.create_window(40,280,anchor="nw",window=start_check_btn)

#################################################################
# scraper by username
scraper = Label(me,text=" Get Followers ",fg="white",bg="#1B9DF0",font="FangSong 16 italic bold")
def browseFiles_scraper():
    filename = filedialog.askopenfilename(initialdir = "./",title = "Select a File",filetypes = (("Text files","*.txt*"),("all files","*.*")))
    file_ent_scrap.configure(text=f"{filename}")
file_btn_scrap = Button(me,text="Choose file",bg="black",fg="white",font="FangSong 12",command=browseFiles_scraper,width=16,padx=0)
file_ent_scrap= Label(me,text="",fg="white",bg="#1B9DF0",wraplength=240)
def scrap():
    text_area3.delete("1.0","end")
    try:
        with open(file_ent_scrap.cget("text"),"r",encoding="utf-8") as users_file:
            user_reader = users_file.readlines()
        text_area3.insert(END,"Start scraping followers....\n")
        me.update()
        text_area3.see("end")
        for i in user_reader:
            auth = tweepy.OAuth2AppHandler(keys[api_num2[0]][0].strip(),keys[api_num2[0]][1].strip())
            api = tweepy.API(auth,wait_on_rate_limit=True)
            n=0
            with open(f"./my files/scraper/users/{i.strip()} followers usernames.txt","w",encoding="utf-8") as screen_names:
                text_area3.insert(END,f"start scraping {i.strip()} followers screen names\n") 
                for page in tweepy.Cursor(api.get_followers, screen_name=i.strip(),count=100).pages():                 
                    for j in page:
                        screen_names.writelines(f"{j.screen_name}\n")
                        n=n+1
            text_area3.insert(END,f"{i} followers usernames file created,number of followers:{n}\n") 
        time.sleep(100)    
        for i in user_reader:
            auth = tweepy.OAuth2AppHandler(keys[api_num2[0]][0].strip(),keys[api_num2[0]][1].strip())
            api = tweepy.API(auth,wait_on_rate_limit=True)
            n=0
            with open(f"./my files/scraper/users/{i.strip()} followers ids.txt","w",encoding="utf-8") as screen_names:
                text_area3.insert(END,f"start scraping {i.strip()} followers ids\n") 
                for page in tweepy.Cursor(api.get_followers, screen_name=i.strip(),count=100).pages():                 
                    for j in page:
                        screen_names.writelines(f"{j.id}\n")
                        n=n+1
            text_area3.insert(END,f"{i} followers ids file created,number of followers:{n}\n")     
            me.update()
            text_area3.see("end")       
    except Exception as e:
        text_area3.insert(END,e)                
def thread_start_scrap():
    threading.Thread(target=scrap).start()
start_scrap_btn = Button(me,text="Start",bg="black",fg="white",font="FangSong 14",command=thread_start_scrap,width=14,padx=0)
# layout
canvas4.create_window(275,105,anchor="nw",window=scraper)
canvas4.create_window(290,140,anchor="nw",window=file_btn_scrap)
canvas4.create_window(265,185,anchor="nw",window=file_ent_scrap)
canvas4.create_window(290,280,anchor="nw",window=start_scrap_btn)
#############################################################################################################################################################################################
#change bio and name
bio_name = Label(me,text=" Change bio, Name, Location ",fg="white",bg="#1B9DF0",font="FangSong 13 italic bold")
def browseFiles_bio():
    filename = filedialog.askopenfilename(initialdir = "./",title = "Select a File",filetypes = (("Text files","*.txt*"),("all files","*.*")))
    file_ent_check4.configure(text=f"{filename}")
file_btn_check4 = Button(me,text="Choose file",bg="black",fg="white",font="FangSong 12",command=browseFiles_bio,width=16,padx=0)
file_ent_check4= Label(me,text="",fg="white",bg="#1B9DF0",wraplength=200)
def change_bio_name():  
        my_time=float(time_lbl.cget("text"))
        text_area3.delete("1.0","end")
        my_text=[]
        try:
            with open(file_ent_check4.cget("text"),"r",encoding='utf-8') as my_file:
                reader = my_file.readlines()
                for i in reader:
                    my_text.append(i.strip().split(":"))  
            q=0
            for i in my_tokens_2: 
                try:
                    if q == len(my_text):
                        q=0
                    text_area3.insert(END,f"Start changing {i['Name']} info...\n")
                    me.update()
                    time.sleep(5)
                    auth = tweepy.OAuth1UserHandler(keys[api_num2[0]][0].strip(),keys[api_num2[0]][1].strip(),i["token"], i["secret"])
                    api = tweepy.API(auth,wait_on_rate_limit=True)
                    api.update_profile(name = my_text[q][0],description=my_text[q][1],location=my_text[q][2])
                    text_area3.insert(END,f"{i['Name']} info chnage to name:{my_text[q][0]},description:{my_text[q][1]},location:{my_text[q][2]}\n")
                    me.update()
                    text_area3.see("end")
                    q=q+1
                except Exception as e:
                    text_area3.insert(END,f"{e}\n")
                    me.update() 
                    text_area3.see("end")   
                    q=q+1
        except Exception as e:
            text_area3.insert(END,f"{e}\n")
            me.update()
            text_area3.see("end")
        text_area3.insert(END,f"Finished")
        me.update()   
        text_area3.see("end") 
def thread_start_change_bio_name():
    threading.Thread(target=change_bio_name).start()
start_check_btn3 = Button(me,text="Start",bg="black",fg="white",font="FangSong 14",command=thread_start_change_bio_name,width=14,padx=0)
#checker layout
canvas4.create_window(520,105,anchor="nw",window=bio_name)
canvas4.create_window(545,150,anchor="nw",window=file_btn_check4)
canvas4.create_window(510,200,anchor="nw",window=file_ent_check4)
canvas4.create_window(540,280,anchor="nw",window=start_check_btn3)
#################################################################
# message
messaging = Label(me,text=" Send Message ",fg="white",bg="#1B9DF0",font="FangSong 16 italic bold")
# file of ids 
def browseFiles_message():
    filename = filedialog.askopenfilename(initialdir = "./",title = "Select a File",filetypes = (("Text files","*.txt*"),("all files","*.*")))
    file_ent_message.configure(text=f"{filename}")
file_btn_message = Button(me,text="Ids file",bg="black",fg="white",font="FangSong 12",command=browseFiles_message,width=16,padx=0)
file_ent_message= Label(me,text="",fg="white",bg="#1B9DF0",wraplength=240)
# file of messages
def browseFiles_message_text():
    filename = filedialog.askopenfilename(initialdir = "./",title = "Select a File",filetypes = (("Text files","*.txt*"),("all files","*.*")))
    file_ent_message_text.configure(text=f"{filename}")
file_btn_message_text = Button(me,text="message file",bg="black",fg="white",font="FangSong 12",command=browseFiles_message_text,width=16,padx=0)
file_ent_message_text= Label(me,text="",fg="white",bg="#1B9DF0",wraplength=240)
def start_messaging():
    my_time=float(time_lbl.cget("text"))
    text_area3.delete("1.0","end")
    try:
        with open(file_ent_message.cget("text"),"r",encoding="utf-8") as ids:
            ids_reader = ids.readlines()
        with open(file_ent_message_text.cget("text"),"r",encoding="utf-8") as text_file:
            text_file_reader = text_file.readlines()
        print(text_file_reader)    
        u=0 
        o=0   
        for i in ids_reader:
            if o == len(my_tokens_2):
                break
            try:
                text_area3.insert(END,"Start sending messages....\n")
                me.update()
                text_area3.see("end")
                auth = tweepy.OAuth1UserHandler(keys[api_num2[0]][0].strip(),keys[api_num2[0]][1].strip(),my_tokens_2[o]["token"],my_tokens_2[o]["secret"] )
                api = tweepy.API(auth,wait_on_rate_limit=True)
                api.send_direct_message(recipient_id=i.strip(),text=text_file_reader[0].strip())
                text_area3.insert(END,"message sent\n")
                me.update()
                text_area3.see("end")
                time.sleep(my_time)
                if u == 10:
                    time.sleep(20)
                if u == 499:
                   u =0
                   o=o+1
                u=u+1   
            except Exception as e:
                text_area3.insert(END,f"{e}\n")    
        text_area3.insert(END,"Finished\n")
        me.update()
        text_area3.see("end")
    except Exception as e:
        text_area3.insert(END,f"{e}\n")       

def thread_start_messaging():
    threading.Thread(target=start_messaging).start()    
start_message_btn = Button(me,text="Start",bg="black",fg="white",font="FangSong 14",command=thread_start_messaging,width=14,padx=0)
# layout
canvas4.create_window(765,105,anchor="nw",window=messaging)
canvas4.create_window(780,130,anchor="nw",window=file_btn_message)
canvas4.create_window(760,165,anchor="nw",window=file_ent_message)
canvas4.create_window(780,200,anchor="nw",window=file_btn_message_text)
canvas4.create_window(760,235,anchor="nw",window=file_ent_message_text)
canvas4.create_window(780,280,anchor="nw",window=start_message_btn)
#################################################################
#others 
canvas4.create_window(15,10,anchor="nw",window=file_btn3)
canvas4.create_window(15,60,anchor="nw",window=file_ent3)
canvas4.create_window(450,50,anchor="nw",window=logo3)
canvas4.create_window(810,10,anchor="nw",window=inst3)
canvas4.create_window(8,340,anchor="nw",window=text_area3)
# rectangles
canvas4.create_rectangle(15,120,250,330,width=2,outline="white")
canvas4.create_rectangle(260,120,495,330,width=2,outline="white")
canvas4.create_rectangle(505,120,740,330,width=2,outline="white")
canvas4.create_rectangle(750,120,985,330,width=2,outline="white")
######################################################################################################################################################################################################
#another functions 2 page
logo4=Label(me,text="FullBot",bg="#1B9DF0",font="FangSong 18 italic bold",fg="black")
canvas5 = Canvas(others2, width = 100, height = 1000)
canvas5.pack(fill = "both", expand = True)
canvas5.create_image( 0, 0, image = bg_img, anchor = "nw")
# contstant parts 
def add_inst4():
    top = Toplevel()
    top.title("Instructions")
    l2 = Label(top,font="FangSong 14 italic bold ", text = "Welcome to the another functions instructions page\n here you must use logged api 2 file ")
    change_inst = Label(top,font="FangSong 12 italic bold ", text = "Changing profile and cover pictures\n just put the folder that contain the images and the program will change them randomly")
    l2.pack() 
    change_inst.pack()

text_area4 = Text(me,width=122,height=13)
inst4 = Button(me,text="Instructions",bg="white",fg="#1B9DF0",font="FangSong 16 italic bold",command=add_inst4)

#############################################################################################################################################################################################
# change profile picture
prf_pic = Label(me,text=" Change profile pics ",fg="white",bg="#1B9DF0",font="FangSong 13 italic bold")
# get dirctory
def browseFolder():
    filename = filedialog.askdirectory(initialdir = "./",title = "Select a Folder")
    folder_ent_check1.configure(text=f"{filename}")
folder_btn_check1 = Button(me,text="Choose folder",bg="black",fg="white",font="FangSong 12",command=browseFolder,width=16,padx=0)
folder_ent_check1= Label(me,text="",fg="white",bg="#1B9DF0",wraplength=200)
def change_prf():
    my_time=float(time_lbl.cget("text"))
    text_area4.delete("1.0","end")
    try:
        dir_list = os.listdir(folder_ent_check1.cget("text"))
    except Exception as e:
            text_area4.insert(END,f"{e}\n")
            me.update()
    for i in my_tokens_2:
        try:
            text_area4.insert(END,f"Start changing {i['Name']} pic...\n")
            me.update()
            text_area4.see("end")
            time.sleep(5)
            n = random.randint(0,len(dir_list)-1)
            auth = tweepy.OAuth1UserHandler(keys[api_num2[0]][0].strip(),keys[api_num2[0]][1].strip(),i["token"], i["secret"])
            api = tweepy.API(auth,wait_on_rate_limit=True)  
            api.update_profile_image(filename=f"{folder_ent_check1.cget('text')}/{dir_list[n]}")  
            text_area4.insert(END,f"{i['Name']} pic changed to {dir_list[n]}\n")
            me.update()
            text_area4.see("end")
        except Exception as e:
            text_area4.insert(END,f"{e}\n")
            me.update()    
    text_area4.insert(END,f"Finished")
def thread_start_change_prf():
    threading.Thread(target=change_prf).start()    
start_prf_btn1 = Button(me,text="Start",bg="black",fg="white",font="FangSong 14",command=thread_start_change_prf,width=14,padx=0)
#layout
canvas5.create_window(30,105,anchor="nw",window=prf_pic)
canvas5.create_window(55,150,anchor="nw",window=folder_btn_check1)
canvas5.create_window(20,200,anchor="nw",window=folder_ent_check1)
canvas5.create_window(50,285,anchor="nw",window=start_prf_btn1)
#############################################################################################################################################################################################
# change banner
banner_pic = Label(me,text=" Change banner pics ",fg="white",bg="#1B9DF0",font="FangSong 13 italic bold")
# get dirctory
def browseFolder1():
    filename = filedialog.askdirectory(initialdir = "./",title = "Select a Folder")
    folder_ent_check2.configure(text=f"{filename}")
folder_btn_check2 = Button(me,text="Choose folder",bg="black",fg="white",font="FangSong 12",command=browseFolder1,width=16,padx=0)
folder_ent_check2= Label(me,text="",fg="white",bg="#1B9DF0",wraplength=230)
def change_banner():
    my_time=float(time_lbl.cget("text"))
    text_area4.delete("1.0","end")
    try:
        dir_list = os.listdir(folder_ent_check2.cget("text"))
    except Exception as e:
            text_area4.insert(END,f"{e}\n")
            me.update() 
            text_area4.see("end")
    for i in my_tokens_2:
        try:
            text_area4.insert(END,f"Start changing {i['Name']} banner...\n")
            me.update()
            text_area4.see("end")
            time.sleep(5)
            n = random.randint(0,len(dir_list)-1)
            auth = tweepy.OAuth1UserHandler(keys[api_num2[0]][0].strip(),keys[api_num2[0]][1].strip(),i["token"], i["secret"])
            api = tweepy.API(auth,wait_on_rate_limit=True)  
            api.update_profile_banner(filename=f"{folder_ent_check2.cget('text')}/{dir_list[n]}")  
            text_area4.insert(END,f"{i['Name']} banner changed to {dir_list[n]}\n")
            me.update()
            text_area4.see("end")
        except Exception as e:
            text_area4.insert(END,f"{e}\n")
            me.update()    
            text_area4.see("end")
    text_area4.insert(END,f"Finished")
def thread_start_change_banner():
    threading.Thread(target=change_banner).start()    
start_check_btn2 = Button(me,text="Start",bg="black",fg="white",font="FangSong 14",command=thread_start_change_banner,width=14,padx=0)
#layout
canvas5.create_window(275,105,anchor="nw",window=banner_pic)
canvas5.create_window(300,150,anchor="nw",window=folder_btn_check2)
canvas5.create_window(265,200,anchor="nw",window=folder_ent_check2)
canvas5.create_window(295,285,anchor="nw",window=start_check_btn2) 
###############################################################################################################
# customized function: instant bot
#instant bot: some accuonts will tweet and some will support by liking and retweeting
inst_sup = Label(me,text=" Instant Support ",fg="white",bg="#1B9DF0",font="FangSong 13 italic bold")
#timer
time_id_lbl = Label(me,text="Total time (hours)",fg="white",bg="#1B9DF0",font="FangSong 12 italic bold")
time_id_ent = Entry(me,width=16)
# accounts that will tweet
my_tokens_3=[]
api_num3=[]
def browseFiles_others():
    my_tokens_3.clear()
    api_num3.clear()
    filename = filedialog.askopenfilename(initialdir = "./",title = "Select a File",filetypes = (("Text files","*.txt*"),("all files","*.*")))
    file_ent_sup.configure(text=f"{filename}")
    try:
        with open(file_ent_sup.cget("text"),"r",encoding="utf-8") as api_file:
            my_lines = api_file.readlines()
            for i in my_lines:
                dic = json.loads(i)
                my_tokens_3.append(dic) 
            api_num3.append(my_tokens_3[0]["ID"]-1)    
    except:
        messagebox.showwarning("warning","you must add the path of the file")

file_btn_sup = Button(me,text="Accounts to tweet",bg="black",fg="white",font="FangSong 10 bold",command=browseFiles_others,width=16,padx=0,pady=0)
file_ent_sup= Label(me,text="",fg="white",bg="#1B9DF0",wraplength=500)
# accounts that will support
my_tokens_4=[]
api_num4=[]
def browseFiles_others():
    my_tokens_4.clear()
    api_num4.clear()
    filename = filedialog.askopenfilename(initialdir = "./",title = "Select a File",filetypes = (("Text files","*.txt*"),("all files","*.*")))
    file_ent_sup2.configure(text=f"{filename}")
    try:
        with open(file_ent_sup2.cget("text"),"r",encoding="utf-8") as api_file:
            my_lines = api_file.readlines()
            for i in my_lines:
                dic = json.loads(i)
                my_tokens_4.append(dic) 
            api_num3.append(my_tokens_4[0]["ID"]-1)    
    except:
        messagebox.showwarning("warning","you must add the path of the file")
file_btn_sup2 = Button(me,text="Accounts to support",bg="black",fg="white",font="FangSong 10 bold",command=browseFiles_others,width=16,padx=0,pady=0)
file_ent_sup2= Label(me,text="",fg="white",bg="#1B9DF0",wraplength=500)
# tweets file 
def browse_media_sup():
    filename = filedialog.askopenfilename(initialdir = "./",title = "Select a File")
    media_file_lbl_sup.configure(text=f"{filename}")
media_file_sup = Button(me,text="Add media file ",bg="black",fg="white",font="FangSong 10",command=browse_media_sup,width=16,padx=0)
media_file_lbl_sup= Label(me,text="",fg="white",bg="#1B9DF0",wraplength=500,padx=0,pady=0)

msg_area_sup = Text(me,width=25,height=5)
# replys file
def browseFiles_reply_sup():
    filename = filedialog.askopenfilename(initialdir = "./",title = "Select replys File",filetypes = (("Text files","*.txt*"),("all files","*.*")))
    replys_file_lbl_sup.configure(text=f"{filename}")
replys_file_sup = Button(me,text="Add replys file",bg="black",fg="white",font="FangSong 10 bold",command=browseFiles_reply_sup,width=16,padx=0)
replys_file_lbl_sup= Label(me,text="",fg="white",bg="#1B9DF0",wraplength=500,padx=0,pady=0) 
# qoutes file
def browseFiles_qoutes_sup():
    filename = filedialog.askopenfilename(initialdir = "./",title = "Select qoutes File",filetypes = (("Text files","*.txt*"),("all files","*.*")))
    qoutes_file_lbl_sup.configure(text=f"{filename}")
qoutes_file_sup = Button(me,text="Add qoutes file",bg="black",fg="white",font="FangSong 10 bold",command=browseFiles_qoutes_sup,width=16,padx=0,pady=0)
qoutes_file_lbl_sup= Label(me,text="",fg="white",bg="#1B9DF0",wraplength=500,padx=0,pady=0)
# function to start tweet and support  
def instant_support():
    my_time=float(time_lbl.cget("text"))
    all_time= 60*60*int(time_id_ent.get())/my_time
    text_area4.insert(END,f"time:{time_id_ent.get()} hours\n")
    me.update()
    text_area4.see("end")
    repeats=0
    while repeats<all_time:  
        try:
            with open(replys_file_lbl_sup.cget("text"),"r",encoding="utf-8") as replys:
                replys_reader = replys.readlines()
        except Exception as e:
            text_area4.insert(END,f"{e}\n")
            me.update()    
            text_area4.see("end")
        try:
            with open(qoutes_file_lbl_sup.cget("text"),"r",encoding="utf-8") as qoutes:
                qoutes_reader = qoutes.readlines()
        except Exception as e:
            text_area4.insert(END,f"{e}\n")
            me.update()    
            text_area4.see("end")                        
        counter=0
        for i in my_tokens_3:
            #tweeting
            try:
                auth = tweepy.OAuth1UserHandler(
                keys[api_num3[0]][0].strip(),keys[api_num3[0]][1].strip(),
                i["token"], i["secret"] )
                api = tweepy.API(auth,wait_on_rate_limit=True)
                tweet_txt=api.update_status_with_media(msg_area_sup.get("1.0","end"),filename=media_file_lbl_sup.cget("text"))
                tweet_id=tweet_txt._json["id"]
                text_area4.insert(END,f"{i['Name']} tweeted with {msg_area} and {media_file_lbl_sup.cget('text')}\n")
                me.update()
                text_area4.see("end")
                counter = counter+1 
                #reply
                for j in my_tokens_4:    
                    try:
                        reply_txt = replys_reader[math.floor(random.randint(0,len(replys_reader)-1))].strip()
                        auth = tweepy.OAuth1UserHandler(
                        keys[api_num3[0]][0].strip(),keys[api_num3[0]][1].strip(),
                        j["token"], j["secret"] )
                        api = tweepy.API(auth,wait_on_rate_limit=True)
                        api.update_status(status=f"@{i['Name']} {reply_txt}",in_reply_to_status_id=tweet_id)
                        text_area4.insert("end",f"{j['Name']} replyed to {tweet_id} with {reply_txt}\n")
                        me.update()
                        text_area4.see("end")
                    except Exception as e:
                        text_area4.insert(END,f"{e}\n")
                        me.update()    
                        text_area4.see("end")
                    time.sleep(5)    
                #like the tweet        
                for j in my_tokens_4: 
                    try:
                        auth = tweepy.OAuth1UserHandler(
                        keys[api_num3[0]][0].strip(),keys[api_num3[0]][1].strip(),
                        j["token"], j["secret"] )
                        api = tweepy.API(auth,wait_on_rate_limit=True)
                        api.create_favorite(id=tweet_id)
                        text_area4.insert("end",f"{j['Name']} liked {tweet_id}\n")
                        me.update()
                        text_area4.see("end")                
                    except Exception as e:
                        text_area4.insert(END,f"{e}\n")
                        me.update()    
                        text_area4.see("end") 
                    time.sleep(5)
                # retweet 
                for j in my_tokens_4:    
                    try:
                        auth = tweepy.OAuth1UserHandler(
                        keys[api_num3[0]][0].strip(),keys[api_num3[0]][1].strip(),
                        j["token"], j["secret"] )
                        api = tweepy.API(auth,wait_on_rate_limit=True)
                        api.retweet(id=tweet_id)
                        text_area4.insert("end",f"{j['Name']} retweeted {tweet_id}\n")
                        me.update()
                        text_area4.see("end")                
                    except Exception as e:
                        text_area4.insert(END,f"{e}\n")
                        me.update()    
                        text_area4.see("end")                                 
                    time.sleep(5)
                # qoute                    
                for j in my_tokens_4:    
                    try:
                        qoute_txt = qoutes_reader[math.floor(random.randint(0,len(qoutes_reader)-1))].strip()
                        auth = tweepy.OAuth1UserHandler(
                        keys[api_num3[0]][0].strip(),keys[api_num3[0]][1].strip(),
                        j["token"], j["secret"] )
                        api = tweepy.API(auth,wait_on_rate_limit=True)
                        api.update_status(qoute_txt.strip(),attachment_url=f"https://twitter.com/{i['Name']}/status/{tweet_id}")
                        text_area4.insert("end",f"{j['Name']} qouted {tweet_id} with {qoute_txt}\n")
                        me.update()
                        text_area4.see("end")
                    except Exception as e:
                        text_area4.insert(END,f"{e}\n")
                        me.update()    
                        text_area4.see("end") 
                    time.sleep(5)                                
            except Exception as e:
                text_area4.insert(END,f"{e}\n")
                me.update()    
                text_area4.see("end") 
            text_area4.insert(END,f"rest for {my_time} secs...\n")
            me.update()
            text_area4.see("end")        
            time.sleep(my_time)   
            repeats=repeats+1    
# start button
def thread_start_instant_sup():
    threading.Thread(target=instant_support).start()
start_support_btn=Button(me,text="Start",bg="black",fg="white",width=16,font="FangSong 14",padx=0,pady=0,command=thread_start_instant_sup)
#layout of instant support
canvas5.create_window(610,85,anchor="nw",window=inst_sup)
canvas5.create_window(620,110,anchor="nw",window=file_ent_sup)
canvas5.create_window(480,110,anchor="nw",window=file_btn_sup)
canvas5.create_window(620,140,anchor="nw",window=file_ent_sup2)
canvas5.create_window(480,140,anchor="nw",window=file_btn_sup2)
canvas5.create_window(620,170,anchor="nw",window=media_file_lbl_sup)
canvas5.create_window(480,170,anchor="nw",window=media_file_sup)
canvas5.create_window(480,258,anchor="nw",window=msg_area_sup)
canvas5.create_window(620,200,anchor="nw",window=replys_file_lbl_sup)
canvas5.create_window(480,200,anchor="nw",window=replys_file_sup)
canvas5.create_window(620,230,anchor="nw",window=qoutes_file_lbl_sup)
canvas5.create_window(480,230,anchor="nw",window=qoutes_file_sup)
canvas5.create_window(805,309,anchor="nw",window=start_support_btn)
canvas5.create_window(720,60,anchor="nw",window=time_id_lbl)
canvas5.create_window(860,62,anchor="nw",window=time_id_ent)
#others
canvas5.create_window(450,50,anchor="nw",window=logo4)
canvas5.create_window(850,10,anchor="nw",window=inst4)
canvas5.create_window(8,355,anchor="nw",window=text_area4)
# rectangles
canvas5.create_rectangle(10,120,235,330,width=2,outline="white")
canvas5.create_rectangle(245,120,470,330,width=2,outline="white")
canvas5.create_rectangle(478,100,990,345,width=2,outline="white")
me.mainloop()
