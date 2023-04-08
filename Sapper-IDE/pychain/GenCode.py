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


os.environ["OPENAI_API_KEY"] = "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"
f1 = open("PromptTemplate.json", "r")
prompt_template = json.loads(f1.read())


def sapper(request):
    chain = sapperchain()
    chain.promptbase(prompt_template)
    initrecord = {"id":"","input":"preInfo","output":[],"runflag":"","User_Specified_Conditions":"","Character_Setting":"","Personality":"","Backstory":"","Appearance":"","Image":"","preInfo":""}
    query = update_request(initrecord, request)
    User_Specified_Conditions=query["User_Specified_Conditions"]
    Character_Setting=query["Character_Setting"]
    Personality=query["Personality"]
    Backstory=query["Backstory"]
    Appearance=query["Appearance"]
    Image=query["Image"]
    preInfo=query["preInfo"]
    query["output"] = []
    if query["runflag"]:
        preInfo = """Welcome! I'm an AI service that can help you create unique and believable characters with a backstory, setting, personality, and appearance. To begin, please provide me with the character type and personality traits you'd like me to use. I'll take it from there to create a unique character for you."""
        query["preInfo"]=preInfo
    if query["runflag"]:
        query["output"].append(preInfo)
        stop, query, Unit = get_value("preInfo", request, query)
    stop, query, User_Specified_Conditions = get_value("User_Specified_Conditions", request, query)
    if stop and query["runflag"]:
        query["runflag"] = False
        query["input"] = "User_Specified_Conditions"
        savequery(query)
        return {'Answer': query["output"]}
    if query["runflag"]:
        Character_Setting = chain.worker({"Character_Setting":["Instruction"]},[User_Specified_Conditions],{"temperature":0.7,"max_tokens":225,"top_p":1,"frequency_penalty":0,"presence_penalty":0,"engine":" gpt-3.5-turbo"})
        query["Character_Setting"]=Character_Setting
    if query["runflag"]:
        Personality = chain.worker({"Personality":["Instruction"]},[Character_Setting],{"temperature":0.7,"max_tokens":225,"top_p":1,"frequency_penalty":0,"presence_penalty":0,"engine":" gpt-3.5-turbo"})
        query["Personality"]=Personality
    if query["runflag"]:
        query["output"].append(Personality)
    if query["runflag"]:
        Backstory = chain.worker({"Backstory":["Instruction"]},[Character_Setting],{"temperature":0.7,"max_tokens":225,"top_p":1,"frequency_penalty":0,"presence_penalty":0,"engine":" gpt-3.5-turbo"})
        query["Backstory"]=Backstory
    if query["runflag"]:
        query["output"].append(Backstory)
    if query["runflag"]:
        Appearance = chain.worker({"Appearance":["Instruction"]},[Character_Setting],{"temperature":0.7,"max_tokens":225,"top_p":1,"frequency_penalty":0,"presence_penalty":0,"engine":" gpt-3.5-turbo"})
        query["Appearance"]=Appearance
    if query["runflag"]:
        query["output"].append(Appearance)
    if query["runflag"]:
        Image = chain.worker({"Image":["Instruction"]},[Appearance],{"temperature":0.7,"max_tokens":225,"top_p":1,"frequency_penalty":0,"presence_penalty":0,"engine":" gpt-3.5-turbo"})
        query["Image"]=Image
    if query["runflag"]:
        query["output"].append(Image)



    resetquery(query, initrecord)
    return {'Answer': query["output"]}
