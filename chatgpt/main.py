import openai
openai.api_key = "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"
while True:
    ask = input("robot:")
    response = openai.Completion.create(
        model = "text-davinci-003",
        prompt = ask,
        temperature=0.9,
        max_tokens=150,
        top_p=1,
        frequency_penalty=0.0,
        presence_penalty=0.6,
    )
    text = response['choices'][0]['text']
    print("robot:" + text)