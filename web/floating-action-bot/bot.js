let status = document.getElementById('status');
window.onload = function(){
    fetch('http://localhost:5004/status',{
        method:'GET'
    })
    .then(function(response){
        status.innerHTML = "<i class='fas fa-circle'></i> Online";
    })
    .catch(function(response){
        status.innerHTML = "<i class='fas fa-circle' style='color:red'></i> Offline";
    })
}


let chatbox = document.getElementById('main-box');
chatbox.style.display = "none"
function openchat() {
    chatbox.style.display = "block"
}
function closechat() {
    chatbox.style.display = "none"
}


let id = Math.floor(Math.random() * 1000 + 1);
console.log(id)
let ul = document.getElementById('conversation');
var chat = document.getElementById("chat-container");

function send() {
    let msg = document.getElementById('chat-input').value;
    let li = document.createElement('li');
    li.appendChild(document.createTextNode(msg));
    li.className = "sender"
    ul.appendChild(li);
    respond(msg);
    document.getElementById('chat-input').value = "";
    chat.scrollTop = chat.scrollHeight;
}
function respond(msg) {
    data = {
        query: msg,
        id: id
    }
    fetch(`http://localhost:5004/respond`, {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify(data)
    })
        .then(function (response) {
            return response.json();
        })
        .then(function (data) {
            console.log(data);
            if (data[0]) {
                for(let d of data){
                    let li = document.createElement('li');
                    li.innerHTML = d;
                    li.className = 'responder';
                    ul.appendChild(li)
                    chat.scrollTop = chat.scrollHeight;
                }
            }
            else {
                let li = document.createElement('li');
                let t = document.createTextNode("Sorry, I'm having technical issues");
                li.className = 'responder';
                li.appendChild(t)
                ul.appendChild(li)
                chat.scrollTop = chat.scrollHeight;
            }

        })
        .catch(function (err) {
            let li = document.createElement('li');
            let t = document.createTextNode("I'm having some technical issues. Try again later :)");
            li.className = 'responder';
            li.appendChild(t)
            ul.appendChild(li)
            chat.scrollTop = chat.scrollHeight;
        });

}
var input = document.getElementById("chat-input");
input.addEventListener("keyup", function (event) {
    event.preventDefault();
    if (event.keyCode === 13) {
        document.getElementById("btn").click();
    }
});