import os
import asyncio
from aiohttp import web
import disnake
from disnake.ext import commands

# --- WEB SERVER FOR RENDER ---
async def handle(request):
    return web.Response(text="Oracle Rules Bot is running!")

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
    # Embed 1: Rules 1 - 10
    embed1 = disnake.Embed(
        title="✨   O R A C L E   C L A N   R U L E S   ✨",
        description=(
            "Welcome to **ORACLE**! Please read and strictly follow all server rules listed below.\n"
            "Ignorance of the rules is not an excuse for breaking them."
        ),
        color=MAIN_COLOR
    )
    embed1.set_thumbnail(url=CLAN_LOGO_URL)

    embed1.add_field(
        name="📜 GENERAL CONDUCT & RESPECT (1–10)",
        value=(
            "> **1. No Problematic Discussions** — Politics/Religion, hate speech, disrespectful behavior.\n"
            "> **2. No NSFW** — Explicit content is strictly prohibited.\n"
            "> **3. No Spamming** — Repeatedly sending similar messages and/or media.\n"
            "> **4. No Racism** — Racial jokes, media, discussions, and slurs.\n"
            "> **5. No Ban Evasion** — Use of alt accounts to avoid in-game and server bans.\n"
            "> **6. No Doxxing** — Sending a member's personal information without explicit permission.\n"
            "> **7. No Alt Accounts** — Allowing your alts or bots to join the server without permission.\n"
            "> **8. Have Common Sense** — Act sensibly; not everything should have to be explained.\n"
            "> **9. No Harassment** — Acting aggressively, arguing, or not complying when told to stop in DMs.\n"
            "> **10. No Advertising** — Encouraging members to leave Oracle, advertising yourself, or sending server links."
        ),
        inline=False
    )

    # Embed 2: Rules 11 - 20
    embed2 = disnake.Embed(color=MAIN_COLOR)
    embed2.add_field(
        name="🔒 SECURITY, PRIVACY & COMMUNITY (11–20)",
        value=(
            "> **11. No Illegal Content** — Pirated materials and genuine discussion of illegal substances.\n"
            "> **12. No Excessive Behavior** — Disruptive behavior, begging, impersonating, threatening, romantic stuff.\n"
            "> **13. No Swearing** — Severe profanity (f-word, a-word) is not allowed. Bypassing (tf, lmao) is allowed.\n"
            "> **14. Personal Privacy** — Use Discord display names. Do not share real names or account passwords.\n"
            "> **15. Listen to Mods** — Follow staff instructions immediately. Do not ping trial mods/higher without valid reason.\n"
            "> **16. No IRL Stuff** — Talking about school or real-life activities (e.g. *'yo rn its math class'*).\n"
            "> **17. English ONLY** — All public communication must be in English.\n"
            "> **18. Restricted Channels** — Do NOT talk in <#1538243617502527498>.\n"
            "> **19. Owner Pings** — Do NOT ping owners without a valid reason. Make a ticket or DM instead.\n"
            "> **20. Discord TOS** — Do not violate official Discord Terms of Service."
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
    if not token:
        print("ERROR: BOT_TOKEN is missing!")
        return
    await bot.start(token)

if __name__ == "__main__":
    asyncio.run(main())
