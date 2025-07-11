from discord.ext import commands
import discord

class Utils(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @commands.command(name='ping')
    async def ping(self, ctx: commands.Context):
        """
        Responds with 'Pong!' to check if the bot is responsive.
        """
        await ctx.send('Pong!')

    @commands.command(name='info')
    async def info(self, ctx: commands.Context):
        """
        Provides basic information about the bot.
        """
        embed = discord.Embed(title="Bot Information", description="This is a simple Discord bot.", color=discord.Color.blue())
        embed.add_field(name="Author", value="Your Name", inline=False)
        embed.add_field(name="Version", value="1.0.0", inline=False)
        await ctx.send(embed=embed)

async def setup(bot: commands.Bot):
    """
    This function is called to set up the Utils cog.
    """
    await bot.add_cog(Utils(bot))
    print("Utils cog loaded successfully.")