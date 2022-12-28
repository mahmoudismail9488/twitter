import tweepy
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import json
import sys
# function to log in twitter and get access token and access token secret and put object with (name, pass, access token, secret)
# get file with user pass email pass
# get file with user pass phone-number
#function to get file path input 
def enter_file():
    file = input("Enter the path of the file: ")
    return file
#function to display menu
def menu():
    process=int(input("""Enter number of the operation: 
    1. Login to accounts
    2. Do operation(follow,message,..etc)
    3. Exit
    """))
    return process
#function to take the input and perform
def start():
    num=menu()
    all_logged=[]
    my_inputs = []
    #function to get the inputs from the file 
    if num == 1:    
        #open the file and get data
        with open(enter_file(),"r") as my_file:
            my_lines = my_file.readlines()
            for i in my_lines:
                my_inputs.append(i.split(":"))
              
    # loop in our dtat to get access token and secret            
        for i in my_inputs:
            my_obj ={}
            driver = webdriver.Chrome("/media/som3aaz/Mahmoud ismail/freelancing/mostqel/twitter bot/full bot/chromedriver")  
            oauth1_user_handler = tweepy.OAuth1UserHandler(
                        "LrgWcTL5LWkb8qpSOa03J9Yp1", "0aCXBkrJnxaZ3CB04JDotoNdHOFHFVQrj9WF7ur7NcbhO6q8zt",
                        callback="oob")
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
                my_obj["token"] = access_token
                my_obj["secret"] = access_token_secret
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
                    my_obj["token"] = access_token
                    my_obj["secret"] = access_token_secret
                    all_logged.append(my_obj)
                except:
                    print(f"error in the account:{i[0]}") 
        
        with open("./logged.txt","a") as logged_file:
            print(all_logged)
            for l in all_logged:
                logged_file.write(f"{json.dumps(l)}\n")
    elif num == 2:
        my_tokens=[]
        with open(enter_file(),"r") as api_file:
            my_lines = api_file.readlines()
            for i in my_lines:
                dic = json.loads(i)
                my_tokens.append(dic)
        operateion=int(input("""Enter operation number: 
        1.instant support
        2.Send message
        3.Retweet
        4.Tweet
        5.Get data about an account
        """))

        if operateion == 1:
            replys=["جربته و رائع","شكراً جزيل","الله يسعدك 🙏🏻","جزاك الله خير","خصم لي الكود شكراً👏👏","شكراً من القلب 🤲🤲","ثانكيو👌👌👌","شكراً شكراً شكراً على الكو","كودك خصم لي 👍","خصملي كثيرررر😍😍","شكراً من القلب 🤲🤲","ثانكيو👌👌👌","شكراً شكراً شكراً على الكو","كودك خصم لي 👍","خصملي كثيرررر😍😍"]
            j=0

            for i in my_tokens:
                auth = tweepy.OAuth1UserHandler(
                "LrgWcTL5LWkb8qpSOa03J9Yp1", "0aCXBkrJnxaZ3CB04JDotoNdHOFHFVQrj9WF7ur7NcbhO6q8zt",
                i["token1"], i["secret1"] )
                api = tweepy.API(auth)
                try:
                    api.create_favorite(id=1602856973950914561)
                    api.retweet(id=1602856973950914561)
                    print(j)
                    j=j+1
                    time.sleep(5)
                except Exception as e:
                    print(e)

                

                


        else:
            print("we are working on the other operations")
    elif num == 3:
        print("good bye")
        sys.exit()
start()




