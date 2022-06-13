import re
import long_responses as long
import pandas as pd
import csv
import json
data1 = json.loads(open("intents.json").read())
 
print(data1["intents"][1]["responses"])
print(str(data1["intents"][0]["responses"]))

def listToString(s): 
    str1 = "" 
    for ele in s: 
        str1 += ele   
    return str1

A=listToString(data1["intents"][0]["responses"]) 
B=listToString(data1["intents"][1]["responses"]) 
C=listToString(data1["intents"][2]["responses"]) 
D=listToString(data1["intents"][3]["responses"]) 
E=listToString(data1["intents"][4]["responses"]) 
F=listToString(data1["intents"][5]["responses"]) 
G=listToString(data1["intents"][6]["responses"]) 
H=listToString(data1["intents"][7]["responses"]) 
I=listToString(data1["intents"][8]["responses"]) 
J=listToString(data1["intents"][9]["responses"]) 


K=listToString(data1["intents"][10]["responses"]) 
L=listToString(data1["intents"][11]["responses"]) 
M=listToString(data1["intents"][12]["responses"]) 
N=listToString(data1["intents"][13]["responses"]) 
O=listToString(data1["intents"][14]["responses"]) 
P=listToString(data1["intents"][15]["responses"]) 
Q=listToString(data1["intents"][16]["responses"]) 
R=listToString(data1["intents"][17]["responses"]) 
S=listToString(data1["intents"][18]["responses"]) 
T=listToString(data1["intents"][19]["responses"])

U=listToString(data1["intents"][20]["responses"]) 
V=listToString(data1["intents"][21]["responses"]) 
W=listToString(data1["intents"][22]["responses"]) 
X=listToString(data1["intents"][23]["responses"]) 
Y=listToString(data1["intents"][24]["responses"]) 
Z=listToString(data1["intents"][25]["responses"]) 
A1=listToString(data1["intents"][26]["responses"]) 
A2=listToString(data1["intents"][27]["responses"]) 
A3=listToString(data1["intents"][28]["responses"]) 
A4=listToString(data1["intents"][29]["responses"])

A5=listToString(data1["intents"][30]["responses"])
A6=listToString(data1["intents"][33]["responses"])






def message_probability(user_message, recognised_words, single_response=False, required_words=[]):
    message_certainty = 0
    has_required_words = True

    # Counts how many words are present in each predefined message
    for word in user_message:
        if word in recognised_words:
            message_certainty += 1

    # Calculates the percent of recognised words in a user message
    percentage = float(message_certainty) / float(len(recognised_words))

    # Checks that the required words are in the string
    for word in required_words:
        if word not in user_message:
            has_required_words = False
            break

    # Must either have the required words, or be a single response
    if has_required_words or single_response:
        return int(percentage * 100)
    else:
        return 0


def check_all_messages(message):
    highest_prob_list = {}

    # Simplifies response creation / adds it to the dict
    def response(bot_response, list_of_words, single_response=False, required_words=[]):
        nonlocal highest_prob_list
        highest_prob_list[bot_response] = message_probability(message, list_of_words, single_response, required_words)

    # Responses -------------------------------------------------------------------------------------------------------
    print(str(data1["intents"][0]["responses"]))
    print(data1["intents"][0]["patterns"])
   # response('Hi there! My name is Sally!,Would you like to ask a question?$Yes Please,No Thanks', ['hello', 'hi', 'hey', 'sup', 'heyo'], single_response=True)
    
    response(A,data1["intents"][0]["patterns"], single_response=True)
    response(B,data1["intents"][1]["patterns"], single_response=True)
    response(C,data1["intents"][2]["patterns"], single_response=True)
    response(D,data1["intents"][3]["patterns"], single_response=True)
    response(E,data1["intents"][4]["patterns"], single_response=True)
    response(F,data1["intents"][5]["patterns"], single_response=True)
    response(G,data1["intents"][6]["patterns"], single_response=True)
    response(H,data1["intents"][7]["patterns"], single_response=True)
    response(I,data1["intents"][8]["patterns"], single_response=True)
    response(J,data1["intents"][9]["patterns"], single_response=True)
    response(K,data1["intents"][10]["patterns"], single_response=True)
    
    response(L,data1["intents"][11]["patterns"], single_response=True)
    response(M,data1["intents"][12]["patterns"], single_response=True)
    response(N,data1["intents"][13]["patterns"], single_response=True)
    response(O,data1["intents"][14]["patterns"], single_response=True)
    response(P,data1["intents"][15]["patterns"], single_response=True)
    response(Q,data1["intents"][16]["patterns"], single_response=True)
    response(R,data1["intents"][17]["patterns"], single_response=True)
    response(S,data1["intents"][18]["patterns"], single_response=True)
    response(T,data1["intents"][19]["patterns"], single_response=True)
    response(U,data1["intents"][20]["patterns"], single_response=True)
    response(V,data1["intents"][21]["patterns"], single_response=True)
    
    response(W,data1["intents"][22]["patterns"], single_response=True)
    response(X,data1["intents"][23]["patterns"], single_response=True)
    response(Y,data1["intents"][24]["patterns"], single_response=True)
    response(Z,data1["intents"][25]["patterns"], single_response=True)
    response(A1,data1["intents"][26]["patterns"], single_response=True)
    response(A2,data1["intents"][27]["patterns"], single_response=True)
    response(A3,data1["intents"][28]["patterns"], single_response=True)
    response(A4,data1["intents"][29]["patterns"], single_response=True)
    response(A5,data1["intents"][30]["patterns"], single_response=True)
    response(A6,data1["intents"][33]["patterns"], single_response=True)

    



