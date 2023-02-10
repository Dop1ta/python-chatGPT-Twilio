import openai

# Define OpenAI API key 
openai.api_key = "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"
response = openai.Completion.create(
    engine = "text-davinci-003",
    prompt = 'cuanto es 2 mas 2',
    temperature = 0.6,
    max_tokens = 150
)



twr = response.choices[0].text
print(twr)