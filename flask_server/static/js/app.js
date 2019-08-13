var editor = ace.edit("editor");
editor.setTheme("ace/theme/twilight");
editor.session.setMode("ace/mode/python");

function sendCode(){
  document.getElementById("outputArea").value = "";
  document.getElementById("errorArea").value = "";
//  code =  document.getElementById("codeArea").value;
  code = editor.getValue();
  in_data = document.getElementById("inputArea").value;
  timeout = document.getElementById("TOvalue").value;
  if (isNaN(timeout)){
    alert("Timeout is not a number!");
    return;
  }
  data = JSON.stringify({"code": code, "input": in_data, "timeout": timeout})
  console.log(data);
  $.ajax({
      type:'post',
      contentType: "application/json",
      data: data,
      url: "FlaskServer/",
      cache:false,
      async:'asynchronous',
      dataType:'json',
      success: function(data) {
         console.log(JSON.stringify(data));
         document.getElementById("outputArea").value = data["output"];
         document.getElementById("errorArea").value = data["error"];
      },
      error: function(request, status, error) {
        console.log("Error: " + error)
      }
   });
}