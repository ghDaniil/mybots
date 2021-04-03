# discord_webhook import DiscordWebhook, DiscordEmbed
import conf
import discord
# 
# 
# 

# webhook = DiscordWebhook(url=conf.webhook_URL)# 
# 
# 

# webhook.set_content("danil)hello")# 
# 
# 

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
#
# )# 
# 

# webhook.add_embed(embed)# 

# webhook.execute()
intense = discord.Intents.default()
intense.members = True

client = discord.Client(intents=intense)



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

    if message.channel.id == 825339772032778281:
        ctx = message.content.split(" ", maxsplit=1)
        msg = None
        if message.content == "/hello":
            msg = f'hello, {message.author.name}. Am not allone! My name {client.user.name}'
        elif message.content =="/about_me":
            msg = f'he your {message.author.name}, {message.author.id}'
            if message.author.nick:
                msg = f'he your {message.author.name}, {message.author.id}, {message.author.nick}'
        elif ctx[0] == "/repeat":
            msg = ctx[1]
        elif message.content == "/get_members":
            msg ="1"
            if message.author.guild.name == "Bots" :
                for idx, member in list(enumerate(message.author.guild.members)):
                    msg += f'{idx+1}. {member.name} { f"[{member.nick}]" if member.nick else ""}-{member.id}\n'
        elif ctx[0] == "/get_member":
            print(1)
            if message.author.guild.name == "Bots" :
                print(2)
                i = ctx[1]
                a = message.author.guild.members
                for n in a:
                    print(3)
                    if i == a[n]:
                        print(4)
                        msg = f'есть такой'
                    elif i != a[n] and a[n] == len(a):
                        msg - f'такова нет'
        if msg != None:
            await message.channel.send(msg)



client.run(conf.bot_token)