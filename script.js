function sendMessage() {
    let userInput = document.getElementById('user-input').value;
    if (userInput.trim() === "") return;

    let chatBox = document.getElementById('chat-box');
    let userMessage = document.createElement('div');
    userMessage.textContent = "User: " + userInput;
    chatBox.appendChild(userMessage);

    document.getElementById('user-input').value = "";

    fetch('http://localhost:5000/get_response', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({ message: userInput })
    })
    .then(response => response.json())
    .then(data => {
        let botMessage = document.createElement('div');
        botMessage.textContent = "Infinibot: " + data.response;
        chatBox.appendChild(botMessage);
    })
    .catch(error => {
        console.error('Error:', error);
    });
}
