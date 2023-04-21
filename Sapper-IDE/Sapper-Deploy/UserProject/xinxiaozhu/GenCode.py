from sapperchain import sapperchain
import os
import json
from flask import jsonify

file_path = os.path.join(os.path.dirname(__file__), 'storage.json')


def read_json():
    with open(file_path, 'r', encoding='utf-8') as f:
        data = json.load(f)
    return data


def write_json(data):
    with open(file_path, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False)


def update_request(initrecord, query):
    initrecord["id"] = query['id']
    initrecord["runflag"] = True
    data = read_json()
    has_id = False
    for record in data:
        if record['id'] == query['id']:
            has_id = True
            return record
    if not has_id:
        new_record = initrecord
        data.append(new_record)
        write_json(data)
        return new_record


def get_value(vary, request, query):
    if vary == query["input"]:
        query["runflag"] = True
        query["input"] = ""
        query[vary] = request["query"]
        return False, query, request["query"]
    else:
        return True, query, query[vary]


def resetquery(query,initrecord):
    initrecord["id"] = query['id']
    initrecord["runflag"] = True
    query = initrecord
    data = read_json()
    for i in range(len(data)):
        record = data[i]
        if record['id'] == query['id']:
            data[i] = query
    write_json(data)


def savequery(query):
    data = read_json()
    for i in range(len(data)):
        record = data[i]
        if record['id'] == query['id']:
            data[i] = query
    write_json(data)



f1 = open("UserProject/xinxiaozhu/PromptTemplate.json", "r", encoding='UTF-8')
prompt_template = json.loads(f1.read())


