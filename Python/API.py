# 활용

# 라이브러리 설치
# pip install requests
import requests

# 1. 이메일 보내기

# def send_email():
#     api_url = "http://wonieschool.com/api/email"
#     payload = {
#         'to' : "", # emial-adress
#         'subject' : "Hello!!",
#         'body' : "It is just E-mail.",    
#     }
#     api_key = "" # API-KEY
#     headers = {
#         'X-Authorization': f"Bearer {api_key}"
#     }

#     response = requests.post(api_url, json= payload, headers=headers)

#     if response.status_code == 200:
#         print(response.json())
#     else:
#         print(response.text)

# send_email()

# 2. AI와 대화하기

# def chat_with_ai():
#     api_url = "https://wonieschool.com/api/ai/text_generation"
    # api_key = "" # API-KEY
#     headers = {
#         'X-Authorization': f"Bearer {api_key}"
#     }
#     payload = {
#         "prompt": "Hello my name is Tommy. nice meet you. what is your name?"
#     }
#     response =  requests.post(api_url, json=payload, headers=headers)
#     if response.status_code == 200:
#         print(response.json())
#     else:
#         print(response.text)

# chat_with_ai()

# 3. AI 목소리로 말하기.

# def get_ai_audio():
#     api_url = "https://wonieschool.com/api/ai/speech_generation"
#     api_key = "" # API-KEY
#     headers = {
#         'X-Authorization': f"Bearer {api_key}"
#     }
#     payload = {
#         "prompt": "Hello, super mega foxy awsome hot guys!",
#         "voice": "nova"     
#     }
#     response =  requests.post(api_url, json=payload, headers=headers)
#     if response.status_code == 200:
#         with open("ai_audio.mp3", "wb") as f:
#             f.write(response.content)
#             print("Audio saved")
#     else:
#         print(response.text)

# get_ai_audio()



# 4. AI와 목소리로 대화하기

def get_ai_audio(text):
    api_url = "https://wonieschool.com/api/ai/speech_generation"
    api_key = "" # API-KEY
    headers = {
        'X-Authorization': f"Bearer {api_key}"
    }
    payload = {
        "prompt": text,
        "voice": "nova"     
    }
    response =  requests.post(api_url, json=payload, headers=headers)
    if response.status_code == 200:
        with open("ai_audio.mp3", "wb") as f:
            f.write(response.content)
            print("Audio saved")
    else:
        print(response.text)

def talk_to_ai(text):
    api_url = "https://wonieschool.com/api/ai/text_generation"
    api_key = "" # API-KEY
    headers = {
        'X-Authorization': f"Bearer {api_key}"
    }
    payload = {
        "prompt": text
    }
    response =  requests.post(api_url, json=payload, headers=headers)
    if response.status_code == 200:
        ai_answer_text = response.json()['message']
        get_ai_audio(ai_answer_text)
        print(response.json())
    else:
        print(response.text)

talk_to_ai("where is south korea?")