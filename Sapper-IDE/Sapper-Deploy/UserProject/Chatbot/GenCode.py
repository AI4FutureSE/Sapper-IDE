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



f1 = open("UserProject/Chatbot/PromptTemplate.json", "r")
prompt_template = json.loads(f1.read())


def Chatbot(request):
    chain = sapperchain(request['OpenaiKey'])
    chain.promptbase(prompt_template)

    initrecord = {"id":"","input":"preInfo","output":[],"runflag":"","human":"","history":"","chatbot":"","preInfo":""}
    query = update_request(initrecord, request)
    human=query["human"]
    history=query["history"]
    chatbot=query["chatbot"]
    preInfo=query["preInfo"]
    query["output"] = []
    if query["runflag"]:
        preInfo = """
    Hi there! I'm an AI chatbot and I'm here to help you with your conversation. To get started, all you need to do is type your message into the chat box and I'll take it from there. I look forward to talking to you soon!"""
        query["preInfo"]=preInfo
    if query["runflag"]:
        query["output"].append(preInfo)
        stop, query, Unit = get_value("preInfo", request, query)
    while human != 'Good Bye':
        stop, query, human = get_value("human", request, query)
        if stop and query["runflag"]:
            query["runflag"] = False
            query["input"] = "human"
            savequery(query)
            return {'Answer': query["output"]}
        if query["runflag"]:
            chatbot = chain.worker("T}ojRf(E+G5adzGNmnQV",[history,human],{"temperature":0.7,"max_tokens":225,"top_p":1,"frequency_penalty":0,"presence_penalty":0,"engine":" gpt-3.5-turbo"})
            query["chatbot"]=chatbot
        if query["runflag"]:
            query["output"].append(chatbot)
        if query["runflag"]:
            history = chain.worker("SAM[RY+V]*1^d,Gp0u=V",[history,human,chatbot],{"engine":"PythonREPL"})
            query["history"]=history




    resetquery(query, initrecord)
    return {'Answer': query["output"]}
