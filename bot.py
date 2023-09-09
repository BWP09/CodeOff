import nextcord as nc, random, asyncio, datetime
from nextcord.ext import commands, tasks

import util, lib.log as log, lib.color as color

config = util.Config("config/config.yml")
logger = log.Logger(config.path__logs_config)

intents = nc.Intents.all()
bot = commands.Bot(intents = intents)

@bot.event
async def on_ready():
    await bot.change_presence(activity = nc.Game(config.bot__status_playing), status = config.bot__status_type)

@bot.event
async def on_message(message: nc.Message):
    config.reload_config()
    
    username = str(message.author).split("#")[0]
    author = message.author
    author_id = int(message.author.id)
    channel = message.channel
    channel_id = int(message.channel.id)
    server = message.guild
    
    try: server_id = int(message.guild.id)
    except: server_id = 0

    if server_id != config.harassment__target_guild_id:
        return

    if author_id != config.harassment__target_user_id:
        return
    
    if len(message.content) > 100:
        await message.channel.send("Not the paragraph 😭💀", reference = message)
        return
    
    rand = random.randint(0, 10)
    
    if rand == 0:
        text = ""
        
        match random.randint(0, 11):
            case 0:  text = "\"bro 💀\""
            case 1:  text = "\"stfu\""
            case 2:  text = "\"beef 😠!\""
            case 3:  text = "\"brooooOO!\""
            case 4:  text = "\"💀\""
            case 5:  text = "\"💀💀\""
            case 6:  text = "\"💀💀💀\""
            case 7:  text = "\"we're beefing!\""
            case 8:  text = "\"kys\""
            case 9:  text = "\"🤓☝\""
            case 10: text = "\"🤓☝ actually!\""
            case 11: text = "\"all buns!@!!!!\""
        
        await message.channel.send(text, reference = message)
    
    elif rand == 1:
        emoji = ""

        match random.randint(0, 2):
            case 0: emoji = "💀"
            case 1: emoji = "🤓"
            case 2: emoji = "🤪"
        
        await message.add_reaction(emoji)

@bot.event
async def on_typing(channel: nc.TextChannel, user: nc.Member, when):
    if user.id == config.harassment__target_user_id:
        await asyncio.sleep(2)

        if user.typing:
            await channel.send(f"<@{config.harassment__target_user_id}> stop typing")

@bot.slash_command(description = "Harass Keegan!", guild_ids = [config.harassment__target_guild_id])
async def harass(interaction: nc.Interaction):
    config.reload_config()

    guild = interaction.guild
    user = await guild.fetch_member(config.harassment__target_user_id)

    try:                                     # SOOOO MUCH NESTING 😭🤮
        if user.voice:
            rand = random.randint(0, 1)
        
        else:
            rand = 1

        if rand == 0:
            print("Voice")

            rand = random.randint(0, 3)

            if rand == 0:
                print("  disconnect")
                await interaction.send(f"Kicked <@{config.harassment__target_user_id}> from <#{user.voice.channel.id}> 😋")

                await user.disconnect()

            elif rand == 1:
                wait_time = random.randint(config.harassment__mute_time_lower, config.harassment__mute_time_upper)
                
                print(f"  mute, {wait_time}")
                await interaction.send(f"Muted <@{config.harassment__target_user_id}> for {wait_time} seconds 😝")
                
                await user.edit(mute = True)
                await asyncio.sleep(wait_time)
                await user.edit(mute = False)
            
            elif rand == 2:
                wait_time = random.randint(config.harassment__deafen_time_lower, config.harassment__deafen_time_upper)

                print(f"  deafen, {wait_time}")
                await interaction.send(f"Deafened <@{config.harassment__target_user_id}> for {wait_time} seconds 😃")

                await user.edit(deafen = True)
                await asyncio.sleep(wait_time)
                await user.edit(deafen = False)

            elif rand == 3:
                channel = random.choice([channel for channel in await guild.fetch_channels() if channel.type == nc.ChannelType.voice and channel.id != user.voice.channel.id])
                
                print(f"  move, to {channel.name}")
                await interaction.send(f"Moved <@{config.harassment__target_user_id}> to <#{channel.id}> 😌")

                await user.move_to(channel)
        
        elif rand == 1:
            print("Text")

            rand = random.randint(0, 1)

            if rand == 0:
                wait_time = random.randint(config.harassment__timeout_time_lower, config.harassment__timeout_time_upper)

                print(f"  timeout, {wait_time}")
                await interaction.send(f"Timed <@{config.harassment__target_user_id}> out for {wait_time} seconds 🤑")
                
                await user.edit(timeout = datetime.timedelta(seconds = wait_time))
            
            elif rand == 1:
                wait_time = random.randint(config.harassment__lockout_time_lower, config.harassment__lockout_time_upper)

                print(f"  lockout, {wait_time}")
                await interaction.send(f"Lockout! for {wait_time} seconds 🤭☺️")

                channels = await guild.fetch_channels()

                for channel in channels:
                    perms = channel.overwrites_for(user)
                    perms.view_channel = False

                    await channel.set_permissions(user, overwrite = perms)
                
                await asyncio.sleep(wait_time)

                for channel in channels:
                    perms = channel.overwrites_for(user)
                    perms.view_channel = True

                    await channel.set_permissions(user, overwrite = perms)
    
    except Exception as e:
        print(f"    {e}")
    
    print()

@tasks.loop(seconds = 5)
async def random_messages():
    if not config.harassment__random_messages:
        return

    if random.randint(0, 5) == 0:
        guild = await bot.fetch_guild(config.harassment__target_guild_id)
        channel = random.choice([channel for channel in await guild.fetch_channels() if channel.type == nc.ChannelType.text])
        
        text = ""
        attach = ""

        match random.randint(0, 9):
            case 0: text = f"<@{config.harassment__target_user_id}> why are you so short"
            case 1: text = f"why are you short <@{config.harassment__target_user_id}> "
            case 2: text = f"<@{config.harassment__target_user_id}> wErE bEeFiNG"
            case 3: text = f"stop fucking brynley <@{config.harassment__target_user_id}> 😭"
            case 4: text = f"stop fisting brynley 😭😭😭 <@{config.harassment__target_user_id}>"
            case 5: text = f"<@{config.harassment__target_user_id}> stop fucking brynley 😭😭"
            case 6: text = f"Jayden wants you so bad rn <@{config.harassment__target_user_id}>"
            case 7: text = f"<@{config.harassment__target_user_id}>"; attach = "images/nobitches.png"
            case 8: text = f"😭"; attach = "images/keeganid.png"
            case 9: text = "goober"; attach = "images/goober.png"

        if attach:
            message = await channel.send(text, file = nc.File(attach))

            if attach == "images/goober.png":
                await asyncio.sleep(2)
                await message.delete()
                await channel.send("sorry... :/")

        else:
            await channel.send(text)

random_messages.start()
bot.run(config.token)