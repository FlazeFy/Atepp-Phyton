from modules.user.models.models_user import user
from configs.configs import con
from sqlalchemy import select
import json

async def get_my_profile(id:str):
    # Query builder
    query = select(
        user.c.username,
        user.c.email,
        user.c.company,
        user.c.social_media,
        user.c.phone,
        user.c.created_at,
        user.c.updated_at
    ).where(
        user.c.id == id,
    )

    # Exec
    result = con.execute(query)
    data = result.first()

    res = (
        f"**Signed in as {data.username}**\n"
        f"Email : {data.email}\n"
        f"Company : {data.company or '-'}\n"
        f"Phone Number : {data.phone or '-'}\n"
        f"Joined at : {data.created_at}\n"
        f"Updated at : {data.updated_at or '-'}\n\n"
        f"**Social Media :**\n"
    )

    for socmed in data.social_media:
        res += f"- {socmed['socmed_name'].capitalize()}: {socmed['socmed_url']}\n"

    return res