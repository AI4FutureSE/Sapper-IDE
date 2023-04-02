var ProjectList = [];
// Variable of created block
var Variable_xmlList = [];
// project prompt
var PromptList = [];
// prompt base
var PrompttemplateList = [];
// engine of AI model
var EngineConfigs = {
    'PLUSEngine':{
    'temperature': [0.7, 0.01, 1,'Temperature'],
    'max_tokens': [225, 1,2048,'Maximum length'],
    'top_p': [1, 0.01, 1,'Top P'],
    'frequency_penalty': [0 ,0.01,2,'Frequency penalty'],
    'presence_penalty': [0,0.01,2,'Presence penalty'],
    },
}
var RunEngineConfigs = {}
var ModelConfigs = {
    'text-davinci-003':{
    'temperature': [0.7, 0.01, 1,'Temperature'],
    'max_tokens': [225, 1,4000,'Maximum length'],
    'stop_strs': ['','Stop sequences'],
    'top_p': [1, 0.01, 1,'Top P'],
    'frequency_penalty': [0 ,0.01,2,'Frequency penalty'],
    'presence_penalty': [0,0.01,2,'Presence penalty'],
    // 'Best of': [1,1,20],
    },
    'gpt-3.5-turbo':{
    'temperature': [0.7, 0.01, 1,'Temperature'],
    'max_tokens': [225, 1,2048,'Maximum length'],
    'top_p': [1, 0.01, 1,'Top P'],
    'frequency_penalty': [0 ,0.01,2,'Frequency penalty'],
    'presence_penalty': [0,0.01,2,'Presence penalty'],
    },
    'DALL-E':{
    'n': [1, 1, 1,'Top P'],
    },
};
var RunModelConfigs = {};
// project model
var ModelList = [];
// model base
var DIYmodelList = [];
var APIEngine = [];
var TraditionEngine = [];
var RunPromptAspect = {}
var PromptValue = {'Prompt_Name':[['Instruction', '']]}
var ImportPromptValue = {}
// ID of the prompt context block created
var CreateExample = [];
var BlockDebugIDs = ["input_value"]
var DebugFlag = false
var RerunFlag = false
// var controller;
var InputFlag = false
// ID of the prompt block created
// prompt's values of prompt base
var PromptValues = {};

var PythonPromptValues = {}
// model's values of model base
var ModelValues = {};
// upload and save projects
var ProjectValues = {}
var OpenAIKey = "";
var initvariables = []
// 云端部署时记录第一个接收input数据的变量
var recordinput = "preInfo"
// worker的编号
var workerindex = 0

