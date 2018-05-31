import discord
from discord.ext import commands
import asyncio

client = discord.Client()

@client.event
async def on_ready():
    pass
    


@client.event
async def on_message(message):
    if message.content == "bot":
        await client.send_message(message.channel,"Put a name in chat pls.")
    if message.content == "aidan":
        await client.send_message(message.channel,"Amen")
    if message.content == "bar":
        await client.send_message(message.channel,"The orangutan")
    if message.content == "mort":
        await client.send_message(message.channel,"Fortnite pro")
    if message.content == "subject":
        await client.send_message(message.channel,"Never mention subject ever again")
    if message.content == "olly":
        await client.send_message(message.channel,"Olly is fat")
    if message.content == "kieran":
        await client.send_message(message.channel,"The skinny roadman")
    if message.content == "ryan":
        await client.send_message(message.channel,"The massive retard")
    if message.content == "ledge":
        await client.send_message(message.channel,"Faggy fox")
    if message.content == "josh":
        await client.send_message(message.channel,"Dumb ass")
    if message.content == "knobday":
        await client.send_message(message.channel,"Is a pedo")
    if message.content == "paddy":
        await client.send_message(message.channel,"Ultimate rage case")
    if message.content == "lindon":
        await client.send_message(message.channel,"The cool kid")


client.run('NDUxMzY0MzQ3MzA2OTY3MDc2.DfAtjg.CN2li1siAJY2jDSZB-ShFI1t3ow')

