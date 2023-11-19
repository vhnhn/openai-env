from openai import OpenAI
client = OpenAI()

def image_with_openai(model, prompt, size, quality, n, style):
    response = client.images.generate(
      model=model,
      prompt=prompt,
      size=size,
      quality=quality,
      n=n,
      style=style
    )
    return response.data[0].url

def main():
    prompt = ""
    model="dall-e-3"
    size="1024x1024"
    quality="hd"
    n=1
    style = "vivid"

    while True:
        user_input = input(">>> Enter new picture prompt: ")

        if user_input.lower() == "!exit":
            print("Exiting the chat.")
            break
        if user_input.lower() == "!clear":
            prompt=""
            print("***DEBUG***", prompt)
        else:
            prompt += user_input
            print("***DEBUG***", prompt)
            response = image_with_openai(model, prompt, size, quality, n, style)
            
            # Extract and print the AI's response
            print(">>>AI:", response)
            print()

if __name__ == "__main__":
    main()