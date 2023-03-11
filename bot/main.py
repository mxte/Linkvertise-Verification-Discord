import discord, os
from discord.ext import commands
from discord.ui import View


domain = "YOUR FLASK DOMAIN" # Don't put https://
class MyView(discord.ui.View): 
    def __init__(self):
        super().__init__(timeout=None)
    @discord.ui.button(label="Verify", style=discord.ButtonStyle.green, custom_id='persistent_view:green')
    async def button_callback(self, interaction, button):
        await interaction.response.send_message(f"Your verification link is https://{domain}/verify/{interaction.user.id}", ephemeral = True) # Send a message when the button is clicked

#Making the Button persistent, meaning it will never expire and if the bot is restarted the button will still work.

class PersistentViewBot(commands.Bot):
    def __init__(self):
        intents = discord.Intents.default()
        intents.message_content = True

        super().__init__(command_prefix=commands.when_mentioned_or('YOUR BOT PREFIX'), intents=intents)

    async def setup_hook(self) -> None:
        self.add_view(MyView())

    async def on_ready(self):
        print(self.user)


bot = PersistentViewBot()        

#This is just to get an embed, you can change it up to however you want it.
@bot.command() 
async def button(ctx):
    embed = discord.Embed (title="Verification", description="Based Verification Embed")
    await ctx.send(embed=embed, view=MyView())

bot.run("YOUR BOT TOKEN")
