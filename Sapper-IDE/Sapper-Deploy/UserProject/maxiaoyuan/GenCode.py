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



f1 = open("UserProject/maxiaoyuan/PromptTemplate.json", "r", encoding='UTF-8')
prompt_template = json.loads(f1.read())


def maxiaoyuan(sapper_request):
    chain = sapperchain(sapper_request['OpenaiKey'])
    chain.promptbase(prompt_template)

    initrecord = {"id":"","input":"preInfo","output":[],"runflag":"","question":"","aside":"","judge":"","judge ":"","problem_analysis":"","judge2":"","code_generation":"","code":"","judge3":"","code_analysis":"","circulate":"","requirement":"","code_modification":"","judge4":"","preInfo":""}
    sapper_query = update_request(initrecord, sapper_request)
    question=sapper_query["question"]
    aside=sapper_query["aside"]
    judge=sapper_query["judge"]
    judge =sapper_query["judge "]
    problem_analysis=sapper_query["problem_analysis"]
    judge2=sapper_query["judge2"]
    code_generation=sapper_query["code_generation"]
    code=sapper_query["code"]
    judge3=sapper_query["judge3"]
    code_analysis=sapper_query["code_analysis"]
    circulate=sapper_query["circulate"]
    requirement=sapper_query["requirement"]
    code_modification=sapper_query["code_modification"]
    judge4=sapper_query["judge4"]
    preInfo=sapper_query["preInfo"]
    sapper_query["output"] = []
    if sapper_query["runflag"]:
        preInfo = """Hello, welcome to Code Little Ape. You can send me a programming-related question or a piece of code, and I will assist you in solving your problem and provide an analysis of the code.If have any suggestion，please send mail to 1402581803@qq.com."""
        sapper_query["preInfo"]=preInfo
    if sapper_query["runflag"]:
        sapper_query["output"].append(preInfo)
        stop, sapper_query, Unit = get_value("preInfo", sapper_request, sapper_query)
    stop, sapper_query, question = get_value("question", sapper_request, sapper_query)
    if stop and sapper_query["runflag"]:
        sapper_query["runflag"] = False
        sapper_query["input"] = "question"
        savequery(sapper_query)
        return {'Answer': sapper_query["output"]}
    aside = 'Please select mode, mode 1 problem analysis, mode 2 code analysis.Input(1/2)';
    if sapper_query["runflag"]:
        sapper_query["output"].append(aside)
    stop, sapper_query, judge = get_value("judge", sapper_request, sapper_query)
    if stop and sapper_query["runflag"]:
        sapper_query["runflag"] = False
        sapper_query["input"] = "judge"
        savequery(sapper_query)
        return {'Answer': sapper_query["output"]}
    if judge  == '1':
        if sapper_query["runflag"]:
            problem_analysis = chain.worker("MkR()k2p[-aU,U0l~@]z",[question],{"temperature":0.7,"max_tokens":2000,"top_p":1,"frequency_penalty":0,"presence_penalty":0,"engine":" gpt-3.5-turbo"})
            sapper_query["problem_analysis"]=problem_analysis
        if sapper_query["runflag"]:
            sapper_query["output"].append(problem_analysis)
        aside = 'Do you need to generate code？Input（yes/no）';
        if sapper_query["runflag"]:
            sapper_query["output"].append(aside)
        stop, sapper_query, judge2 = get_value("judge2", sapper_request, sapper_query)
        if stop and sapper_query["runflag"]:
            sapper_query["runflag"] = False
            sapper_query["input"] = "judge2"
            savequery(sapper_query)
            return {'Answer': sapper_query["output"]}
        if judge2 == 'yes':
            if sapper_query["runflag"]:
                code_generation = chain.worker("0@D@K1mugkQy5NKv!i%N",[question,problem_analysis],{"temperature":0.7,"max_tokens":4000,"top_p":1,"frequency_penalty":0,"presence_penalty":0,"engine":" gpt-3.5-turbo"})
                sapper_query["code_generation"]=code_generation
            code = code_generation;
            if sapper_query["runflag"]:
                sapper_query["output"].append(code)

    else:
        code = question;

    if judge2 != 'no':
        aside = '  Do you need code analysis？Input（yes/no）';
        if sapper_query["runflag"]:
            sapper_query["output"].append(aside)
        stop, sapper_query, judge3 = get_value("judge3", sapper_request, sapper_query)
        if stop and sapper_query["runflag"]:
            sapper_query["runflag"] = False
            sapper_query["input"] = "judge3"
            savequery(sapper_query)
            return {'Answer': sapper_query["output"]}
        if judge3 == 'yes':
            if sapper_query["runflag"]:
                code_analysis = chain.worker("-.F(79I]cXI,#X][Bsu|",[code],{"temperature":0.7,"max_tokens":3000,"top_p":1,"frequency_penalty":0,"presence_penalty":0,"engine":" gpt-3.5-turbo"})
                sapper_query["code_analysis"]=code_analysis
            if sapper_query["runflag"]:
                sapper_query["output"].append(code_analysis)

        aside = 'If you\'re asking whether a code needs to be modified or not, please enter "Needs modification" if it does, or "No modification required" if it doesn\'t.';
        if sapper_query["runflag"]:
            sapper_query["output"].append(aside)
        stop, sapper_query, circulate = get_value("circulate", sapper_request, sapper_query)
        if stop and sapper_query["runflag"]:
            sapper_query["runflag"] = False
            sapper_query["input"] = "circulate"
            savequery(sapper_query)
            return {'Answer': sapper_query["output"]}
        while circulate == 'Needs modification':
            aside = 'Please enter the requirement';
            if sapper_query["runflag"]:
                sapper_query["output"].append(aside)
            stop, sapper_query, requirement = get_value("requirement", sapper_request, sapper_query)
            if stop and sapper_query["runflag"]:
                sapper_query["runflag"] = False
                sapper_query["input"] = "requirement"
                savequery(sapper_query)
                return {'Answer': sapper_query["output"]}
            if sapper_query["runflag"]:
                code_modification = chain.worker("CHStU|;dN?IkxcxeCFV;",[code,requirement],{"temperature":0.2,"max_tokens":4000,"top_p":1,"frequency_penalty":0,"presence_penalty":0,"engine":" gpt-3.5-turbo"})
                sapper_query["code_modification"]=code_modification
            if sapper_query["runflag"]:
                sapper_query["output"].append(code_modification)
            aside = '  Do you need code analysis？Input（yes/no）';
            if sapper_query["runflag"]:
                sapper_query["output"].append(aside)
            stop, sapper_query, judge4 = get_value("judge4", sapper_request, sapper_query)
            if stop and sapper_query["runflag"]:
                sapper_query["runflag"] = False
                sapper_query["input"] = "judge4"
                savequery(sapper_query)
                return {'Answer': sapper_query["output"]}
            if judge4 == 'yes':
                if sapper_query["runflag"]:
                    code_analysis = chain.worker("BFfzZym6E4!JOvT]JbNh",[code_modification],{"temperature":0.7,"max_tokens":225,"top_p":1,"frequency_penalty":0,"presence_penalty":0,"engine":" gpt-3.5-turbo"})
                    sapper_query["code_analysis"]=code_analysis
                if sapper_query["runflag"]:
                    sapper_query["output"].append(code_analysis)

            aside = 'If you\'re asking whether a code needs to be modified or not, please enter "Needs modification" if it does, or "No modification required" if it doesn\'t.';
            if sapper_query["runflag"]:
                sapper_query["output"].append(aside)
            stop, sapper_query, circulate = get_value("circulate", sapper_request, sapper_query)
            if stop and sapper_query["runflag"]:
                sapper_query["runflag"] = False
                sapper_query["input"] = "circulate"
                savequery(sapper_query)
                return {'Answer': sapper_query["output"]}
            code = code_modification;





    resetquery(sapper_query, initrecord)
    return {'Answer': sapper_query["output"]}