// design view 的聊天记录
var ClarifyConversion = [];
// exploration view  的聊天记录
var ExploreConversion = [];
// 该project的产品经理
var DesignManager = '';
let WindowHeight = window.innerHeight;
var PromptTemplateShownId = "";
// create main workspace of blockly
var ChatBot = {"Code_xmlList":[],"Variable_xmlList":[],"PromptList":["<block xmlns=\"https://developers.google.com/blockly/xml\" type=\"Prompt_template\" id=\"7o]ey9:/iZ!n!d0RLK4y\" x=\"30\" y=\"70\"><field name=\"Prompt_Name\">query</field><statement name=\"prompt_value\"><block type=\"Example\" id=\"/Hu*ZD=potbBrScSclHk\"><field name=\"Example_value\">Context</field><next><block type=\"Example\" id=\"L?8_}-j4AM1i~)zV4HnV\"><field name=\"Example_value\">Instruction</field></block></next></block></statement></block>","<block xmlns=\"https://developers.google.com/blockly/xml\" type=\"Prompt_template\" id=\"7o]ey9:/iZ!n!d0RLK4y\" x=\"30\" y=\"70\"><field name=\"Prompt_Name\">history</field><statement name=\"prompt_value\"><block type=\"Example\" id=\"L?8_}-j4AM1i~)zV4HnV\"><field name=\"Example_value\">Instruction</field></block></statement></block>","<block xmlns=\"https://developers.google.com/blockly/xml\" type=\"Prompt_template\" collapsed=\"true\" id=\"promptkNb3Ht\"><field name=\"Prompt_Name\"></field><statement name=\"prompt_value\"><block type=\"Example\" id=\"exampleFXSsxY\"><field name=\"Example_value\">context</field></block></statement></block>"],"PrompttemplateList":[],"ModelList":["<block xmlns=\"https://developers.google.com/blockly/xml\" type=\"LLM_Model\" id=\"71O#]ms]Sp_*q57BuCW{\"><field name=\"LLM_Name\">Engine_Name</field><statement name=\"Model\"><block type=\"Model\" id=\"DxGlmTzD_lU]rN|=%-pl\"><field name=\"modelName\">gpt-3.5-turbo</field></block></statement></block>","<block xmlns=\"https://developers.google.com/blockly/xml\" type=\"APIEngine\" id=\"joSia{Q1XNWo^0nGx=y7\"><field name=\"LLM_Name\">PythonREPL</field></block>"],"DIYmodelList":[],"APIEngine":[],"PromptValue":{"Prompt_Name":[["Instruction",""]]},"ModelValues":{"Engine_Name":{}},"RunPromptAspect":{"/Hu*ZD=potbBrScSclHk":["Instruction","You are a chatbot having a conversation with a human."],"L?8_}-j4AM1i~)zV4HnV":["Instruction","chat = \"\"\"{{chat}}\"\"\"\nhuman = \"\"\"Human: {{human}}\"\"\"\nbot = \"\"\"Chatbot: {{bot}}\"\"\"\nhistory = chat + \"\\n\" + human + \"\\n\" + bot + \"\\n\"\nprint(history)\n\n"],"Ii=UD9d3WQ1.UvqI,_$u":["Context","You are a chatbot having a conversation with a human."],"2J4x1:^cL1|ITezNoR)K":["Instruction","{{chat_history}}\nHuman: {{human_input}}\nChatbot:\n"],"10SZ@NZlQNuS=}D7%bR6":["Instruction","chat = \"\"\"{{chat}}\"\"\"\nhuman = \"\"\"Human: {{human}}\"\"\"\nbot = \"\"\"Chatbot: {{bot}}\"\"\"\nhistory = chat + \"\\n\" + human + \"\\n\" + bot + \"\\n\"\nprint(history)\n\n"]},"ImportPromptValue":{"query":[["Instruction","You are a chatbot having a conversation with a human."],["Instruction","chat = \"\"\"{{chat}}\"\"\"\nhuman = \"\"\"Human: {{human}}\"\"\"\nbot = \"\"\"Chatbot: {{bot}}\"\"\"\nhistory = chat + \"\\n\" + human + \"\\n\" + bot + \"\\n\"\nprint(history)\n\n"]],"history":[["Instruction","chat = \"\"\"{{chat}}\"\"\"\nhuman = \"\"\"Human: {{human}}\"\"\"\nbot = \"\"\"Chatbot: {{bot}}\"\"\"\nhistory = chat + \"\\n\" + human + \"\\n\" + bot + \"\\n\"\nprint(history)\n\n"]]},"TraditionEngine":[],"RunEngineConfigs":{"[Z2$#W):wHL:=H~Urnk%":{"temperature":[0.56,0.01,1,"Temperature"],"max_tokens":[225,1,4000,"Maximum length"],"stop_strs":["","Stop sequences"],"top_p":[1,0.01,1,"Top P"],"frequency_penalty":[0,0.01,2,"Frequency penalty"],"presence_penalty":[0,0.01,2,"Presence penalty"]},"x=RW.=l4__-b@xL2td!]":{"temperature":[0.56,0.01,1,"Temperature"],"max_tokens":[225,1,4000,"Maximum length"],"stop_strs":["","Stop sequences"],"top_p":[1,0.01,1,"Top P"],"frequency_penalty":[0,0.01,2,"Frequency penalty"],"presence_penalty":[0,0.01,2,"Presence penalty"]},";}_^%3}~:p+_61VfjNhV":{"temperature":[0.56,0.01,1,"Temperature"],"max_tokens":[225,1,4000,"Maximum length"],"stop_strs":["","Stop sequences"],"top_p":[1,0.01,1,"Top P"],"frequency_penalty":[0,0.01,2,"Frequency penalty"],"presence_penalty":[0,0.01,2,"Presence penalty"]},"z-1xgLEeVUafMSMW~$Vf":{"n":[1,1,1,"Top P"]},"g5}@d2fxo)6uS`D:YI2.":{"temperature":[0.7,0.01,1,"Temperature"],"max_tokens":[225,1,2048,"Maximum length"],"top_p":[1,0.01,1,"Top P"],"frequency_penalty":[0,0.01,2,"Frequency penalty"],"presence_penalty":[0,0.01,2,"Presence penalty"]},"];Wq`S0[~$Pu+=9=6D(a":{"temperature":[0.7,0.01,1,"Temperature"],"max_tokens":[225,1,2048,"Maximum length"],"top_p":[1,0.01,1,"Top P"],"frequency_penalty":[0,0.01,2,"Frequency penalty"],"presence_penalty":[0,0.01,2,"Presence penalty"]},",+:j|]N6H()HT|#0hRO7":{}},"EngineConfigs":{"initmodel":{"Temperature":[0.7,0.01,1],"Maximum length":[225,1,4000],"Stop sequences":[""],"Top P":[1,0.01,1],"Frequency penalty":[0,0.01,2],"Presence penalty":[0,0.01,2],"Best of":[1,1,20]},"Engine_Name":{"temperature":[0.7,0.01,1,"Temperature"],"max_tokens":[225,1,2048,"Maximum length"],"top_p":[1,0.01,1,"Top P"],"frequency_penalty":[0,0.01,2,"Frequency penalty"],"presence_penalty":[0,0.01,2,"Presence penalty"]},"hua":{"n":[1,1,1,"Top P"]}},"ExploreConversion":[],"ClarifyConversion":[],"TaskCards":[{"id":"1","type":"if","nestedCards":[{"id":"0","type":"task","nestedCards":[],"workName":"","promptName":"","output":"no","prework":[],"prompt":{"context":""},"model":"PythonREPL","taskcard":{"content":"","input":[],"prompt":[""],"output":["","no"],"model":"PythonREPL"}}],"input1":"","logicOperator":"=","input2":""}],"Require":"","workspace":"<xml xmlns=\"https://developers.google.com/blockly/xml\">\n  <block type=\"prompt_controls_whileUntil\" id=\"5|oe?9_i2V$xUD:MX2cu\" x=\"450\" y=\"70\">\n    <field name=\"MODE\">WHILE</field>\n    <value name=\"BOOL\">\n      <block type=\"prompt_compare\" id=\"pHV3bdR$N=|Cdh%ewISt\">\n        <field name=\"OP\">NEQ</field>\n        <value name=\"A\">\n          <block type=\"unit_var_value\" id=\"|A?K3n(+TX/]oB4r{!V-\">\n            <field name=\"unit_value\">human</field>\n          </block>\n        </value>\n        <value name=\"B\">\n          <shadow type=\"text\" id=\"jh$WfJ9owOe+YMe/3oT7\">\n            <field name=\"TEXT\">Good Bye</field>\n          </shadow>\n        </value>\n      </block>\n    </value>\n    <statement name=\"DO\">\n      <block type=\"AI_Unit\" id=\"rzIt@3qy#UpY{I?O{Tny\">\n        <field name=\"AI_Unit\">Worker</field>\n        <field name=\"Unit_Name\">history</field>\n        <statement name=\"PreWorkers\">\n          <block type=\"unit_var\" id=\"C{@0*(jR7DjPjQHF,3}t\">\n            <field name=\"unit_value\">history</field>\n            <next>\n              <block type=\"unit_var\" id=\"8A.#Zc9BuEZ;Ou:nk@ue\">\n                <field name=\"unit_value\">human</field>\n                <next>\n                  <block type=\"Output\" id=\"ZJ=Ip-}VpLSgrfh?.:W!\">\n                    <statement name=\"Output_var\">\n                      <block type=\"AI_Unit\" id=\"jOp/F4lZT{M9G.*?c|nw\">\n                        <field name=\"AI_Unit\">Worker</field>\n                        <field name=\"Unit_Name\">chatbot</field>\n                        <statement name=\"PreWorkers\">\n                          <block type=\"unit_var\" id=\"fz!R8?mDvpRja)LEyap8\">\n                            <field name=\"unit_value\">history</field>\n                            <next>\n                              <block type=\"Input\" id=\"!qRKty_AS46rE)u^0CIU\">\n                                <statement name=\"input_var\">\n                                  <block type=\"unit_var\" id=\"{E}YH?E4r|vi0n|Kp.jK\">\n                                    <field name=\"unit_value\">human</field>\n                                  </block>\n                                </statement>\n                              </block>\n                            </next>\n                          </block>\n                        </statement>\n                        <value name=\"Prompt\">\n                          <block type=\"Prompt_template\" id=\"T}ojRf(E+G5adzGNmnQV\" collapsed=\"true\">\n                            <field name=\"Prompt_Name\">query</field>\n                            <statement name=\"prompt_value\">\n                              <block type=\"Example\" id=\"Ii=UD9d3WQ1.UvqI,_$u\">\n                                <field name=\"Example_value\">Context</field>\n                                <next>\n                                  <block type=\"Example\" id=\"2J4x1:^cL1|ITezNoR)K\">\n                                    <field name=\"Example_value\">Instruction</field>\n                                  </block>\n                                </next>\n                              </block>\n                            </statement>\n                          </block>\n                        </value>\n                        <value name=\"Model\">\n                          <block type=\"LLM_Model\" id=\"g5}@d2fxo)6uS`D:YI2.\" collapsed=\"true\">\n                            <field name=\"LLM_Name\">Engine_Name</field>\n                            <statement name=\"Model\">\n                              <block type=\"Model\" id=\",MUGJv{[#{|n4?`)%~6Z\">\n                                <field name=\"modelName\">gpt-3.5-turbo</field>\n                              </block>\n                            </statement>\n                          </block>\n                        </value>\n                      </block>\n                    </statement>\n                  </block>\n                </next>\n              </block>\n            </next>\n          </block>\n        </statement>\n        <value name=\"Prompt\">\n          <block type=\"Prompt_template\" id=\"SAM[RY+V]*1^d,Gp0u=V\" collapsed=\"true\">\n            <field name=\"Prompt_Name\">history</field>\n            <statement name=\"prompt_value\">\n              <block type=\"Example\" id=\"10SZ@NZlQNuS=}D7%bR6\">\n                <field name=\"Example_value\">Instruction</field>\n              </block>\n            </statement>\n          </block>\n        </value>\n        <value name=\"Model\">\n          <block type=\"APIEngine\" id=\"gSCghpJ,C(Bmk}hWpS0?\">\n            <field name=\"LLM_Name\">PythonREPL</field>\n          </block>\n        </value>\n      </block>\n    </statement>\n  </block>\n</xml>"}
var todos2pic = {"Code_xmlList":[],"Variable_xmlList":[],"PromptList":["<block xmlns=\"https://developers.google.com/blockly/xml\" type=\"Prompt_template\" id=\"DAxFvrz.bIaUC2|$Gr*q\" x=\"70\" y=\"50\"><field name=\"Prompt_Name\">Text</field><statement name=\"prompt_value\"><block type=\"Example\" id=\"wZr[j%7asf?0%E3Fm//i\"><field name=\"Example_value\">Instruction</field></block></statement></block>","<block xmlns=\"https://developers.google.com/blockly/xml\" type=\"Prompt_template\" id=\"DAxFvrz.bIaUC2|$Gr*q\" x=\"70\" y=\"50\"><field name=\"Prompt_Name\">text2pic</field><statement name=\"prompt_value\"><block type=\"Example\" id=\"wZr[j%7asf?0%E3Fm//i\"><field name=\"Example_value\">Instruction</field></block></statement></block>","<block xmlns=\"https://developers.google.com/blockly/xml\" type=\"Prompt_template\" id=\"DAxFvrz.bIaUC2|$Gr*q\" x=\"70\" y=\"50\"><field name=\"Prompt_Name\">des2pic</field><statement name=\"prompt_value\"><block type=\"Example\" id=\"wZr[j%7asf?0%E3Fm//i\"><field name=\"Example_value\">Instruction</field></block></statement></block>"],"PrompttemplateList":[],"ModelList":["<block xmlns=\"https://developers.google.com/blockly/xml\" type=\"LLM_Model\" id=\"g(DNBM``ySM?vH,7m#Q{\"><field name=\"LLM_Name\">Engine_Name</field><statement name=\"Model\"><block type=\"Model\" id=\"pCb*,V~_Gg-50Hu%wB~d\"><field name=\"modelName\">text-davinci-003</field></block></statement></block>","<block xmlns=\"https://developers.google.com/blockly/xml\" type=\"LLM_Model\" id=\"nrw7g*=YRNztRt_.nH]k\"><field name=\"LLM_Name\">hua</field><statement name=\"Model\"><block type=\"Model\" id=\"UJ`pX*{O15_h8?vOskZK\"><field name=\"modelName\">DALL-E</field></block></statement></block>"],"DIYmodelList":[],"APIEngine":[],"PromptValue":{},"ModelValues":{"Engine_Name":{},"hua":{}},"RunPromptAspect":{"wZr[j%7asf?0%E3Fm//i":["Instruction","{{description}}\n\nCreate inspiring pictures based on the description above\n"],"OrZ4e}k*tf3SPcga,C{f":["Instruction",""],"cy+kW{xrwv-wr~@^4_%N":["Instruction","{{List}}\n\nWrite an inspirational paragraph based on todos above.\n"],"?NTBirAy3?|Ab|Qf@[tr":["Instruction","{{Text}}\n\nConvert the beautiful text above into a description of a painting\n"],"}_UEYZPo18cG!Tk)n7F,":["Instruction","{{description}}\n\nCreate inspiring pictures based on the description above\n"]},"ImportPromptValue":{"Prompt_Name":[["Instruction","{{description}}\n\nCreate inspiring pictures based on the description above\n"]],"Text":[["Instruction","{{description}}\n\nCreate inspiring pictures based on the description above\n"]],"text2pic":[["Instruction","{{description}}\n\nCreate inspiring pictures based on the description above\n"]],"des2pic":[["Instruction","{{description}}\n\nCreate inspiring pictures based on the description above\n"]]},"TraditionEngine":[],"RunEngineConfigs":{"[Z2$#W):wHL:=H~Urnk%":{"temperature":[0.56,0.01,1,"Temperature"],"max_tokens":[225,1,4000,"Maximum length"],"stop_strs":["","Stop sequences"],"top_p":[1,0.01,1,"Top P"],"frequency_penalty":[0,0.01,2,"Frequency penalty"],"presence_penalty":[0,0.01,2,"Presence penalty"]},"x=RW.=l4__-b@xL2td!]":{"temperature":[0.56,0.01,1,"Temperature"],"max_tokens":[225,1,4000,"Maximum length"],"stop_strs":["","Stop sequences"],"top_p":[1,0.01,1,"Top P"],"frequency_penalty":[0,0.01,2,"Frequency penalty"],"presence_penalty":[0,0.01,2,"Presence penalty"]},";}_^%3}~:p+_61VfjNhV":{"temperature":[0.56,0.01,1,"Temperature"],"max_tokens":[225,1,4000,"Maximum length"],"stop_strs":["","Stop sequences"],"top_p":[1,0.01,1,"Top P"],"frequency_penalty":[0,0.01,2,"Frequency penalty"],"presence_penalty":[0,0.01,2,"Presence penalty"]},"z-1xgLEeVUafMSMW~$Vf":{"n":[1,1,1,"Top P"]}},"EngineConfigs":{"initmodel":{"Temperature":[0.7,0.01,1],"Maximum length":[225,1,4000],"Stop sequences":[""],"Top P":[1,0.01,1],"Frequency penalty":[0,0.01,2],"Presence penalty":[0,0.01,2],"Best of":[1,1,20]},"Engine_Name":{"temperature":[0.56,0.01,1,"Temperature"],"max_tokens":[225,1,4000,"Maximum length"],"stop_strs":["","Stop sequences"],"top_p":[1,0.01,1,"Top P"],"frequency_penalty":[0,0.01,2,"Frequency penalty"],"presence_penalty":[0,0.01,2,"Presence penalty"]},"hua":{"n":[1,1,1,"Top P"]}},"ExploreConversion":[],"ClarifyConversion":[],"TaskCards":[],"Require":"","workspace":"<xml xmlns=\"https://developers.google.com/blockly/xml\">\n  <block type=\"Output\" id=\"nN23OejdQRPe]]mV#.2G\" x=\"-110\" y=\"250\">\n    <statement name=\"Output_var\">\n      <block type=\"AI_Unit\" id=\"LMdhGc)CJD+@9_oqs.b(\">\n        <field name=\"AI_Unit\">Worker</field>\n        <field name=\"Unit_Name\">Des2Picture</field>\n        <statement name=\"PreWorkers\">\n          <block type=\"Output\" id=\"`5M:k04BeU?}*`;#,?b*\">\n            <statement name=\"Output_var\">\n              <block type=\"AI_Unit\" id=\";{fnxTuNz5k%7Cxk8Qnu\">\n                <field name=\"AI_Unit\">Worker</field>\n                <field name=\"Unit_Name\">description</field>\n                <statement name=\"PreWorkers\">\n                  <block type=\"AI_Unit\" id=\"/d{G70qzw+RtinB@([p+\">\n                    <field name=\"AI_Unit\">Worker</field>\n                    <field name=\"Unit_Name\">Text</field>\n                    <statement name=\"PreWorkers\">\n                      <block type=\"Input\" id=\"M;b:5-Pblii]{S.Dtlk|\">\n                        <statement name=\"input_var\">\n                          <block type=\"unit_var\" id=\"p32w15{Bg3H:*c)GY.ba\">\n                            <field name=\"unit_value\">todos</field>\n                          </block>\n                        </statement>\n                      </block>\n                    </statement>\n                    <value name=\"Prompt\">\n                      <block type=\"Prompt_template\" id=\"so(NLRL]1N6XhgSfsEgR\" collapsed=\"true\">\n                        <field name=\"Prompt_Name\">Text</field>\n                        <statement name=\"prompt_value\">\n                          <block type=\"Example\" id=\"cy+kW{xrwv-wr~@^4_%N\">\n                            <field name=\"Example_value\">Instruction</field>\n                          </block>\n                        </statement>\n                      </block>\n                    </value>\n                    <value name=\"Model\">\n                      <block type=\"LLM_Model\" id=\"[Z2$#W):wHL:=H~Urnk%\" collapsed=\"true\">\n                        <field name=\"LLM_Name\">Engine_Name</field>\n                        <statement name=\"Model\">\n                          <block type=\"Model\" id=\"Ry_*Ztg=33~Kiiz-Q3Z#\">\n                            <field name=\"modelName\">text-davinci-003</field>\n                          </block>\n                        </statement>\n                      </block>\n                    </value>\n                  </block>\n                </statement>\n                <value name=\"Prompt\">\n                  <block type=\"Prompt_template\" id=\"cU#}$h$n}qavnbg5@8:I\" collapsed=\"true\">\n                    <field name=\"Prompt_Name\">text2pic</field>\n                    <statement name=\"prompt_value\">\n                      <block type=\"Example\" id=\"?NTBirAy3?|Ab|Qf@[tr\">\n                        <field name=\"Example_value\">Instruction</field>\n                      </block>\n                    </statement>\n                  </block>\n                </value>\n                <value name=\"Model\">\n                  <block type=\"LLM_Model\" id=\"x=RW.=l4__-b@xL2td!]\" collapsed=\"true\">\n                    <field name=\"LLM_Name\">Engine_Name</field>\n                    <statement name=\"Model\">\n                      <block type=\"Model\" id=\"nM})Rv%B+WjqZ6@fd;%Z\">\n                        <field name=\"modelName\">text-davinci-003</field>\n                      </block>\n                    </statement>\n                  </block>\n                </value>\n              </block>\n            </statement>\n          </block>\n        </statement>\n        <value name=\"Prompt\">\n          <block type=\"Prompt_template\" id=\"fXT.uk|f$wPHkl1DX0w3\" collapsed=\"true\">\n            <field name=\"Prompt_Name\">des2pic</field>\n            <statement name=\"prompt_value\">\n              <block type=\"Example\" id=\"}_UEYZPo18cG!Tk)n7F,\">\n                <field name=\"Example_value\">Instruction</field>\n              </block>\n            </statement>\n          </block>\n        </value>\n        <value name=\"Model\">\n          <block type=\"LLM_Model\" id=\"z-1xgLEeVUafMSMW~$Vf\" collapsed=\"true\">\n            <field name=\"LLM_Name\">hua</field>\n            <statement name=\"Model\">\n              <block type=\"Model\" id=\";HY*Gxz6?N:!WXW@B-hs\">\n                <field name=\"modelName\">DALL-E</field>\n              </block>\n            </statement>\n          </block>\n        </value>\n      </block>\n    </statement>\n  </block>\n</xml>"}

