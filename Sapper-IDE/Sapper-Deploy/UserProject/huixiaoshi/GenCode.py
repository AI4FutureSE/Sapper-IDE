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



f1 = open("UserProject/huixiaoshi/PromptTemplate.json", "r", encoding='UTF-8')
prompt_template = json.loads(f1.read())


def huixiaoshi(sapper_request):
    chain = sapperchain(sapper_request['OpenaiKey'])
    chain.promptbase(prompt_template)

    initrecord = {"id":"","input":"preInfo","output":[],"runflag":"","human":"","describe":"","describe1":"","describe2":"","select1":"","object":"","select2":"","paintstyle":"","style1":"","strengthen":"","picture":"","preInfo":""}
    sapper_query = update_request(initrecord, sapper_request)
    human=sapper_query["human"]
    describe=sapper_query["describe"]
    describe1=sapper_query["describe1"]
    describe2=sapper_query["describe2"]
    select1=sapper_query["select1"]
    object=sapper_query["object"]
    select2=sapper_query["select2"]
    paintstyle=sapper_query["paintstyle"]
    style1=sapper_query["style1"]
    strengthen=sapper_query["strengthen"]
    picture=sapper_query["picture"]
    preInfo=sapper_query["preInfo"]
    sapper_query["output"] = []
    if sapper_query["runflag"]:
        preInfo = """Welcome to our AI service! 
            This AI service will help you create a painting based on a brief description or poem. To get started, please provide the poem or description that you would like to use as the basis for your painting. Then, you will be prompted to describe the picture that comes to your mind. After that, the AI will generate a painting according to your input. Get ready to create your masterpiece!"""
        sapper_query["preInfo"]=preInfo
    if sapper_query["runflag"]:
        sapper_query["output"].append(preInfo)
        stop, sapper_query, Unit = get_value("preInfo", sapper_request, sapper_query)
    stop, sapper_query, human = get_value("human", sapper_request, sapper_query)
    if stop and sapper_query["runflag"]:
        sapper_query["runflag"] = False
        sapper_query["input"] = "human"
        savequery(sapper_query)
        return {'Answer': sapper_query["output"]}
    if sapper_query["runflag"]:
        describe = chain.worker("oD%!BM;b.iz8@A:]DCV@",[human],{"temperature":0.1,"max_tokens":600,"stop_strs":"","top_p":1,"frequency_penalty":0,"presence_penalty":0,"model":"t","engine":" text-davinci-003"})
        sapper_query["describe"]=describe
    if sapper_query["runflag"]:
        describe1 = chain.worker("UBRFkzd,DG5JOsBr_8P1",[human],{"temperature":0.1,"max_tokens":600,"stop_strs":"","top_p":1,"frequency_penalty":0,"presence_penalty":0,"model":"t","engine":" text-davinci-003"})
        sapper_query["describe1"]=describe1
    if sapper_query["runflag"]:
        describe2 = chain.worker("Q5(9bwQOhQE-n}2z,hex",[human],{"temperature":0.1,"max_tokens":600,"stop_strs":"","top_p":1,"frequency_penalty":0,"presence_penalty":0,"model":"t","engine":" text-davinci-003"})
        sapper_query["describe2"]=describe2
    if sapper_query["runflag"]:
        select1 = chain.worker("jl=[lJJ*L:aNNu3Bo],N",[describe,describe1,describe2],{"temperature":0.1,"max_tokens":600,"stop_strs":"","top_p":1,"frequency_penalty":0,"presence_penalty":0,"model":"t","engine":" text-davinci-003"})
        sapper_query["select1"]=select1
    if sapper_query["runflag"]:
        object = chain.worker("KBSb9C2nX]sZF(s4CP^7",[select1],{"temperature":0.7,"max_tokens":600,"stop_strs":"","top_p":1,"frequency_penalty":0,"presence_penalty":0,"model":"t","engine":" text-davinci-003"})
        sapper_query["object"]=object
    if sapper_query["runflag"]:
        select2 = chain.worker("lZ*S^Fr~yqgx}AQ^w(+/",[object],{"temperature":0.7,"max_tokens":225,"top_p":1,"frequency_penalty":0,"presence_penalty":0,"model":"g","engine":" gpt-3.5-turbo"})
        sapper_query["select2"]=select2
    if sapper_query["runflag"]:
        paintstyle = chain.worker("BQ+I3V3W!ub0avH4M{gE",[human],{"temperature":0.1,"max_tokens":600,"stop_strs":"","top_p":1,"frequency_penalty":0,"presence_penalty":0,"model":"t","engine":" text-davinci-003"})
        sapper_query["paintstyle"]=paintstyle
    if sapper_query["runflag"]:
        style1 = chain.worker("gtrhg_aH~mx.ZpJw;^%D",[paintstyle],{"temperature":0.7,"max_tokens":225,"top_p":1,"frequency_penalty":0,"presence_penalty":0,"model":"g","engine":" gpt-3.5-turbo"})
        sapper_query["style1"]=style1
    if sapper_query["runflag"]:
        strengthen = chain.worker("ZT5flqDeE_.fBl1oj|~l",[paintstyle,human],{"temperature":0.7,"max_tokens":225,"top_p":1,"frequency_penalty":0,"presence_penalty":0,"model":"g","engine":" gpt-3.5-turbo"})
        sapper_query["strengthen"]=strengthen
    if sapper_query["runflag"]:
        picture = chain.worker("K^uFMsQ.ZC|/yGf3E.Dw",[select2,paintstyle,style1,strengthen],{"n":1,"model":"D","engine":" DALL-E"})
        sapper_query["picture"]=picture
    if sapper_query["runflag"]:
        sapper_query["output"].append(picture)



    resetquery(sapper_query, initrecord)
    return {'Answer': sapper_query["output"]}
