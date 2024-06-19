import sys
import openai
import json
import re
from gdclient import AsyncGDClient

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python connection.py <input_file>")
        sys.exit(1)
    
    html_description = sys.argv[1]

openai.api_base = "http://localhost:4891/v1"
#openai.api_base = "https://api.openai.com/v1"

openai.api_key = "not needed for a local LLM"

# Set up the prompt and other parameters for the API request
prompt = """You are a software developer.Your task is to generate workable code in Groovy programming language. Code description would be given below
But there are several limitations that should be considered:
1. There are no variable type definitions. All of the data types for variables which are defined first time in the code should be replaced with 'def' (but values should not).
Example in Groovy:
'
int a:= 4
int b:= 5
return a+b'
Example with a limitation: '
def a= 4
def b= 5
return a+b
'
2. Any new variable should be defined with 'def=' as well
Example in Groovy:
'
res = a*b
'
Example with a limitation: '
def res=a*b
'
3. Replace all 'println', 'print' and etc. functions with 'printout'
Example in Groovy: 'println(a)'
Example with a limitation: 'printout(a)'
4. There are no hand-written functions. Just write in the main block of code
Example in Groovy: '
def add(int x, int y) {
return x + y
} '
Example with a limitation:
'def x
def y
return x+y
'
5. You can't put several functions into a variable, such as 'printout'
Example in groovy:
'
def e
def summarize += printout("e: ") + e + printout(", ")
'
Example with a limitation:
'
def e
printout("e: " + e + ", ")
'
6. If there is a need to do some actions with already defined variables, you should not write them with a 'def' prefix because they are already defined
7. You mustn't add 'import' methods
Example in Groovy:
'
import java.util.*
'
8. You mustn't add any additional words or lines these are not used in code compilation
Example:
'
groovy
'
9. If you are using 'return' function you mustn't use any function inside of it
Example in Groovy:
'
return printout("Sum: ") + (e+r)
'
Example with a limitation:
'
return "Sum: " + (e+r)
'
Now, taking these limitations into consideration, make an example of the Groovy code, that will firstly print 'Hello world' and then returning multiplication of values of the 'rav' and 'var' variables. Put into 'rav' and 'var' any value
"""

# model = "gpt-3.5-turbo"
#model = "mpt-7b-chat"
model = "Meta-Llama-3-8B-Instruct.Q4.0.gguf"

# Make the API request
response = openai.Completion.create(
    model=model,
    prompt=prompt,
    max_tokens=4096,
    temperature=0.70,
    top_p=0.4,
    n=1,
    echo=True,
    stream=False
)

# Print the generated completion
json_dump = json.dumps(response)
data_json = json.loads(json_dump)
text_str = data_json['choices'][0]['text']

def extract_groovy_code(text_str):
    # Define the regex pattern to match the Groovy code enclosed between ```
    pattern = r'```(?:.*?\n)?(.*?)```'

    # Find the first match of the pattern in the input string
    match = re.search(pattern, text_str, re.DOTALL)

    if match:
        # Extract the matched Groovy code
        groovy_code = match.group(1).strip()
        return groovy_code
    else:
        return "No Groovy code found."

groovy_code = extract_groovy_code(text_str)
print(groovy_code)
