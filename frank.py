# This example requires the 'message_content' intent.
import discord
import random
import os
from dotenv import load_dotenv

comments = [
    "Wow, you must really love animals. Too bad they are all pixelated and fake.",
    "I admire your dedication to your zoo. It’s not easy to ignore the real world and all its problems.",
    "How do you manage to balance your time between your zoo and your other hobbies? Oh wait, you don’t have any other hobbies.",
    "You know, there are actual zoos out there that need your support and donations. But I guess clicking on a screen is more fun and rewarding.",
    "I’m so happy for you and your zoo. You’ve achieved so much in such a short time. It’s almost like you have no life outside of it.",
    "I’m sorry, I can’t talk to you right now. I’m busy doing something important and meaningful. Unlike some people.",
    "You’re so lucky to have such a relaxing and stress-free hobby. I wish I could escape from reality like you do.",
    "I’m impressed by how much you care about your zoo. You must have a lot of empathy and compassion. For virtual animals, that is.",
    "You’re so good at running your zoo. You should apply for a job at a real one. Oh wait, you don’t have the skills or qualifications for that.",
    "I’m glad you enjoy your zoo game. It’s nice to have something to distract you from your failures and disappointments.",
]


class Frank(discord.Client):
    async def on_ready(self):
        print(f"Logged on as {self.user}!")

    async def on_message(self, message):        
        if message.channel.name == "zooo" and str(self.user) != str(message.author):
            await message.channel.send(random.choice(comments))


intents = discord.Intents.default()
intents.message_content = True

load_dotenv()

key = os.getenv("KEY")

client = Frank(intents=intents)
client.run(key)
