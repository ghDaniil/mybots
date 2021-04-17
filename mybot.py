# discord_webhook import DiscordWebhook, DiscordEmbed
import conf
import discord
from discord.ext import commands
import img_handler as imhl
import os
# 
# 
# 

# webhook = DiscordWebhook(url=conf.webhook_URL)# 



# webhook.set_content("danil)hello")# 



# embed = DiscordEmbed()
# embed.set_author(
#     name="danil",
#     icon_url = "https://www.logolynx.com/images/logolynx/7b/7b0dfa3b959ffbdb99667da77b20a70b.png%22,# 

# )
# embed.set_title("это данил")
# embed.set_video(
#     url="https://www.youtube.com/watch?v=VQ7lKPSUc2g",
#     height="200",
#     width="300"

# )# 


# webhook.add_embed(embed)# 

# webhook.execute()
intense = discord.Intents.default()
intense.members = True

client = discord.Client(intents=intense)
myDefault = 825339772032778281


@client.event
async def on_message(message):
    #<Message 
    #id=825339001132417045 
    #channel=<TextChannel id=822806350886207542 name='флудильня' position=0 nsfw=False news=False category_id=822806350886207539> type=<MessageType.default: 0> author=<Member id=825313853243129876 name='daniilprogromist' discriminator='0958' bot=False nick=None guild=<Guild id=822806350886207538 name='Bots' shard_id=None chunked=False member_count=29>> flags=<MessageFlags value=0>>
    if message.author == client.user:
        return
    if message.author.bot:
        return
# <Message id=827859492376150017 channel=<TextChannel id=825339772032778281 name='danilulan-bot' position=11 nsfw=False news=False category_id=825215092731412490> type=<MessageType.default: 0> 
# author=<Member id=827842775193485312 name='daniil2' discriminator='5474' bot=False nick=None guild=<Guild id=822806350886207538 name='Bots' shard_id=None chunked=False member_count=35>> flags=<MessageFlags value=0>>
    global myDefault    
    if message.channel.id == myDefault:
        msg = None

        ctx = message.content.split(" ", maxsplit=1)
        
        # 1
        if message.content == "/hello":
            msg = f'hello, {message.author.name}. Am not allone! My name {client.user.name}'
        # 2
        elif message.content =="/about_me":
            msg = f'he your {message.author.name}, {message.author.id}'
            if message.author.nick:
                msg = f'he your {message.author.name}, {message.author.id}, {message.author.nick}'
        # 3
        elif ctx[0] == "/repeat":
            msg = ctx[1]
        # 5
        elif message.content == "/get_members":
            msg =""
            if message.author.guild.name == "Bots" :
                for idx, member in list(enumerate(message.author.guild.members)):
                    msg += f'{idx+1}. {member.name} { f"[{member.nick}]" if member.nick else ""}-{member.id}\n'
        # 4
        elif ctx[0] == "/get_member":
            if message.author.guild.name == "Bots" :
                for idx, member in list(enumerate(message.author.guild.members)):
                    if ctx[1] == member.name or int(ctx[1]) == member.id :
                        msg= f'есть такой: {member.name}, {member.id}, {member.nick}'
                        break
                else:
                    msg = f'нету или не верно написан id,name'
        # 6
        elif message.content == "/get_channels":
            msg =""
            for idx, channel in list(enumerate(message.author.guild.channels)):
                print(channel)
                msg += f'{idx+1}. {channel.name} - id({channel.id})\n'
        # 7
        elif ctx[0] == "/goto" :
            if message.author.guild.name == "Bots" :
                for idx, channel in list(enumerate(message.author.guild.channels)):
                    if ctx[1] == channel.name or ctx[1] == str(channel.id) :
                        myDefault = ctx[1]
                        break
                else:
                    msg = f'нету  этого места проверте id, name'

        if msg != None:
            await message.channel.send(msg)








bot = commands.Bot(command_prefix="!", intents=intense)

@bot.command(name = "hello")
async def command_hello(ctx, *args):
    message = "".join(args)
    if ctx.channel.id ==  825339772032778281:
        msg = f'hello {message}'
        await ctx.channel.send(msg)

@bot.command(name = "about")
async def command_about(ctx, *args):
    if ctx.channel.id ==  825339772032778281:
        msg = f'he your {ctx.author.name}, {ctx.author.id}'
        await ctx.channel.send(msg)

@bot.command(name = "repeat")
async def command_repeat(ctx, *args):
    if ctx.channel.id ==  825339772032778281:
        message = "".join(args)
        msg = message
        await ctx.channel.send(msg)

@bot.command(name = "members")
async def command_members(ctx, *args):
    global myDefault
    if ctx.channel.id ==  myDefault:
        msg=""
        for idx, member in list(enumerate(ctx.author.guild.members)):
            msg += f'{idx+1}. {member.name} { f"[{member.nick}]" if member.nick else ""}-{member.id}\n'
        await ctx.channel.send(msg)

@bot.command(name = "member")
async def command_member(ctx, member:discord.Member=None ):
    msg=None
    global myDefault
    if ctx.channel.id ==  myDefault:

        if member:
            msg= f'есть такой: {member.name}, {member.id}, {"({member.nick})" if member.nick else "" }'


        if msg == None:
            await ctx.channel.send("error")
        else:
            await ctx.channel.send(msg)

@bot.command(name = "vs")
async def command_vs(ctx, f1:discord.Member=None, f2:discord.Member=None  ):
    msg=None
    global myDefault
    if ctx.channel.id ==  myDefault:
        if f1 and f2:
            await imhl.vs_create(f1.avatar_url,f2.avatar_url)
            await ctx.channel.send( file=discord.File(os.path.join("./img/result.png")))


@bot.command(name = "channels")
async def command_channels(ctx, *args):
    if ctx.channel.id ==  825339772032778281:
        msg =""
        for idx, channel in list(enumerate(ctx.author.guild.channels)):
            msg += f'{idx+1}. {channel.name} - id({channel.id})\n'
    await ctx.channel.send(msg)
      
@bot.command(name = "goto")  
async def command_goto(ctx, *args):
    message = " ".join(args)
    global myDefault  
    if ctx.channel.id ==  825339772032778281:
        if ctx.author.guild.name == "Bots" :
            msg ="покеда"
            for idx, channel in list(enumerate(ctx.author.guild.channels)):
                if message == channel.name or message == str(channel.id) :
                    myDefault = message
                    print(myDefault)
                    print(message)
                    break
            else:
                msg = f'нету  этого места проверте id, name'
        await ctx.channel.send(msg)




bot.run(conf.bot_token)
client.run(conf.bot_token)