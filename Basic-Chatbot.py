'''responses = {
    "Hi": "Hello",
    "how are  you": "I'm good thanks!",
    "bye": "Goodbye!"
}

while True:
    user_input = input("You: ").lower()
    if user_input in responses:
        print(f"Bot: {responses[user_input]}")
    elif user_input == "exit":
        break
    else:
        print("Bot: Sorry, I didn't understand that.")
        '''
        
import random
from typing import Dict, List
import re
import time

class SmartChatBot:
    def __init__(self):
        # Multi-response dictionary with categories
        self.responses: Dict[str, List[str]] = {
            "greeting": ["Hello there!", "Hi!", "Hey, good to see you!"],
            "farewell": ["Goodbye!", "See you later!", "Take care!"],
            "status": ["I'm doing great, thanks!", "All good here!", "Feeling awesome!"],
            "help": ["How can I assist you?", "Need help with something?", "I'm here for you!"],
            "time": [f"The current time is {time.strftime('%H:%M:%S')}"],
            "thanks": ["You're welcome!", "My pleasure!", "Anytime!"]
        }
        
        # Pattern-based responses
        self.patterns = {
            r"hi|hello|hey": "greeting",
            r"bye|goodbye|see you": "farewell",
            r"how (are|r) you|how's it going": "status",
            r"help|assist": "help",
            r"time|what time": "time",
            r"thank(s| you)": "thanks"
        }
        
        self.conversation_history = []
        self.user_name = None
    
    def get_response(self, category: str) -> str:
        """Get a random response from a category"""
        if category == "time":  # Update time dynamically
            return f"The current time is {time.strftime('%H:%M:%S')}"
        return random.choice(self.responses[category])
    
    def match_pattern(self, user_input: str) -> str:
        """Match input to patterns and return appropriate response"""
        user_input = user_input.lower().strip()
        
        # Store conversation history
        self.conversation_history.append(user_input)
        
        # Check for name setting
        if user_input.startswith("my name is "):
            self.user_name = user_input[11:].capitalize()
            return f"Nice to meet you, {self.user_name}!"
        
        # Pattern matching
        for pattern, category in self.patterns.items():
            if re.search(pattern, user_input):
                response = self.get_response(category)
                return response if not self.user_name else f"{self.user_name}, {response}"
        
        # Special commands
        if user_input == "history":
            return "Conversation history:\n" + "\n".join(self.conversation_history)
        
        # Default response
        return "I'm not sure what you mean. Try something else!"
    
    def run(self):
        """Run the chatbot"""
        print("Welcome to SmartChat! (Type 'exit' to quit)")
        print("You can say things like 'hi', 'how are you', 'time', or 'my name is [name]'")
        
        while True:
            try:
                user_input = input("You: ")
                if not user_input:
                    print("Bot: Please say something!")
                    continue
                    
                if user_input.lower() == "exit":
                    farewell = self.get_response("farewell")
                    print(f"Bot: {farewell}")
                    break
                    
                response = self.match_pattern(user_input)
                print(f"Bot: {response}")
                
            except KeyboardInterrupt:
                print("\nBot: Caught you trying to escape! Goodbye!")
                break
            except Exception as e:
                print(f"Bot: Oops, something went wrong: {str(e)}")

def main():
    bot = SmartChatBot()
    bot.run()

if __name__ == "__main__":
    main()