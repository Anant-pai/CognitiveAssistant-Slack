import os
import time
from slackclient import SlackClient
import json
import urllib
import requests

# SlackBot's ID as an environment variable
BOT_ID = os.environ.get("BOT_ID")

# constants
AT_BOT = "<@" + BOT_ID + ">"
EXAMPLE_COMMAND = "ask analytics"
EXAMPLE_COMMAND_2 = "what about"
EXAMPLE_COMMAND_3 = "how about"
url = "http://sbybz221033.cloud.dst.ibm.com:5000/getSqlResponse"
response = ' '
global_request = ' '


# instantiate Slack & Twilio cliesnts
slack_client = SlackClient(os.environ.get('SLACK_BOT_TOKEN'))


def parse_slack_output(slack_rtm_output):
    """
        The Slack Real Time Messaging API is an events firehose.
        this parsing function returns None unless a message is
        directed at the Bot, based on its ID.
    """
    output_list = slack_rtm_output
    if output_list and len(output_list) > 0:
        for output in output_list:
            if output and 'text' in output and AT_BOT in output['text']:
                # return text after the @ mention, whitespace removed
                return output['text'].split(AT_BOT)[1].strip().lower(), \
                       output['channel']
    return None, None


def handle_command1(command, channel):
    """
        Receives commands directed at the bot and determines if they
        are valid commands. If so, then acts on the commands. If not,
        returns back what it needs for clarification.
    """
    answer = "Not sure what you mean. Use the *" + EXAMPLE_COMMAND + \
               "* command with numbers, delimited by spaces."

    # If command starts with 'ask analytics'
    if command.startswith(EXAMPLE_COMMAND):

        # Remove 'ask analytics' from string and call API
        string_wo_ask = command.partition(' ')[2]
        request = string_wo_ask.partition(' ')[2]
        global global_request
        global_request = request
        answer = api_call(request)

    # If command starts with 'what about' or 'how about'
    if command.startswith(EXAMPLE_COMMAND_2) or command.startswith(EXAMPLE_COMMAND_3):

        # Remove 'what about' from string
        string_wo_how = command.partition(' ')[2]
        requestaddon = string_wo_how.partition(' ')[2]

        # addend to previous question
        request = global_request
        request += requestaddon
        global global_request
        global_request = request

        # call API
        answer = api_call(request)

    slack_client.api_call("chat.postMessage", channel=channel,
                          text=answer, as_user=True)




def api_call(request):
    """
        Takes, as an argument, the question and performs the
        secure API call. Returns a string with the answer
        and insights parsed and formatted from JSON data structure.
        If an error is received from the API call, it returns
        an error string to the user.
    """
    q = request
    data = json.dumps({"query": q})
    headers = {'content-type': 'application/json'}
    r = requests.post(url, data=data, headers=headers)

    # Format the string (adding bold, itlic, and filler text)
    try:
        insights = '\n _Here is some other information you may find useful..._'
        for i in range(3):
            insights += '\n_     -'
            insights += r.json()['insights'][i]['text'] + '_'
        return ('*' + r.json()['answer']['text'] + '*' + insights)

    # Error message
    except ValueError, e:
        return ("Sorry, I don't know that yet. Try asking me a different question.")



if __name__ == "__main__":
    READ_WEBSOCKET_DELAY = 1 # 1 second delay between reading from firehose
    if slack_client.rtm_connect():
        print("StarterBot connected and running!")
        while True:
            command, channel = parse_slack_output(slack_client.rtm_read())
            if command and channel:
                handle_command1(command, channel)
            time.sleep(READ_WEBSOCKET_DELAY)
    else:
        print("Connection failed. Invalid Slack token or bot ID?")
