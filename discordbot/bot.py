# bot.py
import os
import discord
from pymongo import MongoClient

TOKEN = os.getenv('DISCORD_TOKEN') 
CONNECTION_STRING=os.getenv('CONNECTION_STRING')
mongo_client = MongoClient(CONNECTION_STRING)

print(f'TOKEN {TOKEN}')

class MyClient(discord.Client):
    async def on_ready(self):
        collection = mongo_client.taskboard.tasks
        print(f'Logged on as {self.user}!')
        task_msg = f'There are {collection.count_documents({})} tasks in database!'
        print(task_msg)
        client.send_message(client.get_channel("1257292028492906668"), task_msg)


    async def on_message(self, message):
        print(f'Message from {message.author}: {message.content}')

intents = discord.Intents(messages=True)
# intents.message_content = True

client = MyClient(intents=intents)
client.run(TOKEN)