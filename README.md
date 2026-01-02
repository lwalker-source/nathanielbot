# Nathaniel Bot - Discord Meme Bot

A Discord bot built with Python that delivers random memes on demand. This project demonstrates proficiency in asynchronous programming, API integration, and environment configuration management.

## Features

- **Meme Command**: Users can type `$meme` to receive a random meme fetched from an external API
- **Responsive Event Handling**: Implements Discord event listeners for message handling
- **Environment Security**: Uses environment variables to securely manage bot tokens
- **SSL/TLS Security**: Custom SSL certificate handling for secure HTTPS connections on macOS

## Technologies & Skills Demonstrated

### Core Technologies
- **Python 3.14** - Primary programming language
- **Discord.py** - Discord bot framework for Python
- **Asyncio** - Asynchronous programming for non-blocking operations
- **Requests Library** - HTTP requests for external API calls

### Key Technical Skills

1. **Asynchronous Programming**
   - Implemented async/await patterns to handle non-blocking I/O operations
   - Used `asyncio.run_in_executor()` to run blocking requests without freezing the bot
   - Managed event-driven architecture with Discord event handlers

2. **API Integration**
   - Integrated with the Meme API to fetch random memes
   - Parsed JSON responses from external APIs
   - Handled HTTP requests within async context

3. **Environment & Configuration Management**
   - Implemented secure token management using environment variables
   - Used `python-dotenv` for loading configuration from `.env` files
   - Prevented hardcoding sensitive credentials

4. **SSL/TLS Certificate Handling**
   - Resolved SSL certificate verification errors on macOS
   - Implemented custom SSL context configuration
   - Monkey-patched aiohttp connector for proper certificate handling
   - Demonstrated troubleshooting of system-level Python configuration issues

5. **Object-Oriented Design**
   - Extended Discord's `Client` class with custom behavior
   - Implemented event handlers as class methods
   - Created clean separation of concerns with utility functions

## Installation

### Prerequisites
- Python 3.14+
- Virtual environment (recommended)

### Setup

1. Clone the repository:
```bash
git clone https://github.com/lwalker-source/nathanielbot.git
cd nathanielbot
```

2. Create and activate a virtual environment:
```bash
python3 -m venv .venv
source .venv/bin/activate
```

3. Install dependencies:
```bash
python3 -m pip install discord.py certifi python-dotenv requests
```

4. Create a `.env` file with your Discord bot token:
```
DISCORD_BOT_TOKEN=your_bot_token_here
```

5. Run the bot:
```bash
python3 discordbot.py
```

## Usage

Once the bot is running and connected to your Discord server, users can invoke commands:

- `$meme` - Sends a random meme to the channel

## Code Architecture

### Main Components

- **MyClient Class**: Custom Discord client that extends the base `discord.Client` class
  - `on_ready()`: Called when the bot successfully connects to Discord
  - `on_message()`: Processes incoming messages and executes commands

- **get_meme() Function**: Async function that fetches memes from external API
  - Uses executor to run blocking requests asynchronously
  - Parses JSON responses

- **SSL Configuration**: Custom SSL context setup
  - Uses certifi library for cross-platform certificate management
  - Patches aiohttp connector for proper HTTPS handling

## Lessons Learned

- **Asynchronous Programming**: Understanding the importance of non-blocking I/O in event-driven applications
- **Debugging**: Troubleshooting platform-specific SSL certificate issues
- **API Integration**: Working with RESTful APIs and JSON parsing
- **Best Practices**: Secure credential management and clean code organization
- **Python Ecosystem**: Working with popular libraries like discord.py and requests

## Future Enhancements

- Add more commands (image search, jokes, quotes, etc.)
- Implement a command prefix system
- Add error handling and logging
- Database integration for user preferences
- Command cooldowns to prevent spam
- Help command documentation

## License

This project is open source and available under the MIT License.

## Author

**lwalker-source** - [GitHub Profile](https://github.com/lwalker-source)
