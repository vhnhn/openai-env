# hello-openai
 Playing arround with open ai

# Chat with OpenAI Python Script

This Python script allows you to interact with the OpenAI GPT-3.5 Turbo model in a chat-like manner. You can have a conversation with the model by inputting messages, and the script uses the OpenAI API to generate responses.

## Prerequisites

- Python installed on your machine
- OpenAI API key

## Installation

1. **Clone the repository:**

    ```bash
    git clone https://github.com/your-username/your-repo.git
    ```

2. **Install the required dependencies:**

    ```bash
    pip install openai
    ```

3. **Set your OpenAI API key as a global variable.** You can do this by exporting it in your terminal:

    ```bash
    export OPENAI_API_KEY="your-api-key"
    ```

4. **Run the script:**

    ```bash
    python your_script_name.py
    ```

## Usage

- Type your messages in the command line and receive responses from the OpenAI GPT-3.5 Turbo model.
- Use the following special commands:
  - `!exit`: Exit the chat.
  - `!set_model`: Set a new model for the conversation.
  - `!set_sys`: Set a new system content for the conversation.
  - `!append_sys`: Append to the current system content.
  - `!print_sys`: Print the current system content.

## Example

```bash
>>> You: Hi.
>>>AI: Hello! How can I assist you today?

>>> You: !set_sys
Enter new system content: You are a helpful assistant providing information on various topics.

>>> You: What is the capital of France?
>>>AI: The capital of France is Paris.

>>> You: !exit
Exiting the chat.
```

Feel free to customize the script and README to better suit your needs!