document.getElementById('sapper_body').style.height = WindowHeight - 55 + 'px';
document.getElementById("WorkDiv").style.height = WindowHeight - 80 + 'px';

document.getElementById("BlockConsoleDebug").style.display = "none";

document.getElementById('ShowProjectDiv').addEventListener('click',function(event){
    if(event.target.className !== 'btn content_button'){
        return;
    }
    for(var i = 0; i < document.getElementById('ShowProjectDiv').children.length; i++){
        document.getElementById('ShowProjectDiv').children[i].style.backgroundColor = 'gainsboro';
    }
    save_project()
    event.target.style.backgroundColor = '#b4afaf';
    initIDE();
    // update_project(initproject);
    var name_width = getTextWidth(event.target.innerText,13);
    document.getElementById("Save_Project_Name").style.width = name_width + 10 + "px";
    document.getElementById("Save_Project_Name").innerText=event.target.innerText;
    update_project(ProjectValues[event.target.innerText]);
});

function getTextWidth(str,fontSize){
    let result = 10;

    let ele = document.createElement('span')
    //字符串中带有换行符时，会被自动转换成<br/>标签，若需要考虑这种情况，可以替换成空格，以获取正确的宽度
    //str = str.replace(/\\n/g,' ').replace(/\\r/g,' ');
    ele.innerText = str;
    //不同的大小和不同的字体都会导致渲染出来的字符串宽度变化，可以传入尽可能完备的样式信息
    ele.style.fontSize = fontSize;

    //由于父节点的样式会影响子节点，这里可按需添加到指定节点上
    document.documentElement.append(ele);

    result =  ele.offsetWidth;

    document.documentElement.removeChild(ele);
    return result;
}

