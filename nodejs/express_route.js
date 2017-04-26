/*
reference: http://qnimate.com/express-js-middleware-tutorial/
*/

var app = require("express")();

app.get("/", function(httpRequest, httpResponse, next){
    httpResponse.write("Hello");
    // next(); //remove this and see what happens 
});

app.get("/", function(httpRequest, httpResponse, next){
    httpResponse.write(" World !!!");
    httpResponse.end();
});

app.listen(8080);