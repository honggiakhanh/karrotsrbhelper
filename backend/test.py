from openai import OpenAI

# Point the OpenAI client at Ollama running on your computer
client = OpenAI(
    base_url="http://localhost:11434/v1",
    api_key="ollama",  # Ollama ignores this, but the library needs some value
)

response = client.chat.completions.create(
    model="llama3.2:3b",
    messages=[
        {"role": "system", "content": "You are a helpful assistant. Answer in 2-3 sentences."},
        {"role": "user", "content": "What is a trading card game?"},
    ],
)

print(response.choices[0].message.content)