def xinxiaozhu(sapper_request):
    chain = sapperchain(sapper_request['OpenaiKey'])
    chain.promptbase(prompt_template)

    initrecord = {"id":"","input":"preInfo","output":[],"runflag":"","word":"","Essential_information":"","Other_Information":"","User_Profile":"","Living_conditions_and_Symptoms":"","Symptom":"","Detailed_Questions":"","Answer":"","Final_Judgment":"","Treatment_Plan":"","Specific_Examples":"","bot":"","User":"","human":"","history":"","chatbot":"","preInfo":""}
    sapper_query = update_request(initrecord, sapper_request)
    word=sapper_query["word"]
    Essential_information=sapper_query["Essential_information"]
    Other_Information=sapper_query["Other_Information"]
    User_Profile=sapper_query["User_Profile"]
    Living_conditions_and_Symptoms=sapper_query["Living_conditions_and_Symptoms"]
    Symptom=sapper_query["Symptom"]
    Detailed_Questions=sapper_query["Detailed_Questions"]
    Answer=sapper_query["Answer"]
    Final_Judgment=sapper_query["Final_Judgment"]
    Treatment_Plan=sapper_query["Treatment_Plan"]
    Specific_Examples=sapper_query["Specific_Examples"]
    bot=sapper_query["bot"]
    User=sapper_query["User"]
    human=sapper_query["human"]
    history=sapper_query["history"]
    chatbot=sapper_query["chatbot"]
    preInfo=sapper_query["preInfo"]
    sapper_query["output"] = []
    if sapper_query["runflag"]:
        preInfo = """Hi, I am an AI assistant designed to help the psychologist to provide treatment for users. 
    To get started, please provide basic information about yourself, such as your name, gender, age, occupation, family status, and social relationships. 
    This information will be used to generate your personal profile. 
    Thank you for your cooperation."""
        sapper_query["preInfo"]=preInfo
    if sapper_query["runflag"]:
        sapper_query["output"].append(preInfo)
        stop, sapper_query, Unit = get_value("preInfo", sapper_request, sapper_query)
    word = 'Welcome to the Psychotherapist Module';
    if sapper_query["runflag"]:
        sapper_query["output"].append(word)
    Essential_information = 'Name, Gender, Age, Occupation';
    if sapper_query["runflag"]:
        sapper_query["output"].append(Essential_information)
    Other_Information = 'Family status, Social relationships';
    if sapper_query["runflag"]:
        sapper_query["output"].append(Other_Information)
    stop, sapper_query, Essential_information = get_value("Essential_information", sapper_request, sapper_query)
    if stop and sapper_query["runflag"]:
        sapper_query["runflag"] = False
        sapper_query["input"] = "Essential_information"
        savequery(sapper_query)
        return {'Answer': sapper_query["output"]}
    if sapper_query["runflag"]:
        User_Profile = chain.worker("KALwdu]h-p@.L1yIhq*T",[Essential_information],{"temperature":0.7,"max_tokens":3000,"top_p":1,"frequency_penalty":0,"presence_penalty":0,"model":"g","engine":" gpt-3.5-turbo"})
        sapper_query["User_Profile"]=User_Profile
    if sapper_query["runflag"]:
        sapper_query["output"].append(User_Profile)
    stop, sapper_query, Living_conditions_and_Symptoms = get_value("Living_conditions_and_Symptoms", sapper_request, sapper_query)
    if stop and sapper_query["runflag"]:
        sapper_query["runflag"] = False
        sapper_query["input"] = "Living_conditions_and_Symptoms"
        savequery(sapper_query)
        return {'Answer': sapper_query["output"]}
    if sapper_query["runflag"]:
        Symptom = chain.worker("!O2^Or5qNolHE@K=Li2#",[Living_conditions_and_Symptoms,User_Profile],{"temperature":0.7,"max_tokens":3000,"top_p":1,"frequency_penalty":0,"presence_penalty":0,"model":"g","engine":" gpt-3.5-turbo"})
        sapper_query["Symptom"]=Symptom
    if sapper_query["runflag"]:
        sapper_query["output"].append(Symptom)
    if sapper_query["runflag"]:
        Detailed_Questions = chain.worker("ZLm-(CJW:oddX/X_MaXc",[Symptom],{"temperature":0.7,"max_tokens":3000,"top_p":1,"frequency_penalty":0,"presence_penalty":0,"model":"g","engine":" gpt-3.5-turbo"})
        sapper_query["Detailed_Questions"]=Detailed_Questions
    if sapper_query["runflag"]:
        sapper_query["output"].append(Detailed_Questions)
    stop, sapper_query, Answer = get_value("Answer", sapper_request, sapper_query)
    if stop and sapper_query["runflag"]:
        sapper_query["runflag"] = False
        sapper_query["input"] = "Answer"
        savequery(sapper_query)
        return {'Answer': sapper_query["output"]}
    if sapper_query["runflag"]:
        Final_Judgment = chain.worker("b2]L^#npO(~KgSPyy:][",[Detailed_Questions,Answer],{"temperature":0.7,"max_tokens":3000,"top_p":1,"frequency_penalty":0,"presence_penalty":0,"model":"g","engine":" gpt-3.5-turbo"})
        sapper_query["Final_Judgment"]=Final_Judgment
    if sapper_query["runflag"]:
        sapper_query["output"].append(Final_Judgment)
    if sapper_query["runflag"]:
        Treatment_Plan = chain.worker("gSoY]Kl7-Sc/|n4tEqo:",[Final_Judgment,User_Profile],{"temperature":0.7,"max_tokens":3000,"top_p":1,"frequency_penalty":0,"presence_penalty":0,"model":"g","engine":" gpt-3.5-turbo"})
        sapper_query["Treatment_Plan"]=Treatment_Plan
    if sapper_query["runflag"]:
        sapper_query["output"].append(Treatment_Plan)
    if sapper_query["runflag"]:
        Specific_Examples = chain.worker("FFX9$c5vyHiKNAf7c2/C",[Treatment_Plan,User_Profile],{"temperature":0.7,"max_tokens":3000,"top_p":1,"frequency_penalty":0,"presence_penalty":0,"model":"g","engine":" gpt-3.5-turbo"})
        sapper_query["Specific_Examples"]=Specific_Examples
    if sapper_query["runflag"]:
        sapper_query["output"].append(Specific_Examples)
    bot = 'Are you satisfied with this suggestion';
    if sapper_query["runflag"]:
        sapper_query["output"].append(bot)
    stop, sapper_query, User = get_value("User", sapper_request, sapper_query)
    if stop and sapper_query["runflag"]:
        sapper_query["runflag"] = False
        sapper_query["input"] = "User"
        savequery(sapper_query)
        return {'Answer': sapper_query["output"]}
    while User == 'Dissatisfied':
        if sapper_query["runflag"]:
            Treatment_Plan = chain.worker("dWES9*8XlxL/DDtGdl9z",[Final_Judgment,User_Profile],{"temperature":0.7,"max_tokens":3000,"top_p":1,"frequency_penalty":0,"presence_penalty":0,"model":"g","engine":" gpt-3.5-turbo"})
            sapper_query["Treatment_Plan"]=Treatment_Plan
        if sapper_query["runflag"]:
            sapper_query["output"].append(Treatment_Plan)
        if sapper_query["runflag"]:
            Specific_Examples = chain.worker("C}~4@B{FL//[?8Lij,%3",[Treatment_Plan,User_Profile],{"temperature":0.7,"max_tokens":3000,"top_p":1,"frequency_penalty":0,"presence_penalty":0,"model":"g","engine":" gpt-3.5-turbo"})
            sapper_query["Specific_Examples"]=Specific_Examples
        if sapper_query["runflag"]:
            sapper_query["output"].append(Specific_Examples)

    bot = 'May I ask if you have any further questions';
    if sapper_query["runflag"]:
        sapper_query["output"].append(bot)
    while human != 'bye':
        stop, sapper_query, human = get_value("human", sapper_request, sapper_query)
        if stop and sapper_query["runflag"]:
            sapper_query["runflag"] = False
            sapper_query["input"] = "human"
            savequery(sapper_query)
            return {'Answer': sapper_query["output"]}
        if sapper_query["runflag"]:
            chatbot = chain.worker("j)%Zkj-NoVAX~0-N;~}d",[history,human],{"temperature":0.7,"max_tokens":3000,"top_p":1,"frequency_penalty":0,"presence_penalty":0,"model":"g","engine":" gpt-3.5-turbo"})
            sapper_query["chatbot"]=chatbot
        if sapper_query["runflag"]:
            sapper_query["output"].append(chatbot)
        if sapper_query["runflag"]:
            history = chain.worker("Cy.y;ei]^i~5@$fLo+YQ",[history,human,chatbot],{"engine":"PythonREPL"})
            sapper_query["history"]=history




    resetquery(sapper_query, initrecord)
    return {'Answer': sapper_query["output"]}
