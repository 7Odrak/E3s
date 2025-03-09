import ollama

print(ollama.chat("", [{"role": "user", "content": ""}]['message']['content']))
