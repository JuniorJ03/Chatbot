💬 GPT-3.5 Turbo Chatbot
A simple Python chatbot using OpenAI's gpt-3.5-turbo model.

📦 Requirements
Python 3.7+

openai Python package

Install the OpenAI Python package:

bash
Copy
Edit
pip install openai
🔑 Setup
Get your API key from https://platform.openai.com/account/api-keys

Replace "sk-" in the script with your actual secret key:

python
openai.api_key = "sk-your-api-key"
🚀 How to Run
Save the script as chat.py, then run it in your terminal:

bash
python chat.py
Type your messages, and GPT will respond. To exit, type:

bash
Copy
Edit
exit
or

nginx
Copy
Edit
quit

vbnet
Copy
Edit
You: Hello!
GPT: Hello! How can I help you today?

You: What's the capital of France?
GPT: The capital of France is Paris.

You: quit
Exiting chat.
⚠️ Notes
This script uses the older OpenAI SDK method (openai.ChatCompletion.create) which only works with openai < 1.0.0.

To use the latest SDK, see the updated version here.
