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



f1 = open("UserProject/AirSim/PromptTemplate.json", "r", encoding='UTF-8')
prompt_template = json.loads(f1.read())


def AirSim(sapper_request):
    chain = sapperchain(sapper_request['OpenaiKey'])
    chain.promptbase(prompt_template)

    initrecord = {"id":"","input":"preInfo","output":[],"runflag":"","human":"","history":"","chatbot":"","preInfo":""}
    sapper_query = update_request(initrecord, sapper_request)
    human=sapper_query["human"]
    history=sapper_query["history"]
    chatbot=sapper_query["chatbot"]
    preInfo=sapper_query["preInfo"]
    sapper_query["output"] = []
    if sapper_query["runflag"]:
        preInfo = """Hi there! I'm an AI assistant that can help you use the AirSim simulator for drones. To get started, you will need to input take off."""
        sapper_query["preInfo"]=preInfo
    if sapper_query["runflag"]:
        sapper_query["output"].append(preInfo)
        stop, sapper_query, Unit = get_value("preInfo", sapper_request, sapper_query)
    while human != 'exit':
        stop, sapper_query, human = get_value("human", sapper_request, sapper_query)
        if stop and sapper_query["runflag"]:
            sapper_query["runflag"] = False
            sapper_query["input"] = "human"
            savequery(sapper_query)
            return {'Answer': sapper_query["output"]}
        if sapper_query["runflag"]:
            chatbot = chain.worker("{0kH/PQQW;J^6,(HkAH^",[history,human],{"temperature":0.7,"max_tokens":225,"top_p":1,"frequency_penalty":0,"presence_penalty":0,"model":"g","engine":" gpt-3.5-turbo"})
            sapper_query["chatbot"]=chatbot
        if sapper_query["runflag"]:
            sapper_query["output"].append(chatbot)
        if sapper_query["runflag"]:
            history = chain.worker("UFUnq/1)d.XmdyGsK1`H",[history,human,chatbot],{"engine":"PythonREPL"})
            sapper_query["history"]=history




    resetquery(sapper_query, initrecord)
    return {'Answer': sapper_query["output"]}
