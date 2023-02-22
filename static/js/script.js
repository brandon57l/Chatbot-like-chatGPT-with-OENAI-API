

message = (function () {
    var self = {}
    var msg_container = document.getElementById('msg-container')
    var user_input = document.getElementById('text')
    var prompt


    self.init = function (){
        window.localStorage.setItem("prompt", "Conseillé: Bonjour et bienvenue au Le Karousel. Je suis votre conseiller virtuel, prêt à vous aider à faire le meilleur choix parmi nos plats et boissons. Qu'aimeriez-vous manger aujourd'hui? Vous pouvez me dire ce que vous avez envie de manger ou me poser des questions sur nos plats et nos boissons.");
        prompt = window.localStorage.getItem("prompt")
        msg_container.scrollTop = msg_container.scrollHeight

    }

    self.getPrompt = function (){
        return prompt
    }

    self.setPrompt = function (newPrompt){
        prompt = newPrompt
        return 
    }

    self.newMessage = function (){       
               
        new_div_msg = document.createElement("div")
        new_div_msg.className = "msg-right"
        new_div_msg.innerHTML = user_input.value

        msg_container.appendChild(new_div_msg)

        window.localStorage.setItem("prompt",prompt+"\nClient: "+user_input.value)
        
    }

    self.response = function (res){

        new_div_msg = document.createElement("div")
        new_div_msg.className = "msg-left"
        new_div_msg.innerHTML = res.chatbot_response
        console.log(res)

        msg_container.appendChild(new_div_msg)

        window.localStorage.setItem("prompt",prompt+"\nConseillé: "+res.chatbot_response)
        prompt = window.localStorage.getItem("prompt")


    }
    return self
})()


// function submitForm(event) {
//     event.preventDefault();
//     // your form submission logic here
//     console.log("hello")
// }

function fetchData (event){
    event.preventDefault();
    message.setPrompt(window.localStorage.getItem("prompt")+"\n"+"Client: "+document.getElementById('text').value)
    console.log('in fetch')
    $.ajax({
    url: "/chatbot/",
    type: 'POST',
    data: {
        text: $("#text").val(),
        storage_prompt: message.getPrompt(),
      },
    beforeSend: function() {
        message.newMessage()
     },
    success: function(data) {
        console.log(data);
        message.response(data)
        var msg_container = document.getElementById('msg-container')
        msg_container.scrollTop = msg_container.scrollHeight
    }
    })

}


// Ready function

message.init();