######################### Appoinment Booking ###############################
    # response('Enter Your Appointment Name',['book appointment','appointment'], single_response=True)
    response('Enter Your Appointment Name',['book appointment','appointment'], single_response=True)
    response("Enter Your Contact Details", ['enter',"details"], required_words=['details'])
    response("Select Department$ Cardiologist, Neurologist, Dermatologist", ['select',"department"], required_words=['department'])
    # response("Book your Appointment Date$Today,Tomorrow,Day After Tomorrow", ['appointment',"date"], required_words=['date'])
    # response("Please select Time slot", ['select_time'], required_words=['select_time'])










    
   ################################Contact###########
    # response('Name', ['Okay'], required_words=['Okay'])
    response('Please type your Name', ['Contact', 'team', 'member'], required_words=['team'])
    response("Please type your Email id", ['enter',"email"], required_words=['email'])
    response("Please type your Phone Number", ['enter_phone'], required_words=['enter_phone'])
    response("Please type your Query", ['enter',"query"], required_words=['query'])
    response("Success! We will send this to the VermiGold team to get back to you shortly, either by email or phone number", ['thank_you'], required_words=['thank_you'])
    response("Please type your valid Email id", ['valid_gmail'], required_words=['valid_gmail'])

    
    # response('Enter your name:', ['Name'], required_words=['Name'])
    
    

    # Longer responses
   # response(long.R_ADVICE, ['alive', 'next','trip'], required_words=['alive'])
   # response(long.R_EATING, ['yes', 'Yes', 'yup'], required_words=['Yes', 'yes'])

    best_match = max(highest_prob_list, key=highest_prob_list.get)
    # print(highest_prob_list)
    # print(f'Best match = {best_match} | Score: {highest_prob_list[best_match]}')

    return long.unknown() if highest_prob_list[best_match] < 1 else best_match


# Used to get the response

def get_response(user_input):
    
    ####################################    
    response_list = []
    answer_list = []
    splitmsg_list = []
#################################
    # print(user_input)

    if "_name_" in user_input:
        name_var = user_input.split("_name_")[0]
        # print("user_input---->",user_input)
        new_user_input = "enter email"
        user_input = new_user_input
        split_message = re.split(r'\s+|[,;?!.-]\s*', user_input.lower())
    elif "_email_" in user_input:
        regex = '^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$'  
        email =  user_input.split('_')[0]
        # print(email)
        # print(re.search(regex,email))
        if(re.search(regex,email)): 
            # print("Valid Email")
            new_user_input = "enter_phone"
            user_input = new_user_input
            split_message = re.split(r'\s+|[,;?!.-]\s*', user_input.lower())
        else:
            # print("Invalid Email")
            new_user_input = "valid_gmail"
            user_input = new_user_input
            split_message = re.split(r'\s+|[,;?!.-]\s*', user_input.lower())
    elif "_phone_" in user_input:
        contact_var = user_input.split("_phone_")[0]
        # print("user_input---->",user_input)
        new_user_input = "enter query"
        user_input = new_user_input
        split_message = re.split(r'\s+|[,;?!.-]\s*', user_input.lower())
    elif "_query_" in user_input:
        contact_var = user_input.split("_query_")[0]
        # print("user_input---->",user_input)
        new_user_input = "thank_you"
        user_input = new_user_input
        split_message = re.split(r'\s+|[,;?!.-]\s*', user_input.lower())
        
    elif "_appointmentname_" in user_input:
       contact_var = user_input.split("_appointmentname_")[0]
       # booking_list.append(contact_var)
       # print("user_input---->",user_input)
       new_user_input = "enter details"
       user_input = new_user_input
       split_message = re.split(r'\s+|[,;?!.-]\s*', user_input.lower())
       
       
    elif "_contactdetails_" in user_input:
        contact_var = user_input.split("_contactdetails_")[0]
        # print("user_input---->",user_input)
        new_user_input = "select department"
        user_input = new_user_input
        split_message = re.split(r'\s+|[,;?!.-]\s*', user_input.lower())
    elif "_date_" in user_input:
        contact_var = user_input.split("_date_")[0]
        # print("user_input---->",user_input)
        new_user_input = "select_time"
        user_input = new_user_input
        split_message = re.split(r'\s+|[,;?!.-]\s*', user_input.lower())
        
        
        
    else:
        split_message = re.split(r'\s+|[,;?!.-]\s*', user_input.lower())
        
    response = check_all_messages(split_message)
    
        
######################################################    
 ######################################################    
    # response_list.append(response)
    # answer_list.append(user_input)
    # splitmsg_list.append(split_message)
    # all_list = [[response_list],[answer_list],[splitmsg_list]]
    # df = pd.DataFrame(all_list,columns = ['Response' , 'Answer', 'Split Message'])
   # # df.to_csv("chatbot.csv")
    
    
########################################################  
    
    
########################################################   

    
    # print("The response:", response)
    return response


# Testing the response system
# while True:
#    print('Bot: ' + get_response(input('You: ')))
