import tweepy
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
import time
import json
import sys
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

# start the app GUI 
me=tk.Tk()
me.title("Twitter FullBot")
me.geometry("1000x600")
me.maxsize(1000,600)
me.minsize(1000,600)

# tabs of our program
tabControl = ttk.Notebook(me)
Welcome = ttk.Frame(tabControl,width=1000,height=600)
Add_accounts = ttk.Frame(tabControl,width=1000,height=600)
Operations = ttk.Frame(tabControl,width=1000,height=600)
others = ttk.Frame(tabControl,width=1000,height=600)
tabControl.add(Welcome, text ='  Welcome  ')
tabControl.add(Add_accounts, text ='  Add Accounts  ')
tabControl.add(Operations, text ='  Operations  ')
tabControl.add(others, text ='  Another Functions  ')
tabControl.pack(expand = 1, fill ="both") 

# background imgs
bg_img= ImageTk.PhotoImage(Image.open("./my files/Ful.png")) 
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
note=Label(me,text=" Note: Follow the instructions of it's function in the bot to avoid errors",bg="#1B9DF0",fg="black",font = "FangSong 16 bold",anchor="w",width=60)
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
canvas1.create_window(0,540,anchor="nw",window=note)

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
    text_area.delete("1.0","end")
    my_inputs = []
    keys=[]
    try:
        # open and read file of APIs
        with open("./my files/keys.txt","r") as keys_file:
            my_keys=keys_file.readlines()
            for i in my_keys:
                keys.append(i.split(":"))                 
        #open the file and get data
        if file_ent.cget("text")!= "":
            with open(file_ent.cget("text"),"r") as my_file:
                my_lines = my_file.readlines()
                for i in my_lines:
                    my_inputs.append(i.split(":"))
            # loop in our dtat to get access token and secret  
            n=0
            if v.get() == "Headless":
                chrome_options = Options()
                chrome_options.add_argument("--headless")
            else:
                chrome_options = Options()


            while n<len(my_keys):  
                all_logged=[]   
                text_area.insert(END,f"start logging to accounts with API {n+1}\n")      
                for i in my_inputs:
                    my_obj ={}
                    driver = webdriver.Chrome("./my files/chromedriver",options=chrome_options)  

                    oauth1_user_handler = tweepy.OAuth1UserHandler(
                                keys[n][0].strip(), keys[n][1].strip(),
                                callback="oob")
                    
                    me.update()        
                    my_link = oauth1_user_handler.get_authorization_url()
                    driver.get(my_link)
                    driver.find_element("xpath",'/html/body/div[2]/div/form/fieldset[1]/div[1]/input').send_keys(i[0].strip())
                    time.sleep(3)
                    driver.find_element("xpath",'/html/body/div[2]/div/form/fieldset[1]/div[2]/input').send_keys(i[1].strip())
                    time.sleep(3)
                    driver.find_element("xpath","/html/body/div[2]/div/form/fieldset[2]/input[1]").click()
                    try:
                        verifier = driver.find_element("xpath","/html/body/div[2]/div/p/kbd/code").text
                        time.sleep(3)
                        access_token, access_token_secret = oauth1_user_handler.get_access_token(verifier)
                        my_obj["Name"]=i[0]
                        my_obj["pass"] = i[1]
                        my_obj[f"token{n+1}"] = access_token
                        my_obj[f"secret{n+1}"] = access_token_secret
                        text_area.insert(END,f"{i[0]} logged successfully\n")
                        all_logged.append(my_obj)

                    except:
                        try:
                            
                            driver.find_element("xpath","/html/body/div[2]/div/form/input[8]").send_keys(i[2].strip())
                            time.sleep(3)
                            driver.find_element("xpath","/html/body/div[2]/div/form/input[9]").click()
                            time.sleep(3)
                            driver.find_element("xpath","/html/body/div[2]/div/form/fieldset/input[1]").click()
                            time.sleep(3)
                            verifier = driver.find_element("xpath","/html/body/div[2]/div/p/kbd/code").text
                            access_token, access_token_secret = oauth1_user_handler.get_access_token(verifier)
                            my_obj["Name"]=i[0]
                            my_obj["pass"] = i[1]
                            my_obj[f"token{n+1}"] = access_token
                            my_obj[f"secret{n+1}"] = access_token_secret
                            text_area.insert(END,f"{i[0]} logged successfully\n")
                            all_logged.append(my_obj)
                        except:
                            text_area.insert(END,f"error in the account:{i[0]}\n") 
                    me.update()        
                
                n=n+1
                with open(f"./my files/logged API {n}.txt","a") as logged_file:
                    for l in all_logged:
                        logged_file.write(f"{json.dumps(l)}\n")
            text_area.insert(END,f"Finished,see you later")             
            
        else:
            messagebox.showwarning("warning","you must add the path of the file")
    except Exception as e:
        text_area.insert(END,f"{e}") 


