from modules.project.repositories.queries_project import get_all_my_project, get_endpoint_by_project, get_history_run_endpoint
from modules.dictionary.repositories.queries_dictionary import get_my_dictionary
from modules.user.repositories.queries_user import get_my_profile
from helpers.typography import send_long_message

async def on_message_handler(bot, message):
    if message.author == bot.user:
        return

    if bot.user.mentioned_in(message):
        server_name = message.guild.name if message.guild else 'Unknown Server'
        await message.channel.send(f'Hello! everyone in {server_name}. Im Atepp Bot, what do you want me to do?')
        await message.channel.send('1. Show my project\n2. Show my variable\n3. Show my profile')

    if message.content == '!ping':
        server_name = message.guild.name if message.guild else 'Unknown Server'
        await message.channel.send(f'Pong from {server_name}!')
    elif message.content == '1':
        res = await get_all_my_project()
        await message.channel.send(f"Showing my project :\n\n{res}")
    elif message.content == '2':
        page = 1
        [res, total_page, items_per_page] = await get_my_dictionary(currentPage=page)
        if total_page == 1:
            await message.channel.send(f"Showing my dictionaries :\n\n{res}")
        else:
            while page <= total_page:
                [res, _, _] = await get_my_dictionary(currentPage=page)
                await message.channel.send(f"Showing my dictionaries in Page {page}/{total_page}:\n\n{res}")
                page += 1
    elif message.content == '3':
        res = await get_my_profile(id="2d98f524-de02-11ed-b5ea-0242ac120002")
        await message.channel.send(f"Showing my profile :\n\n{res}")
            
    elif message.content.endswith('/endpoint'):
        project_slug = message.content[:-len('/endpoint')].strip()
        res = await get_endpoint_by_project(project_slug)
        await message.channel.send(f"Opening project {project_slug} :\n\n{res}")
    elif message.content.endswith('/history/run'):
        id = message.content[:-len('/history/run')].strip()
        res = await get_history_run_endpoint(id)
        await send_long_message(message.channel, f"Opening endpoint history with id {id}:\n\n{res}")


