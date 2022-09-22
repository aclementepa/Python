var http = require('http');
var dt = require('./module1');
var url = require('url');
var fs = require('fs');
var rs = fs.createReadStream('./newfile1.txt');
var uc = require('upper-case');


//http.createServer(function (req, res) {
    // res.writeHead(200, {'Content-Type': 'text/plain'});
    
    // res.write('Hello World!');
    // res.write("The date and time are currently: " + dt.myDateTime());

    // search url: /winter
    // res.write(req,.url);
    
    //search url: /?year=2017&month=July
    //var q = url.parse(req.url, true).query;
    //var txt = q.year + " " + q.month;
    //res.write(txt)

    //res.end();

    //read an html file and display to webpage
    /*fs.readFile('demo1.html', function(err, data) {
        res.writeHead(200, {'Content-Type': 'text/html'});
        res.write(data);
        return res.end();
    });
    */

    // File Creation

    /*
    fs.appendFile('newfile1.txt', 'Hello content!', function(err) {
        if (err) throw err;
        console.log('Saved!');
        // or update
        // console.log('Updated!');
    });
    
    fs.open('newfile2.txt', 'w', function(err, file) {
        if (err) throw err;
        console.log('Saved!');
        // or update
        // console.log('Replaced!');
    })
    */
    //delete files
    /*
    fs.unlink('newfile2.txt', function(err) {
        if (err) throw err;
        console.log('File deleted!');
    })
    */

    // Split a web address into readable parts
    /*
    var adr = 'http://localhost:8080/default.htm?year=2017&month=february';
    var q = url.parse(adr, true)

    console.log(q.host); //returns 'localhost:8080'
    console.log(q.pathname); //returns '/default.htm'
    console.log(q.search); //returns '?year=2017&month=february'

    var qdata = q.query; //returns an object: {year: 2017, month: 'february'}
    console.log(qdata.month); //returns february
    */

    // Serve a webpage based on the path
    /*
    var q = url.parse(req.url, true);
    var filename = "." + q.pathname;
    fs.readFile(filename, function(err, data) {
        if (err) {
        res.writeHead(404, {'Content-Type': 'text/html'});
        return res.end("404 Not Found");
        } 
        res.writeHead(200, {'Content-Type': 'text/html'});
        res.write(data);
        return res.end();
    });
    */

   // Uppercase "Hello World!"
    /*
    res.writeHead(200, {'Content-Type': 'text/plain'});
    res.write(uc.upperCase("Hello World!"));
    res.end();
    */

//}).listen(8080);

// Create an event (opening & closing a file)
/*
rs.on('open', function() {
    console.log("The file is open");
});
*/
/*
var events = require('events');
var eventEmitter = new events.EventEmitter();

// Create event handler
var myEventHandler = function () {
    console.log('I hear a scream!');
}

// Assign the event handler to an event
eventEmitter.on('scream', myEventHandler);

// Fire the 'scream' event
eventEmitter.emit('scream');

*/
/*
// File uploads

var formidable = require('formidable');
// Creating an upload form


http.createServer(function (req, res) {
    res.writeHead(200, {'Content-Type': 'text/html'});
    res.write('<form action="fileupload" method="post" enctype="multipart/form-data">');
    res.write('<input type="file" name="filetoupload"><br>');
    res.write('<input type="submit">');
    res.write('</form>');
    return res.end();
}).listen(8080);
*/