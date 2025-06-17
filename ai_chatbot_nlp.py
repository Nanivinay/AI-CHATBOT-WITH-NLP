import nltk
nltk.data.path.append("C:/Users/Jyoth/AppData/Roaming/nltk_data")
from nltk.stem import WordNetLemmatizer
import random

lemmatizer = WordNetLemmatizer()

intents = {
    'greeting': {
        'keywords': ['hello', 'hi', 'hey', 'greetings'],
        'responses': ['Hello there!', 'Hi, how can I assist you?', 'Hey! What can I do for you?']
    },
    'goodbye': {
        'keywords': ['bye', 'goodbye', 'see you', 'take care'],
        'responses': ['Goodbye!', 'See you later!', 'Take care!']
    },
    'thanks': {
        'keywords': ['thanks', 'thank you', 'appreciate'],
        'responses': ['You\'re welcome!', 'Glad to help!', 'No problem!']
    },
    'about': {
        'keywords': ['who are you', 'what is your name', 'about you'],
        'responses': ['I am your AI chatbot made using Python and NLTK!', 'Just a friendly chatbot created by Vinay.']
    },
    'fallback': {
        'responses': ['Sorry, I didn’t understand that.', 'Could you please rephrase?', 'I\'m not sure how to answer that.']
    }
}

def get_response(user_input):
    user_input = user_input.lower()
    for intent, data in intents.items():
        for keyword in data.get('keywords', []):
            if keyword in user_input:
                return random.choice(data['responses'])
    return random.choice(intents['fallback']['responses'])

def chatbot():
    print("🤖 Chatbot is now online! Type 'exit' to quit.")
    while True:
        user_input = input("You: ")
        if user_input.lower() == 'exit':
            print("🤖 Chatbot: Bye! Have a great day.")
            break
        response = get_response(user_input)
        print(f"🤖 Chatbot: {response}")

if __name__ == "__main__":
    chatbot()
