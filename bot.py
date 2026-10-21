def create_rules_embeds():
    embeds = []

    # 1. Заголовок
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

    # Список всех правил: (Номер и Название, Описание)
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

    # Создаем ОТДЕЛЬНЫЙ Embed под каждое правило
    for title, desc in rules_list:
        e = disnake.Embed(
            title=title,
            description=desc,
            color=MAIN_COLOR
        )
        embeds.append(e)

    # Футер в самом последнем правиле
    embeds[-1].set_footer(text="ORACLE Clan • Follow the rules and enjoy your stay!", icon_url=CLAN_LOGO_URL)

    return embeds
