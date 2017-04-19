var fs = require('fs')
var txt = fs.readFileSync(process.argv[2])
var ln = txt.toString().split('\n').length
if(ln > 0) {
	ln -= 1
}
console.log(ln)