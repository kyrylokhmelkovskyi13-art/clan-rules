import os
import asyncio
from aiohttp import web
import disnake
from disnake.ext import commands

# --- WEB SERVER FOR RENDER ---
async def handle(request):
    return web.Response(text="Oracle Rules Bot is online!")

async def start_web_server():
    app = web.Application()
    app.router.add_get("/", handle)
    runner = web.AppRunner(app)
    await runner.setup()
    
    port = int(os.environ.get("PORT", 8080))
    site = web.TCPSite(runner, "0.0.0.0", port)
    await site.start()

# --- MAIN BOT CODE ---
intents = disnake.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix="!", intents=intents)

MAIN_COLOR = disnake.Color.from_rgb(255, 120, 0)
CLAN_LOGO_URL = "https://cdn.discordapp.com/attachments/1562156677946413146/1562346664382042112/a_fe9fab8ec421d49f0940f9c8f36f1805.webp"

def create_rules_embeds():
    # Header Embed
    embed1 = disnake.Embed(
        title="✨   O R A C L E   C L A N   R U L E S   ✨",
        description=(
            "Welcome to **ORACLE**! Please read and strictly follow all server rules listed below.\n"
            "Ignorance of the rules is not an excuse for breaking them."
        ),
        color=MAIN_COLOR
    )
    embed1.set_thumbnail(url=CLAN_LOGO_URL)

    # General Conduct
    embed1.add_field(
        name="📜 GENERAL CONDUCT & RESPECT",
        value=(
            "> **1. No Problematic Discussions** — No Politics, Religion, hate speech, or disrespectful behavior.\n"
            "> **2. No NSFW** — Explicit content is strictly prohibited.\n"
            "> **3. No Spamming** — Avoid sending repetitive messages, emojis, or media.\n"
            "> **4. No Racism** — Zero tolerance for racial slurs, jokes, or discriminatory discussions.\n"
            "> **8. Common Sense** — Act maturely. Not every minor detail needs an explicit rule.\n"
            "> **9. No Harassment** — Aggressive behavior, toxicity, or uninvited DM harassment is forbidden.\n"
            "> **12. No Excessive Behavior** — Excessive swearing, begging, impersonation, threats, or romantic spam are not allowed.\n"
            "> **13. No Swearing** — Severe profanity (f-word, a-word) is prohibited. Bypassing words (e.g., *tf, lmao*) is allowed."
        ),
        inline=False
    )

    # Security & Privacy
    embed2 = disnake.Embed(color=MAIN_COLOR)
    embed2.add_field(
        name="🔒 SECURITY & PRIVACY",
        value=(
            "> **5. No Ban Evasion** — Using alt accounts to bypass server or in-game bans will result in a permanent ban.\n"
            "> **6. No Doxxing** — Sharing anyone's personal information without explicit consent is strictly banned.\n"
            "> **7. No Alt Accounts** — Unapproved alt accounts or bot joins are not permitted.\n"
            "> **14. Personal Privacy** — Do not share real names; always address members by Discord display names. Account sharing/password sharing is forbidden.\n"
            "> **16. No IRL Info** — Do not discuss real-life schedules or private activities (e.g., *'im in math class right now'*)."
        ),
        inline=False
    )

    # Server Policy & Advertising
    embed2.add_field(
        name="🌐 SERVER POLICY & COMMUNITY",
        value=(
            "> **10. No Advertising** — Unsolicited DM advertising, server invites, or poaching clan members is forbidden.\n"
            "> **11. No Illegal Content** — No piracy, illegal substances, or dangerous material.\n"
            "> **15. Listen to Staff** — Always follow instructions from Moderators and Staff. Do not ping trial mods/staff without reason.\n"
            "> **17. English ONLY** — All public channels are strictly English-only.\n"
            "> **18. Restricted Channels** — Do NOT post messages in <#1538243617502527498>.\n"
            "> **19. Owner Pings** — Do not ping owners directly without valid reasons; open a ticket or DM instead.\n"
            "> **20. Discord TOS** — Must comply with all official Discord Terms of Service."
        ),
        inline=False
    )
    embed2.set_footer(text="ORACLE Clan • Follow the rules and enjoy your stay!", icon_url=CLAN_LOGO_URL)

    return [embed1, embed2]

@bot.command(name="post_rules")
@commands.has_permissions(administrator=True)
async def post_rules(ctx):
    await ctx.message.delete()
    embeds = create_rules_embeds()
    await ctx.send(content="||@everyone||", embeds=embeds)

@bot.event
async def on_ready():
    print(f"Rules Bot logged in as {bot.user}")

async def main():
    await start_web_server()
    token = os.getenv("BOT_TOKEN")
    if token:
        await bot.start(token)

if __name__ == "__main__":
    asyncio.run(main())
