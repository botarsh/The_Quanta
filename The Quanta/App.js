var express = require("express");
const path = require('path');
const {spawn} = require('child_process');
var app = express();
app.listen(3000,function(){
  console.log("hgfeiuafh");
  });
  
  app.get('/',function(req,res) {
    res.render('./project/index.html');
  });

  function runScript(){
    return spawn('python', [
      "-u", 
      path.join(__dirname, 'send_sms.py')
    ]);
  }
  
  
  

const subprocess = runScript()


  
  /*
  function runScript(){
    return spawn('python', [
      "-u", 
      path.join(__dirname, 'multiple.py')
    ]);
  }
  
*/



  /* 
function runScript(){
  return spawn('python', [
    "-u", 
    path.join(__dirname, 'send_sms1.py')
  ]);
}

function runScript(){
  return spawn('python', [
    "-u", 
    path.join(__dirname, 'send_sms.py')
  ]);
}*/