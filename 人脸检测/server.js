var express = require('express');
var app = express();

app.use(express.static('public'));

app.get('/form.html', function (req, res) {
   res.sendFile( __dirname + "/" + "form.html" );
})

app.get('/process_post', function (req, res) {

   // 输出 JSON 格式
   // var jso = {
   //     "first_name":req.body.first_name,
   //     "last_name":req.body.last_name
   // };
   // console.log(jso);
   res.send("JSON.stringify(jso)");
})





var server = app.listen(8081, function () {
 
  var host = server.address().address
  var port = server.address().port
 
  console.log("服务器成功")
 
})