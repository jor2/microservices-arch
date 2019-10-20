var express = require('express');
var app = express();

app.get('*', (req, res) => {
   res.send(JSON.stringify("Hello World! - from javascript api..."));
})

var server = app.listen(4000, function () {

  var host = server.address().address
  var port = server.address().port

  console.log("Node.js API app listening at http://%s:%s", host, port)
})