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



f1 = open("UserProject/yunxiaojuan/PromptTemplate.json", "r", encoding='UTF-8')
prompt_template = json.loads(f1.read())


def yunxiaojuan(sapper_request):
    chain = sapperchain(sapper_request['OpenaiKey'])
    chain.promptbase(prompt_template)

    initrecord = {"id":"","input":"preInfo","output":[],"runflag":"","help":"","select":"","text":"","answer":"","analysis_all":"","analysis":"","judge":"","t_analysis":"","new_analysis":"","suggest":"","select_0":"","material_type":"","flowchart_content":"","flowchart_all":"","flowchart":"","t_flowchart":"","select_":"","material":"","code_content":"","code_all":"","code":"","t_code":"","article_content":"","article_all":"","article":"","t_article":"","question_type":"","question_attribute":"","question_class":"","difficulty":"","question":"","knownledge_points":"","requirement":"","defind":"","information":"","defined__questuin":"","preInfo":""}
    sapper_query = update_request(initrecord, sapper_request)
    help=sapper_query["help"]
    select=sapper_query["select"]
    text=sapper_query["text"]
    answer=sapper_query["answer"]
    analysis_all=sapper_query["analysis_all"]
    analysis=sapper_query["analysis"]
    judge=sapper_query["judge"]
    t_analysis=sapper_query["t_analysis"]
    new_analysis=sapper_query["new_analysis"]
    suggest=sapper_query["suggest"]
    select_0=sapper_query["select_0"]
    material_type=sapper_query["material_type"]
    flowchart_content=sapper_query["flowchart_content"]
    flowchart_all=sapper_query["flowchart_all"]
    flowchart=sapper_query["flowchart"]
    t_flowchart=sapper_query["t_flowchart"]
    select_=sapper_query["select_"]
    material=sapper_query["material"]
    code_content=sapper_query["code_content"]
    code_all=sapper_query["code_all"]
    code=sapper_query["code"]
    t_code=sapper_query["t_code"]
    article_content=sapper_query["article_content"]
    article_all=sapper_query["article_all"]
    article=sapper_query["article"]
    t_article=sapper_query["t_article"]
    question_type=sapper_query["question_type"]
    question_attribute=sapper_query["question_attribute"]
    question_class=sapper_query["question_class"]
    difficulty=sapper_query["difficulty"]
    question=sapper_query["question"]
    knownledge_points=sapper_query["knownledge_points"]
    requirement=sapper_query["requirement"]
    defind=sapper_query["defind"]
    information=sapper_query["information"]
    defined__questuin=sapper_query["defined__questuin"]
    preInfo=sapper_query["preInfo"]
    sapper_query["output"] = []
    if sapper_query["runflag"]:
        preInfo = """
        Hello! Welcome to our Al Service. 
        With this service, you can generate corresponding questions based on user needs by selecting the required functionality and following the prompts to enter user requirements. We also provide two additional functions: 
        learning analysis and material search. 
        These features help you analyze your personal learning situation and generate appropriate questions based on your needs, or find materials that meet your expectations for creating questions and generate them accordingly. 
        We aim to provide you with suitable exercises. 
        So, let's get started!
        """
        sapper_query["preInfo"]=preInfo
    if sapper_query["runflag"]:
        sapper_query["output"].append(preInfo)
        stop, sapper_query, Unit = get_value("preInfo", sapper_request, sapper_query)
    help = 'Please select the desired function: 1. Incorrect question analysis 2. Search for materials 3. Generate questions based on fixed patterns 4. Create custom questions.';
    if sapper_query["runflag"]:
        sapper_query["output"].append(help)
    stop, sapper_query, select = get_value("select", sapper_request, sapper_query)
    if stop and sapper_query["runflag"]:
        sapper_query["runflag"] = False
        sapper_query["input"] = "select"
        savequery(sapper_query)
        return {'Answer': sapper_query["output"]}
    if select == '1':
        help = 'Please enter the question：';
        if sapper_query["runflag"]:
            sapper_query["output"].append(help)
        stop, sapper_query, text = get_value("text", sapper_request, sapper_query)
        if stop and sapper_query["runflag"]:
            sapper_query["runflag"] = False
            sapper_query["input"] = "text"
            savequery(sapper_query)
            return {'Answer': sapper_query["output"]}
        help = 'Please enter the incorrect answer you provided：';
        if sapper_query["runflag"]:
            sapper_query["output"].append(help)
        stop, sapper_query, answer = get_value("answer", sapper_request, sapper_query)
        if stop and sapper_query["runflag"]:
            sapper_query["runflag"] = False
            sapper_query["input"] = "answer"
            savequery(sapper_query)
            return {'Answer': sapper_query["output"]}
        analysis_all = 'The question entered by the user is';
        if sapper_query["runflag"]:
            analysis_all = analysis_all + text;
            sapper_query["analysis_all"]=analysis_all
        if sapper_query["runflag"]:
            analysis_all = analysis_all + ',The user\'s incorrect answer is：';
            sapper_query["analysis_all"]=analysis_all
        if sapper_query["runflag"]:
            analysis_all = analysis_all + answer;
            sapper_query["analysis_all"]=analysis_all
        if sapper_query["runflag"]:
            analysis = chain.worker(";sH|@w^bnJDP80jzgzTX",[analysis_all],{"temperature":0.7,"max_tokens":225,"top_p":1,"frequency_penalty":0,"presence_penalty":0,"engine":" gpt-3.5-turbo"})
            sapper_query["analysis"]=analysis
        if sapper_query["runflag"]:
            sapper_query["output"].append(analysis)
        help = 'Please enterwhether to modify (input True to modify，input False to not modify)';
        if sapper_query["runflag"]:
            sapper_query["output"].append(help)
        stop, sapper_query, judge = get_value("judge", sapper_request, sapper_query)
        if stop and sapper_query["runflag"]:
            sapper_query["runflag"] = False
            sapper_query["input"] = "judge"
            savequery(sapper_query)
            return {'Answer': sapper_query["output"]}
        t_analysis = analysis_all;
        new_analysis = analysis;
        while judge == 'False':
            analysis_all = t_analysis;
            if sapper_query["runflag"]:
                analysis_all = analysis_all + ',The result of the student\'s analysis is:';
                sapper_query["analysis_all"]=analysis_all
            if sapper_query["runflag"]:
                analysis_all = analysis_all + new_analysis;
                sapper_query["analysis_all"]=analysis_all
            help = 'Please provide the modification requirements:';
            if sapper_query["runflag"]:
                sapper_query["output"].append(help)
            stop, sapper_query, suggest = get_value("suggest", sapper_request, sapper_query)
            if stop and sapper_query["runflag"]:
                sapper_query["runflag"] = False
                sapper_query["input"] = "suggest"
                savequery(sapper_query)
                return {'Answer': sapper_query["output"]}
            if sapper_query["runflag"]:
                analysis_all = analysis_all + 'The student\'s revision feedback is';
                sapper_query["analysis_all"]=analysis_all
            if sapper_query["runflag"]:
                analysis_all = analysis_all + suggest;
                sapper_query["analysis_all"]=analysis_all
            if sapper_query["runflag"]:
                new_analysis = chain.worker("+Nk,{|dYCP,1T/8K~=JA",[analysis_all],{"temperature":0.7,"max_tokens":225,"top_p":1,"frequency_penalty":0,"presence_penalty":0,"engine":" gpt-3.5-turbo"})
                sapper_query["new_analysis"]=new_analysis
            if sapper_query["runflag"]:
                sapper_query["output"].append(new_analysis)
            help = 'Please enterwhether to modify (input True to modify，input False to not modify)';
            if sapper_query["runflag"]:
                sapper_query["output"].append(help)
            stop, sapper_query, judge = get_value("judge", sapper_request, sapper_query)
            if stop and sapper_query["runflag"]:
                sapper_query["runflag"] = False
                sapper_query["input"] = "judge"
                savequery(sapper_query)
                return {'Answer': sapper_query["output"]}

        select = '3';
        select_0 = '1';

    if select == '2':
        help = 'Please enter the material type (1. flowchart 2. code 3. article)';
        if sapper_query["runflag"]:
            sapper_query["output"].append(help)
        stop, sapper_query, material_type = get_value("material_type", sapper_request, sapper_query)
        if stop and sapper_query["runflag"]:
            sapper_query["runflag"] = False
            sapper_query["input"] = "material_type"
            savequery(sapper_query)
            return {'Answer': sapper_query["output"]}
        if material_type == '1':
            help = 'Please enter the content required for the flowchart:';
            if sapper_query["runflag"]:
                sapper_query["output"].append(help)
            stop, sapper_query, flowchart_content = get_value("flowchart_content", sapper_request, sapper_query)
            if stop and sapper_query["runflag"]:
                sapper_query["runflag"] = False
                sapper_query["input"] = "flowchart_content"
                savequery(sapper_query)
                return {'Answer': sapper_query["output"]}
            flowchart_all = 'The content of the flowchart is:';
            if sapper_query["runflag"]:
                flowchart_all = flowchart_all + flowchart_content;
                sapper_query["flowchart_all"]=flowchart_all
            if sapper_query["runflag"]:
                flowchart = chain.worker("xUIVkkdYb7gPcDz,Ij.M",[flowchart_all],{"temperature":0.7,"max_tokens":225,"top_p":1,"frequency_penalty":0,"presence_penalty":0,"engine":" gpt-3.5-turbo"})
                sapper_query["flowchart"]=flowchart
            if sapper_query["runflag"]:
                sapper_query["output"].append(flowchart)
            help = 'Please enterwhether to modify (input True to modify，input False to not modify)';
            if sapper_query["runflag"]:
                sapper_query["output"].append(help)
            stop, sapper_query, judge = get_value("judge", sapper_request, sapper_query)
            if stop and sapper_query["runflag"]:
                sapper_query["runflag"] = False
                sapper_query["input"] = "judge"
                savequery(sapper_query)
                return {'Answer': sapper_query["output"]}
            t_flowchart = flowchart_all;
            while judge == 'False':
                flowchart_all = t_flowchart;
                if sapper_query["runflag"]:
                    flowchart_all = flowchart_all + 'The original flowchart is as follows:';
                    sapper_query["flowchart_all"]=flowchart_all
                if sapper_query["runflag"]:
                    flowchart_all = flowchart_all + flowchart;
                    sapper_query["flowchart_all"]=flowchart_all
                help = 'Please provide the requirements for the modifications.';
                if sapper_query["runflag"]:
                    sapper_query["output"].append(help)
                stop, sapper_query, suggest = get_value("suggest", sapper_request, sapper_query)
                if stop and sapper_query["runflag"]:
                    sapper_query["runflag"] = False
                    sapper_query["input"] = "suggest"
                    savequery(sapper_query)
                    return {'Answer': sapper_query["output"]}
                if sapper_query["runflag"]:
                    flowchart_all = flowchart_all + 'The user\'s suggested modifications are:';
                    sapper_query["flowchart_all"]=flowchart_all
                if sapper_query["runflag"]:
                    flowchart_all = flowchart_all + suggest;
                    sapper_query["flowchart_all"]=flowchart_all
                if sapper_query["runflag"]:
                    flowchart = chain.worker("Z1jScwXeSXcin4FtJhbt",[flowchart_all],{"temperature":0.7,"max_tokens":225,"top_p":1,"frequency_penalty":0,"presence_penalty":0,"engine":" gpt-3.5-turbo"})
                    sapper_query["flowchart"]=flowchart
                if sapper_query["runflag"]:
                    sapper_query["output"].append(flowchart)
                help = 'Please enterwhether to modify (input True to modify，input False to not modify)';
                if sapper_query["runflag"]:
                    sapper_query["output"].append(help)
                stop, sapper_query, judge = get_value("judge", sapper_request, sapper_query)
                if stop and sapper_query["runflag"]:
                    sapper_query["runflag"] = False
                    sapper_query["input"] = "judge"
                    savequery(sapper_query)
                    return {'Answer': sapper_query["output"]}

            select = '4';
            select_ = '1';
            material = flowchart;
        elif material_type == '2':
            help = 'Please enter the content required for the code:';
            if sapper_query["runflag"]:
                sapper_query["output"].append(help)
            stop, sapper_query, code_content = get_value("code_content", sapper_request, sapper_query)
            if stop and sapper_query["runflag"]:
                sapper_query["runflag"] = False
                sapper_query["input"] = "code_content"
                savequery(sapper_query)
                return {'Answer': sapper_query["output"]}
            code_all = 'The content of the code is:';
            code_all = code_content;
            if sapper_query["runflag"]:
                code = chain.worker("/=5j:`S={qscd]J7a4j#",[code_all],{"temperature":0.7,"max_tokens":225,"top_p":1,"frequency_penalty":0,"presence_penalty":0,"engine":" gpt-3.5-turbo"})
                sapper_query["code"]=code
            if sapper_query["runflag"]:
                sapper_query["output"].append(code)
            help = 'Please enterwhether to modify (input True to modify，input False to not modify)';
            if sapper_query["runflag"]:
                sapper_query["output"].append(help)
            stop, sapper_query, judge = get_value("judge", sapper_request, sapper_query)
            if stop and sapper_query["runflag"]:
                sapper_query["runflag"] = False
                sapper_query["input"] = "judge"
                savequery(sapper_query)
                return {'Answer': sapper_query["output"]}
            t_code = code_all;
            while judge == 'False':
                code_all = t_code;
                if sapper_query["runflag"]:
                    code_all = code_all + 'The original code is as follows:';
                    sapper_query["code_all"]=code_all
                if sapper_query["runflag"]:
                    code_all = code_all + code;
                    sapper_query["code_all"]=code_all
                help = 'Please provide the requirements for the modifications:';
                if sapper_query["runflag"]:
                    sapper_query["output"].append(help)
                stop, sapper_query, suggest = get_value("suggest", sapper_request, sapper_query)
                if stop and sapper_query["runflag"]:
                    sapper_query["runflag"] = False
                    sapper_query["input"] = "suggest"
                    savequery(sapper_query)
                    return {'Answer': sapper_query["output"]}
                if sapper_query["runflag"]:
                    code_all = code_all + 'The user\'s suggested modifications are:';
                    sapper_query["code_all"]=code_all
                if sapper_query["runflag"]:
                    code_all = code_all + suggest;
                    sapper_query["code_all"]=code_all
                if sapper_query["runflag"]:
                    code = chain.worker(")B9Y9meF-+RH}SY!x0*7",[code_all],{"temperature":0.7,"max_tokens":225,"top_p":1,"frequency_penalty":0,"presence_penalty":0,"engine":" gpt-3.5-turbo"})
                    sapper_query["code"]=code
                if sapper_query["runflag"]:
                    sapper_query["output"].append(code)
                help = 'Please enterwhether to modify (input True to modify，input False to not modify)';
                if sapper_query["runflag"]:
                    sapper_query["output"].append(help)
                stop, sapper_query, judge = get_value("judge", sapper_request, sapper_query)
                if stop and sapper_query["runflag"]:
                    sapper_query["runflag"] = False
                    sapper_query["input"] = "judge"
                    savequery(sapper_query)
                    return {'Answer': sapper_query["output"]}

            select = '4';
            material = code;
            select_ = '1';
        elif material_type == '3':
            help = 'Please enter the content required for the article:';
            if sapper_query["runflag"]:
                sapper_query["output"].append(help)
            stop, sapper_query, article_content = get_value("article_content", sapper_request, sapper_query)
            if stop and sapper_query["runflag"]:
                sapper_query["runflag"] = False
                sapper_query["input"] = "article_content"
                savequery(sapper_query)
                return {'Answer': sapper_query["output"]}
            article_all = 'The content of the article is:';
            article_all = article_content;
            if sapper_query["runflag"]:
                article = chain.worker("RZS8USKW(Xn=y]K[L~3R",[article_all],{"temperature":0.7,"max_tokens":225,"top_p":1,"frequency_penalty":0,"presence_penalty":0,"engine":" gpt-3.5-turbo"})
                sapper_query["article"]=article
            if sapper_query["runflag"]:
                sapper_query["output"].append(article)
            help = 'Please enterwhether to modify (input True to modify，input False to not modify)';
            if sapper_query["runflag"]:
                sapper_query["output"].append(help)
            stop, sapper_query, judge = get_value("judge", sapper_request, sapper_query)
            if stop and sapper_query["runflag"]:
                sapper_query["runflag"] = False
                sapper_query["input"] = "judge"
                savequery(sapper_query)
                return {'Answer': sapper_query["output"]}
            t_article = article_all;
            while judge == 'False':
                article_all = t_article;
                if sapper_query["runflag"]:
                    article_all = article_all + 'The original article is as follows:';
                    sapper_query["article_all"]=article_all
                if sapper_query["runflag"]:
                    article_all = article_all + article;
                    sapper_query["article_all"]=article_all
                help = 'Please provide the requirements for the modifications:';
                if sapper_query["runflag"]:
                    sapper_query["output"].append(help)
                stop, sapper_query, suggest = get_value("suggest", sapper_request, sapper_query)
                if stop and sapper_query["runflag"]:
                    sapper_query["runflag"] = False
                    sapper_query["input"] = "suggest"
                    savequery(sapper_query)
                    return {'Answer': sapper_query["output"]}
                if sapper_query["runflag"]:
                    article_all = article_all + 'The user\'s suggested modifications are:';
                    sapper_query["article_all"]=article_all
                if sapper_query["runflag"]:
                    article_all = article_all + suggest;
                    sapper_query["article_all"]=article_all
                if sapper_query["runflag"]:
                    article = chain.worker("Jfm~nyk.4#YY5~r%zwMC",[article_all],{"temperature":0.7,"max_tokens":225,"top_p":1,"frequency_penalty":0,"presence_penalty":0,"engine":" gpt-3.5-turbo"})
                    sapper_query["article"]=article
                if sapper_query["runflag"]:
                    sapper_query["output"].append(article)
                help = 'Please enterwhether to modify (input True to modify，input False to not modify)';
                if sapper_query["runflag"]:
                    sapper_query["output"].append(help)
                stop, sapper_query, judge = get_value("judge", sapper_request, sapper_query)
                if stop and sapper_query["runflag"]:
                    sapper_query["runflag"] = False
                    sapper_query["input"] = "judge"
                    savequery(sapper_query)
                    return {'Answer': sapper_query["output"]}


        select = '4';
        material = article;
        select_ = '1';

    if select == '3':
        help = 'Please select your desired question type (1. Multiple choice 2. Fill in the blank).';
        if sapper_query["runflag"]:
            sapper_query["output"].append(help)
        stop, sapper_query, question_type = get_value("question_type", sapper_request, sapper_query)
        if stop and sapper_query["runflag"]:
            sapper_query["runflag"] = False
            sapper_query["input"] = "question_type"
            savequery(sapper_query)
            return {'Answer': sapper_query["output"]}
        if question_type == '1':
            if select_0 == '1':
                question_attribute = "User's incorrect question analysis:";
                if sapper_query["runflag"]:
                    question_attribute = question_attribute + analysis;
                    sapper_query["question_attribute"]=question_attribute
                help = 'Please select the subject to which your desired questions belong:';
                if sapper_query["runflag"]:
                    sapper_query["output"].append(help)
                stop, sapper_query, question_class = get_value("question_class", sapper_request, sapper_query)
                if stop and sapper_query["runflag"]:
                    sapper_query["runflag"] = False
                    sapper_query["input"] = "question_class"
                    savequery(sapper_query)
                    return {'Answer': sapper_query["output"]}
                if sapper_query["runflag"]:
                    question_attribute = question_attribute + 'Generate questions belonging to the subject:';
                    sapper_query["question_attribute"]=question_attribute
                if sapper_query["runflag"]:
                    question_attribute = question_attribute + question_class;
                    sapper_query["question_attribute"]=question_attribute
                help = 'Please choose the difficulty level of the questions you want:';
                if sapper_query["runflag"]:
                    sapper_query["output"].append(help)
                stop, sapper_query, difficulty = get_value("difficulty", sapper_request, sapper_query)
                if stop and sapper_query["runflag"]:
                    sapper_query["runflag"] = False
                    sapper_query["input"] = "difficulty"
                    savequery(sapper_query)
                    return {'Answer': sapper_query["output"]}
                if sapper_query["runflag"]:
                    question_attribute = question_attribute + 'The difficulty level of generating questions:';
                    sapper_query["question_attribute"]=question_attribute
                if sapper_query["runflag"]:
                    question_attribute = question_attribute + difficulty;
                    sapper_query["question_attribute"]=question_attribute
                if sapper_query["runflag"]:
                    question = chain.worker("Nb^;ahH@EBq(x|m~SJi!",[question_attribute],{"temperature":0.7,"max_tokens":225,"top_p":1,"frequency_penalty":0,"presence_penalty":0,"engine":" gpt-3.5-turbo"})
                    sapper_query["question"]=question
                if sapper_query["runflag"]:
                    sapper_query["output"].append(question)
            else:
                help = 'Please select the knowledge points that you would like the questions to cover:';
                if sapper_query["runflag"]:
                    sapper_query["output"].append(help)
                stop, sapper_query, knownledge_points = get_value("knownledge_points", sapper_request, sapper_query)
                if stop and sapper_query["runflag"]:
                    sapper_query["runflag"] = False
                    sapper_query["input"] = "knownledge_points"
                    savequery(sapper_query)
                    return {'Answer': sapper_query["output"]}
                if sapper_query["runflag"]:
                    question_attribute = question_attribute + 'Generating questions involves the knowledge points being covered:';
                    sapper_query["question_attribute"]=question_attribute
                if sapper_query["runflag"]:
                    question_attribute = question_attribute + knownledge_points;
                    sapper_query["question_attribute"]=question_attribute
                help = 'Please enter the subject to which you want the question to belong:';
                if sapper_query["runflag"]:
                    sapper_query["output"].append(help)
                stop, sapper_query, question_class = get_value("question_class", sapper_request, sapper_query)
                if stop and sapper_query["runflag"]:
                    sapper_query["runflag"] = False
                    sapper_query["input"] = "question_class"
                    savequery(sapper_query)
                    return {'Answer': sapper_query["output"]}
                if sapper_query["runflag"]:
                    question_attribute = question_attribute + 'Generate the subject to which the question belongs.';
                    sapper_query["question_attribute"]=question_attribute
                if sapper_query["runflag"]:
                    question_attribute = question_attribute + question_class;
                    sapper_query["question_attribute"]=question_attribute
                help = 'Please select the difficulty level for your desired question:';
                if sapper_query["runflag"]:
                    sapper_query["output"].append(help)
                stop, sapper_query, difficulty = get_value("difficulty", sapper_request, sapper_query)
                if stop and sapper_query["runflag"]:
                    sapper_query["runflag"] = False
                    sapper_query["input"] = "difficulty"
                    savequery(sapper_query)
                    return {'Answer': sapper_query["output"]}
                if sapper_query["runflag"]:
                    question_attribute = question_attribute + 'choose the difficulty level of the questions:';
                    sapper_query["question_attribute"]=question_attribute
                if sapper_query["runflag"]:
                    question_attribute = question_attribute + difficulty;
                    sapper_query["question_attribute"]=question_attribute
                if sapper_query["runflag"]:
                    question = chain.worker("O)yU/^RFx~X_y.9mAC[e",[question_attribute],{"temperature":0.7,"max_tokens":225,"top_p":1,"frequency_penalty":0,"presence_penalty":0,"engine":" gpt-3.5-turbo"})
                    sapper_query["question"]=question
                if sapper_query["runflag"]:
                    sapper_query["output"].append(question)

        elif question_type == '2':
            if select_0 == '1':
                question_attribute = "User's incorrect question analysis:";
                if sapper_query["runflag"]:
                    question_attribute = question_attribute + analysis;
                    sapper_query["question_attribute"]=question_attribute
                help = 'Please select the subject to which your desired questions belong:';
                if sapper_query["runflag"]:
                    sapper_query["output"].append(help)
                stop, sapper_query, question_class = get_value("question_class", sapper_request, sapper_query)
                if stop and sapper_query["runflag"]:
                    sapper_query["runflag"] = False
                    sapper_query["input"] = "question_class"
                    savequery(sapper_query)
                    return {'Answer': sapper_query["output"]}
                if sapper_query["runflag"]:
                    question_attribute = question_attribute + 'Generate questions belonging to the subject:';
                    sapper_query["question_attribute"]=question_attribute
                if sapper_query["runflag"]:
                    question_attribute = question_attribute + question_class;
                    sapper_query["question_attribute"]=question_attribute
                help = 'Please choose the difficulty level of the questions you want:';
                if sapper_query["runflag"]:
                    sapper_query["output"].append(help)
                stop, sapper_query, difficulty = get_value("difficulty", sapper_request, sapper_query)
                if stop and sapper_query["runflag"]:
                    sapper_query["runflag"] = False
                    sapper_query["input"] = "difficulty"
                    savequery(sapper_query)
                    return {'Answer': sapper_query["output"]}
                if sapper_query["runflag"]:
                    question_attribute = question_attribute + 'The difficulty level of generating questions:';
                    sapper_query["question_attribute"]=question_attribute
                if sapper_query["runflag"]:
                    question_attribute = question_attribute + difficulty;
                    sapper_query["question_attribute"]=question_attribute
                if sapper_query["runflag"]:
                    question = chain.worker("tbU3SxE;*UOVYZ4F^W~f",[question_attribute],{"temperature":0.7,"max_tokens":225,"top_p":1,"frequency_penalty":0,"presence_penalty":0,"engine":" gpt-3.5-turbo"})
                    sapper_query["question"]=question
                if sapper_query["runflag"]:
                    sapper_query["output"].append(question)
            else:
                help = 'Please select the knowledge points that you would like the questions to cover:';
                if sapper_query["runflag"]:
                    sapper_query["output"].append(help)
                stop, sapper_query, knownledge_points = get_value("knownledge_points", sapper_request, sapper_query)
                if stop and sapper_query["runflag"]:
                    sapper_query["runflag"] = False
                    sapper_query["input"] = "knownledge_points"
                    savequery(sapper_query)
                    return {'Answer': sapper_query["output"]}
                if sapper_query["runflag"]:
                    question_attribute = question_attribute + 'Generating questions involves the knowledge points being covered:';
                    sapper_query["question_attribute"]=question_attribute
                if sapper_query["runflag"]:
                    question_attribute = question_attribute + knownledge_points;
                    sapper_query["question_attribute"]=question_attribute
                help = 'Generate questions belonging to the subject:';
                if sapper_query["runflag"]:
                    sapper_query["output"].append(help)
                stop, sapper_query, question_class = get_value("question_class", sapper_request, sapper_query)
                if stop and sapper_query["runflag"]:
                    sapper_query["runflag"] = False
                    sapper_query["input"] = "question_class"
                    savequery(sapper_query)
                    return {'Answer': sapper_query["output"]}
                if sapper_query["runflag"]:
                    question_attribute = question_attribute + 'Generate questions belonging to the subject:';
                    sapper_query["question_attribute"]=question_attribute
                if sapper_query["runflag"]:
                    question_attribute = question_attribute + question_class;
                    sapper_query["question_attribute"]=question_attribute
                help = 'Please choose the difficulty level of the questions you want:';
                if sapper_query["runflag"]:
                    sapper_query["output"].append(help)
                stop, sapper_query, difficulty = get_value("difficulty", sapper_request, sapper_query)
                if stop and sapper_query["runflag"]:
                    sapper_query["runflag"] = False
                    sapper_query["input"] = "difficulty"
                    savequery(sapper_query)
                    return {'Answer': sapper_query["output"]}
                if sapper_query["runflag"]:
                    question_attribute = question_attribute + 'The difficulty level of generating questions:';
                    sapper_query["question_attribute"]=question_attribute
                if sapper_query["runflag"]:
                    question_attribute = question_attribute + difficulty;
                    sapper_query["question_attribute"]=question_attribute
                if sapper_query["runflag"]:
                    question = chain.worker("}6+4r1y3[6q.;KR!MryV",[question_attribute],{"temperature":0.7,"max_tokens":225,"top_p":1,"frequency_penalty":0,"presence_penalty":0,"engine":" gpt-3.5-turbo"})
                    sapper_query["question"]=question
                if sapper_query["runflag"]:
                    sapper_query["output"].append(question)



    if select == '4':
        help = 'Please select your requirements for the questions:';
        if sapper_query["runflag"]:
            sapper_query["output"].append(help)
        stop, sapper_query, requirement = get_value("requirement", sapper_request, sapper_query)
        if stop and sapper_query["runflag"]:
            sapper_query["runflag"] = False
            sapper_query["input"] = "requirement"
            savequery(sapper_query)
            return {'Answer': sapper_query["output"]}
        if select_ == '1':
            defind = 'The specific requirements for the questions:';
            if sapper_query["runflag"]:
                defind = defind + requirement;
                sapper_query["defind"]=defind
            if sapper_query["runflag"]:
                information = chain.worker("-XTt`,;!QqaFU-CXKE6^",[defind],{"temperature":0.7,"max_tokens":225,"top_p":1,"frequency_penalty":0,"presence_penalty":0,"engine":" gpt-3.5-turbo"})
                sapper_query["information"]=information
            if sapper_query["runflag"]:
                information = information + '.The materials needed for the questions:';
                sapper_query["information"]=information
            if sapper_query["runflag"]:
                information = information + material;
                sapper_query["information"]=information
            if sapper_query["runflag"]:
                defined__questuin = chain.worker("a$Z/vWnN!xgge|xt0HF:",[information],{"temperature":0.7,"max_tokens":225,"top_p":1,"frequency_penalty":0,"presence_penalty":0,"engine":" gpt-3.5-turbo"})
                sapper_query["defined__questuin"]=defined__questuin
            if sapper_query["runflag"]:
                sapper_query["output"].append(defined__questuin)
        else:
            defind = 'The specific requirements for the questions:';
            if sapper_query["runflag"]:
                defind = defind + requirement;
                sapper_query["defind"]=defind
            if sapper_query["runflag"]:
                information = chain.worker("OH;4zipv`UT[yNNB%WHd",[defind],{"temperature":0.7,"max_tokens":225,"top_p":1,"frequency_penalty":0,"presence_penalty":0,"engine":" gpt-3.5-turbo"})
                sapper_query["information"]=information
            if sapper_query["runflag"]:
                defined__questuin = chain.worker("H]*u8G#wbL*6$Zk0-)NR",[information],{"temperature":0.7,"max_tokens":225,"top_p":1,"frequency_penalty":0,"presence_penalty":0,"engine":" gpt-3.5-turbo"})
                sapper_query["defined__questuin"]=defined__questuin
            if sapper_query["runflag"]:
                sapper_query["output"].append(defined__questuin)





    resetquery(sapper_query, initrecord)
    return {'Answer': sapper_query["output"]}
