# CryptoSwap Discord Bot ₿💬🤖

CryptoSwap is a Discord bot that provides real-time exchange rates between cryptocurrencies and fiat currencies. It allows users to quickly and easily check real-time conversion rates directly within Discord's chat user interface.

## Features

- **Help Command**: Explains how to use the bot and its features.
- **Swap Command**: Fetches the exchange rate between a cryptocurrency and a target currency.
- **Error Handling**: Displays user-friendly error messages for invalid parameters or unsupported currencies.

## Prerequisites

- Python 3.8 or higher
- A Discord bot token
- An API key for the cryptocurrency exchange rate service
- A Guild ID (a unique identifier for a Discord server)

## Installation

1. Clone this repository:
   ```bash
   git clone https://github.com/ItsFQ/Crypto-Swap-Bot.git

2. Navigate to the project directory:
   ```bash
   cd Crypto-Swap-Bot
3. Create a .env file in the project directory with the following content:
    ```.env
    BOT_TOKEN='your-discord-bot-token'
    API_KEY='your-api-key'
    GUILD_ID='your-guild-id'
    ```
5. Install the required Python libraries:
   ```bash
     pip install -r requirements.txt
    ```
## Run
   ```bash
    python3 main.py
  ```

## Usage
In your Discord server:
- Use `!help` to see all available commands.
- Use `!swap BTC USD` to convert Bitcoin to US Dollars (example).
- Replace `BTC` and `USD` with any supported cryptocurrency or fiat currency codes.
