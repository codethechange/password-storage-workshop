require('dotenv').config()

const express = require('express');
const http = require('http');
const multer = require('multer')
const app = express();
const upload = multer()

const { Pool, Client } = require('pg')

// pools will use environment variables
// for connection information
const pool = new Pool()

app.get('/', (req, res) => res.status(200).send(`
    <html>
        <body>
        <form id="myForm" action="javascript:;" onsubmit="sendRequest(this)">
            <label for="username">Username: </label><input style="width:400px" type="text" name="username"/><br>
            <label for="password">Password: </label><input style="width:400px" type="text" name="password"/><br>
            <button type="submit">Login</button>
        </form>
        <div id="response">
        </div>
        <script>
        function sendRequest(){
            var xhr = new XMLHttpRequest();
            xhr.open("POST", "/send-request"); 
            xhr.onload = function(event){ 
                res = JSON.parse(event.target.response)
                console.log(res)
                document.getElementById("response").innerHTML = res.length > 0 ? 'You are signed in as ' + res[0].username : 'Invalid password'
            }; 
            // or onerror, onabort
            var formData = new FormData(document.getElementById("myForm")); 
            xhr.send(formData);
        }
        </script>
        </body>
    </html>
`));

app.post('/send-request', upload.single('proposal'), (req, res) => {
    pool.query(`SELECT username FROM table_name WHERE username='` + req.body.username + `' AND password='` + req.body.password + `';`, (err, res2) => {
        res.send(err ? err : res2.rows)
    })
})

const port = 80;
app.set('port', port);
const server = http.createServer(app);
server.listen(port);
