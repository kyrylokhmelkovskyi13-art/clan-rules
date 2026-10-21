import os
import asyncio
from aiohttp import web
import disnake
from disnake.ext import commands

# --- WEB SERVER FOR RENDER HEALTH CHECKS ---
async def handle(request):
    return web.Response(text="Oracle Rules & Perks Bot is running!")

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
BOOSTER_COLOR = disnake.Color.from_rgb(255, 115, 250)  # Рожевий колір бусту
CLAN_LOGO_URL = "https://cdn.discordapp.com/attachments/1562156677946413146/1562346664382042112/a_fe9fab8ec421d49f0940f9c8f36f1805.webp"

TICKETS_CHANNEL_ID = 1537926801211523195
BOOSTER_ROLE_ID = 1538188830069235736

def create_rules_embeds():
    # 1. Header Embed
    header = disnake.Embed(
        title="✨   O R A C L E   C L A N   R U L E S   ✨",
        description=(
            "Welcome to **ORACLE**! Please read and strictly follow all server rules listed below.\n"
            "Ignorance of the rules is not an excuse for breaking them."
        ),
        color=MAIN_COLOR
    )
    header.set_thumbnail(url=CLAN_LOGO_URL)

    # 2. Part 1 (Rules 1 - 10)
    e1 = disnake.Embed(title="📜 PART 1 — GENERAL CONDUCT & SECURITY", color=MAIN_COLOR)
    
    e1.add_field(
        name="1. No Problematic Discussions",
        value="• No discussions regarding Politics, Religion, hate speech, or disrespectful behavior.",
        inline=False
    )
    e1.add_field(
        name="2. No NSFW",
        value="• Explicit and adult content is strictly prohibited.",
        inline=False
    )
    e1.add_field(
        name="3. No Spamming",
        value="• Avoid repeatedly sending similar messages, emojis, or media.",
        inline=False
    )
    e1.add_field(
        name="4. No Racism",
        value="• Racial jokes, discriminatory discussions, media, and slurs are strictly banned.",
        inline=False
    )
    e1.add_field(
        name="5. No Ban Evasion",
        value="• Using alt accounts to avoid in-game or server bans will result in a permanent ban.",
        inline=False
    )
    e1.add_field(
        name="6. No Doxxing",
        value="• Sending a member's personal information without their express permission is prohibited.",
        inline=False
    )
    e1.add_field(
        name="7. No Alt Accounts",
        value="• Allowing your alts or bots to join the server without permission is not allowed.",
        inline=False
    )
    e1.add_field(
        name="8. Have Common Sense",
        value="• Act sensibly; not everything should have to be explicitly explained.",
        inline=False
    )
    e1.add_field(
        name="9. No Harassment",
        value="• Acting aggressively, arguing, or failing to stop when asked in member DMs.",
        inline=False
    )
    e1.add_field(
        name="10. No Advertising",
        value="• Encouraging members to leave Oracle, self-advertising, or sending server invite links.",
        inline=False
    )

    # 3. Part 2 (Rules 11 - 20)
    e2 = disnake.Embed(title="🔒 PART 2 — COMMUNITY & SERVER POLICIES", color=MAIN_COLOR)

    e2.add_field(
        name="11. No Illegal Content",
        value="• Pirated materials and genuine discussions of illegal substances are forbidden.",
        inline=False
    )
    e2.add_field(
        name="12. No Excessive Behavior",
        value="• Disruptive behavior, begging for items/DMs, impersonation, threats, or romantic spam.",
        inline=False
    )
    e2.add_field(
        name="13. No Swearing",
        value="• Severe profanity (f-word, a-word) is prohibited. Bypassing words (e.g., tf, lmao) is allowed.",
        inline=False
    )
    e2.add_field(
        name="14. Do Not Reveal Personal Information",
        value="• Always call people by their Discord display name. Do not share real names or account passwords.",
        inline=False
    )
    e2.add_field(
        name="15. Listen to the Mods",
        value="• Follow staff instructions immediately. Do not ping trial mods or higher without a valid reason.",
        inline=False
    )
    e2.add_field(
        name="16. No IRL Stuff",
        value="• Do not discuss school or real-life activities (e.g., 'yo rn its math class').",
        inline=False
    )
    e2.add_field(
        name="17. Speak English ONLY",
        value="• All public chat communication must strictly remain in English.",
        inline=False
    )
    e2.add_field(
        name="18. Restricted Channels",
        value="• Do NOT post messages in <#1538243617502527498>.",
        inline=False
    )
    e2.add_field(
        name="19. Do NOT Ping Owners",
        value="• Do not ping owners without a valid reason. Make a ticket or DM instead.",
        inline=False
    )
    e2.add_field(
        name="20. Discord TOS",
        value="• Do not violate official Discord Terms of Service.",
        inline=False
    )

    e2.set_footer(text="ORACLE Clan • Follow the rules and enjoy your stay!", icon_url=CLAN_LOGO_URL)

    return [header, e1, e2]

# --- COMMANDS ---

@bot.command(name="post_rules")
@commands.has_permissions(administrator=True)
async def post_rules(ctx):
    await ctx.message.delete()
    embeds = create_rules_embeds()
    await ctx.send(embeds=embeds)

@bot.command(name="post_booster_perks")
@commands.has_permissions(administrator=True)
async def post_booster_perks(ctx):
    await ctx.message.delete()

    embed = disnake.Embed(
        title="🚀   S E R V E R   B O O S T E R   P E R K S   🚀",
        description=(
            "Boost our server to unlock exclusive perks and rewards!\n"
            "Your support helps the **ORACLE** community grow."
        ),
        color=BOOSTER_COLOR
    )
    embed.set_thumbnail(url=CLAN_LOGO_URL)

    embed.add_field(
        name="💎 1 BOOST PERKS",
        value=(
            "> 💰 **Extra Entries** in giveaways\n"
            "> ⚡ **Bypass Slowmode** in chat channels\n"
            "> 😃 **Ability to change** your nickname"
        ),
        inline=False
    )

    embed.add_field(
        name="🔥 2 BOOSTS PERKS",
        value=(
            "> 🤩 **1 Custom Emoji** added to the server\n"
            "> 👻 **Custom Role** (custom color & emoji next to name)\n"
            "> 😁 **1 Custom Sticker** added to the server"
        ),
        inline=False
    )

    embed.add_field(
        name="⚠️ IMPORTANT NOTE",
        value="> Perks will be lost if you leave or unboost the server *(added emoji/sticker will stay)*.",
        inline=False
    )

    embed.add_field(
        name="🎟️ HOW TO CLAIM",
        value=f"> Open a ticket in <#{TICKETS_CHANNEL_ID}> to claim your perks!\n\n*Make spear happy :3*",
        inline=False
    )

    embed.set_footer(text="ORACLE Clan • Thank you for boosting!", icon_url=CLAN_LOGO_URL)

    await ctx.send(content=f"<@&{BOOSTER_ROLE_ID}> **BOOSTER PERKS** 🚀", embed=embed)

@bot.event
async def on_ready():
    print(f"Bot logged in as {bot.user}")

async def main():
    await start_web_server()
    token = os.getenv("BOT_TOKEN")
    if not token:
        print("ERROR: BOT_TOKEN is missing!")
        return
    await bot.start(token)

if __name__ == "__main__":
    asyncio.run(main())
