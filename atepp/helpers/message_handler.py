from modules.project.queries_project import get_all_my_project

async def on_message_handler(bot, message):
    if message.author == bot.user:
        return

    if bot.user.mentioned_in(message):
        server_name = message.guild.name if message.guild else 'Unknown Server'
        await message.channel.send(f'Hello! everyone in {server_name}. Im Atepp Bot, what do you want me to do?')
        await message.channel.send('1. Show my project')

    if message.content == '!ping':
        server_name = message.guild.name if message.guild else 'Unknown Server'
        await message.channel.send(f'Pong from {server_name}!')
    elif message.content == '1':
        res = await get_all_my_project()
        await message.channel.send(f"Showing my project :\n\n{res}")

