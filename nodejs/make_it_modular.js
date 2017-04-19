/*
reference: http://stackoverflow.com/questions/35542194/learnyounode-6-make-it-modular-correct-results-and-throwing-error-at-the-same
*/

var path = require('path');
var mymodule = require('./module/mymodule');
var dir = process.argv[2];
var filterExtension = process.argv[3];

var callback = function (err, list) {
    if (err) throw err;
    list.forEach(function (file) {
        console.log(file);
    })
}

mymodule(dir, filterExtension, callback);