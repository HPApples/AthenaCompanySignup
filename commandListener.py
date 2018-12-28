import discord
import sqlite3
import event

from discord.ext import commands

class CommandListener:

    def __init__(self, bot):
        self.bot = bot

    # Create event command
    @commands.command(pass_context=True, name="create", brief="")
    async def createEvent(self, ctx):
        # Get into from context
        info = ctx.message.content
        info = info.split(" ")

        # Exit if not enough info
        if (len(info) < 2):
            ctx.send("No date specified")
            return

        # Get event data
        title = "Operation"
        date = info[1]
        color = 0xFF4500
        eventchannel = self.bot.get_channel(502824760036818964)
        thing = (ctx.guild.emojis[46])

        # Create event
        event = event.Event(title, date, color, ctx.guild.emojis)
        eventEmbed = event.createEmbed()
        eventMessage = await eventchannel.send(embed=eventEmbed)
        
        # Put message ID in footer
        eventEmbed = eventMessage.embeds[0]
        eventEmbed.set_footer(text="Message ID: " + str(eventMessage.id))
        await eventMessage.edit(embed=eventEmbed)

        # Add reactions
        await eventMessage.add_reaction(thing)

    # Add additional role to event command
    @commands.command(pass_context=True, name="addrole", brief="")
    async def addRole(self, ctx):
        # Get into from context
        info = ctx.message.content
        info = info.split(" ")

        # Get data
        eventID = info[1]
        roleList = info[2:]
        role = ""
        for word in info:
            role += word + " "

        eventchannel = self.bot.get_channel(502824760036818964)

        try:
            eventMessage = await eventchannel.get_message(int(eventID))
        except:
            await ctx.send("That event does not exist.")
            return

        eventEmbed = eventMessage.embeds[0]

        fields = eventEmbed.fields
        for field in fields:
            if field.name == "Additional Roles":
                additionalRoles = field.value + " \n" + str(role)
                eventEmbed.remove_field(3)
            else:
                additionalRoles =  ":one: " + role
                await eventMessage.add_reaction(emoji=":one:")

        otherRoles = additionalRoles.split("\n")
        number = len(otherRoles)
        await ctx.send(number)

        eventEmbed.add_field(name="Additional Roles", value=additionalRoles)
        await eventMessage.edit(embed=em)

def setup(bot):
    bot.add_cog(CommandListener(bot))