'use strict';

var express = require('express');
var app = express();

app.get('/', function (req, res) {
   res.writeHead(200, {'Content-Type': 'application/json'});
   res.end(JSON.stringify("Hello World!"));
})

var server = app.listen(4000, function () {

  var host = server.address().address
  var port = server.address().port

  console.log("Node.js API app listening at http://%s:%s", host, port)

})