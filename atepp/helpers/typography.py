async def send_long_message(channel, message):
    for i in range(0, len(message), 2000):
        await channel.send(message[i:i+2000])