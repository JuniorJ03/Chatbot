import openai

openai.api_key = "sk-"

def chat_with_gpt(prompt):
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "user", "content": prompt}
            ]
        )
        return response.choices[0].message()

if __name__ == "__main__":
        while True:
            user_input = input("You: ")
            if user_input.lower() in ["exit", "quit"]:
                print("Exiting chat.")
                break
            response = chat_with_gpt(user_input)
            print(f"GPT: {response}")