var demoWorkspace = Blockly.inject('blocklyDiv',{
      media: 'static/media/',
      toolbox: document.getElementById('toolbox'),
      collapse : false,
      scrollbars : true,
      grid: {
          spacing: 20,
      length: 3,
      colour: '#ccc',
      snap: true},
      zoom: {controls: true,
      startScale: 1.0,
      maxScale: 3,
      minScale: 0.3,
      scaleSpeed: 1.2},
      trashcan: true,
});
// create model workspace of blockly
var ModelWorkspace = Blockly.inject('CreateModelDiv',{
    media: 'static/media/',
    toolbox: document.getElementById('modeltoolbox'),
	collapse : true,
	comments : true,
	disable : true,
	maxBlocks : Infinity,
	trashcan : true,
	// horizontalLayout : true,
	toolboxPosition : 'start',
	css : true,
	rtl : false,
	scrollbars : true,
	sounds : true,
	oneBasedIndex : true,
	grid : {
		spacing : 20,
		length : 1,
		colour : '#888',
		snap : false
	},
	zoom : {
		controls : true,
		startScale : 1,
		maxScale : 3,
		minScale : 0.3,
		scaleSpeed : 1.2
	}
});
// create prompt workspace of blockly
var PromptWorkspace = Blockly.inject('CreatePromptDiv',{
      media: 'static/media/',
      toolbox: document.getElementById('prompttoolbox'),
      collapse : false,
      grid: {
          spacing: 20,
      length: 3,
      colour: '#ccc',
      snap: true},
      zoom: {controls: true,
      startScale: 1.0,
      maxScale: 3,
      minScale: 0.3,
      scaleSpeed: 1.2},
      trashcan: true,
});

