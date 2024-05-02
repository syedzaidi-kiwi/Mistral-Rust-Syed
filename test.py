from mistralrs import Runner, Which, ChatCompletionRequest

runner = Runner(
    which=Which.GGUF(
        tok_model_id="mistralai/Mistral-7B-Instruct-v0.1",
        quantized_model_id="TheBloke/Mistral-7B-Instruct-v0.1-GGUF",
        quantized_filename="mistral-7b-instruct-v0.1.Q4_K_M.gguf",
        tokenizer_json=None,
        repeat_last_n=64,
    )
)

try:
    res = runner.send_chat_completion_request(
        ChatCompletionRequest(
            model="mistral",
            messages=[{"role":"user", "content":"What is Artificial Intelligence?."}],
            max_tokens=256,
            presence_penalty=1.0,
            top_p=0.1,
            temperature=0.1,
        )
    )
    print(res.choices[0].message.content)
    print(res.usage)
except Exception as e:
    print(f"An error occurred: {e}")
