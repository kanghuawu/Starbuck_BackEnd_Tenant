var net = require('net')


var server = net.createServer(function (socket) {  
	// socket handling logic 
	var time = "";
	now = new Date()
	time = now.getFullYear()+"-"+(twoDigit(now.getMonth()+1))+"-"+twoDigit(now.getDate())+" "
		+twoDigit(now.getHours())+":"+twoDigit(now.getMinutes())+'\n'
	// console.log(time)
	socket.end(time)
})

function twoDigit(num){
	if (num < 10) {
		return "0"+num;
	}else{
		return num;
	}
}

server.listen(process.argv[2])  

/*
var net = require('net')

function zeroFill (i) {
  return (i < 10 ? '0' : '') + i
}

function now () {
  var d = new Date()
  return d.getFullYear() + '-' +
    zeroFill(d.getMonth() + 1) + '-' +
    zeroFill(d.getDate()) + ' ' +
    zeroFill(d.getHours()) + ':' +
    zeroFill(d.getMinutes())
}

var server = net.createServer(function (socket) {
  socket.end(now() + '\n')
})

server.listen(Number(process.argv[2]))

*/