/*
 npm install url
*/
var url = require('url')
var http = require('http') 

var server = http.createServer(function (req, res) { 
	res.writeHead(200, { 'Content-Type': 'application/json' })
	if (req.method === 'GET' ) {
		parsed_url = url.parse(req.url, true)
		if (parsed_url.pathname === '/api/parsetime') {
			res.end(JSON.stringify(parseTime(parsed_url.query.iso)))
		}else if (parsed_url.pathname === '/api/unixtime') {
			res.end(JSON.stringify({'unixtime': new Date(parsed_url.query.iso).getTime()}))
		}else{
			res.end(JSON.stringify({'message':'wrong api'}))
		}
	}else{
		res.end(JSON.stringify({'message':'wrong method'}))
	}
})

function parseTime(time){
	var parsed = {}
	time = new Date(time)
	parsed['hour'] = time.getHours()
	parsed['minute'] = time.getMinutes()
	parsed['second'] = time.getSeconds()
	return parsed
}

server.listen(process.argv[2]) 

/*

var http = require('http')
var url = require('url')

function parsetime (time) {
  return {
    hour: time.getHours(),
    minute: time.getMinutes(),
    second: time.getSeconds()
  }
}

function unixtime (time) {
  return { unixtime: time.getTime() }
}

var server = http.createServer(function (req, res) {
  var parsedUrl = url.parse(req.url, true)
  var time = new Date(parsedUrl.query.iso)
  var result

  if (/^\/api\/parsetime/.test(req.url)) {
    result = parsetime(time)
  } else if (/^\/api\/unixtime/.test(req.url)) {
    result = unixtime(time)
  }

  if (result) {
    res.writeHead(200, { 'Content-Type': 'application/json' })
    res.end(JSON.stringify(result))
  } else {
    res.writeHead(404)
    res.end()
  }
})
server.listen(Number(process.argv[2]))
*/