from datetime import date, datetime, time, timedelta
import secret

VERSION = 8
# PURGE_ON_CONNECT = False
_test_channel = 530411066585382912
if secret.DEBUG:
    EVENT_CHANNEL = _test_channel
    EVENT_ARCHIVE_CHANNEL = _test_channel
    COMMAND_CHANNEL = _test_channel
    LOG_CHANNEL = _test_channel
    GAME = 'with bugs'
else:
    EVENT_CHANNEL = 824379373217775698
    EVENT_ARCHIVE_CHANNEL = 824379430105251870
    COMMAND_CHANNEL = 824379459918233611
    LOG_CHANNEL = 824379530608508938
    GAME = 'with events'

JSON_FILEPATH = {
    "events":  "database/events.json",
    "archive": "database/archive.json",
}
ADDITIONAL_ROLE_EMOJIS = [
    "\N{DIGIT ONE}\N{COMBINING ENCLOSING KEYCAP}",
    "\N{DIGIT TWO}\N{COMBINING ENCLOSING KEYCAP}",
    "\N{DIGIT THREE}\N{COMBINING ENCLOSING KEYCAP}",
    "\N{DIGIT FOUR}\N{COMBINING ENCLOSING KEYCAP}",
    "\N{DIGIT FIVE}\N{COMBINING ENCLOSING KEYCAP}",
    "\N{DIGIT SIX}\N{COMBINING ENCLOSING KEYCAP}",
    "\N{DIGIT SEVEN}\N{COMBINING ENCLOSING KEYCAP}",
    "\N{DIGIT EIGHT}\N{COMBINING ENCLOSING KEYCAP}",
    "\N{DIGIT NINE}\N{COMBINING ENCLOSING KEYCAP}",
    "\N{KEYCAP TEN}",
    "\N{REGIONAL INDICATOR SYMBOL LETTER A}",
    "\N{REGIONAL INDICATOR SYMBOL LETTER B}",
    "\N{REGIONAL INDICATOR SYMBOL LETTER C}",
    "\N{REGIONAL INDICATOR SYMBOL LETTER D}",
    "\N{REGIONAL INDICATOR SYMBOL LETTER E}",
    "\N{REGIONAL INDICATOR SYMBOL LETTER F}",
    "\N{REGIONAL INDICATOR SYMBOL LETTER G}",
    "\N{REGIONAL INDICATOR SYMBOL LETTER H}",
    "\N{REGIONAL INDICATOR SYMBOL LETTER I}",
    "\N{REGIONAL INDICATOR SYMBOL LETTER J}",
]

# ATTENDANCE_EMOJI = "\N{HEAVY PLUS SIGN}"
ATTENDANCE_EMOJI = None

EXTRA_EMOJIS = [
    # ATTENDANCE_EMOJI
]

PLATOON_SIZES = ['SQUAD', '1PLT', '2PLT']

# Dummy: an empty spacer. An embed can only have either one or three
# items on a line.
# Additional roles are automatically added at the end of the group list
DEFAULT_GROUPS = {

    "SQUAD": [
        "1st Platoon",
        "Dummy",
        "Dummy",

        "Alpha",
        "Alpha",
        "Dummy"
    ],

    "1PLT": [
        "Company",
        "1st Platoon",
        "Dummy",

        "Alpha",
        "Bravo",
        "Charlie"
    ],
    "2PLT": [
        "Battalion",
        "Company",
        "Dummy",

        "1st Platoon",
        "Alpha",
        "Bravo",

        "2nd Platoon",
        "Echo",
        "Foxtrot"
    ]
}

# NOTE: role name equals emote name
DEFAULT_ROLES = {
    "SQUAD": {
        "ZEUS": "1st Platoon",
        "A1": "Alpha",
        "A2": "Alpha",
    },
    "1PLT": {
        "ZEUS": "Company",
        "1PLT": "1st Platoon",
        "FAC": "1st Platoon",
        "RTO": "1st Platoon",

        "A1": "Alpha",
        "A2": "Alpha",
        "B1": "Bravo",
        "B2": "Bravo",
        "C1": "Charlie",
        "C2": "Charlie",
    },
    "2PLT": {
        "ZEUS": "Battalion",
        "CO": "Company",
        "FAC": "Company",
        "RTO": "Company",

        "1PLT": "1st Platoon",
        "A1": "Alpha",
        "B1": "Bravo",
        "C1": "Charlie",
        "D1": "Delta",

        "2PLT": "2nd Platoon",
        "E1": "Echo",
        "F1": "Foxtrot",
        "G1": "Golf",
        "H1": "Hotel",
    },
}

EMOJI_ZEUS = "ZEUS"

# If a user signs off from a role listed in SIGNOFF_NOTIFY_ROLES when
# there is less than SIGNOFF_NOTIFY_TIME left until the operation start,
# a user defined in secrets.py gets notified about that.
SIGNOFF_NOTIFY_TIME = timedelta(days=1)
SIGNOFF_NOTIFY_ROLES = {
    "SQUAD": [
        "A1"
    ],
    "1PLT": [
        "1PLT", "HQ", "A1", "B1", "C1"
    ],
    "2PLT": [
        "CO", "HQ", "1PLT", "2PLT",
        "A1", "B1", "C1", "D1",
        "E1", "F1", "G1", "H1",
    ],
}

DEFAULT_TIME = time(hour=18, minute=45)
WEEK_TIMES = {
  5: time(hour=18, minute=45),  # friday
  6: time(hour=17, minute=45),  # saturday
}