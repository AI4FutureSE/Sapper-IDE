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



f1 = open("UserProject/chunxiaoxie/PromptTemplate.json", "r", encoding='UTF-8')
prompt_template = json.loads(f1.read())


def chunxiaoxie(sapper_request):
    chain = sapperchain(sapper_request['OpenaiKey'])
    chain.promptbase(prompt_template)

    initrecord = {"id":"","input":"preInfo","output":[],"runflag":"","Text_type":"","bot_one":"","Reply1":"","question":"","history":"","Reply2":"","new_requirement":"","advices":"","Reply3":"","wented_knowledge":"","知识":"","reply":"","Reply4":"","went_rewrite":"","rewrite_better":"","Reply5":"","went_add":"","Reply6":"","choose":"","Outline":"","Reply7":"","enrich_part":"","rich_outline":"","短文本":"","Reply8":"","poilsh_part":"","reply9":"","polish_dirction":"","Polish":"","preInfo":""}
    sapper_query = update_request(initrecord, sapper_request)
    Text_type=sapper_query["Text_type"]
    bot_one=sapper_query["bot_one"]
    Reply1=sapper_query["Reply1"]
    question=sapper_query["question"]
    history=sapper_query["history"]
    Reply2=sapper_query["Reply2"]
    new_requirement=sapper_query["new_requirement"]
    advices=sapper_query["advices"]
    Reply3=sapper_query["Reply3"]
    wented_knowledge=sapper_query["wented_knowledge"]
    知识=sapper_query["知识"]
    reply=sapper_query["reply"]
    Reply4=sapper_query["Reply4"]
    went_rewrite=sapper_query["went_rewrite"]
    rewrite_better=sapper_query["rewrite_better"]
    Reply5=sapper_query["Reply5"]
    went_add=sapper_query["went_add"]
    Reply6=sapper_query["Reply6"]
    choose=sapper_query["choose"]
    Outline=sapper_query["Outline"]
    Reply7=sapper_query["Reply7"]
    enrich_part=sapper_query["enrich_part"]
    rich_outline=sapper_query["rich_outline"]
    短文本=sapper_query["短文本"]
    Reply8=sapper_query["Reply8"]
    poilsh_part=sapper_query["poilsh_part"]
    reply9=sapper_query["reply9"]
    polish_dirction=sapper_query["polish_dirction"]
    Polish=sapper_query["Polish"]
    preInfo=sapper_query["preInfo"]
    sapper_query["output"] = []
    if sapper_query["runflag"]:
        preInfo = """Hi there! 
I'm Chun Chun, your friendly AI assistant providing you with writing advice. I'm here to help you create the perfect text. 
To get started, please tell me the type of writing you need to complete.（For example: prose, poetry, etc.）. 
I'll then provide you with the best writing advice, materials and resources to help you create it.You can update your requirements based on my suggestions.Then collaborate with AI to complete the creation of an article.
"""
        sapper_query["preInfo"]=preInfo
    if sapper_query["runflag"]:
        sapper_query["output"].append(preInfo)
        stop, sapper_query, Unit = get_value("preInfo", sapper_request, sapper_query)
    stop, sapper_query, Text_type = get_value("Text_type", sapper_request, sapper_query)
    if stop and sapper_query["runflag"]:
        sapper_query["runflag"] = False
        sapper_query["input"] = "Text_type"
        savequery(sapper_query)
        return {'Answer': sapper_query["output"]}
    if sapper_query["runflag"]:
        bot_one = chain.worker("B38yKG19;.Cn9NM^lZ7V",[Text_type],{"temperature":0.7,"max_tokens":2048,"top_p":1,"frequency_penalty":0,"presence_penalty":0,"engine":" gpt-3.5-turbo"})
        sapper_query["bot_one"]=bot_one
    if sapper_query["runflag"]:
        sapper_query["output"].append(bot_one)
    Reply1 = "Next, you can have a conversation with a writing robot that will answer your questions and brainstorm with you.The conversation will end when you input 'bey'.";
    if sapper_query["runflag"]:
        sapper_query["output"].append(Reply1)
    question = 'yes';
    while question != 'bey':
        stop, sapper_query, question = get_value("question", sapper_request, sapper_query)
        if stop and sapper_query["runflag"]:
            sapper_query["runflag"] = False
            sapper_query["input"] = "question"
            savequery(sapper_query)
            return {'Answer': sapper_query["output"]}
        if sapper_query["runflag"]:
            bot_one = chain.worker("R`cj=cibYgd*2$E$8AAH",[Text_type,history,question],{"temperature":0.7,"max_tokens":2048,"top_p":1,"frequency_penalty":0,"presence_penalty":0,"engine":" gpt-3.5-turbo"})
            sapper_query["bot_one"]=bot_one
        if sapper_query["runflag"]:
            sapper_query["output"].append(bot_one)
        if sapper_query["runflag"]:
            history = chain.worker("n?{lFAQ%+rp)72JSi[OU",[history,question,bot_one],{"engine":"PythonREPL"})
            sapper_query["history"]=history

    Reply2 = 'You can input more specific requirements for the article you want to write after communicating with the robot, such as the topic, style, or other more detailed requirements.';
    if sapper_query["runflag"]:
        sapper_query["output"].append(Reply2)
    stop, sapper_query, new_requirement = get_value("new_requirement", sapper_request, sapper_query)
    if stop and sapper_query["runflag"]:
        sapper_query["runflag"] = False
        sapper_query["input"] = "new_requirement"
        savequery(sapper_query)
        return {'Answer': sapper_query["output"]}
    if sapper_query["runflag"]:
        advices = chain.worker("Q9O@~?MjGQth8hhS77oC",[Text_type,new_requirement],{"temperature":0.7,"max_tokens":2048,"top_p":1,"frequency_penalty":0,"presence_penalty":0,"engine":" gpt-3.5-turbo"})
        sapper_query["advices"]=advices
    if sapper_query["runflag"]:
        sapper_query["output"].append(advices)
    Reply3 = "Find the materials and knowledge you want for the article based on your ideas. Input 'over' to stop.nowledge you want for the article.";
    if sapper_query["runflag"]:
        sapper_query["output"].append(Reply3)
    stop, sapper_query, wented_knowledge = get_value("wented_knowledge", sapper_request, sapper_query)
    if stop and sapper_query["runflag"]:
        sapper_query["runflag"] = False
        sapper_query["input"] = "wented_knowledge"
        savequery(sapper_query)
        return {'Answer': sapper_query["output"]}
    while wented_knowledge != 'over':
        if sapper_query["runflag"]:
            知识 = chain.worker("B0WCVj@zMsESFX8hdx_u",[wented_knowledge],{"temperature":0.7,"max_tokens":2048,"top_p":1,"frequency_penalty":0,"presence_penalty":0,"engine":" gpt-3.5-turbo"})
            sapper_query["知识"]=知识
        if sapper_query["runflag"]:
            sapper_query["output"].append(知识)
        if sapper_query["runflag"]:
            sapper_query["output"].append(Reply3)
        stop, sapper_query, wented_knowledge = get_value("wented_knowledge", sapper_request, sapper_query)
        if stop and sapper_query["runflag"]:
            sapper_query["runflag"] = False
            sapper_query["input"] = "wented_knowledge"
            savequery(sapper_query)
            return {'Answer': sapper_query["output"]}

    reply = 'Please identify the parts you want to use and divide them into two parts based on whether or not they need to be abbreviated.';
    if sapper_query["runflag"]:
        sapper_query["output"].append(reply)
    Reply4 = "Please input any extraneous knowledge you have. Input 'over' to stop..";
    if sapper_query["runflag"]:
        sapper_query["output"].append(Reply4)
    stop, sapper_query, went_rewrite = get_value("went_rewrite", sapper_request, sapper_query)
    if stop and sapper_query["runflag"]:
        sapper_query["runflag"] = False
        sapper_query["input"] = "went_rewrite"
        savequery(sapper_query)
        return {'Answer': sapper_query["output"]}
    while went_rewrite != 'over':
        if sapper_query["runflag"]:
            rewrite_better = chain.worker("11@vQnzYWEwP^d?2s=Mu",[went_rewrite],{"temperature":0.7,"max_tokens":2048,"top_p":1,"frequency_penalty":0,"presence_penalty":0,"engine":" gpt-3.5-turbo"})
            sapper_query["rewrite_better"]=rewrite_better
        if sapper_query["runflag"]:
            sapper_query["output"].append(rewrite_better)
        if sapper_query["runflag"]:
            sapper_query["output"].append(Reply4)
        stop, sapper_query, went_rewrite = get_value("went_rewrite", sapper_request, sapper_query)
        if stop and sapper_query["runflag"]:
            sapper_query["runflag"] = False
            sapper_query["input"] = "went_rewrite"
            savequery(sapper_query)
            return {'Answer': sapper_query["output"]}

    Reply5 = 'Please input any knowledge that any additional content you want to add to the prompt.';
    if sapper_query["runflag"]:
        sapper_query["output"].append(Reply5)
    stop, sapper_query, went_add = get_value("went_add", sapper_request, sapper_query)
    if stop and sapper_query["runflag"]:
        sapper_query["runflag"] = False
        sapper_query["input"] = "went_add"
        savequery(sapper_query)
        return {'Answer': sapper_query["output"]}
    Reply6 = 'Input "1" to generate long-form text (outline first, then generate content paragraph by paragraph according to the outline), input "2" to generate short-form text.';
    if sapper_query["runflag"]:
        sapper_query["output"].append(Reply6)
    stop, sapper_query, choose = get_value("choose", sapper_request, sapper_query)
    if stop and sapper_query["runflag"]:
        sapper_query["runflag"] = False
        sapper_query["input"] = "choose"
        savequery(sapper_query)
        return {'Answer': sapper_query["output"]}
    if choose == '1':
        if sapper_query["runflag"]:
            Outline = chain.worker("R;GpCSDc8pqReTVoq*r8",[went_add,new_requirement,Text_type],{"temperature":0.7,"max_tokens":2048,"top_p":1,"frequency_penalty":0,"presence_penalty":0,"engine":" gpt-3.5-turbo"})
            sapper_query["Outline"]=Outline
        if sapper_query["runflag"]:
            sapper_query["output"].append(Outline)
        Reply7 = "Input the content of the outline, input 'over' to stop.";
        if sapper_query["runflag"]:
            sapper_query["output"].append(Reply7)
        stop, sapper_query, enrich_part = get_value("enrich_part", sapper_request, sapper_query)
        if stop and sapper_query["runflag"]:
            sapper_query["runflag"] = False
            sapper_query["input"] = "enrich_part"
            savequery(sapper_query)
            return {'Answer': sapper_query["output"]}
        while enrich_part != 'over':
            if sapper_query["runflag"]:
                rich_outline = chain.worker("t$.S($c0Wp66;YnG~~o8",[enrich_part],{"temperature":0.7,"max_tokens":2048,"top_p":1,"frequency_penalty":0,"presence_penalty":0,"engine":" gpt-3.5-turbo"})
                sapper_query["rich_outline"]=rich_outline
            if sapper_query["runflag"]:
                sapper_query["output"].append(rich_outline)
            if sapper_query["runflag"]:
                sapper_query["output"].append(Reply7)
            stop, sapper_query, enrich_part = get_value("enrich_part", sapper_request, sapper_query)
            if stop and sapper_query["runflag"]:
                sapper_query["runflag"] = False
                sapper_query["input"] = "enrich_part"
                savequery(sapper_query)
                return {'Answer': sapper_query["output"]}

    elif choose == '2':
        if sapper_query["runflag"]:
            短文本 = chain.worker("+R5T2GO$%C^Md}%aum_1",[went_add,new_requirement,Text_type],{"temperature":0.7,"max_tokens":2048,"top_p":1,"frequency_penalty":0,"presence_penalty":0,"engine":" gpt-3.5-turbo"})
            sapper_query["短文本"]=短文本
        if sapper_query["runflag"]:
            sapper_query["output"].append(短文本)

    Reply8 = "Please input the content you want to polish, input 'over' to stop.";
    if sapper_query["runflag"]:
        sapper_query["output"].append(Reply8)
    stop, sapper_query, poilsh_part = get_value("poilsh_part", sapper_request, sapper_query)
    if stop and sapper_query["runflag"]:
        sapper_query["runflag"] = False
        sapper_query["input"] = "poilsh_part"
        savequery(sapper_query)
        return {'Answer': sapper_query["output"]}
    while poilsh_part != 'over':
        reply9 = 'Please input the direction you want to polish.';
        if sapper_query["runflag"]:
            sapper_query["output"].append(reply9)
        stop, sapper_query, polish_dirction = get_value("polish_dirction", sapper_request, sapper_query)
        if stop and sapper_query["runflag"]:
            sapper_query["runflag"] = False
            sapper_query["input"] = "polish_dirction"
            savequery(sapper_query)
            return {'Answer': sapper_query["output"]}
        if sapper_query["runflag"]:
            Polish = chain.worker("Q+O;pFY8yOVquwNpYy8h",[poilsh_part,reply9,reply9,polish_dirction],{"temperature":0.7,"max_tokens":2048,"top_p":1,"frequency_penalty":0,"presence_penalty":0,"engine":" gpt-3.5-turbo"})
            sapper_query["Polish"]=Polish
        if sapper_query["runflag"]:
            sapper_query["output"].append(Polish)
        if sapper_query["runflag"]:
            sapper_query["output"].append(Reply8)
        stop, sapper_query, poilsh_part = get_value("poilsh_part", sapper_request, sapper_query)
        if stop and sapper_query["runflag"]:
            sapper_query["runflag"] = False
            sapper_query["input"] = "poilsh_part"
            savequery(sapper_query)
            return {'Answer': sapper_query["output"]}




    resetquery(sapper_query, initrecord)
    return {'Answer': sapper_query["output"]}
