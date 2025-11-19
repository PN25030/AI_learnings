from agent import WeatherAgent
import os
import sys

def main():
    print("Initializing Weather Agent...")
    try:
        agent = WeatherAgent()
    except ValueError as e:
        print(e)
        print("Please set up your .env file with valid API keys.")
        return

    print("Weather Agent ready! Ask about the weather. Type 'quit' to exit.")
    
    while True:
        try:
            user_input = input("You: ")
            if user_input.lower() in ['quit', 'exit']:
                break
            
            response = agent.chat_with_agent(user_input)
            print(f"Agent: {response}")
        except KeyboardInterrupt:
            print("\nExiting...")
            break

if __name__ == "__main__":
    main()
