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

    initrecord = {"id":"","input":"preInfo","output":[],"runflag":"","AI_talk":"","Text_type":"","Reply1":"","question":"","AIReply":"","history":"","bot_one":"","abbreviation":"","Reply8":"","Audience":"","Theme":"","Style":"","Identity":"","Information":"","Reply2":"","wented_knowledge":"","find_knowledge":"","Simplify_knowledge":"","Reply3":"","materials":"","AI_reply1":"","choose_user":"","AI_writing":"","AI_reply2":"","poilsh_part":"","AI_reply3":"","polish_dirction":"","polish":"","preInfo":""}
    sapper_query = update_request(initrecord, sapper_request)
    AI_talk=sapper_query["AI_talk"]
    Text_type=sapper_query["Text_type"]
    Reply1=sapper_query["Reply1"]
    question=sapper_query["question"]
    AIReply=sapper_query["AIReply"]
    history=sapper_query["history"]
    bot_one=sapper_query["bot_one"]
    abbreviation=sapper_query["abbreviation"]
    Reply8=sapper_query["Reply8"]
    Audience=sapper_query["Audience"]
    Theme=sapper_query["Theme"]
    Style=sapper_query["Style"]
    Identity=sapper_query["Identity"]
    Information=sapper_query["Information"]
    Reply2=sapper_query["Reply2"]
    wented_knowledge=sapper_query["wented_knowledge"]
    find_knowledge=sapper_query["find_knowledge"]
    Simplify_knowledge=sapper_query["Simplify_knowledge"]
    Reply3=sapper_query["Reply3"]
    materials=sapper_query["materials"]
    AI_reply1=sapper_query["AI_reply1"]
    choose_user=sapper_query["choose_user"]
    AI_writing=sapper_query["AI_writing"]
    AI_reply2=sapper_query["AI_reply2"]
    poilsh_part=sapper_query["poilsh_part"]
    AI_reply3=sapper_query["AI_reply3"]
    polish_dirction=sapper_query["polish_dirction"]
    polish=sapper_query["polish"]
    preInfo=sapper_query["preInfo"]
    sapper_query["output"] = []
    if sapper_query["runflag"]:
        preInfo = """Hi there! 

        I'm Chun Chun, your friendly AI assistant providing you with writing advice. I'm here to help you create the perfect text. 

        To get started, please tell me the type of writing you need to complete.（For example: prose, poetry, etc.）. 

        I'll then provide you with the best writing advice, materials and resources to help you create it.You can update your requirements based on my suggestions.Then collaborate with AI to complete the creation of an article."""
        sapper_query["preInfo"]=preInfo
    if sapper_query["runflag"]:
        sapper_query["output"].append(preInfo)
        stop, sapper_query, Unit = get_value("preInfo", sapper_request, sapper_query)
    AI_talk = 'Please provide me with the type of text you would like me to write.';
    if sapper_query["runflag"]:
        sapper_query["output"].append(AI_talk)
    stop, sapper_query, Text_type = get_value("Text_type", sapper_request, sapper_query)
    if stop and sapper_query["runflag"]:
        sapper_query["runflag"] = False
        sapper_query["input"] = "Text_type"
        savequery(sapper_query)
        return {'Answer': sapper_query["output"]}
    Reply1 = "Next, you can have a conversation with a writing robot that will answer your questions and brainstorm with you.The conversation will end when you input 'bey'.Please ask questions from the perspectives of the target audience, the main topic of the article, the style of the article, the materials needed for the article, and the identity of the article's author during the inquiry process.";
    if sapper_query["runflag"]:
        sapper_query["output"].append(Reply1)
    question = 'yes';
    while question != 'bey':
        AIReply = 'Please enter the question you want to ask.';
        if sapper_query["runflag"]:
            sapper_query["output"].append(AIReply)
        stop, sapper_query, question = get_value("question", sapper_request, sapper_query)
        if stop and sapper_query["runflag"]:
            sapper_query["runflag"] = False
            sapper_query["input"] = "question"
            savequery(sapper_query)
            return {'Answer': sapper_query["output"]}
        if sapper_query["runflag"]:
            bot_one = chain.worker("R`cj=cibYgd*2$E$8AAH",[Text_type,history,question],{"model":"t","engine":" text-davinci-003"})
            sapper_query["bot_one"]=bot_one
        if sapper_query["runflag"]:
            sapper_query["output"].append(bot_one)
        if sapper_query["runflag"]:
            abbreviation = chain.worker("|Mi`-w1#PGiP(A$mH4hm",[bot_one],{"model":"t","engine":" text-davinci-003"})
            sapper_query["abbreviation"]=abbreviation
        if sapper_query["runflag"]:
            history = chain.worker("n?{lFAQ%+rp)72JSi[OU",[history,question,abbreviation],{"engine":"PythonREPL"})
            sapper_query["history"]=history

    Reply8 = 'Target audience of the article, article topic, writing style, and author identity, please provide them in order for me.';
    if sapper_query["runflag"]:
        sapper_query["output"].append(Reply8)
    stop, sapper_query, Audience = get_value("Audience", sapper_request, sapper_query)
    if stop and sapper_query["runflag"]:
        sapper_query["runflag"] = False
        sapper_query["input"] = "Audience"
        savequery(sapper_query)
        return {'Answer': sapper_query["output"]}
    stop, sapper_query, Theme = get_value("Theme", sapper_request, sapper_query)
    if stop and sapper_query["runflag"]:
        sapper_query["runflag"] = False
        sapper_query["input"] = "Theme"
        savequery(sapper_query)
        return {'Answer': sapper_query["output"]}
    stop, sapper_query, Style = get_value("Style", sapper_request, sapper_query)
    if stop and sapper_query["runflag"]:
        sapper_query["runflag"] = False
        sapper_query["input"] = "Style"
        savequery(sapper_query)
        return {'Answer': sapper_query["output"]}
    stop, sapper_query, Identity = get_value("Identity", sapper_request, sapper_query)
    if stop and sapper_query["runflag"]:
        sapper_query["runflag"] = False
        sapper_query["input"] = "Identity"
        savequery(sapper_query)
        return {'Answer': sapper_query["output"]}
    if sapper_query["runflag"]:
        Information = chain.worker("i/gw0DU96nRf(2-~Ge9*",[Audience,Theme,Style,Identity],{"engine":"PythonREPL"})
        sapper_query["Information"]=Information
    Reply2 = 'Please enter the materials and examples you want to search for in the article, and AI will help find some of them. If "over" is output, it means to stop searching.';
    if sapper_query["runflag"]:
        sapper_query["output"].append(Reply2)
    stop, sapper_query, wented_knowledge = get_value("wented_knowledge", sapper_request, sapper_query)
    if stop and sapper_query["runflag"]:
        sapper_query["runflag"] = False
        sapper_query["input"] = "wented_knowledge"
        savequery(sapper_query)
        return {'Answer': sapper_query["output"]}
    while wented_knowledge != 'over':
        if sapper_query["runflag"]:
            find_knowledge = chain.worker("-uCv8V,22c;Gj^rTs;^q",[wented_knowledge],{"model":"t","engine":" text-davinci-003"})
            sapper_query["find_knowledge"]=find_knowledge
        if sapper_query["runflag"]:
            Simplify_knowledge = chain.worker("W*{TJk*fU7/nlfeZ1hqs",[find_knowledge],{"model":"t","engine":" text-davinci-003"})
            sapper_query["Simplify_knowledge"]=Simplify_knowledge
        if sapper_query["runflag"]:
            sapper_query["output"].append(Simplify_knowledge)
        if sapper_query["runflag"]:
            sapper_query["output"].append(Reply2)
        stop, sapper_query, wented_knowledge = get_value("wented_knowledge", sapper_request, sapper_query)
        if stop and sapper_query["runflag"]:
            sapper_query["runflag"] = False
            sapper_query["input"] = "wented_knowledge"
            savequery(sapper_query)
            return {'Answer': sapper_query["output"]}

    Reply3 = 'Please select and input the relevant parts from the materials you have searched for that can be used in your article.';
    if sapper_query["runflag"]:
        sapper_query["output"].append(Reply3)
    stop, sapper_query, materials = get_value("materials", sapper_request, sapper_query)
    if stop and sapper_query["runflag"]:
        sapper_query["runflag"] = False
        sapper_query["input"] = "materials"
        savequery(sapper_query)
        return {'Answer': sapper_query["output"]}
    AI_reply1 = 'Input "start," AI begins writing.';
    if sapper_query["runflag"]:
        sapper_query["output"].append(AI_reply1)
    stop, sapper_query, choose_user = get_value("choose_user", sapper_request, sapper_query)
    if stop and sapper_query["runflag"]:
        sapper_query["runflag"] = False
        sapper_query["input"] = "choose_user"
        savequery(sapper_query)
        return {'Answer': sapper_query["output"]}
    if choose_user == 'start':
        if sapper_query["runflag"]:
            AI_writing = chain.worker("5qi.shLZ]tEXqDZeTm-U",[Identity,Text_type,Information,materials],{"temperature":0.7,"max_tokens":2048,"top_p":1,"frequency_penalty":0,"presence_penalty":0,"engine":" gpt-3.5-turbo"})
            sapper_query["AI_writing"]=AI_writing
        if sapper_query["runflag"]:
            sapper_query["output"].append(AI_writing)
        AI_reply2 = "Please input the content you want to polish, input 'over' to stop.";
        if sapper_query["runflag"]:
            sapper_query["output"].append(AI_reply2)
        stop, sapper_query, poilsh_part = get_value("poilsh_part", sapper_request, sapper_query)
        if stop and sapper_query["runflag"]:
            sapper_query["runflag"] = False
            sapper_query["input"] = "poilsh_part"
            savequery(sapper_query)
            return {'Answer': sapper_query["output"]}
        while poilsh_part != 'over':
            AI_reply3 = 'Please input the direction you want to polish.';
            if sapper_query["runflag"]:
                sapper_query["output"].append(AI_reply3)
            stop, sapper_query, polish_dirction = get_value("polish_dirction", sapper_request, sapper_query)
            if stop and sapper_query["runflag"]:
                sapper_query["runflag"] = False
                sapper_query["input"] = "polish_dirction"
                savequery(sapper_query)
                return {'Answer': sapper_query["output"]}
            if sapper_query["runflag"]:
                polish = chain.worker("?l#]YX`_(k:@Sh:?%Z:o",[poilsh_part,polish_dirction],{"model":"t","engine":" text-davinci-003"})
                sapper_query["polish"]=polish
            if sapper_query["runflag"]:
                sapper_query["output"].append(polish)
            if sapper_query["runflag"]:
                sapper_query["output"].append(AI_reply2)
            stop, sapper_query, poilsh_part = get_value("poilsh_part", sapper_request, sapper_query)
            if stop and sapper_query["runflag"]:
                sapper_query["runflag"] = False
                sapper_query["input"] = "poilsh_part"
                savequery(sapper_query)
                return {'Answer': sapper_query["output"]}





    resetquery(sapper_query, initrecord)
    return {'Answer': sapper_query["output"]}