start_btn=Button(me,text="Start",width=20,font="FangSong 16",padx=0,command=start_login)
canvas2.create_window(450,50,anchor="nw",window=logo1)
canvas2.create_window(35,385,anchor="nw",window=start_btn)
canvas2.create_window(35,280,anchor="nw",window=file_btn)
canvas2.create_window(35,330,anchor="nw",window=file_ent)
canvas2.create_window(810,10,anchor="nw",window=inst1)
canvas2.create_window(30,110,anchor="nw",window=add_lbl1)
canvas2.create_window(30,150,anchor="nw",window=radio1)
canvas2.create_window(30,190,anchor="nw",window=radio2)
canvas2.create_window(500,100,anchor="nw",window=text_area)
canvas2.create_rectangle(25,255,330,455,width=2,outline="white")


######################################################################################################################################################################################################
#Opertaions page
keys=[]
with open("./my files/keys.txt","r") as keys_file:
            my_keys=keys_file.readlines()
            for i in my_keys:
                keys.append(i.split(":")) 
               
def add_inst2():
    top = Toplevel()
    top.title("Instructions")
    l2 = Label(top,font="FangSong 14 italic ", text = "")
    l2.pack() 

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
my_tokens=[]
def browseFiles1():
    filename = filedialog.askopenfilename(initialdir = "./",title = "Select a File",filetypes = (("Text files","*.txt*"),("all files","*.*")))
    file_ent2.configure(text=f"{filename}")
    try:
        with open(file_ent2.cget("text"),"r") as api_file:
            my_lines = api_file.readlines()
            for i in my_lines:
                dic = json.loads(i)
                my_tokens.append(dic) 
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
                for i in my_tokens:
                    auth = tweepy.OAuth1UserHandler(
                    keys[0][0].strip(),keys[0][1].strip(),
                    i["token1"], i["secret1"] )
                    api = tweepy.API(auth)
                    api.create_favorite(id=like_id_ent.get())
                    text_area2.insert("end",f"{i['Name']} liked {like_id_ent.get()}\n")
                    me.update()
                    time.sleep(my_time)
            elif ids_file_lbl.cget("text") != "" and ids_file_lbl.cget("text") != "()":
                with open(ids_file_lbl.cget("text"),"r") as ids_file:
                    reader = ids_file.readlines()
                for i in reader:
                    for j in my_tokens:
                        auth = tweepy.OAuth1UserHandler(
                        keys[0][0].strip(),keys[0][1].strip(),
                        j["token1"], j["secret1"] )
                        api = tweepy.API(auth)
                        api.create_favorite(id=int(i.strip()))
                        text_area2.insert("end",f"{j['Name']} liked {i.strip()}\n")
                        me.update()
                        time.sleep(my_time)
        except Exception as e:
            text_area2.insert("end",f"{e}\n") 
start_like_btn = Button(me,text="Start",bg="black",fg="white",font="FangSong 14",command=like_tweet,width=14,padx=0)
#like layout
canvas3.create_window(30,105,anchor="nw",window=like)
canvas3.create_window(20,140,anchor="nw",window=like_id_lbl)
canvas3.create_window(100,140,anchor="nw",window=like_id_ent)
canvas3.create_window(45,170,anchor="nw",window=like_separator)
canvas3.create_window(45,190,anchor="nw",window=ids_file)
canvas3.create_window(28,230,anchor="nw",window=ids_file_lbl)
canvas3.create_window(40,290,anchor="nw",window=start_like_btn)

