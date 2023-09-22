import nextcord
from nextcord.ext import commands
import asyncio
import random
import requests

description = "serving sad content"
intents = nextcord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix="!", description=description, intents=intents)

words = open("words.txt",'r')
wordCount = 0
wordArr = []
for word in words: wordArr.append(word)
words.close()
URL = "http://philosophyapi.pythonanywhere.com/api/ideas/?search="

turtle = """```
       /^\\
      |   |
/\     |_|     /\\
| \___/' `\___/ |
 \_/  \___/  \_/
  |\__/   \__/|
  |/  \___/  \|
 ./\__/   \__/\,
 | /  \___/  \ |
 \/     V     \/
```"""

@bot.event
async def on_message(message):
    await bot.process_commands(message)

@bot.command(help = "responds with a random sad quote")
async def quote(ctx):
    word = random.choice(wordArr)
    if (word == wordArr[-1]):
        print("condition tripped")
        await ctx.send(turtle)
        count = 0
        return
    r = requests.get(url = URL+word)
    data = r.json()
    count = data["count"]
    safeRand = count
    count = 0 
    if (safeRand == 0): safeRand = 1
    elif (safeRand == 1): safeRand = 1
    quote = data["results"][random.randint(0,safeRand-1)]
    await ctx.send(quote["quote"]+"\n\n"+"-"+quote["author"])

file = open("../token.txt", 'r')
TOKEN = file.read()
bot.run(TOKEN)

