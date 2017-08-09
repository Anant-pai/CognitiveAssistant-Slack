import os
from slackclient import SlackClient

BOT_NAME = 'sherlockbot'

slack_client = SlackClient(os.environ.get('SLACK_BOT_TOKEN'))

if __name__ == "__main__":
    api_call = slack_client.api_call("users.list")
    if api_call.get('ok'):
        users = api_call.get('members')
        for user in users:
            if 'name' in user and user.get('name') == BOT_NAME:
                print('hello')
                print("Bot ID for '" + user['name'] + "'is " + user.get('id'))
                print(os.environ.get('SLACK_BOT_TOKEN'))
                print(os.environ.get('BOT_ID'))

    else:
        print("could not find bot user with the name " + BOT_NAME)

