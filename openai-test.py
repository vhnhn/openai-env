from openai import OpenAI
client = OpenAI()

def chat_with_openai(model, messages):
    completion = client.chat.completions.create(
      model=model,
      messages=messages
    )
    return completion.choices[0].message

def main():
    messages = [
        {"role": "system", "content": "You are helping me learning and building a python app. Write your responses with markdown compatibility."},
        {"role": "user", "content": "Hi."}
    ]
    model="gpt-3.5-turbo"

    while True:
        user_input = input(">>> You: ")

        if user_input.lower() == "!exit":
            print("Exiting the chat.")
            break
        elif user_input.lower() == "!set_model":
            new_model = input("Enter new model: ")
            model = new_model
        elif user_input.lower() == "!set_sys":
            new_system_content = input("Enter new system content: ")
            messages[0]["content"] = new_system_content
        elif user_input.lower() == "!append_sys":
            print("Current system content:", messages[0]["content"])
            new_system_content = input("Append to current system content: ")
            messages[0]["content"] += new_system_content
            print("New system content:", messages[0]["content"])
        elif user_input.lower() == "!print_sys":
            print("Current system content:", messages[0]["content"])
        else:
            messages.append({"role": "user", "content": user_input})
            print("***DEBUG***", user_input)
            response = chat_with_openai(model, messages)
            
            # Extract and print the AI's response
            print(">>>AI:", response.content)
            print()

if __name__ == "__main__":
    main()