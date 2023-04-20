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



f1 = open("UserProject/Todos/PromptTemplate.json", "r")
prompt_template = json.loads(f1.read())


def Todos(request):
    chain = sapperchain(request['OpenaiKey'])
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
    Welcome! I'm your AI assistant, designed to help you create inspirational content. To get started, input a list of items, a piece of text, or a description of a painting, and I'll use it to generate an inspirational paragraph, a description of a painting, or inspiring pictures. Let's get creative!"""
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
        Text = chain.worker("so(NLRL]1N6XhgSfsEgR",[todos],{"temperature":0.56,"max_tokens":225,"stop_strs":"","top_p":1,"frequency_penalty":0,"presence_penalty":0,"engine":" text-davinci-003"})
        query["Text"]=Text
    if query["runflag"]:
        description = chain.worker("cU#}$h$n}qavnbg5@8:I",[Text],{"temperature":0.56,"max_tokens":225,"stop_strs":"","top_p":1,"frequency_penalty":0,"presence_penalty":0,"engine":" text-davinci-003"})
        query["description"]=description
    if query["runflag"]:
        query["output"].append(description)
    if query["runflag"]:
        Des2Picture = chain.worker("fXT.uk|f$wPHkl1DX0w3",[description],{"n":1,"engine":" DALL-E"})
        query["Des2Picture"]=Des2Picture
    if query["runflag"]:
        query["output"].append(Des2Picture)



    resetquery(query, initrecord)
    return {'Answer': query["output"]}