######################################################################################################################################################################################################
#folow
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
                for i in my_tokens:
                    auth = tweepy.OAuth1UserHandler(
                    keys[0][0].strip(),keys[0][1].strip(),
                    i["token1"], i["secret1"] )
                    api = tweepy.API(auth)
                    api.create_friendship(screen_name=follow_usr_ent.get())
                    text_area2.insert("end",f"{i['Name']} followed {follow_usr_ent.get()}\n")
                    me.update()
                    time.sleep(my_time)
            elif users_file_lbl.cget("text") != "" and users_file_lbl.cget("text") != "()":
                with open(users_file_lbl.cget("text"),"r") as users_file:
                    reader = users_file.readlines()
                for i in reader:
                    for j in my_tokens:
                        auth = tweepy.OAuth1UserHandler(
                        keys[0][0].strip(),keys[0][1].strip(),
                        j["token1"], j["secret1"] )
                        api = tweepy.API(auth)
                        api.create_friendship(screen_name=i.strip())
                        text_area2.insert("end",f"{j['Name']} followed {i.strip()}\n")
                        me.update()
                        time.sleep(my_time)
        except Exception as e:
            text_area2.insert("end",f"{e}\n")    
    
start_follow_btn = Button(me,text="Start",bg="black",fg="white",font="FangSong 14",command=follow_someone,width=14,padx=0)
#follow layout
canvas3.create_window(30,335,anchor="nw",window=follow)
canvas3.create_window(17,370,anchor="nw",window=follow_usr_lbl)
canvas3.create_window(102,370,anchor="nw",window=follow_usr_ent)
canvas3.create_window(45,400,anchor="nw",window=follow_separator)
canvas3.create_window(45,420,anchor="nw",window=users_file)
canvas3.create_window(28,460,anchor="nw",window=users_file_lbl)
canvas3.create_window(40,520,anchor="nw",window=start_follow_btn)
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
        with open(replys_file_lbl.cget("text"),"r") as rply_file:
            reader = rply_file.readlines()
        try:
            for i in my_tokens:
                reply_txt = reader[math.floor(random.randint(0,len(reader)-1))].strip()
                auth = tweepy.OAuth1UserHandler(
                keys[0][0].strip(),keys[0][1].strip(),
                i["token1"], i["secret1"] )
                api = tweepy.API(auth)
                api.update_status(status=f"@{usr_reply_ent.get()} {reply_txt}",in_reply_to_status_id=tweet_id_ent.get())
                text_area2.insert("end",f"{i['Name']} replyed to {tweet_id_ent.get()} with {reply_txt}\n")
                me.update()
                time.sleep(my_time)
        except Exception as e:
            text_area2.insert("end",f"{e}\n")       
    else:
        messagebox.showwarning("warning","you must fill all enteries(username,tweet id, replys file)")        
                
        

start_reply_btn = Button(me,text="Start",bg="black",fg="white",font="FangSong 14",command=reply_to_tweet,width=14,padx=0)
#reply layout
canvas3.create_window(265,105,anchor="nw",window=reply)
canvas3.create_window(255,140,anchor="nw",window=tweet_id_lbl)
canvas3.create_window(330,140,anchor="nw",window=tweet_id_ent)
canvas3.create_window(252,170,anchor="nw",window=username_reply)
canvas3.create_window(332,170,anchor="nw",window=usr_reply_ent)
canvas3.create_window(280,195,anchor="nw",window=replys_file)
canvas3.create_window(263,230,anchor="nw",window=replys_file_lbl)
canvas3.create_window(275,290,anchor="nw",window=start_reply_btn)

