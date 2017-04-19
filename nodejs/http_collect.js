/*
npm install bl
*/

var bl = require('bl')
var http = require('http')
var link = process.argv[2]
http.get(link, function(res){
	res.pipe(bl(function(error, data){
		if(error) console.log(error)
		console.log(data.toString().length)
		console.log(data.toString())
	}))
})
