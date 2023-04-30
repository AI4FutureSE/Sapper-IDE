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



f1 = open("UserProject/qingxiaoxie/PromptTemplate.json", "r", encoding='UTF-8')
prompt_template = json.loads(f1.read())


def qingxiaoxie(sapper_request):
    chain = sapperchain(sapper_request['OpenaiKey'])
    chain.promptbase(prompt_template)

    initrecord = {"id":"","input":"preInfo","output":[],"runflag":"","Genre":"","Writing_purpose":"","Writing_style":"","System":"","Content_requirements":"","Writing_materials":"","Extracting_key_points_from_thematerials":"","Material_integration":"","Content_integration":"","Writing_ideas":"","Write":"","Article":"","Template_writing":"","Select":"","Editing":"","Select1":"","Paragraph":"","Editing_instructions":"","Edit_paragraph_by_paragraph":"","preInfo":""}
    sapper_query = update_request(initrecord, sapper_request)
    Genre=sapper_query["Genre"]
    Writing_purpose=sapper_query["Writing_purpose"]
    Writing_style=sapper_query["Writing_style"]
    System=sapper_query["System"]
    Content_requirements=sapper_query["Content_requirements"]
    Writing_materials=sapper_query["Writing_materials"]
    Extracting_key_points_from_thematerials=sapper_query["Extracting_key_points_from_thematerials"]
    Material_integration=sapper_query["Material_integration"]
    Content_integration=sapper_query["Content_integration"]
    Writing_ideas=sapper_query["Writing_ideas"]
    Write=sapper_query["Write"]
    Article=sapper_query["Article"]
    Template_writing=sapper_query["Template_writing"]
    Select=sapper_query["Select"]
    Editing=sapper_query["Editing"]
    Select1=sapper_query["Select1"]
    Paragraph=sapper_query["Paragraph"]
    Editing_instructions=sapper_query["Editing_instructions"]
    Edit_paragraph_by_paragraph=sapper_query["Edit_paragraph_by_paragraph"]
    preInfo=sapper_query["preInfo"]
    sapper_query["output"] = []
    if sapper_query["runflag"]:
        preInfo = """Hi there! Welcome to our AI Writing service. We're here to help you craft the perfect article. To get started, please provide us with the genre you would like to write in and the purpose of your article. We will then provide you with key points and a basic approach for writing in that genre. Thanks for using our AI Writing service!"""
        sapper_query["preInfo"]=preInfo
    if sapper_query["runflag"]:
        sapper_query["output"].append(preInfo)
        stop, sapper_query, Unit = get_value("preInfo", sapper_request, sapper_query)
    stop, sapper_query, Genre = get_value("Genre", sapper_request, sapper_query)
    if stop and sapper_query["runflag"]:
        sapper_query["runflag"] = False
        sapper_query["input"] = "Genre"
        savequery(sapper_query)
        return {'Answer': sapper_query["output"]}
    stop, sapper_query, Writing_purpose = get_value("Writing_purpose", sapper_request, sapper_query)
    if stop and sapper_query["runflag"]:
        sapper_query["runflag"] = False
        sapper_query["input"] = "Writing_purpose"
        savequery(sapper_query)
        return {'Answer': sapper_query["output"]}
    if sapper_query["runflag"]:
        Writing_style = chain.worker("n7n.sV2-l~gCdfz#oZ|7",[Genre,Writing_purpose],{"temperature":0.3,"max_tokens":2025,"stop_strs":"","top_p":1,"frequency_penalty":0,"presence_penalty":0,"engine":" text-davinci-003"})
        sapper_query["Writing_style"]=Writing_style
    System = 'Please choose your writing method: "1. Writing based on given materials, 2. Writing using a general template" (Please enter the corresponding number).';
    if sapper_query["runflag"]:
        sapper_query["output"].append(System)
    stop, sapper_query, Content_requirements = get_value("Content_requirements", sapper_request, sapper_query)
    if stop and sapper_query["runflag"]:
        sapper_query["runflag"] = False
        sapper_query["input"] = "Content_requirements"
        savequery(sapper_query)
        return {'Answer': sapper_query["output"]}
    if Content_requirements == '1':
        System = 'Please provide writing materials.';
        if sapper_query["runflag"]:
            sapper_query["output"].append(System)
        stop, sapper_query, Writing_materials = get_value("Writing_materials", sapper_request, sapper_query)
        if stop and sapper_query["runflag"]:
            sapper_query["runflag"] = False
            sapper_query["input"] = "Writing_materials"
            savequery(sapper_query)
            return {'Answer': sapper_query["output"]}
        if sapper_query["runflag"]:
            Extracting_key_points_from_thematerials = chain.worker("Iw=k#vR.:]Oh$LI~aI|L",[Writing_materials],{"temperature":0.3,"max_tokens":1989,"stop_strs":"","top_p":1,"frequency_penalty":0,"presence_penalty":0,"engine":" text-davinci-003"})
            sapper_query["Extracting_key_points_from_thematerials"]=Extracting_key_points_from_thematerials
        if sapper_query["runflag"]:
            Material_integration = chain.worker("nO9Tp0_I5us8ldX|ST,C",[Writing_style,Extracting_key_points_from_thematerials],{"temperature":0.3,"max_tokens":1988,"stop_strs":"","top_p":1,"frequency_penalty":0,"presence_penalty":0,"engine":" text-davinci-003"})
            sapper_query["Material_integration"]=Material_integration
        System = 'Material processing is complete. Please wait patiently for the article to be generated.';
        if sapper_query["runflag"]:
            sapper_query["output"].append(System)
        if sapper_query["runflag"]:
            Content_integration = chain.worker("P[.QztnLM=9o~|79%kMP",[Writing_style,Material_integration],{"temperature":0.3,"max_tokens":1862,"stop_strs":"","top_p":1,"frequency_penalty":0,"presence_penalty":0,"engine":" text-davinci-003"})
            sapper_query["Content_integration"]=Content_integration
        if sapper_query["runflag"]:
            Writing_ideas = chain.worker("P[mqG{UFlCb_e28Y0oHr",[Writing_style,Content_integration],{"temperature":0.3,"max_tokens":1896,"stop_strs":"","top_p":1,"frequency_penalty":0,"presence_penalty":0,"engine":" text-davinci-003"})
            sapper_query["Writing_ideas"]=Writing_ideas
        if sapper_query["runflag"]:
            Write = chain.worker("/q:p~1xd8VJOR3e2U5t%",[Genre,Writing_ideas],{"temperature":0.3,"max_tokens":1899,"stop_strs":"","top_p":1,"frequency_penalty":0,"presence_penalty":0,"engine":" text-davinci-003"})
            sapper_query["Write"]=Write
        if sapper_query["runflag"]:
            sapper_query["output"].append(Write)
        Article = Material_integration;
        if sapper_query["runflag"]:
            sapper_query["output"].append(Article)
    elif Content_requirements == '2':
        System = 'The template is being generated. Please wait patiently for the article to be generated.';
        if sapper_query["runflag"]:
            sapper_query["output"].append(System)
        if sapper_query["runflag"]:
            Template_writing = chain.worker("^5aIGNf~VZ,JoLZ#:%_)",[Genre,Writing_purpose,Writing_style],{"temperature":0.3,"max_tokens":1209,"stop_strs":"","top_p":1,"frequency_penalty":0,"presence_penalty":0,"engine":" text-davinci-003"})
            sapper_query["Template_writing"]=Template_writing
        if sapper_query["runflag"]:
            sapper_query["output"].append(Template_writing)
        Article = Material_integration;
        if sapper_query["runflag"]:
            sapper_query["output"].append(Article)
        System = 'Are you still satisfied with the generated article?';
        if sapper_query["runflag"]:
            sapper_query["output"].append(System)
        System = '1.Satisfied, 2. Unsatisfied, Start editing (Please enter the number to make your choice)';
        if sapper_query["runflag"]:
            sapper_query["output"].append(System)
        stop, sapper_query, Select = get_value("Select", sapper_request, sapper_query)
        if stop and sapper_query["runflag"]:
            sapper_query["runflag"] = False
            sapper_query["input"] = "Select"
            savequery(sapper_query)
            return {'Answer': sapper_query["output"]}
        if Select == '1':
            System = 'Thank you for using it';
            if sapper_query["runflag"]:
                sapper_query["output"].append(System)
        elif Select == '2':
            while Editing != 'Stop':
                System = 'Please choose the degree of modification: "1. Paragraph modification, 2. AI rewriting" (Enter the corresponding number to select).';
                if sapper_query["runflag"]:
                    sapper_query["output"].append(System)
                stop, sapper_query, Select1 = get_value("Select1", sapper_request, sapper_query)
                if stop and sapper_query["runflag"]:
                    sapper_query["runflag"] = False
                    sapper_query["input"] = "Select1"
                    savequery(sapper_query)
                    return {'Answer': sapper_query["output"]}
                if Select1 == '1':
                    System = 'Please provide the paragraph you want to modify.';
                    if sapper_query["runflag"]:
                        sapper_query["output"].append(System)
                    stop, sapper_query, Paragraph = get_value("Paragraph", sapper_request, sapper_query)
                    if stop and sapper_query["runflag"]:
                        sapper_query["runflag"] = False
                        sapper_query["input"] = "Paragraph"
                        savequery(sapper_query)
                        return {'Answer': sapper_query["output"]}
                    System = 'Please provide your modification requirements.';
                    if sapper_query["runflag"]:
                        sapper_query["output"].append(System)
                    stop, sapper_query, Editing_instructions = get_value("Editing_instructions", sapper_request, sapper_query)
                    if stop and sapper_query["runflag"]:
                        sapper_query["runflag"] = False
                        sapper_query["input"] = "Editing_instructions"
                        savequery(sapper_query)
                        return {'Answer': sapper_query["output"]}
                    while Editing != 'Stop':
                        if sapper_query["runflag"]:
                            Edit_paragraph_by_paragraph = chain.worker("$G]Vr]@%:(3Cd)my;mtz",[Paragraph,Editing_instructions],{"temperature":0.3,"max_tokens":1790,"stop_strs":"","top_p":1,"frequency_penalty":0,"presence_penalty":0,"engine":" text-davinci-003"})
                            sapper_query["Edit_paragraph_by_paragraph"]=Edit_paragraph_by_paragraph
                        if sapper_query["runflag"]:
                            sapper_query["output"].append(Edit_paragraph_by_paragraph)
                        System = 'Are you satisfied with the produced article?';
                        if sapper_query["runflag"]:
                            sapper_query["output"].append(System)
                        System = 'If satisfied, please enter "Stop" to exit. If not satisfied, please enter "Continue".';
                        if sapper_query["runflag"]:
                            sapper_query["output"].append(System)
                        stop, sapper_query, Editing = get_value("Editing", sapper_request, sapper_query)
                        if stop and sapper_query["runflag"]:
                            sapper_query["runflag"] = False
                            sapper_query["input"] = "Editing"
                            savequery(sapper_query)
                            return {'Answer': sapper_query["output"]}

                elif Select1 == '2':
                    if sapper_query["runflag"]:
                        Content_integration = chain.worker("tgSx^Y+{Qd!oc$+e%%5Y",[Writing_style,Material_integration],{"temperature":0.3,"max_tokens":1824,"stop_strs":"","top_p":1,"frequency_penalty":0,"presence_penalty":0,"engine":" text-davinci-003"})
                        sapper_query["Content_integration"]=Content_integration
                    if sapper_query["runflag"]:
                        Writing_ideas = chain.worker("KvcJaM3?Eh@baX3pF,rj",[Writing_style,Content_integration],{"temperature":0.3,"max_tokens":1826,"stop_strs":"","top_p":1,"frequency_penalty":0,"presence_penalty":0,"engine":" text-davinci-003"})
                        sapper_query["Writing_ideas"]=Writing_ideas
                    if sapper_query["runflag"]:
                        Write = chain.worker("I|9{ZuZUn:J{]0fA322Q",[Genre,Writing_ideas],{"temperature":0.3,"max_tokens":1831,"stop_strs":"","top_p":1,"frequency_penalty":0,"presence_penalty":0,"engine":" text-davinci-003"})
                        sapper_query["Write"]=Write
                    if sapper_query["runflag"]:
                        sapper_query["output"].append(Write)
                    Article = Material_integration;
                    if sapper_query["runflag"]:
                        sapper_query["output"].append(Article)
                    System = 'Are you satisfied with the generated article?';
                    if sapper_query["runflag"]:
                        sapper_query["output"].append(System)
                    System = 'If satisfied, please enter "Stop" to exit. If not satisfied, please enter "Continue".';
                    if sapper_query["runflag"]:
                        sapper_query["output"].append(System)
                    stop, sapper_query, Editing = get_value("Editing", sapper_request, sapper_query)
                    if stop and sapper_query["runflag"]:
                        sapper_query["runflag"] = False
                        sapper_query["input"] = "Editing"
                        savequery(sapper_query)
                        return {'Answer': sapper_query["output"]}


            System = '感谢使用';
            if sapper_query["runflag"]:
                sapper_query["output"].append(System)





    resetquery(sapper_query, initrecord)
    return {'Answer': sapper_query["output"]}
