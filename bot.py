
import discord
from discord.ext import commands
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
import time

bot = commands.Bot(command_prefix='.')
import os
from dotenv import load_dotenv

load_dotenv()

TOKEN = os.getenv("DISCORD_TOKEN")

@bot.event
async def on_ready():
    print(f'{bot.user} has connected to Discord!')

@bot.command()
async def amazon(ctx, *val):


        """Generate a price and url for an amazon item"""
        exit = False
        print(val)
        val2 = ""
        val2 = val2.join(val) + ' '
        chrome_options = Options()
        chrome_options.add_argument("--headless")
        driver = webdriver.Chrome('C:\webdrivers\chromedriver_win32\chromedriver.exe', chrome_options= chrome_options)
        url = "https://www.amazon.ca/"
        def geturl(search):
            """Generate a url from given search"""
            template = "https://www.amazon.ca/s?k={}&ref=nb_sb_noss_1"
            search = search.replace(' ', '+')
            return template.format(search)
        print(val2)

        url = geturl(val2)
        print(url)
        driver.get(url)
        soup = BeautifulSoup(driver.page_source, 'html.parser')


        i = 0
        num = ""
        asin = ""
        try:
            while True:
                span = driver.find_elements_by_class_name('a-badge-supplementary-text')
                print (span)
                asin = span[i].get_attribute("id")
                i += 1
                if ("-amazons-choice-supplementary") in asin:
                    break
            num = asin[0:10]
            print(num)
        except:
            await ctx.send("there is no amazon choice for the item ruhroh")


        url = "https://www.amazon.ca/dp/" + num
        
        print(num)
        driver.get(url)
        print(asin)
        """Generate a price and url for an amazon item"""

        def get_product_price(url):
            """Gets product price"""
            price = None
            try:
                price = driver.find_element_by_id('corePrice_feature_div').text
            except:
                pass
            for x in range(2):
                if price == None and x == 0:
                    try:
                        price = driver.find_element_by_id('corePrice_feature_div').text
                    except:
                        pass
                elif price == None and x == 1:
                    price = "Not Available"
            return price


        def get_product_name(url):
            """Gets product name"""
            product = None
            try:
                product = driver.find_element_by_id('productTitle').text
            except:
                pass
            if product is None:
                product = "Not available"
            return product


        price = get_product_price(url)
        name = get_product_name(url)

        print(price)
        print(name)
        if  not exit:
            "sending message"
            await ctx.send(f'The price is: {price}')
            await ctx.send(f'The name is: {name}')
            await ctx.send(f'the url is: {url}')
        user = str(ctx.message.author)
        print(user)
        f = open(user+".txt","a")
        content = val2 +price+ name+ url
        f.write(content+"\n")

@bot.command()
async def voicecommand(ctx):
    """Listen for voice commands in a voice channel"""
    # Ensure the bot and the user are in the same voice channel
    if ctx.author.voice and ctx.voice_client and ctx.author.voice.channel == ctx.voice_client.channel:
        await ctx.send("Listening for your voice command...")

        # Use SpeechRecognition to listen to voice input
        recognizer = sr.Recognizer()

        def listen_to_voice():
            with sr.Microphone() as source:
                print("Listening...")
                audio = recognizer.listen(source)

            try:
                # Convert speech to text
                command_text = recognizer.recognize_google(audio)
                print(f"Recognized command: {command_text}")
                return command_text
            except sr.UnknownValueError:
                return "Sorry, I couldn't understand that."
            except sr.RequestError:
                return "Error with the speech recognition service."

        command_text = await asyncio.to_thread(listen_to_voice)
        await ctx.send(f'You said: "{command_text}"')

        # Handle voice commands (customize as needed)
        if "amazon" in command_text.lower():
            await ctx.send("Voice command recognized: Amazon")
            # Call the .amazon command or logic here (customize as needed)
            await amazon(ctx, *command_text.split()[1:])  # Assumes "amazon <search>"
        else:
            await ctx.send("Voice command not recognized.")
    else:
        await ctx.send("Both the bot and the user must be in the same voice channel.")
@bot.command()
async def join(ctx,val):
    channel = discord.utils.get(ctx.message.guild.voice_channels, name = val)
    if channel:
        await channel.connect()
        discord.AudioSource.read()
    else:
        await ctx.send(f'the channel: {val} does not exist')

@bot.command()
async def leave(ctx):
    if(ctx.voice_client):
        await ctx.guild.voice_client.disconnect()
        await ctx.send("Left voice channel")
    else:
        await ctx.send("I am not in a voice channel")
@bot.command()
async def logout(ctx):
    await bot.logout()
bot.run(TOKEN)
