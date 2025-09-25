class PirateChat {
    constructor() {
        this.chatMessages = document.getElementById('chat-messages');
        this.userInput = document.getElementById('user-input');
        this.sendButton = document.getElementById('send-button');
        this.statusMessage = document.getElementById('status-message');

        this.init();
    }

    init() {
        this.sendButton.addEventListener('click', () => this.sendMessage());
        this.userInput.addEventListener('keypress', (e) => {
            if (e.key === 'Enter') {
                this.sendMessage();
            }
        });

        this.startConversation();
    }

    startConversation() {
        this.addMessage('pirate', "Ahoy there, matey! Welcome to the pirate ship! What be on yer mind today?");
        this.enableInput();
    }

    enableInput() {
        this.userInput.disabled = false;
        this.sendButton.disabled = false;
        this.userInput.focus();
    }

    disableInput() {
        this.userInput.disabled = true;
        this.sendButton.disabled = true;
    }

    showStatus(message) {
        this.statusMessage.textContent = message;
    }

    clearStatus() {
        this.statusMessage.textContent = '';
    }

    addMessage(sender, message) {
        const messageDiv = document.createElement('div');
        messageDiv.className = `message ${sender}`;

        const senderDiv = document.createElement('div');
        senderDiv.className = 'sender';
        senderDiv.textContent = sender === 'user' ? 'You' : 'Pirate';

        const contentDiv = document.createElement('div');
        contentDiv.className = 'content';
        contentDiv.textContent = message;

        messageDiv.appendChild(senderDiv);
        messageDiv.appendChild(contentDiv);

        this.chatMessages.appendChild(messageDiv);
        this.chatMessages.scrollTop = this.chatMessages.scrollHeight;
    }

    async sendMessage() {
        const message = this.userInput.value.trim();
        if (!message) return;

        this.addMessage('user', message);
        this.userInput.value = '';
        this.disableInput();

        try {
            this.showStatus('Translating...');

            const translateResponse = await fetch('/translate', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                },
                body: JSON.stringify({ message: message })
            });

            if (!translateResponse.ok) {
                throw new Error('Translation failed');
            }

            const translateData = await translateResponse.json();
            const translatedMessage = translateData.translated_message;

            this.showStatus('Thinking...');

            const pirateResponse = await fetch('/pirate-response', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                },
                body: JSON.stringify({ message: translatedMessage })
            });

            if (!pirateResponse.ok) {
                throw new Error('Pirate response failed');
            }

            const pirateData = await pirateResponse.json();
            this.addMessage('pirate', pirateData.response);

        } catch (error) {
            console.error('Error:', error);
            this.addMessage('pirate', 'Arrr, the seas be rough and I be having trouble understanding ye!');
        } finally {
            this.clearStatus();
            this.enableInput();
        }
    }
}

document.addEventListener('DOMContentLoaded', () => {
    new PirateChat();
});