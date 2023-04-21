/*
----------------------------------------------------------------------------
Project Name: [Sapper IDE]
File: [index.js]
Copyright (C) [2023] [Prompt Sapper]
License: [Creative Commons Attribution-NonCommercial-NoDerivatives 4.0 International License]
----------------------------------------------------------------------------
This file is part of [Sapper IDE].
[Sapper IDE] is free software: you can redistribute it and/or modify
it under the terms of the Creative Commons Attribution-NonCommercial-NoDerivatives 4.0 International License as published by
the Creative Commons Corporation, either version 4.0 of the License,
or (at your option) any later version.
[Sapper IDE] is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
Creative Commons Attribution-NonCommercial-NoDerivatives 4.0 International License for more details.
You should have received a copy of the Creative Commons Attribution-NonCommercial-NoDerivatives 4.0 International License
along with [Sapper IDE]. If not, see https://creativecommons.org/licenses/by-nc-nd/4.0/legalcode.
----------------------------------------------------------------------------
*/
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
      media: '../static/media/',
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
    media: '../static/media/',
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
      media: '../static/media/',
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
    "DesignManager":'',
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
// document.getElementById("taskNodeDisplay").value = DesignManager
// initIDE();
// upload_project1("chatbot",ChatBot)
//
// upload_project1("todos2pic",todos2pic)
// initIDE();

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
    // Make the div draggable


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
        if (5<=newWidth) { // 设置左侧最小宽度防止变得太小
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
        if (newWidth >= 5) { // 设置左侧最小宽度防止变得太小
            leftWrapper.style.width = newWidth + 'px';
        }
    });

    document.addEventListener('mouseup', (e) => {
        isMouseDown = false;
    });
}

designSeparator()
exploreSeparator()
