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



f1 = open("UserProject/wenxiaojie/PromptTemplate.json", "r", encoding='UTF-8')
prompt_template = json.loads(f1.read())


def wenxiaojie(sapper_request):
    chain = sapperchain(sapper_request['OpenaiKey'])
    chain.promptbase(prompt_template)

    initrecord = {"id":"","input":"preInfo","output":[],"runflag":"","hint":"","theme":"","reader":"","genre":"","General":"","idea":"","materials ":"","Personalized":"","human":"","human1":"","mold_piece":"","stuff":"","Expanding":"","Assessing":"","human2":"","module":"","request":"","Rewriting":"","human3":"","incomplete":"","Completing":"","preInfo":""}
    sapper_query = update_request(initrecord, sapper_request)
    hint=sapper_query["hint"]
    theme=sapper_query["theme"]
    reader=sapper_query["reader"]
    genre=sapper_query["genre"]
    General=sapper_query["General"]
    idea=sapper_query["idea"]
    materials =sapper_query["materials "]
    Personalized=sapper_query["Personalized"]
    human=sapper_query["human"]
    human1=sapper_query["human1"]
    mold_piece=sapper_query["mold_piece"]
    stuff=sapper_query["stuff"]
    Expanding=sapper_query["Expanding"]
    Assessing=sapper_query["Assessing"]
    human2=sapper_query["human2"]
    module=sapper_query["module"]
    request=sapper_query["request"]
    Rewriting=sapper_query["Rewriting"]
    human3=sapper_query["human3"]
    incomplete=sapper_query["incomplete"]
    Completing=sapper_query["Completing"]
    preInfo=sapper_query["preInfo"]
    sapper_query["output"] = []
    if sapper_query["runflag"]:
        preInfo = """Welcome to our personalized long article supported by artificial intelligence, Wen Xiao jie"""
        sapper_query["preInfo"]=preInfo
    if sapper_query["runflag"]:
        sapper_query["output"].append(preInfo)
        stop, sapper_query, Unit = get_value("preInfo", sapper_request, sapper_query)
    hint = 'You need to input relevant information about the “topic”, “audience”, and “genre” of the article in order to help you generate a general outline.' \
           'Then, you need to input the “article ideas” and relevant information about the “materials” to be used in order to help you generate a personalized outline.';
    if sapper_query["runflag"]:
        sapper_query["output"].append(hint)
    stop, sapper_query, theme = get_value("theme", sapper_request, sapper_query)
    if stop and sapper_query["runflag"]:
        sapper_query["runflag"] = False
        sapper_query["input"] = "theme"
        savequery(sapper_query)
        return {'Answer': sapper_query["output"]}
    stop, sapper_query, reader = get_value("reader", sapper_request, sapper_query)
    if stop and sapper_query["runflag"]:
        sapper_query["runflag"] = False
        sapper_query["input"] = "reader"
        savequery(sapper_query)
        return {'Answer': sapper_query["output"]}
    stop, sapper_query, genre = get_value("genre", sapper_request, sapper_query)
    if stop and sapper_query["runflag"]:
        sapper_query["runflag"] = False
        sapper_query["input"] = "genre"
        savequery(sapper_query)
        return {'Answer': sapper_query["output"]}
    if sapper_query["runflag"]:
        General = chain.worker("#v%[C^~axK.|}|/[INdt",[theme,reader,genre],{"temperature":0.7,"max_tokens":225,"top_p":1,"frequency_penalty":0,"presence_penalty":0,"model":"g","engine":" gpt-3.5-turbo"})
        sapper_query["General"]=General
    if sapper_query["runflag"]:
        sapper_query["output"].append(General)
    stop, sapper_query, idea = get_value("idea", sapper_request, sapper_query)
    if stop and sapper_query["runflag"]:
        sapper_query["runflag"] = False
        sapper_query["input"] = "idea"
        savequery(sapper_query)
        return {'Answer': sapper_query["output"]}
    stop, sapper_query, materials  = get_value("materials ", sapper_request, sapper_query)
    if stop and sapper_query["runflag"]:
        sapper_query["runflag"] = False
        sapper_query["input"] = "materials "
        savequery(sapper_query)
        return {'Answer': sapper_query["output"]}
    if sapper_query["runflag"]:
        Personalized = chain.worker("t(5Y~.gpfjjN_cn~(oJL",[General,idea,materials ],{"temperature":0.7,"max_tokens":225,"top_p":1,"frequency_penalty":0,"presence_penalty":0,"model":"g","engine":" gpt-3.5-turbo"})
        sapper_query["Personalized"]=Personalized
    if sapper_query["runflag"]:
        sapper_query["output"].append(Personalized)
    hint = 'Whether to start expanding (1, start expanding；2, do not start expanding)';
    if sapper_query["runflag"]:
        sapper_query["output"].append(hint)
    stop, sapper_query, human = get_value("human", sapper_request, sapper_query)
    if stop and sapper_query["runflag"]:
        sapper_query["runflag"] = False
        sapper_query["input"] = "human"
        savequery(sapper_query)
        return {'Answer': sapper_query["output"]}
    while human == '1':
        human1 = 'a';
        hint = 'Enter the idea you want to expand and the material you want to use';
        if sapper_query["runflag"]:
            sapper_query["output"].append(hint)
        stop, sapper_query, mold_piece = get_value("mold_piece", sapper_request, sapper_query)
        if stop and sapper_query["runflag"]:
            sapper_query["runflag"] = False
            sapper_query["input"] = "mold_piece"
            savequery(sapper_query)
            return {'Answer': sapper_query["output"]}
        stop, sapper_query, stuff = get_value("stuff", sapper_request, sapper_query)
        if stop and sapper_query["runflag"]:
            sapper_query["runflag"] = False
            sapper_query["input"] = "stuff"
            savequery(sapper_query)
            return {'Answer': sapper_query["output"]}
        while human1 == 'a':
            if sapper_query["runflag"]:
                Expanding = chain.worker("AC!=C`=KX$Ks.(2lGI/D",[mold_piece,stuff],{"temperature":0.7,"max_tokens":225,"top_p":1,"frequency_penalty":0,"presence_penalty":0,"model":"g","engine":" gpt-3.5-turbo"})
                sapper_query["Expanding"]=Expanding
            if sapper_query["runflag"]:
                sapper_query["output"].append(Expanding)
            if sapper_query["runflag"]:
                Assessing = chain.worker("iCz{0McG6!2Am}YbOG%A",[mold_piece,stuff,Expanding],{"temperature":0.7,"max_tokens":225,"top_p":1,"frequency_penalty":0,"presence_penalty":0,"model":"g","engine":" gpt-3.5-turbo"})
                sapper_query["Assessing"]=Assessing
            if sapper_query["runflag"]:
                sapper_query["output"].append(Assessing)
            hint = 'Whether this expanded text is satisfactory (a, not satisfied, rewritten; b, satisfied, expand the next one).';
            if sapper_query["runflag"]:
                sapper_query["output"].append(hint)
            stop, sapper_query, human1 = get_value("human1", sapper_request, sapper_query)
            if stop and sapper_query["runflag"]:
                sapper_query["runflag"] = False
                sapper_query["input"] = "human1"
                savequery(sapper_query)
                return {'Answer': sapper_query["output"]}

        hint = 'Whether to continue to expand the next paragraph of text (1, continue; 2, do not continue)';
        if sapper_query["runflag"]:
            sapper_query["output"].append(hint)
        stop, sapper_query, human = get_value("human", sapper_request, sapper_query)
        if stop and sapper_query["runflag"]:
            sapper_query["runflag"] = False
            sapper_query["input"] = "human"
            savequery(sapper_query)
            return {'Answer': sapper_query["output"]}

    hint = 'Whether to start rewriting the article for polishing (1, start rewriting; 2, do not start to rewrite)';
    if sapper_query["runflag"]:
        sapper_query["output"].append(hint)
    stop, sapper_query, human2 = get_value("human2", sapper_request, sapper_query)
    if stop and sapper_query["runflag"]:
        sapper_query["runflag"] = False
        sapper_query["input"] = "human2"
        savequery(sapper_query)
        return {'Answer': sapper_query["output"]}
    while human2 == '1':
        human1 = 'a';
        hint = 'Enter the paragraph you want to rewrite and the rewrite requirement';
        if sapper_query["runflag"]:
            sapper_query["output"].append(hint)
        stop, sapper_query, module = get_value("module", sapper_request, sapper_query)
        if stop and sapper_query["runflag"]:
            sapper_query["runflag"] = False
            sapper_query["input"] = "module"
            savequery(sapper_query)
            return {'Answer': sapper_query["output"]}
        stop, sapper_query, request = get_value("request", sapper_request, sapper_query)
        if stop and sapper_query["runflag"]:
            sapper_query["runflag"] = False
            sapper_query["input"] = "request"
            savequery(sapper_query)
            return {'Answer': sapper_query["output"]}
        while human1 == 'a':
            if sapper_query["runflag"]:
                Rewriting = chain.worker("[I_SkCmaX?:MSX2et0-U",[module,request],{"temperature":0.7,"max_tokens":225,"top_p":1,"frequency_penalty":0,"presence_penalty":0,"model":"g","engine":" gpt-3.5-turbo"})
                sapper_query["Rewriting"]=Rewriting
            if sapper_query["runflag"]:
                sapper_query["output"].append(Rewriting)
            if sapper_query["runflag"]:
                Assessing = chain.worker("e+JwntoH_KkUE}eS^t6%",[module,request,Rewriting],{"temperature":0.7,"max_tokens":225,"top_p":1,"frequency_penalty":0,"presence_penalty":0,"model":"g","engine":" gpt-3.5-turbo"})
                sapper_query["Assessing"]=Assessing
            if sapper_query["runflag"]:
                sapper_query["output"].append(Assessing)
            hint = 'Whether this rewritten text is satisfactory (a, dissatisfied, rewritten; b, satisfied, rewrite the next one).';
            if sapper_query["runflag"]:
                sapper_query["output"].append(hint)
            stop, sapper_query, human1 = get_value("human1", sapper_request, sapper_query)
            if stop and sapper_query["runflag"]:
                sapper_query["runflag"] = False
                sapper_query["input"] = "human1"
                savequery(sapper_query)
                return {'Answer': sapper_query["output"]}

        hint = 'Whether to continue to rewrite the article for editing (1, continue; 2, end)';
        if sapper_query["runflag"]:
            sapper_query["output"].append(hint)
        stop, sapper_query, human2 = get_value("human2", sapper_request, sapper_query)
        if stop and sapper_query["runflag"]:
            sapper_query["runflag"] = False
            sapper_query["input"] = "human2"
            savequery(sapper_query)
            return {'Answer': sapper_query["output"]}

    hint = 'Whether to start modifying sentences with the help of Wen Xiaojie (1, yes; 2, No)';
    if sapper_query["runflag"]:
        sapper_query["output"].append(hint)
    stop, sapper_query, human3 = get_value("human3", sapper_request, sapper_query)
    if stop and sapper_query["runflag"]:
        sapper_query["runflag"] = False
        sapper_query["input"] = "human3"
        savequery(sapper_query)
        return {'Answer': sapper_query["output"]}
    while human3 == '1':
        human1 = 'a';
        hint = 'Enter an incomplete sentence to be prompted';
        if sapper_query["runflag"]:
            sapper_query["output"].append(hint)
        stop, sapper_query, incomplete = get_value("incomplete", sapper_request, sapper_query)
        if stop and sapper_query["runflag"]:
            sapper_query["runflag"] = False
            sapper_query["input"] = "incomplete"
            savequery(sapper_query)
            return {'Answer': sapper_query["output"]}
        while human1 == 'a':
            if sapper_query["runflag"]:
                Completing = chain.worker("S42A*xUu8.~IrwS)wjt?",[incomplete],{"temperature":0.7,"max_tokens":225,"top_p":1,"frequency_penalty":0,"presence_penalty":0,"model":"g","engine":" gpt-3.5-turbo"})
                sapper_query["Completing"]=Completing
            if sapper_query["runflag"]:
                sapper_query["output"].append(Completing)
            hint = 'Whether this supplementary text is satisfactory (a, not satisfied, rewritten; b, satisfied, make up the next one).';
            if sapper_query["runflag"]:
                sapper_query["output"].append(hint)
            stop, sapper_query, human1 = get_value("human1", sapper_request, sapper_query)
            if stop and sapper_query["runflag"]:
                sapper_query["runflag"] = False
                sapper_query["input"] = "human1"
                savequery(sapper_query)
                return {'Answer': sapper_query["output"]}

        hint = 'Whether to continue to start modifying sentences with the help of AI (1, yes; 2, No)';
        if sapper_query["runflag"]:
            sapper_query["output"].append(hint)
        stop, sapper_query, human3 = get_value("human3", sapper_request, sapper_query)
        if stop and sapper_query["runflag"]:
            sapper_query["runflag"] = False
            sapper_query["input"] = "human3"
            savequery(sapper_query)
            return {'Answer': sapper_query["output"]}




    resetquery(sapper_query, initrecord)
    return {'Answer': sapper_query["output"]}
