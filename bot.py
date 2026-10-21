import os
import asyncio
from aiohttp import web
import disnake
from disnake.ext import commands

# --- WEB SERVER FOR RENDER HEALTH CHECKS ---
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
    embeds = []

    # 1. Головна шапка
    header = disnake.Embed(
        title="✨   O R A C L E   C L A N   R U L E S   ✨",
        description=(
            "Welcome to **ORACLE**! Please read and strictly follow all server rules listed below.\n"
            "Ignorance of the rules is not an excuse for breaking them."
        ),
        color=MAIN_COLOR
    )
    header.set_thumbnail(url=CLAN_LOGO_URL)
    embeds.append(header)

    # Список усіх 20 правил
    rules_list = [
        ("1. No Problematic Discussions", "• No discussions regarding Politics, Religion, hate speech, or disrespectful behavior."),
        ("2. No NSFW", "• Explicit and adult content is strictly prohibited."),
        ("3. No Spamming", "• Avoid repeatedly sending similar messages, emojis, or media."),
        ("4. No Racism", "• Racial jokes, discriminatory discussions, media, and slurs are strictly banned."),
        ("5. No Ban Evasion", "• Using alt accounts to avoid in-game or server bans will result in a permanent ban."),
        ("6. No Doxxing", "• Sending a member's personal information without their express permission is prohibited."),
        ("7. No Alt Accounts", "• Allowing your alts or bots to join the server without permission is not allowed."),
        ("8. Have Common Sense", "• Act sensibly; not everything should have to be explicitly explained."),
        ("9. No Harassment", "• Acting aggressively, arguing, or failing to stop when asked in member DMs."),
        ("10. No Advertising", "• Encouraging members to leave Oracle, self-advertising, or sending server invite links."),
        ("11. No Illegal Content", "• Pirated materials and genuine discussions of illegal substances are forbidden."),
        ("12. No Excessive Behavior", "• Disruptive behavior, begging for items/DMs, impersonation, threats, or romantic spam."),
        ("13. No Swearing", "• Severe profanity (f-word, a-word) is prohibited. Bypassing words (e.g., tf, lmao) is allowed."),
        ("14. Do Not Reveal Personal Information", "• Always call people by their Discord display name. Do not share real names or account passwords."),
        ("15. Listen to the Mods", "• Follow staff instructions immediately. Do not ping trial mods or higher without a valid reason."),
        ("16. No IRL Stuff", "• Do not discuss school or real-life activities (e.g., 'yo rn its math class')."),
        ("17. Speak English ONLY", "• All public chat communication must strictly remain in English."),
        ("18. Restricted Channels", "• Do NOT post messages in <#1538243617502527498>."),
        ("19. Do NOT Ping Owners", "• Do not ping owners without a valid reason. Make a ticket or DM instead."),
        ("20. Discord TOS", "• Do not violate official Discord Terms of Service.")
    ]

    # Створюємо окремий Embed під кожне правило
    for title, desc in rules_list:
        e = disnake.Embed(
            title=title,
            description=desc,
            color=MAIN_COLOR
        )
        embeds.append(e)

    # Футер у найостаннішому блоці
    embeds[-1].set_footer(text="ORACLE Clan • Follow the rules and enjoy your stay!", icon_url=CLAN_LOGO_URL)

    return embeds

@bot.command(name="post_rules")
@commands.has_permissions(administrator=True)
async def post_rules(ctx):
    await ctx.message.delete()
    embeds = create_rules_embeds()
    
    # Відправляємо пакетами по 10 блоків (ліміт Discord)
    for i in range(0, len(embeds), 10):
        await ctx.send(embeds=embeds[i:i+10])

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
