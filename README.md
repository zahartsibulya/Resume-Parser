# Telegram Bot & Resume Parser

An automated CV screening system that uses LLMs (Llama 3 via Groq API) to evaluate candidates against job requirements, providing instant feedback via Telegram and logging results to Google Sheets.

## Key Features
* **AI-Powered Parsing:** Extracts structured data (skills, experience, english level) from raw text resumes.
* **Automated Scoring:** Calculates a Match Score based on specific job requirements.
* **Microservice Architecture:** Built using **Clean Architecture** principles (separated Domain, Infrastructure, and Use Cases).
* **No-Code Orchestration:** Integrates with Telegram and Google Sheets via **n8n**.
* **Fast Response Time:** Uses the ultra-fast Groq API for near-instant inference.

## Tech Stack
* **Backend:** Python 3, Flask
* **Architecture:** Clean Architecture, REST API
* **AI/LLM:** Groq API (Llama-3.1-8b-instant)
* **Orchestration:** n8n (Webhooks, Logic Routing)
* **Integrations:** Telegram API, Google Sheets API
* **Environment:** Ngrok for local tunneling

## How it Works (Architecture Flow)
1.  Candidate sends a text resume to the Telegram Bot.
2.  **n8n** receives the webhook and routes the request.
3.  **Flask Microservice** receives the text, parses it via Groq API, evaluates the candidate, and returns a JSON Data Transfer Object (DTO).
4.  **n8n** logs the candidate's data (Name, Score, Status) to a Google Sheet.
5.  **n8n** sends a formatted assessment report back to the candidate in Telegram.

## Local Setup Instructions
1. Clone the repository.
2. Install dependencies: `pip install -r requirements.txt`
3. Create a `.env` file and add your API key:
   `GROQ_API_KEY=your_key_here`
4. Run the server: `python app.py`
5. (Optional) Expose your local server using ngrok: `ngrok http 5000`
6. Set up your n8n workflow to point to your ngrok URL.

## Limitations & Edge Cases
* **Format:** Currently supports raw text input. PDF/Word support is planned for future iterations.
* **AI Hallucinations:** As with any LLM, edge cases exist where the model might infer a skill not explicitly stated. The system is designed to minimize this via a strict `SYSTEM_PROMPT` and `temperature=0.1`.




<img width="659" height="487" alt="image" src="https://github.com/user-attachments/assets/4d43abb9-f9be-4a9f-9a9c-61df4561c365" />
<img width="749" height="252" alt="image" src="https://github.com/user-attachments/assets/fcecd001-685f-4b07-9be0-1fca5379473f" />
<img width="442" height="191" alt="image" src="https://github.com/user-attachments/assets/49dca53c-0aed-4bc1-a89c-f0e5be1756f8" />


