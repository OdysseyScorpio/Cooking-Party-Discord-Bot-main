import discord
import os
import asyncio
import recipes
import json
from discord.interactions import Interaction
from dotenv import load_dotenv
from cooking_templates import *


load_dotenv() # load all the variables from the env file

intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)

class Recipe_Select(discord.ui.Select):
    def __init__(self, thread) -> None:
        super().__init__(placeholder="Select a recipe", options=recipes.options)
        self.thread = thread

    async def callback(self, interaction):
        # create a cooking party
        print(self.values[0])
        cooking_party = recipes.get_party(self.values[0])

        if cooking_party == False:
            await interaction.response.edit_message(content="I cannot help with this recipe yet, please set up the template yourself", view = None)

        else:
            cooking_party.thread = self.thread

            select = Role_Select(cooking_party=cooking_party)
            
            view = discord.ui.View() #TODO: set timeout
            view.add_item(select)
            await interaction.response.edit_message(content="Excellent, I can create and maintain a template for you.", view = None)
            await self.thread.send(cooking_party.post_template, view = view)
            

class Role_Select(discord.ui.Select):
    def __init__(self, cooking_party) -> None:
        super().__init__(placeholder="Select your role", options=cooking_party.options)
        self.cooking_party = cooking_party

    async def callback(self, interaction):
        self.cooking_party.message_id = interaction.message.id
        was_cook_added = self.cooking_party.add_cook(role=self.values[0], name=f"<@{str(interaction.user.id)}>")
        self.cooking_party.update_post()
        
        button = Cancel_Button(cooking_party=self.cooking_party)

        view = discord.ui.View() #TODO: set timeout
        view.add_item(button)

        if was_cook_added:
            await self.cooking_party.thread.send(f"<@{str(interaction.user.id)}> chose: {self.values[0]}")
            await interaction.response.send_message(content = f"You chose: {self.values[0]}.", ephemeral=True, view=view)
            await interaction.followup.edit_message(message_id=interaction.message.id, content=self.cooking_party.post_template)
        else:
            await interaction.response.send_message(content = f"The {self.values[0]} role is already filled", ephemeral=True)

class Cancel_Button(discord.ui.Button):
    def __init__(self, cooking_party) -> None:
        super().__init__(label="Withdraw", style=discord.ButtonStyle.grey, emoji="✖")
        self.cooking_party = cooking_party

    async def callback(self, interaction):
        self.cooking_party.remove_cook(name=f"<@{str(interaction.user.id)}>")
        self.cooking_party.update_post()

        await self.cooking_party.thread.send(content=f"<@{str(interaction.user.id)}> withdrew from their role")
        await interaction.response.edit_message(content="You have been removed from this party", view = None)
        message = self.cooking_party.thread.get_partial_message(self.cooking_party.message_id)
        await message.edit(content=self.cooking_party.post_template)

@client.event
async def on_ready():
    print(f'We have logged in as {client.user}')


@client.event
async def on_thread_create(thread):
    select = Recipe_Select(thread)
    
    view = discord.ui.View() #TODO: set timeout
    view.add_item(select)

    await asyncio.sleep(0.5) # wait 0.5s to prevent sending message before thread creator
    await thread.send("Hi, I might be able to help you host this party. What do you want to cook?", view = view)

#client.run(os.getenv('TOKEN'))

with open('env.json') as f:
    env_data = json.load(f)
token = env_data.get('TOKEN')
client.run(token)