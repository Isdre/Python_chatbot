import discord
import json
import use

token = ""

with open('token.json') as f:
    token = json.load(f)['token']

client = discord.Client()

@client.event
async def on_message(ctx):
    if ctx.author == client.user:
        return
    # print("working")
    x = [ctx.content]
    # print(x)
    response = "".join(use.response_me(x))
    await ctx.channel.send(response)
client.run(token)