######################################################################################################################################################################################################
#tweet
# tweet file without media
def tweet_without_media():
    text_area2.delete("1.0","end")
    my_time=float(time_lbl.cget("text"))
    filename = filedialog.askopenfilename(initialdir = "./",title = "Select a File",filetypes = (("Text files","*.txt*"),("all files","*.*")))
    tweets_file_lbl1.configure(text=f"{filename}") 
    me.update()
    try:
        with open(tweets_file_lbl1.cget("text"),"r") as my_file:
            reader = my_file.readlines()      
        n=0
        for i in my_tokens:
            auth = tweepy.OAuth1UserHandler(
            keys[0][0].strip(),keys[0][1].strip(),
            i["token1"], i["secret1"] )
            api = tweepy.API(auth)
            api.update_status(reader[n].strip())
            time.sleep(my_time)
            text_area2.insert(END,f"{i['Name']} tweeted with {reader[n]}\n")
            me.update()
            n=n+1
    except Exception as e:
        text_area2.insert(END,f"{e}\n")          
            


tweets_file1 = Button(me,text="Tweet Without Media",bg="black",fg="white",font="FangSong 12",command=tweet_without_media,width=17,padx=2)
tweets_file_lbl1= Label(me,text="",fg="white",bg="#1B9DF0",wraplength=200,padx=0,pady=0)  
#tweet file with media 
def tweet_with_media():
    text_area2.delete("1.0","end")
    my_time=float(time_lbl.cget("text"))
    filename = filedialog.askopenfilename(initialdir = "./",title = "Select a File",filetypes = (("Text files","*.txt*"),("all files","*.*")))
    tweets_file_lbl2.configure(text=f"{filename}") 
    me.update()
    try:
        with open(tweets_file_lbl2.cget("text"),"r") as my_file:
            reader = my_file.readlines() 
        data=[]    
        for j in reader:
            data.append(j.split(":"))

        n=0
        for i in my_tokens:
            auth = tweepy.OAuth1UserHandler(
            keys[0][0].strip(),keys[0][1].strip(),
            i["token1"], i["secret1"] )
            api = tweepy.API(auth)
            api.update_status_with_media(data[n][0].strip(),filename=data[n][1].strip())
            time.sleep(my_time)
            text_area2.insert(END,f"{i['Name']} tweeted with {reader[n]}\n")
            me.update()
            n=n+1
    except Exception as e:
        text_area2.insert(END,f"{e}\n")

    
tweets_file2 = Button(me,text="Tweet with Media",bg="black",fg="white",font="FangSong 12",command=tweet_with_media,width=16,padx=0)
tweets_file_lbl2= Label(me,text="",fg="white",bg="#1B9DF0",wraplength=200,padx=0,pady=0) 
tweet = Label(me,text=" Tweet ",fg="white",bg="#1B9DF0",font="FangSong 16 italic bold")

#tweet layout
canvas3.create_window(265,335,anchor="nw",window=tweet)
canvas3.create_window(278,365,anchor="nw",window=tweets_file1)
canvas3.create_window(265,400,anchor="nw",window=tweets_file_lbl1)
canvas3.create_window(285,455,anchor="nw",window=tweets_file2)
canvas3.create_window(265,490,anchor="nw",window=tweets_file_lbl2)

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
                for i in my_tokens:
                    auth = tweepy.OAuth1UserHandler(
                    keys[0][0].strip(),keys[0][1].strip(),
                    i["token1"], i["secret1"] )
                    api = tweepy.API(auth)
                    api.retweet(id=retweet_id_ent.get())
                    text_area2.insert("end",f"{i['Name']} retweeted {retweet_id_ent.get()}\n")
                    me.update()
                    time.sleep(my_time)
            elif ids_file_lbl1.cget("text") != "" and ids_file_lbl1.cget("text") != "()":
                with open(ids_file_lbl1.cget("text"),"r") as ids_file1:
                    reader = ids_file1.readlines()
                for i in reader:
                    for j in my_tokens:
                        auth = tweepy.OAuth1UserHandler(
                        keys[0][0].strip(),keys[0][1].strip(),
                        j["token1"], j["secret1"] )
                        api = tweepy.API(auth)
                        api.retweet(id=int(i.strip()))
                        text_area2.insert("end",f"{j['Name']} retweeted {i.strip()}\n")
                        me.update()
                        time.sleep(my_time)
        except Exception as e:
            text_area2.insert("end",f"{e}\n")    

start_retweet_btn = Button(me,text="Start",bg="black",fg="white",font="FangSong 14",command=retweet_tweet,width=14,padx=0)

