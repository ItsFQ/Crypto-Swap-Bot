# Project: CryptoSwap Discord Bot

# Required Libraries
import requests
import os
from dotenv import load_dotenv
import discord
from discord.ext import commands
from discord import app_commands

# To read in the TOKEN located in the .env file
load_dotenv()

# To get a hold of the TOKEN value
botToken = os.environ['BOT_TOKEN'] 

# To get a hold of the API Key
apiKey = os.environ['API_KEY']

# To get a hold of the GUILD ID
guild_id = int(os.environ['GUILD_ID'])

class MyClient(commands.Bot):
    async def on_ready(self):
        print(f'Logged on as {self.user}!')
        try:
            # Syncs the commands we define for the bot to discord, allowing them to appear in the commands UI
            guild = discord.Object(id=guild_id)
            synced = await self.tree.sync(guild=guild)  
            print(f"Synced {len(synced)} command(s) to guild {guild.id}")
        except Exception as e:
            print(f"Failed to sync commands: {e}")
    
    # To make sure the bot doesn't respond to itself
    async def on_message(self, message):
        if message.author == self.user:
            return


intents = discord.Intents.default()
intents.message_content = True
client = MyClient(command_prefix='$', intents=intents)

GUILD_ID = discord.Object(id=guild_id)

# Error Embed (Displayed in case of invalid paramaters or unsupported currencies)
errorEmbed = discord.Embed(title='Invalid Parameters', description='**Please try again**', color=discord.Colour.red())


# Help Command (Provides info about the bot)
@client.tree.command(name='help', description="Explains what the bot does.", guild=GUILD_ID)
async def helpFunc(interaction: discord.Interaction):
    
    # Help Embed
    helpEmbed = discord.Embed(title='₿ CryptoSwap ₿', description='CryptoSwap instantly delivers real-time exchange rates between any cryptocurrency and any currency of your choice—right inside Discord!', color=discord.Color.yellow())

    helpEmbed.set_thumbnail(url='https://images.emojiterra.com/google/android-12l/512px/1f4dc.png')

    helpEmbed.add_field(name='How to Use...', value=(
            "Use the `/swap` command, entering the full coin name you want to convert "
            "from as the first parameter and the abbreviation of your target currency "
            "as the second parameter.\n\n"
            "**Example:** `/swap BTC USD`\n"
            "This will display the current exchange rate of 1 Bitcoin to United States Dollar."
        ), inline=False)
    
    helpEmbed.add_field(name='Important Note', value=(
            "The bot calculates the exchange rate for 1 unit of the specified currency (fiat or crypto)"
            "in the chosen target currency (fiat or crypto)."
        ), inline=False)
    
    await interaction.response.send_message(embed=helpEmbed)


# Swap Command (Gets Conversion Rate)
@client.tree.command(name='swap', description='Provides an exchange rate from a cryptocurrency to a target currency', guild=GUILD_ID)

# Provides a short description for each input parameter
@app_commands.describe(
    sourcecoin="The currency you want to convert from",
    targetcurrency="The currency to convert to"
)

# Defines what the swap command does
async def swapFunc(interaction: discord.Interaction, sourcecoin: str, targetcurrency: str):    
    
    # Initialize variables 
    base = sourcecoin
    output = 'JSON'
    url = f'https://westinpay.com/currency/crypto_api?api_key={apiKey}&base={base}&output={output}'

    # Sends a request to fetch the required data 
    response = requests.get(url)

    if response.status_code == 200:
        if len(response.json()['data']['rates']) > 1:
            try:
                target_rate = response.json()['data']['rates'][targetcurrency]
                if target_rate:
                    # Swap Embed
                    swapEmbed = discord.Embed(title=f'Exchange Rate -> {sourcecoin} to {targetcurrency}', description=(
                        f"`1 {sourcecoin} is equal to {target_rate} {targetcurrency}`"
                    ), color=discord.Colour.green())
                    
                    await interaction.response.send_message(embed=swapEmbed)
            except:
                await interaction.response.send_message(embed=errorEmbed)
        else:
            await interaction.response.send_message(embed=errorEmbed)
    else:
        # To account for unsuccessful HTTP response status codes
        statusCodeEmbed = discord.Embed(title='Oops! Something Went Wrong.', description=f'Error: {response.status_code}', color=discord.Colour.red())
        await interaction.response.send_message(embed=statusCodeEmbed)

# Starts the bot
client.run(botToken)
