# CognitiveAssistant-Slack
The integration of our Cognitive Marketing Dashboard with Slack.

During this phase of testing, I used a virtual environment to run the code-- instructions below.

_________________
# From https://www.fullstackpython.com/blog/build-first-slack-bot-python.html

Go to the terminal (or Command Prompt on Windows) and change into the directory where you want to store this project. Within that directory, create a new virtualenv to isolate our application dependencies from other Python projects.

'''python
virtualenv starterbot
'''

Activate the virtualenv:

# source starterbot/bin/activate

The official slackclient API helper library built by Slack can send and receive messages from a Slack channel. Install the slackclient library with the pip command:

# pip install slackclient

When pip is finished you should see output like this and you'll be back at the prompt.

Output from using the pip install slackclient command with a virtualenv activated.

We also need to obtain an access token for our Slack team so our bot can use it to connect to the Slack API.
Slack Real Time Messaging (RTM) API

Slack grants programmatic access to their messaging channels via a web API. Go to the Slack web API page and sign up to create your own Slack team. You can also sign into an existing account where you have administrative privileges.

Use the sign in button on the top right corner of the Slack API page.

After you have signed in go to the Bot Users page. Name your bot then click the “Add bot integration” button. Add a bot integration. The page will reload and you will see a newly-generated access token. You can also change the logo to a custom design. For example, I gave this bot the Full Stack Python logo.

Copy and paste the access token for your new Slack bot.

Click the "Save Integration" button at the bottom of the page. Your bot is now ready to connect to Slack's API.

Export the Slack token with the name SLACK_BOT_TOKEN:

export SLACK_BOT_TOKEN='your slack token pasted here'

Obtaining Our Bot’s ID:

Use the print_bot_id.py file to get the bot's ID.

Our code imports the SlackClient and instantiates it with our SLACK_BOT_TOKEN, which we set as an environment variable. When the script is executed by the python command we call the Slack API to list all Slack users and get the ID for the one that matches the name "starterbot".

# python print_bot_id.py
Export the ID as an environment variable named BOT_ID.

# export BOT_ID='bot id returned by script'

Now that all of our code is in place we can run our StarterBot on the command line with the python starterbot.py command.

Console output when the StarterBot is running and connected to the API.

In Slack, create a new channel and invite StarterBot or invite it to an existing channel.

In the Slack user interface create a new channel and invite StarterBot.

Now start giving StarterBot commands in your channel.

Give StarterBot commands in your Slack channel.

As it is currently written above in this tutorial, the line AT_BOT = "<@" + BOT_ID + ">" does not require a colon after the "@starter" (or whatever you named your particular bot) mention.
