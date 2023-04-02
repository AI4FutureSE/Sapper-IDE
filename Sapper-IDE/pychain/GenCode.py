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
f1 = open("pychain/PromptTemplate.json", "r")
prompt_template = json.loads(f1.read())


def sapper(request):
    chain = sapperchain()
    chain.promptbase(prompt_template)
    initrecord = {"id":"","input":"preInfo","output":[],"runflag":"","todos":"","Text":"","description":"","Des2Picture":"","preInfo":""}
    query = update_request(initrecord, request)
    todos=query["todos"]
    Text=query["Text"]
    description=query["description"]
    Des2Picture=query["Des2Picture"]
    preInfo=query["preInfo"]
    query["output"] = []
    if query["runflag"]:
        preInfo = """
    Hi there! Welcome to our AI service. We are here to help you create inspiring pictures and texts with the help of Artificial Intelligence. To get started, please type in a text or description in the field provided. Our AI will then work its magic and generate an output based on your inputs. Let's get creative!"""
        query["preInfo"]=preInfo
    if query["runflag"]:
        query["output"].append(preInfo)
        stop, query, Unit = get_value("preInfo", request, query)
    stop, query, todos = get_value("todos", request, query)
    if stop and query["runflag"]:
        query["runflag"] = False
        query["input"] = "todos"
        savequery(query)
        return {'Answer': query["output"]}
    if query["runflag"]:
        Text = chain.worker({"Text":["Instruction"]},[todos],{"temperature":0.56,"max_tokens":225,"stop_strs":"","top_p":1,"frequency_penalty":0,"presence_penalty":0,"engine":" text-davinci-003"})
        query["Text"]=Text
    if query["runflag"]:
        description = chain.worker({"text2pic":["Instruction"]},[Text],{"temperature":0.56,"max_tokens":225,"stop_strs":"","top_p":1,"frequency_penalty":0,"presence_penalty":0,"engine":" text-davinci-003"})
        query["description"]=description
    if query["runflag"]:
        query["output"].append(description)
    if query["runflag"]:
        Des2Picture = chain.worker({"des2pic":["Instruction"]},[description],{"n":1,"engine":" DALL-E"})
        query["Des2Picture"]=Des2Picture
    if query["runflag"]:
        query["output"].append(Des2Picture)
    


    resetquery(query, initrecord)
    return {'Answer': query["output"]}
