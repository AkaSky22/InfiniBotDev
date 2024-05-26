function sendMessage() {
    var userInput = document.getElementById("userInput").value;
    var chatbox = document.getElementById("chatbox");
    
    var userMessage = document.createElement("div");
    userMessage.innerText = "You: " + userInput;
    chatbox.appendChild(userMessage);

    // Placeholder for bot response
    var botMessage = document.createElement("div");
    botMessage.innerText = "ROBO: ...";  // Replace this with actual bot response
    chatbox.appendChild(botMessage);

    document.getElementById("userInput").value = "";
    chatbox.scrollTop = chatbox.scrollHeight;  // Scroll to bottom
}
