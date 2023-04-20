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



f1 = open("UserProject/sixiaopin/PromptTemplate.json", "r", encoding='UTF-8')
prompt_template = json.loads(f1.read())


def sixiaopin(sapper_request):
    chain = sapperchain(sapper_request['OpenaiKey'])
    chain.promptbase(prompt_template)

    initrecord = {"id":"","input":"preInfo","output":[],"runflag":"","Empty":"","start":"","option":"","chatbot":"","Scene":"","Answer":"","history_1":"","Question":"","Standard_Answer":"","Evaluation":"","Score":"","sentence":"","Career":"","User_2":"","history_2":"","Helper":"","Judge":"","Advice":"","First_Improvement":"","preInfo":""}
    sapper_query = update_request(initrecord, sapper_request)
    Empty=sapper_query["Empty"]
    start=sapper_query["start"]
    option=sapper_query["option"]
    chatbot=sapper_query["chatbot"]
    Scene=sapper_query["Scene"]
    Answer=sapper_query["Answer"]
    history_1=sapper_query["history_1"]
    Question=sapper_query["Question"]
    Standard_Answer=sapper_query["Standard_Answer"]
    Evaluation=sapper_query["Evaluation"]
    Score=sapper_query["Score"]
    sentence=sapper_query["sentence"]
    Career=sapper_query["Career"]
    User_2=sapper_query["User_2"]
    history_2=sapper_query["history_2"]
    Helper=sapper_query["Helper"]
    Judge=sapper_query["Judge"]
    Advice=sapper_query["Advice"]
    First_Improvement=sapper_query["First_Improvement"]
    preInfo=sapper_query["preInfo"]
    sapper_query["output"] = []
    if sapper_query["runflag"]:
        preInfo = """Hi there! I'm a AI language model that can help you with your resume writing and interview preparation. I can provide you with objective feedback on your resume, as well as advice on how to make it better. To get started, please provide me with your resume and I will evaluate it for you."""
        sapper_query["preInfo"]=preInfo
    if sapper_query["runflag"]:
        sapper_query["output"].append(preInfo)
        stop, sapper_query, Unit = get_value("preInfo", sapper_request, sapper_query)
    stop, sapper_query, Empty = get_value("Empty", sapper_request, sapper_query)
    if stop and sapper_query["runflag"]:
        sapper_query["runflag"] = False
        sapper_query["input"] = "Empty"
        savequery(sapper_query)
        return {'Answer': sapper_query["output"]}
    start = '尊敬的用户您好，欢迎您使用思小聘。模拟面试功能请输入1，简历助写等其他求职功能请输入2';
    if sapper_query["runflag"]:
        sapper_query["output"].append(start)
    stop, sapper_query, option = get_value("option", sapper_request, sapper_query)
    if stop and sapper_query["runflag"]:
        sapper_query["runflag"] = False
        sapper_query["input"] = "option"
        savequery(sapper_query)
        return {'Answer': sapper_query["output"]}
    if option == '1':
        chatbot = '欢迎使用思小聘模拟面试服务！请输入您的面试场景，如公务员面试，程序员面试……';
        if sapper_query["runflag"]:
            sapper_query["output"].append(chatbot)
        stop, sapper_query, Scene = get_value("Scene", sapper_request, sapper_query)
        if stop and sapper_query["runflag"]:
            sapper_query["runflag"] = False
            sapper_query["input"] = "Scene"
            savequery(sapper_query)
            return {'Answer': sapper_query["output"]}
        while Answer != 'Bye':
            if sapper_query["runflag"]:
                Question = chain.worker(",?Qwe1/UYdg+VpkS=ZLy",[history_1,Scene],{"temperature":0.7,"max_tokens":225,"stop_strs":"","top_p":1,"frequency_penalty":0,"presence_penalty":0,"engine":" text-davinci-003"})
                sapper_query["Question"]=Question
            if sapper_query["runflag"]:
                sapper_query["output"].append(Question)
            if sapper_query["runflag"]:
                history_1 = chain.worker("-NQrBzr1eZ%1ke8bH(Q!",[history_1,Question],{"temperature":0.7,"max_tokens":225,"stop_strs":"","top_p":1,"frequency_penalty":0,"presence_penalty":0,"engine":" text-davinci-003"})
                sapper_query["history_1"]=history_1
            stop, sapper_query, Answer = get_value("Answer", sapper_request, sapper_query)
            if stop and sapper_query["runflag"]:
                sapper_query["runflag"] = False
                sapper_query["input"] = "Answer"
                savequery(sapper_query)
                return {'Answer': sapper_query["output"]}
            if Answer != 'Bye':
                if sapper_query["runflag"]:
                    Standard_Answer = chain.worker("tHh6ew#9SrI*(h}op4=P",[Question],{"temperature":0.7,"max_tokens":2000,"top_p":1,"frequency_penalty":0,"presence_penalty":0,"engine":" gpt-3.5-turbo"})
                    sapper_query["Standard_Answer"]=Standard_Answer
                if sapper_query["runflag"]:
                    sapper_query["output"].append(Standard_Answer)
                if sapper_query["runflag"]:
                    Evaluation = chain.worker(";-s))NFRkxJDC?.4y6sg",[Scene,Question,Answer,Standard_Answer],{"temperature":0.7,"max_tokens":2000,"top_p":1,"frequency_penalty":0,"presence_penalty":0,"model":"g","engine":" gpt-3.5-turbo"})
                    sapper_query["Evaluation"]=Evaluation
                if sapper_query["runflag"]:
                    sapper_query["output"].append(Evaluation)
                if sapper_query["runflag"]:
                    Score = chain.worker("FtDfDoxqe:eU$[Ob{)Yr",[Scene,Question,Answer,Standard_Answer,Evaluation],{"temperature":0.7,"max_tokens":225,"stop_strs":"","top_p":1,"frequency_penalty":0,"presence_penalty":0,"engine":" text-davinci-003"})
                    sapper_query["Score"]=Score
                if sapper_query["runflag"]:
                    sapper_query["output"].append(Score)
            else:
                chatbot = '感谢使用思小聘！祝您求职顺利！';
                if sapper_query["runflag"]:
                    sapper_query["output"].append(chatbot)


    elif option == '2':
        chatbot = '请输入您的目标职业';
        if sapper_query["runflag"]:
            sapper_query["output"].append(chatbot)
        stop, sapper_query, sentence = get_value("sentence", sapper_request, sapper_query)
        if stop and sapper_query["runflag"]:
            sapper_query["runflag"] = False
            sapper_query["input"] = "sentence"
            savequery(sapper_query)
            return {'Answer': sapper_query["output"]}
        if sapper_query["runflag"]:
            Career = chain.worker("Q%Cm[rL|C/j%I8L0?9t3",[sentence],{"temperature":0.7,"max_tokens":225,"stop_strs":"","top_p":1,"frequency_penalty":0,"presence_penalty":0,"engine":" text-davinci-003"})
            sapper_query["Career"]=Career
        chatbot = '请输入您的需求';
        if sapper_query["runflag"]:
            sapper_query["output"].append(chatbot)
        while User_2 != 'Bye':
            stop, sapper_query, User_2 = get_value("User_2", sapper_request, sapper_query)
            if stop and sapper_query["runflag"]:
                sapper_query["runflag"] = False
                sapper_query["input"] = "User_2"
                savequery(sapper_query)
                return {'Answer': sapper_query["output"]}
            if sapper_query["runflag"]:
                Helper = chain.worker("p(PVY(i,Qrsu#WdcX@8^",[history_2,Career,User_2],{"temperature":0.7,"max_tokens":2000,"top_p":1,"frequency_penalty":0,"presence_penalty":0,"engine":" gpt-3.5-turbo"})
                sapper_query["Helper"]=Helper
            if sapper_query["runflag"]:
                sapper_query["output"].append(Helper)
            if sapper_query["runflag"]:
                history_2 = chain.worker("bhYY80;pURv9xNhfAq-I",[User_2,history_2,Helper],{"temperature":0.7,"max_tokens":225,"stop_strs":"","top_p":1,"frequency_penalty":0,"presence_penalty":0,"engine":" text-davinci-003"})
                sapper_query["history_2"]=history_2
            if User_2 != 'Bye':
                chatbot = '请问您对此结果是否满意？（A.不满意；B.满意。）';
                if sapper_query["runflag"]:
                    sapper_query["output"].append(chatbot)
                stop, sapper_query, Judge = get_value("Judge", sapper_request, sapper_query)
                if stop and sapper_query["runflag"]:
                    sapper_query["runflag"] = False
                    sapper_query["input"] = "Judge"
                    savequery(sapper_query)
                    return {'Answer': sapper_query["output"]}
                if Judge == 'A':
                    stop, sapper_query, Advice = get_value("Advice", sapper_request, sapper_query)
                    if stop and sapper_query["runflag"]:
                        sapper_query["runflag"] = False
                        sapper_query["input"] = "Advice"
                        savequery(sapper_query)
                        return {'Answer': sapper_query["output"]}
                    if sapper_query["runflag"]:
                        First_Improvement = chain.worker("{Kw2D6`m^,u^HmhBEXdA",[Helper,Advice],{"temperature":0.7,"max_tokens":225,"stop_strs":"","top_p":1,"frequency_penalty":0,"presence_penalty":0,"engine":" text-davinci-003"})
                        sapper_query["First_Improvement"]=First_Improvement
                    if sapper_query["runflag"]:
                        sapper_query["output"].append(First_Improvement)
                    chatbot = '请问您对此结果是否满意？（A.不满意；B.满意。）';
                    if sapper_query["runflag"]:
                        sapper_query["output"].append(chatbot)
                    stop, sapper_query, Judge = get_value("Judge", sapper_request, sapper_query)
                    if stop and sapper_query["runflag"]:
                        sapper_query["runflag"] = False
                        sapper_query["input"] = "Judge"
                        savequery(sapper_query)
                        return {'Answer': sapper_query["output"]}
                    if Judge == 'A':
                        while Judge == 'A':
                            if User_2 != 'Bye':
                                chatbot = '非常抱歉您对我的输出结果不满意。请告诉我您不满意的具体原因，我会尽力改进我的算法和输出，以便更好地满足您的需求。';
                                if sapper_query["runflag"]:
                                    sapper_query["output"].append(chatbot)
                                stop, sapper_query, Advice = get_value("Advice", sapper_request, sapper_query)
                                if stop and sapper_query["runflag"]:
                                    sapper_query["runflag"] = False
                                    sapper_query["input"] = "Advice"
                                    savequery(sapper_query)
                                    return {'Answer': sapper_query["output"]}
                                if sapper_query["runflag"]:
                                    First_Improvement = chain.worker("nG=0+EM?G;vag_iLbz3/",[First_Improvement,Advice],{"temperature":0.7,"max_tokens":2000,"top_p":1,"frequency_penalty":0,"presence_penalty":0,"engine":" gpt-3.5-turbo"})
                                    sapper_query["First_Improvement"]=First_Improvement
                                if sapper_query["runflag"]:
                                    sapper_query["output"].append(First_Improvement)
                                chatbot = '请问您对此结果是否满意？（A.不满意；B.满意。）';
                                if sapper_query["runflag"]:
                                    sapper_query["output"].append(chatbot)
                                stop, sapper_query, Judge = get_value("Judge", sapper_request, sapper_query)
                                if stop and sapper_query["runflag"]:
                                    sapper_query["runflag"] = False
                                    sapper_query["input"] = "Judge"
                                    savequery(sapper_query)
                                    return {'Answer': sapper_query["output"]}



                    chatbot = '非常感谢您的反馈，我很高兴能够帮助您。';
                    if sapper_query["runflag"]:
                        sapper_query["output"].append(chatbot)







    resetquery(sapper_query, initrecord)
    return {'Answer': sapper_query["output"]}
