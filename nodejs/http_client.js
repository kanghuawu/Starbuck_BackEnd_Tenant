var http = require('http')
var link = process.argv[2]

http.get(link, function(res){
	res.setEncoding('utf8');
	res.on('data', function(chunk){
		console.log(chunk)
	})
})
