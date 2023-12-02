# Call the official ProgressiveAI Python Library
# From the "progressiveai" library import the "Chat" class to create a connection with ProgressiveAI's AI Models
from progressiveai import Chat, APIError

# Create a chat
try:  # Attempt to make a successful connection
    chat = Chat(  # Create a new instance of the "Chat" class to connect to a preferred AI Model
        # Input your ProgressiveAI API Key
        api_key="keyid-xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx",
        text="Hello, AI!",  # Enter question of your choice
        model="wispar"  # Mention the AI Model you want to use. Right now, we offer "WISPAR Lite", soon "WISPAR" will be also available for use within this Library
    )

    # Get AI response
    # Fetch a response from the AI Model, if not included the request will not be submitted and processed
    response = chat.get_response()
    print(response)  # Print the AI's response

except APIError as e:  # If the connection fails return an API Error. The error will be handled gracefully by the "APIError" class
    print(f"An error occurred: {e.message}")  # Print the error
