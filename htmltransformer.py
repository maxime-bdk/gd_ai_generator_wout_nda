import sys
import openai
import json
import re

def read_file_content(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        #print(file.read())
        return file.read()

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python connection.py <input_file>")
        sys.exit(1)
    
    input_file = sys.argv[1]
    prompt = read_file_content(input_file)

openai.api_base = "http://localhost:4891/v1"
#openai.api_base = "https://api.openai.com/v1"

openai.api_key = "not needed for a local LLM"
perem = read_file_content('output.html')

# Set up the prompt and other parameters for the API request
prompt = perem

# model = "gpt-3.5-turbo"
#model = "mpt-7b-chat"
model = "Meta-Llama-3-8B-Instruct.Q4.0.gguf"

# Make the API request
response = openai.Completion.create(
    model=model,
    prompt=prompt,
    max_tokens=200,
    temperature=0.28,
    top_p=0.95,
    n=1,
    n_ctx=2048,
    echo=True,
    stream=False
)

# Print the generated completion
print(response)
json_dump = json.dumps(response)
print(json.dumps(response))
data_json = json.loads(json_dump)
text_str = data_json['choices'][0]['text']

def resend_text(text_str):
    return text_str

func_call = resend_text(text_str)