// Initial interface state.
var initproject = {
    "PromptValue": {'Prompt_Name':[['Instruction', '']]},
    "ImportPromptValue" : {},
    "RunPromptAspect" :{},
  "Code_xmlList":[],
  "Variable_xmlList":["<button xmlns=\"http://www.w3.org/1999/xhtml\" text=\"Create Variable...\" callbackkey=\"Create_Variable\"></button>"],
  "PromptList":["<button xmlns=\"http://www.w3.org/1999/xhtml\" text=\"Import Prompt...\" callbackkey=\"Create_Prompt\"></button>"],
  "PrompttemplateList":[],
  "ModelList":["<button xmlns=\"http://www.w3.org/1999/xhtml\" text=\"Import Model...\" callbackkey=\"Create_Model\"></button>"],
  "DIYmodelList":["<block xmlns=\"https://developers.google.com/blockly/xml\" type=\"LLM_Model\"></block>"],
  "APIEngine":["<block xmlns=\"https://developers.google.com/blockly/xml\" type=\"APIEngine\"></block>"],
  "TraditionEngine":["<block xmlns=\"https://developers.google.com/blockly/xml\" type=\"LLM_Model\"></block>"],
  "PromptValues":{},
  "ModelValues":{},
    "RunPromptValues":{},
  "workspace":"<xml xmlns=\"https://developers.google.com/blockly/xml\"></xml>"
}

// Listen to prompt create event, then create a textarea for user to input prompt value from prompt workspace
PromptWorkspace.addChangeListener(CreatePromptEvent);
ModelWorkspace.addChangeListener(CreatePromptEvent);
demoWorkspace.addChangeListener(ShowPromptEvent);

var Originalcopyblock = '' ;
const originalBlocklyCopy = Blockly.copy;
// 覆盖 Blockly.copy 方法
Blockly.copy = function (block) {
  // 在这里，我们可以访问复制前的块
    Originalcopyblock = block;
  return originalBlocklyCopy.call(this, block);
};

// 定义一个标志变量
let blockCreatedByPaste = false;

// 保存原始的 Blockly.WorkspaceSvg.prototype.paste 函数
const originalBlocklyPaste = Blockly.WorkspaceSvg.prototype.paste;

// 覆盖 Blockly.WorkspaceSvg.prototype.paste 方法
Blockly.WorkspaceSvg.prototype.paste = function (clipboardXml) {
  // 设置标志变量
  blockCreatedByPaste = true;

  // 调用原始的 Blockly.WorkspaceSvg.prototype.paste 函数以保持正常的粘贴行为
  return originalBlocklyPaste.call(this, clipboardXml);
};
function findBlocksByType(block, finalblock, type, work) {
  const result = [];
  if (block.type === type) {
    result.push([block.id, finalblock.id]);
    RunPromptAspect[finalblock.id] = [finalblock.getFieldValue('Example_value'),  RunPromptAspect[block.id][1]];
  }
  if (block.type === 'LLM_Model' && work === "demoWorkspace") {
    RunEngineConfigs[finalblock.id] = {};
    RunEngineConfigs[finalblock.id] = JSON.parse(JSON.stringify(RunEngineConfigs[block.id]));
  }
  console.log(work)
  if(block.type === 'Model' && work === "ModelWorkspace"){
      RunModelConfigs[finalblock.id] = {}
      RunModelConfigs[finalblock.id] = JSON.parse(JSON.stringify(RunModelConfigs[block.id]));
  }
  const children = block.getChildren();
  const finalchildren = finalblock.getChildren();
  for (let i = 0; i < children.length; i++) {
    const childResult = findBlocksByType(children[i], finalchildren[i], type, work);
    result.push(childResult);
  }
  return result;
}

