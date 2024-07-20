# Cooking-Party-Discord-Bot
A Pycord Discord bot to help host cooking parties in Palia

The Cooking Party Discord Bot is a fan-made tool to help Palia players host cooking parties on discord. Palia's intellectual property is reserved by Singularity 6. This tool is not affiliated in any way with Palia or Singularity 6.

## What does it do?
When a player creates a new thread in a forum channel, the bot will prompt the user to select a recipe from a list. If the selected recipe is supported, the bot will create a sign-up sheet for the cooking party. The sign-up sheet includes a role selection drop-down so other players can select their roles and the bot will update the sheet.

## Bot Setup
Follow the [pycord guide](https://guide.pycord.dev/getting-started/creating-your-first-bot) to set up your discord bot.

### OAuth2
- Scope: bot
- Permissions: Send Messages, Send Messages in Threads

### Privileged Gateway Intents
Select *Message Content Intent*

### .env File
To protect the bot secret, the bot's TOKEN is not included in this repository. Your bot will have its own TOKEN. To include this token into the project and make your code work you will need to create a .env file with the following:
```
TOKEN = YOURtokenHERE
```
 This gets handled in the main.py script with 	`load_dotenv()`

### In Your Server
Consider only giving the bot permission to the forum channel where you want it to participate. Otherwise it will send recipe prompts in other threads.

## The Code
### main.py
This is where the bot handles messages and interactions

### recipes.py
This script contains constants for all the recipe titles. It is responsible for managing the recipe dropdown list by providing the list of options and a function that returns the correct cooking party class object based on the recipe title

### cooking_templates
This repository is where the recipe templates go. There are a few example templates already provided:
- blueberry_pie.py
- celebration_cake.py
- chilli_oil_dumplings.py
- sashimi.py

#### \_\_init\_\_.py
Update this file with any new template scripts to allow for easy import

#### base.py
The parent class for all recipe templates
