from discord_slash.utils.manage_commands import create_choice

GUILDS_PRONOUN_ROLES = {
    # Discord Developer Discord
    844686108125429801: {
        "he-him": 846008528174579742,
        "she-her": 846008548563091486,
        "they-them": 846008568620122182,
        "any": 846008593802461204,
        "ask": 846008616758018088,
    },
    # Discord Moderator Discord
    667560445975986187: {
        "he-him": 740020232315207770,
        "she-her": 740020247192404008,
        "they-them": 740020260521902193,
        "any": 834100284597862456,
        "ask": 834156042283253760,
    },
    # Moderator Mentorship Community
    813988123260092416: {
        "he-him": 813988123260092421,
        "she-her": 813988123260092420,
        "they-them": 813988123260092419,
        "ask": 846009253332254730,
        "any": 846009307627520011,
    },
}

PRONOUN_OPTIONS = [
    create_choice(
        value="he-him",
        name="He/Him",
    ),
    create_choice(
        value="she-her",
        name="She/Her",
    ),
    create_choice(
        value="they-them",
        name="They/Them",
    ),
    create_choice(
        value="any",
        name="Any Pronouns",
    ),
    create_choice(
        value="ask",
        name="Ask for Pronouns",
    ),
]

DMA_API_URL = (
    "https://discordmoderatoracademy.zendesk.com/api/v2/help_center/en-us/articles"
)
DMA_TITLE_REGEX = r"^\d\d\d:\s.*$"
DMA_SERIES_NAMES = {
    1: "Basics",
    2: "Setup and Function",
    3: "Advanced Community Management",
    4: "Moderation Seminars",
    5: "Graduate Classes",
}
DMA_CATEGORY_NAMES = {
    0: "Foundational Understanding",
    1: "Human Moderation",
    2: "Bots and Automation",
    3: "Community Management and Growth",
    4: "Advanced Topics",
    5: "External Services",
}

AUTOROLE_CONFIG = {
    813988123260092416: {
        "DISCORD": 813988123272151050,
        "MODERATOR": 813988123260092423,
        "MEMBER": 813988123260092422,
    },
    667560445975986187: {
        "DISCORD": 667876482982477855,
        "MODERATOR": 808643136771457044,
        "MEMBER": 687070754671558718,
    },
}

BOT_DEVS = [
    165023948638126080,
    141288766760288256,
    249287049482338305
]