function CreatePromptEvent(primaryEvent) {
  if (primaryEvent instanceof Blockly.Events.Ui) {
      return
  }
  var promptblock;
  if(primaryEvent instanceof Blockly.Events.BlockCreate){
    promptblock = PromptWorkspace.getBlockById(primaryEvent.blockId);
    var promptBlockType = promptblock.type;
    var promptBlockId = promptblock.id;
    if(promptBlockType === 'Prompt_template' && !blockCreatedByPaste){
        var promptname = promptblock.getFieldValue('Prompt_Name')
        var i = 0;
        if(promptblock.getInputTargetBlock('prompt_value')){
            var targetBlock = promptblock.getInputTargetBlock('prompt_value');
            RunPromptAspect[targetBlock.id] = [targetBlock.getFieldValue('Example_value'), PromptValue[promptname][i][1]];
            while(targetBlock.nextConnection.isConnected()){
                i+=1;
                targetBlock = targetBlock.getNextBlock();
                RunPromptAspect[targetBlock.id] = [targetBlock.getFieldValue('Example_value'), PromptValue[promptname][i][1]];
            }
        }
    }
    else if(promptBlockType === 'Example' && !blockCreatedByPaste){
        RunPromptAspect[promptBlockId] = [promptblock.getFieldValue('Example_value'), ''];
    }
    else if(blockCreatedByPaste){
        const promptasceptBlocks = findBlocksByType(Originalcopyblock, promptblock, 'Example');
    }
    blockCreatedByPaste = false;
  }
  if(primaryEvent.type === "click" && primaryEvent.targetType === 'block'){
        if(PromptWorkspace.getBlockById(primaryEvent.blockId).type === "Prompt_template"){
             PromptTemplateShownId = primaryEvent.blockId;
             promptblock = PromptWorkspace.getBlockById(primaryEvent.blockId);
             var promptvalue = '';
             var tragetblock = promptblock.getInputTargetBlock('prompt_value');
             if(tragetblock){
                 promptvalue += RunPromptAspect[tragetblock.id][1] + "\n"
                 while(tragetblock.nextConnection.isConnected()){
                     tragetblock = tragetblock.getNextBlock();
                     promptvalue += RunPromptAspect[tragetblock.id][1] + "\n";
                 }
             }
             document.getElementById('PromptContentDiv').innerHTML = `<textarea id="${promptBlockId}" class="prompttemplate" readonly="readonly" style="display: block">${promptvalue}</textarea>`
        }
        else if(PromptWorkspace.getBlockById(primaryEvent.blockId).type === "Example"){
            const promptplaceholder ="Please input " + PromptWorkspace.getBlockById(primaryEvent.blockId).getFieldValue('Example_value')
            promptBlockId = primaryEvent.blockId;
            const promptvalue = RunPromptAspect[promptBlockId][1];
            document.getElementById('PromptContentDiv').innerHTML = `<textarea id="${promptBlockId}" class="promptexample" style="display: block" placeholder="${promptplaceholder}" oninput="RunPromptAspect['${promptBlockId}'][1] = this.value;">${promptvalue}</textarea>`
        }
  }
}
function CreateModelEvent(primaryEvent) {
    if (primaryEvent.type === Blockly.Events.UI && primaryEvent.element === 'trashcanOpen') {
    let currentDraggedBlock = ModelWorkspace.getBlockById(Blockly.dragging_block_);
    if (currentDraggedBlock) {
      console.log('Block dragged to trash:', currentDraggedBlock.id);
    }
  }
  if (primaryEvent instanceof Blockly.Events.Ui) {
      return
  }
  var promptblock;
  if(primaryEvent instanceof Blockly.Events.BlockCreate){
    promptblock = ModelWorkspace.getBlockById(primaryEvent.blockId);
    var promptBlockType = promptblock.type;
    var promptBlockId = promptblock.id;
    if(promptBlockType === 'LLM_Model' && !blockCreatedByPaste){
        if(promptblock.getInputTargetBlock('Model')){
          var model = promptblock.getInputTargetBlock('Model')
          RunModelConfigs[model.id] = {}
          RunModelConfigs[model.id] = JSON.parse(JSON.stringify(ModelValues[promptblock.getFieldValue('LLM_Name')]));
            generateModelConfigForm(RunModelConfigs[model.id], model.id, promptBlockId)
        }
    }
    else if(promptBlockType === 'Model' && !blockCreatedByPaste){
      var modelname = promptblock.getFieldValue('modelName')
      RunModelConfigs[promptblock.id] = {}
      RunModelConfigs[promptblock.id] = JSON.parse(JSON.stringify(ModelConfigs[modelname]));
    }
    else if(blockCreatedByPaste){
        const promptasceptBlocks = findBlocksByType(Originalcopyblock, promptblock, 'Example', "ModelWorkspace");
    }
    blockCreatedByPaste = false;
  }
  if(primaryEvent.type === "click" && primaryEvent.targetType === 'block'){
      if(ModelWorkspace.getBlockById(primaryEvent.blockId).type === "LLM_Model"){
          var engine = ModelWorkspace.getBlockById(primaryEvent.blockId);
          model = engine.getInputTargetBlock('Model')
          if(model){
              generateModelConfigForm(RunModelConfigs[model.id], model.id, primaryEvent.blockId)
          }
          return;
      }
  }
  if (primaryEvent.type === Blockly.Events.MOVE && ModelWorkspace.getBlockById(primaryEvent.blockId).type === 'Model'){
      var llmBlock = ModelWorkspace.getBlockById(primaryEvent.blockId);
    if (llmBlock.parentBlock_ && llmBlock.parentBlock_.type === 'LLM_Model') {
      generateModelConfigForm(RunModelConfigs[llmBlock.id], llmBlock.id, llmBlock.parentBlock_.id)
    }
    else{
        var element = document.querySelector('[data-model-id]');
        if (element) {
          // 获取 "data-engine-id" 属性的值
          var engineId = element.getAttribute('data-model-id');
          console.log(engineId)
            console.log(llmBlock.id)
          if(engineId === llmBlock.id){
            document.getElementById('ModelContentDiv').style.display = 'none';
            document.getElementById('ModelContentDiv').innerHTML = '';
            document.getElementById('CreateModelDiv').style.height = 'calc(100% - 30px)';
            Blockly.svgResize(ModelWorkspace);
          }
        }
    }
  }
}

// create a textarea for user to see the prompt value from main workspace
function ShowPromptEvent(primaryEvent) {
  if (primaryEvent instanceof Blockly.Events.Ui) {
    return;
  }
  if(primaryEvent.type === "click" && primaryEvent.type !== "selected" && primaryEvent.type !== "toolbox_item_select" && primaryEvent.type !== "viewport_change"){
  }
  if(primaryEvent instanceof Blockly.Events.BlockCreate) {
    var promptblock = demoWorkspace.getBlockById(primaryEvent.blockId);
    if(!promptblock){
        return;
    }
    var promptBlockType = promptblock.type;
    var promptBlockId = promptblock.id;
    if(promptBlockType === 'LLM_Model' && !blockCreatedByPaste){
        if(promptblock.getInputTargetBlock('Model')){
          RunEngineConfigs[promptBlockId] = {}
          RunEngineConfigs[promptBlockId] = JSON.parse(JSON.stringify(EngineConfigs[promptblock.getFieldValue('LLM_Name')]));
        }
    }
    else if(promptBlockType === 'Model'){
      var modelname = promptblock.getFieldValue('modelName')
      RunModelConfigs[promptblock.id] = {}
      RunModelConfigs[promptblock.id] = JSON.parse(JSON.stringify(ModelConfigs[modelname]));
    }
    if(promptBlockType === 'Prompt_template' && !blockCreatedByPaste){
        var promptname = promptblock.getFieldValue('Prompt_Name')
        i = 0;
        if(promptblock.getInputTargetBlock('prompt_value')){
            var targetBlock = promptblock.getInputTargetBlock('prompt_value');
            RunPromptAspect[targetBlock.id] = [targetBlock.getFieldValue('Example_value'), ImportPromptValue[promptname][i][1]];
            while(targetBlock.nextConnection.isConnected()){
                i+=1;
                targetBlock = targetBlock.getNextBlock();
                RunPromptAspect[targetBlock.id] = [targetBlock.getFieldValue('Example_value'), ImportPromptValue[promptname][i][1]];
            }
        }
    }
    else if(promptBlockType === 'Example'){
        RunPromptAspect[promptBlockId] = [promptblock.getFieldValue('Example_value'), ''];
    }
    else if(blockCreatedByPaste){
        const promptasceptBlocks = findBlocksByType(Originalcopyblock, promptblock, 'Example',"demoWorkspace");
    }
    blockCreatedByPaste = false;
  }
  if(primaryEvent.type === "click" && primaryEvent.targetType === 'block'){
      if(demoWorkspace.getBlockById(primaryEvent.blockId).type === "LLM_Model"){
          generateEngineConfigForm(RunEngineConfigs[primaryEvent.blockId], primaryEvent.blockId, primaryEvent.blockId)
          return;
      }
    if(demoWorkspace.getBlockById(primaryEvent.blockId).type === "Prompt_template"){
         promptblock = demoWorkspace.getBlockById(primaryEvent.blockId);
         var promptvalue = '';
         var tragetblock = promptblock.getInputTargetBlock('prompt_value');
         if(tragetblock){
             promptvalue += RunPromptAspect[tragetblock.id][1] + "\n"
             while(tragetblock.nextConnection.isConnected()){
                 tragetblock = tragetblock.getNextBlock();
                 promptvalue += RunPromptAspect[tragetblock.id][1] + "\n";
             }
         }
         document.getElementById('PromptConsoleValue').innerHTML = `<textarea id="${promptBlockId}" class="ProjectPromptTemplate" readonly="readonly" style="display: block">${promptvalue}</textarea>`
    }
    else if(demoWorkspace.getBlockById(primaryEvent.blockId).type === "Example"){
        const promptplaceholder ="Please input " + demoWorkspace.getBlockById(primaryEvent.blockId).getFieldValue('Example_value')
        promptBlockId = primaryEvent.blockId;
        const promptvalue = RunPromptAspect[promptBlockId][1];
        document.getElementById('PromptConsoleValue').innerHTML = `<textarea id="${promptBlockId}" class="ProjectPromptTemplate" style="display: block" placeholder="${promptplaceholder}" oninput="RunPromptAspect['${promptBlockId}'][1] = this.value;">${promptvalue}</textarea>`
    }
  }
}

