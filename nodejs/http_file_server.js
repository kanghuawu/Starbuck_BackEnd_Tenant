var http = require('http') 
var fs = require('fs')
var dir = process.argv[3]

var server = http.createServer(function (req, res) { 
	var stream = fs.createReadStream(dir)
	stream.pipe(res)
})

server.listen(process.argv[2])  

/*
var http = require('http')
var fs = require('fs')

var server = http.createServer(function (req, res) {
  res.writeHead(200, { 'content-type': 'text/plain' })

  fs.createReadStream(process.argv[3]).pipe(res)
})

server.listen(Number(process.argv[2]))
*/