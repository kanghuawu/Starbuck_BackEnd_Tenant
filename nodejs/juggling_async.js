/*
npm install bl
*/

var bl = require('bl');
var http = require('http');
var result = [];
var item = 0;

function req(link, next) {
	http.get(link, function(res){
		res.pipe(bl(function(error, data){
			if(error) {
				console.log(error);
			}
			result[item] = data.toString();
			item ++;
			next()
		}))
	
	})
}

function req1() {
	req(process.argv[3], req2)
}

function req2() {
	req(process.argv[4], print)
}

function print() {
	result.forEach(function(str){
		console.log(str)
	})
	
}

req(process.argv[2], req1 ) 



/* 
var http = require('http')
var bl = require('bl')
var results = []
var count = 0

function printResults () {
  for (var i = 0; i < 3; i++) {
    console.log(results[i])
  }
}

function httpGet (index) {
  http.get(process.argv[2 + index], function (response) {
    response.pipe(bl(function (err, data) {
      if (err) {
        return console.error(err)
      }

      results[index] = data.toString()
      count++

      if (count === 3) {
        printResults()
      }
    }))
  })
}

for (var i = 0; i < 3; i++) {
  httpGet(i)
}

*/

/*
const http = require('http')
const bl = require('bl')
const source = process.argv.slice(2)
var count = 0
var content = []
function printContent() {
    for (var i = 0; i < content.length; i++) {
        console.log(content[i])
    }
}
function getContent(source, index) {
    http.get(source[index], function(response) {
        response.pipe(bl(function (error, data) {
            if (error) {
                return console.error(error)
            }
            content[index] = data.toString();
            if (++count == source.length) {
                printContent();
            }
        }))
    })
}
for (var i = 0; i < source.length; i++) {
    getContent(source, i)
}
*/