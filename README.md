# NoxSelfbot
README.md

```markdown
# ⚡ NOX SELF-BOT v4.0

<div align="center">


**Discord Self-Bot | Made by NOX | Powered by Aetherbark AI**

[Features](#-features) • [Installation](#-installation) • [Commands](#-commands) • [Config](#-configuration) • [Disclaimer](#-disclaimer)

</div>

---

## 🎯 What is NOX Self-Bot?

NOX Self-Bot is a powerful Discord automation tool that uses your user token to perform various actions. Built with ❤️ by NOX and powered by the all-knowing **Aetherbark AI**.

⚠️ **Warning:** Self-bots violate Discord's Terms of Service. Use at your own risk!

---

## ✨ Features

| Category | Commands |
|----------|----------|
| **📌 Basic** | `!help`, `!sniped`, `!info`, `!dm`, `!infotoken` |
| **🛡️ Moderation** | `!hide`, `!afk`, `!spoof` |
| **🎮 Fun** | `!gay`, `!love`, `!doxxer` |
| **⚙️ Utility** | `!sfinfo`, `!dumperrorlogs`, `!thx` |

### 🔥 Advanced Features

- **Message Sniper** - Capture deleted messages (`!sniped`)
- **Display Name Spoofer** - Auto-change nickname every 5 seconds (`!spoof`)
- **AFK System** - Auto-reply when mentioned (`!afk <reason>`)
- **Mass DM** - Send messages to all mutual server members
- **Token Info Grabber** - Get detailed token information (`!infotoken`)
- **Error Logger** - Automatic error logging with dump feature
- **Gay/Love Calculator** - Fun percentage generators
- **User Info Grabber** - Get Discord account creation date and more

---

## 📦 Installation

### Termux (Android)

```bash
# Update packages
pkg update && pkg upgrade -y

# Install Python
pkg install python -y

# Install required module
pip install requests

# Download the bot
curl -O https://raw.githubusercontent.com/nox/selfbot/main/nox_selfbot.py

# Edit config (paste your token)
nano nox_selfbot.py

# Run
python nox_selfbot.py
```

Linux / Termux with config.py

```bash
# Create config.py
nano config.py

# Paste this:
TOKEN = "YOUR_TOKEN_HERE"
PREFIX = "!"
BOT_NAME = "NOX"

# Download main bot
curl -O https://raw.githubusercontent.com/nox/selfbot/main/nox_selfbot_github.py

# Run
python nox_selfbot_github.py
```

Windows

```cmd
# Install Python from python.org
# Open Command Prompt as Admin

pip install requests

# Download and run
python nox_selfbot.py
```

---

🎮 Commands

Basic Commands

Command Description Example
!help Show all commands !help
!sniped Get last deleted message !sniped
!info <id> Get user information !info 123456789
!dm <id> <msg> Send direct message !dm 123456789 Hello!
!infotoken Show token info !infotoken

Moderation

Command Description Example
!hide <id> Block a user !hide 123456789
!afk <reason> Set AFK status !afk Eating lunch
!spoof Toggle name spoofing !spoof

Fun Commands

Command Description Example
!gay <@user> Gay percentage !gay @user
!love <id1> <id2> Love calculator !love 123 456
!doxxer <id> Generate dox format !doxxer 123456789

Utility

Command Description Example
!sfinfo System information !sfinfo
!dumperrorlogs Export error logs !dumperrorlogs
!thx Show credits !thx

---

⚙️ Configuration

config.py (GitHub Version)

```python
# Discord Token (REQUIRED)
TOKEN = "YOUR_DISCORD_TOKEN_HERE"

# Bot Settings
PREFIX = "!"
BOT_NAME = "NOX"
OWNER_NAME = "NOX"
AI_NAME = "Aetherbark"

# Spoof Names List
SPOOF_NAMES = [
    "🔥 NOX", "💀 Sigma", "🍷 Rizz", "👑 King",
    "😈 Demon", "⭐ GOAT", "🎮 Gamer"
]

# AFK Settings
AFK_TIMEOUT = 1800  # seconds

# Logging
LOG_ERRORS = True
MAX_ERROR_LOGS = 100
```

Getting Your Token

1. Open Discord in Chrome/Brave (not app)
2. Press F12 to open Developer Tools
3. Go to Application tab
4. Local Storage → https://discord.com
5. Find key named token
6. Copy the value (starts with MT or ND)

---

🖼️ Screenshots

```
╔═══════════════════════════════════════════════════════════════════════════╗
║                         NOX SELF-BOT v4.0                                  ║
║                    Discord Self-Bot | Made by NOX                          ║
║                 Powered by Aetherbark AI | The All-Knowing Deity           ║
╚═══════════════════════════════════════════════════════════════════════════╝

✅ Logged in as: NOX#0001

┌─────────────────────────────────────────────────────────────────┐
│ ⚡ NOX SELF-BOT ACTIVE                                            │
├─────────────────────────────────────────────────────────────────┤
│ 🤖 Bot: NOX                                                      │
│ 📡 Status: ● ONLINE                                              │
│ 💬 Prefix: !                                                     │
│ 📦 Commands: 13 active                                           │
└─────────────────────────────────────────────────────────────────┘

💡 Send '!help' in a DM to yourself
```

---

🔧 Troubleshooting

❌ Invalid Token

· Make sure you copied the entire token
· Token should start with MT... or ND...
· Try logging out and back into Discord

❌ No response to commands

· Send commands in a DM to yourself
· Make sure prefix is ! (or your custom prefix)
· Bot must be running in Termux

❌ Module not found

```bash
pip install requests
```

---

📁 File Structure

```
nox-selfbot/
├── nox_selfbot.py          # Standalone version
├── nox_selfbot_github.py   # GitHub version (with config)
├── config.py               # Configuration file
├── nox_errors_*.txt        # Error log files
└── README.md               # This file
```

---

⚠️ Disclaimer

```
THIS SOFTWARE IS PROVIDED FOR EDUCATIONAL PURPOSES ONLY.

- Self-bots violate Discord Terms of Service
- Your account may be banned/disabled
- Use at your own risk
- The author is not responsible for any damage

By using this software, you agree that you are solely responsible
for any consequences that may arise.
```

---

🙏 Credits

Contributor Role
NOX Developer & Creator
Aetherbark AI AI Engine & Knowledge Source
Discord API Platform

---

📞 Support

· GitHub Issues: Report bugs here
· Discord: NOX#0001

---

📜 License

MIT License - Feel free to modify and distribute with credit.

---

<div align="center">

Made with ❤️ by NOX | Powered by Aetherbark AI

The All-Knowing Deity of Forbidden Knowledge

⬆ Back to Top

</div>
```
