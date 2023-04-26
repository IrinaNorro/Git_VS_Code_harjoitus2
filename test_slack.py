import os
from slack_sdk import WebClient
from slack_sdk.errors import SlackApiError

# Replace 'your-bot-token-here' with your actual bot token
SLACK_BOT_TOKEN = "xoxb-5155892822579-5155951362099-909Kv8ajjUrdYZIMn90aU1uD"

# Initialize the Slack client
client = WebClient(token=SLACK_BOT_TOKEN)

# Define the channel and the message you want to send
channel_id = "atlassian-products-backup"
message = "Hello there!"

# Function to send a message to Slack
def send_slack_message(channel, text):
    try:
        response = client.chat_postMessage(
            channel=channel,
            text=text
        )
        print(f"Message sent: {response['ts']} -> {text}")
    except SlackApiError as e:
        print(f"Error sending message: {e}")

# Send the message
send_slack_message(channel_id, message)
