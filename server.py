import requests
# This is a mock-up function; you'll need to implement it according to your actual API client code.
def send_request_to_server(data):
    url = 'http://127.0.0.1:8080'  # Make sure this matches the server's IP and port
    response = requests.post(url, json=data)
    return response.json()

# Assuming `runner.send_chat_completion_request` sends a request to the server:
res = send_request_to_server({
    "model": "mistral",
    "messages": [{"role": "user", "content": "Tell me a story about the Rust type system."}],
    "max_tokens": 256,
    "presence_penalty": 1.0,
    "top_p": 0.1,
    "temperature": 0.1,
})
print(res['choices'][0]['message']['content'])
print(res['usage'])
