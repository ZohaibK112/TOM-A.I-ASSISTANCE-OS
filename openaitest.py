import requests
import pywhatkit as kit 

def find_my_ip():
    ip_address = requests.get('https://api.ipify.org?format=json').json()
    return ip_address['ip']

def youtube(query):
    kit.playonyt(query)  # Play on YouTube

def search_on_google(query):
    kit.search(query)  # Perform a Google search




# response = openai.ChatCompletion.create(
#     model="gpt-4",
#     messages=[
#         {"role": "system", "content": "You are a helpful assistant."},
#         {"role": "user", "content": "Write an email to my boss for resignation."}
#     ],
#     temperature=1,
#     max_tokens=256,
#     top_p=1,
#     frequency_penalty=0,
#     presence_penalty=0
# )

# print(response['choices'][0]['message']['content'])
