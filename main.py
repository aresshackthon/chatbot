from flask import Flask, render_template, request
# from dialogue_manager import *
from MainBot import get_response
import pandas as pd
import csv
import numpy as np
from flask import Flask, redirect, url_for, render_template, request
from pydrive.auth import GoogleAuth
import pandas as pd
from datetime import datetime
from datetime import date
import os

today = date.today()
d1 = today.strftime("%d_%m_%Y")

now = datetime.now()
dt_string = now.strftime("%d/%m/%Y %H:%M:%S")


gauth = GoogleAuth()
gauth.LocalWebserverAuth()
from pydrive.drive import GoogleDrive
 
response_list = []
user_input_list = []
time_stamp_list = []
    
app = Flask(__name__)
# dialogue_manager = DialogueManager()

@app.route("/")
def home():
    return render_template("index.html")
# @app.route('/website', methods=['GET', 'POST'])
# def website():
#     return redirect('www.google.com')
    
@app.route("/get")
def get_bot_response():
    userText = request.args.get('msg')
    user_input_list.append(userText)
    response_data = get_response(userText)
    response_list.append(response_data)
    
    now = datetime.now()
    dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
    time_stamp_list.append(dt_string)

    old_filename = "data_" + str(d1) + "_.csv"
    if not os.path.exists(old_filename):
        exist_data = pd.DataFrame()
    else:
        exist_data = pd.read_csv(old_filename)
    if response_data == "Success! We will send this to the VermiGold team to get back to you shortly, either by email or phone number":
        print(len(response_list))
        print(len(user_input_list))
        print(len(time_stamp_list))
        user_input_list.append(np.nan)
        response_list.append(np.nan)
        time_stamp_list.append(dt_string)
        ######################### dataframe and drive##########
        
        all_list = [[response_list],[user_input_list]]
        df = pd.DataFrame({'Time':time_stamp_list,
            "Question":response_list,"Answer":user_input_list})
        df.Question = df.Question.shift(1)
        # exist_data=exist_data.append(df)
        # exist_data.to_csv(old_filename,index=False)
        df.to_csv(old_filename,index=False,mode='a',date_format='%Y-%m-%d %H:%M:%S')
        drive = GoogleDrive(gauth)

        file1 = drive.CreateFile({'title': 'Final_Chatbot.csv'})  
        var=pd.read_csv(old_filename)
        print(var)
        file1.SetContentString(f"{var}") 

        file1.Upload()
        
        response_list.clear()
        user_input_list.clear()
        time_stamp_list.clear()


    return response_data
    # return str(dialogue_manager.generate_answer(userText))
 

if __name__ == "__main__":
    app.run(host='0.0.0.0')
