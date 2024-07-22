document.querySelector('.message-input button').addEventListener('click', function() {
    const input = document.querySelector('.message-input input');
    const messageText = input.value.trim();
    
    if (messageText !== '') {
        const chatMessages = document.querySelector('.chat-messages');
        const newMessage = document.createElement('div');
        newMessage.classList.add('message', 'sent');
        newMessage.innerHTML = `<p>${messageText}</p>`;
        chatMessages.appendChild(newMessage);
        
        input.value = '';
        chatMessages.scrollTop = chatMessages.scrollHeight;
    }
});
