import discord
from discord.ext import commands
from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()

TOKEN = os.getenv('DISCORD_BOT_TOKEN')



class Bot(commands.Bot):
    def __init__(self):
        super().__init__(command_prefix="!", intents=discord.Intents.all())

    async def setup_hook(self):
        """
        This function is called after the bot is ready. It loads all cogs located in the commands and events folders.
        """
        for cog in os.listdir("app/commands"):
            if cog.endswith(".py"):
                await self.load_extension(f"app.commands.{cog[:-3]}")
                print(f"Loaded command: {cog[:-3]}")
        
        print("----------")

        print("All commands loaded successfully.")


        for cog in os.listdir("app/events"):
            if cog.endswith(".py"):
                await self.load_extension(f"app.events.{cog[:-3]}")
                print(f"Loaded event: {cog[:-3]}")

        print("----------")
        
        print("All events loaded successfully.")




bot = Bot()


if __name__ == "__main__":
    bot.run(TOKEN)