#retweet layout
canvas3.create_window(495,105,anchor="nw",window=retweet)
canvas3.create_window(490,140,anchor="nw",window=retweet_id_lbl)
canvas3.create_window(565,140,anchor="nw",window=retweet_id_ent)
canvas3.create_window(510,170,anchor="nw",window=retweet_separator)
canvas3.create_window(510,190,anchor="nw",window=ids_file1)
canvas3.create_window(493,230,anchor="nw",window=ids_file_lbl1)
canvas3.create_window(505,290,anchor="nw",window=start_retweet_btn)
######################################################################################################################################################################################################
#qoute
def browseFiles4():
    filename = filedialog.askopenfilename(initialdir = "./",title = "Select a File",filetypes = (("Text files","*.txt*"),("all files","*.*")))
    qoutes_file_lbl.configure(text=f"{filename}")
qoutes_file = Button(me,text="Add qoutes file",bg="black",fg="white",font="FangSong 12",command=browseFiles4,width=16,padx=0)
qoutes_file_lbl= Label(me,text="",fg="white",bg="#1B9DF0",wraplength=200,padx=0,pady=0)
def qoute_tweet():
    text_area2.delete("1.0","end")
    my_time=float(time_lbl.cget("text"))
    try:
        with open(qoutes_file_lbl.cget("text"),"r") as my_file:
            reader = my_file.readlines() 
        data=[]    
        for j in reader:
            data.append(j.split("|"))

        n=0
        for i in my_tokens:
            auth = tweepy.OAuth1UserHandler(
            keys[0][0].strip(),keys[0][1].strip(),
            i["token1"], i["secret1"] )
            api = tweepy.API(auth)
            api.update_status(data[n][0].strip(),attachment_url=data[n][1].strip())
            time.sleep(my_time)
            text_area2.insert(END,f"{i['Name']} tweeted with {data[n][1]} with {data[n][0]}\n")
            me.update()
            n=n+1
    except Exception as e:
        text_area2.insert(END,f"{e}\n")
    

quote = Label(me,text=" Qoute ",fg="white",bg="#1B9DF0",font="FangSong 16 italic bold")
start_qoute_btn = Button(me,text="Start",bg="black",fg="white",font="FangSong 14",command=qoute_tweet,width=14,padx=0)

#qoute layout
canvas3.create_window(512,370,anchor="nw",window=qoutes_file)
canvas3.create_window(493,410,anchor="nw",window=qoutes_file_lbl)
canvas3.create_window(495,335,anchor="nw",window=quote)
canvas3.create_window(505,520,anchor="nw",window=start_qoute_btn)
######################################################################################################################################################################################################
# Rectangles
canvas3.create_rectangle(15,120,240,330,width=2,outline="white")
canvas3.create_rectangle(250,120,475,330,width=2,outline="white")
canvas3.create_rectangle(485,120,705,330,width=2,outline="white")
canvas3.create_rectangle(15,350,245,560,width=2,outline="white")
canvas3.create_rectangle(255,350,475,560,width=2,outline="white")
canvas3.create_rectangle(485,350,705,560,width=2,outline="white")
# other components
canvas3.create_window(712,90,anchor="nw",window=time_lbl1)
canvas3.create_window(922,90,anchor="nw",window=time_lbl)
canvas3.create_window(712,120,anchor="nw",window=schedule_btn)
canvas3.create_window(450,50,anchor="nw",window=logo2)
canvas3.create_window(712,163,anchor="nw",window=text_area2)
canvas3.create_window(810,20,anchor="nw",window=inst2)
canvas3.create_window(15,10,anchor="nw",window=file_btn2)
canvas3.create_window(15,50,anchor="nw",window=file_ent2)




######################################################################################################################################################################################################
#another functions page
logo3=Label(me,text="FullBot",bg="#1B9DF0",font="FangSong 18 italic bold",fg="black")
canvas4 = Canvas(others, width = 100, height = 1000)
canvas4.pack(fill = "both", expand = True)
canvas4.create_image( 0, 0, image = bg_img, anchor = "nw")
canvas4.create_window(450,50,anchor="nw",window=logo3)


me.mainloop()
