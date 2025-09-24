# Pirate Chat Application – AI-Ready Requirements

## Purpose
Create a chat application where a user communicates with a pirate chatbot.

## User Flow
1. The pirate bot starts the conversation with a greeting and invites the user to ask a question.  
2. The user types a message.  
3. The message is sent to the backend server for translation into “pirate language.”  
4. Once the translation is received, it is displayed in the chat.  
5. The translated message is then sent to the backend server to get a response from the pirate bot.  
6. The pirate bot’s response is displayed in the chat.  
7. The chat should remember the full conversation history, which is visible on screen.

## Frontend
- **Technology:** Vanilla JavaScript  
- **UI Elements:**  
  - Title: **“Ask a Pirate”**  
  - Chat window that shows conversation history  
  - Input field for user prompts  
- **Status Messages:**  
  - **“Translating…”** while waiting for translation  
  - **“Thinking…”** while waiting for pirate response  
- **Style:** Pirate-themed  
- **Backend Polling:** Frontend polls the backend for translation and pirate response (no WebSockets).

## Backend
- **Technology:** Python with FastAPI  
- **Endpoints:**  
  1. `/translate` – Receives a message and returns it translated into pirate language. *(Initially, just return the original message as a placeholder.)*  
  2. `/pirate-response` – Receives a message and returns a pirate bot response. *(Initially, return placeholder text.)*

## Additional Requirements
- Single pirate response per user message.  
- Chat conversation history must be preserved and displayed on screen.