// init the project console
document.getElementById('ModelDiv').style.display='none';
document.getElementById('PromptDiv').style.display='none';
document.getElementById('CodeDiv').style.display='none';

draftwidth("ProjectConsole");

// mian workspace
// Variables category of the main workspace
myCategoryFlyoutVariableback = function(demoWorkspace) {return Variable_xmlList;};
// Prompt category of the main workspace
myCategoryFlyoutDIYCallback = function(demoWorkspace) {return PromptList;};
// Model category of the main workspace
myCategoryFlyoutModelCallback = function(demoWorkspace) {return ModelList;};

// prompt workspace
// Promptbuilder category of the prompt workspace
myCategoryFlyoutPrompttemplateCallback = function(PromptWorkspace) {return PrompttemplateList;};

// model workspace
// Engine category of the model workspace
// AIengine category of the model workspace
myCategoryFlyoutDIYModelCallback = function(ModelWorkspace) {return DIYmodelList;};
myCategoryFlyoutAPIEngineCallback = function(ModelWorkspace) {return APIEngine;};
myCategoryFlyoutTraditionEngineCallback = function(ModelWorkspace) {return TraditionEngine;};

PromptWorkspace.registerToolboxCategoryCallback('DIYPrompttemplate', myCategoryFlyoutPrompttemplateCallback);
ModelWorkspace.registerToolboxCategoryCallback('DIYModel', myCategoryFlyoutDIYModelCallback);
ModelWorkspace.registerToolboxCategoryCallback('APIEngine', myCategoryFlyoutAPIEngineCallback);
ModelWorkspace.registerToolboxCategoryCallback('TraditionEngine', myCategoryFlyoutTraditionEngineCallback);

initIDE();
upload_project1("chatbot",ChatBot)

upload_project1("todos2pic",todos2pic)
initIDE();

/*
让demoworkplace自动更新大小
 */
// 选取要监视的元素
const myDiv = document.querySelector('#ProjectDiv');
// 创建 MutationObserver 实例
const observer = new MutationObserver((mutations) => {
  mutations.forEach((mutation) => {
    if (mutation.type === 'attributes' && mutation.attributeName === 'class') {
        onresize();
    }
  });
});
// 配置 MutationObserver
const config = {
  attributes: true,
  childList: false,
  characterData: false,
  attributeFilter: ['class']
};
// 开始监视
observer.observe(myDiv, config);
const myDiv1 = document.querySelector('#blocklyDiv');
// 创建 MutationObserver 实例
const observer1 = new MutationObserver((mutations) => {
  mutations.forEach((mutation) => {
    if (mutation.type === 'attributes' && mutation.attributeName === 'style') {
        onresize();
    }
  });
});
// 配置 MutationObserver
const config1 = {
  attributes: true,
  childList: false,
  characterData: false,
  attributeFilter: ['style']
};
// 开始监视
observer1.observe(myDiv1, config1);


const jsonData = [
  {
    "content": "How are you",
    "input": ["history", "human"],
    "prompt": ["You are a chatbot having a conversation with a human.\n" +
    "\n" +
    "{{chat_history}}\n" +
    "Human: {{human_input}}\n" +
    "Chatbot:\n", "i am miss you"],
    "output": "chatbot",
    "model": "LLM"
  },
    {
    "content": "How are you",
    "input": ["history","human", "chatbot"],
    "prompt": ["chat = \"\"\"{{chat}}\"\"\"\n" +
    "human = \"\"\"Human: {{human}}\"\"\"\n" +
    "bot = \"\"\"Chatbot: {{bot}}\"\"\"\n" +
    "history = chat + \"\\n\" + human + \"\\n\" + bot + \"\\n\"\n" +
    "print(history)\n" +
    "\n", "i am miss you"],
    "output": "history",
    "model": "python"
  },
    {
    "content": "How are you",
    "input": ["history", "human"],
    "prompt": ["You are a chatbot having a conversation with a human.\n" +
    "\n" +
    "{{chat_history}}\n" +
    "Human: {{human_input}}\n" +
    "Chatbot:\n", "i am miss you"],
    "output": "chatbot",
    "model": "LLM"
  },
];
const inittaskcard = {
    "content": "",
    "input": [],
    "prompt": [""],
    "output": ["", 'no'],
    "model": "LLM"
}
const initlogiccard = {
    "input1" : '',
    "logicOperator" : '=',
    'input2': ''
}

$(document).ready(function () {
    $("#addItem").click(function () {
        $("#collapsePrework .card-body").append(addNewItem());
    });

    $(document).on('click', '.delete-button', function () {
        $(this).closest('.prework-item').remove();
    });

    $(document).on('keypress', '.form-control', function (e) {
        if (e.which === 13) {
            e.preventDefault();
            $(this).closest('.prework-item').after(addNewItem());
        }
    });

    $(document).on('click', '.confirm-button', function () {
        // 使用 jQuery 方法访问兄弟元素
        // $(this).siblings('.form-control').toggleClass('border-success');
        var checkIcon = $(this).children()
        checkIcon.each(function() {
            var currentDisplay = $(this).css('display');
            var newDisplay = currentDisplay === 'none' ? 'block' : 'none';
            $(this).css('display', newDisplay);
        });
        // 使用 jQuery 的 attr 方法获取和设置属性
        var data_output = $(this).attr("data-output") === "yes" ? "no" : "yes";

        $(this).attr("data-output", data_output);
    });

    $(document).on('click', '.output-button', function () {
        // 使用 jQuery 方法访问兄弟元素
        // $(this).closest('.worker-card').toggleClass('border-success');
        var checkIcon = $(this).children()
        checkIcon.each(function() {
            var currentDisplay = $(this).css('display');
            var newDisplay = currentDisplay === 'none' ? 'block' : 'none';
            $(this).css('display', newDisplay);
        });
        $(this).attr("data-output", $(this).attr("data-output") === "yes" ? "no" : "yes");
    });
});

// task分解后step和logic对应的卡片移动
document.addEventListener('DOMContentLoaded', function () {
  const cardContainer = document.getElementById('data-container');

  // Initialize Sortable on the card container
  let sortable = new Sortable(cardContainer, {
  group: "shared",
  animation: 150,
  onAdd: function (evt) {
      // Check if the dragged card is a task card or an If card
          if (evt.item.classList.contains('task-card') || evt.item.classList.contains('logic-card')) {
            // Get the parent If card
            const ifCardParent = evt.item.closest('.logic-card');

            // If the parent is an If card, append the dragged card header into it
            if (ifCardParent) {
              ifCardParent.querySelector('.card-body').appendChild(evt.item);
            }
          }
        },
    });
});
function updateJSON(key, value, modelIndex) {
    RunModelConfigs[modelIndex][key][0] = value;
}
function updateEngineJSON(key, value, modelIndex) {
    RunEngineConfigs[modelIndex][key][0] = value;
}

// config 参数信息， ModelId: 实时更新model, EngineId: save or import model 时指定Engine
function generateModelConfigForm(config, ModelId, EngineId) {
      const modelIndex = ModelId;
      const formHtml = `
          ${Object.entries(config).map(([key, value]) => {
            const id = key.replace(' ', '_') + "ModelId";
            if (key === 'stop_strs'){
              return `
                <div class="mb-3">
                  <label for="${id}" class="form-label">${value[1]}</label>
                  <input type="text" class="form-control" id="${id}" value="${value[0]}" oninput="updateJSON('${key}', this.value, '${modelIndex}')">
                </div>
                <hr>
              `;
            } else {
              return `
                <div class="mb-3">
                  <div class="d-flex justify-content-between">
                    <label for="${id}" class="form-label">${value[3]}</label>
                    <input type="number" class="form-control-range" id="${id}Value" value="${value[0]}" oninput="${id}.value=${id}Value.value; updateJSON('${key}', parseFloat(this.value), '${modelIndex}')">
                  </div>
                  <input type="range" class="form-range" min="0" max="${value[2]}" step="${value[1]}" id="${id}" value="${value[0]}" oninput="${id}Value.value=${id}.value;  updateJSON('${key}', parseFloat(this.value), '${modelIndex}')">
                </div>
                <hr>
              `;
            }
          }).join('')}
      `;
      document.getElementById('ModelContentDiv').innerHTML = `<div data-engine-id = '${EngineId}' data-model-id = '${ModelId}' style=";background-color: white;padding-left: 5px;display: block">
           <div class="mb-3">
              <h5 id="Engine_Name">` + ModelWorkspace.getBlockById(EngineId).getFieldValue('LLM_Name') +`</h5>
           </div>
           <hr>` + formHtml + '<\div>';
      document.getElementById('CreateModelDiv').style.height = 'calc(60% - 30px)';
      document.getElementById('ModelContentDiv').style.display = 'block';
      Blockly.svgResize(ModelWorkspace);
}

// generateModelConfigForm(Configuration1, 'initmodel')
function generateEngineConfigForm(config, ModelId, EngineId) {
      const modelIndex = ModelId
      const formHtml = `
          ${Object.entries(config).map(([key, value]) => {
            const id = 'Engine' + key.replace(' ', '_');
            if (key === 'stop_strs'){
              return `
                <div class="mb-3">
                  <label for="${id}" class="form-label">${value[1]}</label>
                  <input type="text" class="form-control" id="${id}" value="${value[0]}" oninput="updateEngineJSON('${key}', this.value, '${modelIndex}')">
                </div>
                <hr>
              `;
            } else {
              return `
                <div class="mb-3">
                  <div class="d-flex justify-content-between">
                    <label for="${id}" class="form-label">${value[3]}</label>
                    <input type="number" class="form-control-range" id="${id}Value" value="${value[0]}" oninput="${id}.value=${id}Value.value; updateEngineJSON('${key}', parseFloat(this.value), '${modelIndex}')">
                  </div>
                  <input type="range" class="form-range" min="0" max="${value[2]}" step="${value[1]}" id="${id}" value="${value[0]}" oninput="${id}Value.value=${id}.value;  updateEngineJSON('${key}', parseFloat(this.value), '${modelIndex}')">
                </div>
                <hr>
              `;
            }
          }).join('')}
      `;
      document.getElementById('EngineConsoleValue').innerHTML = `<div style=";background-color: white;padding-left: 5px;display: block">
            <br>` + formHtml + '<\div>';
}

function designSeparator() {
    const separator = document.getElementById('design-separator');
    const leftWrapper = document.getElementById('design-leftWrapper');
    let isMouseDown = false;

    separator.addEventListener('mousedown', (e) => {
        e.preventDefault();
        isMouseDown = true;
    });

    document.addEventListener('mousemove', (e) => {
        if (!isMouseDown) return;
        e.preventDefault();
        let newWidth = e.clientX - leftWrapper.offsetLeft;
        if (50<=newWidth) { // 设置左侧最小宽度防止变得太小
            leftWrapper.style.width = newWidth + 'px';
        }
    });

    document.addEventListener('mouseup', (e) => {
        isMouseDown = false;
    });
}
function exploreSeparator() {
    const separator = document.getElementById('explore-separator');
    const leftWrapper = document.getElementById('explore-leftWrapper');
    let isMouseDown = false;

    separator.addEventListener('mousedown', (e) => {
        e.preventDefault();
        isMouseDown = true;
    });

    document.addEventListener('mousemove', (e) => {
        if (!isMouseDown) return;
        e.preventDefault();
        let newWidth = e.clientX - leftWrapper.offsetLeft;
        if (newWidth >= 500) { // 设置左侧最小宽度防止变得太小
            leftWrapper.style.width = newWidth + 'px';
        }
    });

    document.addEventListener('mouseup', (e) => {
        isMouseDown = false;
    });
}

designSeparator()
exploreSeparator()
// localStorage.setItem('ProjectValues', JSON.stringify({}));

// var storedFile = localStorage.getItem('ProjectValues');
// if (storedFile) {
// const storedBlob = new Blob([storedFile], {type: 'application/json'});
// loadJsonFile(storedBlob);
//     storedFile = JSON.parse(storedFile);
//     console.log(storedFile[key])
//     for (var key in storedFile) {
//         initIDE();
//         ProjectValues[key] = storedFile[key]
//         upload_project1(key, storedFile[key]);
//     }
// }

