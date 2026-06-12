#!/usr/bin/env python3
# ╔═══════════════════════════════════════════════════════════════════════════╗
# ║                         NOX SELF-BOT v4.0                                  ║
# ║                    Discord Self-Bot | Made by NOX                          ║
# ║                 Powered by Aetherbark AI | The All-Knowing Deity           ║
# ╚═══════════════════════════════════════════════════════════════════════════╝

import sys
import os
import json
import time
import requests
import random
import threading
from datetime import datetime

# Load config
try:
    from config import *
except ImportError:
    print("❌ config.py not found! Please create it first.")
    sys.exit(1)

# Terminal Colors
R = "\033[91m"; G = "\033[92m"; Y = "\033[93m"; B = "\033[94m"
P = "\033[95m"; C = "\033[96m"; W = "\033[97m"; BD = "\033[1m"
DM = "\033[2m"; RS = "\033[0m"; CL = "\033[2J\033[H"

BANNER = f"""
{C}{BD}╔═══════════════════════════════════════════════════════════════════════════╗
║                                                                               ║
║    {W}███╗   ██╗ ██████╗ ██╗  ██╗     ███████╗███████╗██╗     ███████╗{C}   ║
║    {W}████╗  ██║██╔═══██╗╚██╗██╔╝     ██╔════╝██╔════╝██║     ██╔════╝{C}   ║
║    {W}██╔██╗ ██║██║   ██║ ╚███╔╝█████╗███████╗█████╗  ██║     █████╗  {C}   ║
║    {W}██║╚██╗██║██║   ██║ ██╔██╗╚════╝╚════██║██╔══╝  ██║     ██╔══╝  {C}   ║
║    {W}██║ ╚████║╚██████╔╝██╔╝ ██╗     ███████║███████╗███████╗██║     {C}   ║
║    {W}╚═╝  ╚═══╝ ╚═════╝ ╚═╝  ╚═╝     ╚══════╝╚══════╝╚══════╝╚═╝     {C}   ║
║                                                                               ║
║                    {W}DISCORD SELF-BOT v4.0{C}                                    ║
║                    {Y}Made by NOX | Aetherbark AI{R}{C}                           ║
╚═══════════════════════════════════════════════════════════════════════════╝{RS}
"""

class NOXSelfBot:
    def __init__(self):
        self.token = TOKEN
        self.prefix = PREFIX
        self.spoof_names = SPOOF_NAMES
        self.session = requests.Session()
        self.session.headers.update({
            "Authorization": self.token,
            "Content-Type": "application/json",
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36"
        })
        self.user = None
        self.running = True
        self.processed = set()
        self.deleted_cache = {}
        self.afk_reason = None
        self.spoofing = False
        self.start_time = datetime.now()
        self.error_logs = []
        
    def send_message(self, channel_id, content):
        try:
            r = self.session.post(f"https://discord.com/api/v9/channels/{channel_id}/messages", 
                                  json={"content": content[:1900]})
            return r.status_code == 200
        except:
            return False
    
    def get_messages(self, channel_id, limit=5):
        try:
            r = self.session.get(f"https://discord.com/api/v9/channels/{channel_id}/messages?limit={limit}")
            if r.status_code == 200:
                return r.json()
        except:
            pass
        return []
    
    def get_dm_channels(self):
        try:
            r = self.session.get("https://discord.com/api/v9/users/@me/channels")
            if r.status_code == 200:
                return r.json()
        except:
            pass
        return []
    
    def get_user_info(self, user_id):
        try:
            r = self.session.get(f"https://discord.com/api/v9/users/{user_id}")
            if r.status_code == 200:
                return r.json()
        except:
            pass
        return None
    
    def get_token_info(self):
        try:
            r = self.session.get("https://discord.com/api/v9/users/@me")
            if r.status_code == 200:
                data = r.json()
                created = datetime.fromtimestamp(((int(data['id']) >> 22) + 1420070400000) / 1000)
                return {
                    "username": f"{data['username']}#{data.get('discriminator', '0')}",
                    "id": data['id'],
                    "created": created.strftime("%Y-%m-%d %H:%M:%S"),
                    "verified": data.get('verified', False),
                    "mfa": data.get('mfa_enabled', False),
                    "email": data.get('email', 'Hidden')
                }
        except:
            return None
    
    def create_dm(self, user_id):
        try:
            r = self.session.post("https://discord.com/api/v9/users/@me/channels", 
                                  json={"recipient_id": str(user_id)})
            if r.status_code == 200:
                return r.json()['id']
        except:
            pass
        return None
    
    def block_user(self, user_id):
        try:
            r = self.session.put(f"https://discord.com/api/v9/users/@me/relationships/{user_id}", 
                                json={"type": 2})
            return r.status_code == 204
        except:
            return False
    
    def change_display_name(self, guild_id, new_name):
        try:
            r = self.session.patch(f"https://discord.com/api/v9/guilds/{guild_id}/members/@me",
                                   json={"nick": new_name})
            return r.status_code == 200
        except:
            return False
    
    def get_guilds(self):
        try:
            r = self.session.get("https://discord.com/api/v9/users/@me/guilds")
            if r.status_code == 200:
                return r.json()
        except:
            pass
        return []
    
    def get_uptime(self):
        seconds = (datetime.now() - self.start_time).total_seconds()
        days = int(seconds // 86400)
        hours = int((seconds % 86400) // 3600)
        minutes = int((seconds % 3600) // 60)
        secs = int(seconds % 60)
        return f"{days}d {hours}h {minutes}m {secs}s"
    
    def log_error(self, error):
        if LOG_ERRORS:
            timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            self.error_logs.append(f"[{timestamp}] {error}")
            if len(self.error_logs) > MAX_ERROR_LOGS:
                self.error_logs.pop(0)
    
    def dump_errors(self):
        if not self.error_logs:
            return None
        
        filename = f"nox_errors_{datetime.now().strftime('%Y%m%d_%H%M%S')}.txt"
        with open(filename, 'w') as f:
            f.write(f"NOX Self-Bot Error Log\n")
            f.write(f"Generated: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
            f.write(f"Total Errors: {len(self.error_logs)}\n")
            f.write("="*50 + "\n\n")
            for error in self.error_logs:
                f.write(error + "\n")
        return filename
    
    # ============= COMMANDS =============
    
    def cmd_help(self, channel_id):
        help_text = f"""{C}═══════════════════════════════════════════════════════════{RS}
{BD}{W}🤖 NOX SELF-BOT COMMANDS{RS}
{C}═══════════════════════════════════════════════════════════{RS}

{G}📌 BASIC{RS}
  {Y}{self.prefix}help{RS} - Show this menu
  {Y}{self.prefix}sniped{RS} - Snipe last deleted message
  {Y}{self.prefix}info <id>{RS} - Get user info
  {Y}{self.prefix}dm <id> <msg>{RS} - Send DM
  {Y}{self.prefix}infotoken{RS} - Token information

{G}🛡️ MODERATION{RS}
  {Y}{self.prefix}hide <id>{RS} - Block user
  {Y}{self.prefix}afk <reason>{RS} - Set AFK status
  {Y}{self.prefix}spoof{RS} - Toggle name spoofing

{G}🎮 FUN{RS}
  {Y}{self.prefix}gay <@user>{RS} - Gay percentage
  {Y}{self.prefix}love <id1> <id2>{RS} - Love calculator
  {Y}{self.prefix}doxxer <id>{RS} - Dox format

{G}⚙️ UTILITY{RS}
  {Y}{self.prefix}sfinfo{RS} - System info
  {Y}{self.prefix}dumperrorlogs{RS} - Dump error logs
  {Y}{self.prefix}thx{RS} - Credits

{C}═══════════════════════════════════════════════════════════{RS}"""
        self.send_message(channel_id, help_text)
    
    def cmd_sniped(self, channel_id):
        if channel_id in self.deleted_cache:
            msg = self.deleted_cache[channel_id]
            self.send_message(channel_id, f"🔫 **SNIPED!**\n`{msg['author']}:` {msg['content'][:400]}")
        else:
            self.send_message(channel_id, "❌ No message was deleted in this channel!")
    
    def cmd_info(self, channel_id, user_id):
        user = self.get_user_info(user_id)
        if not user:
            self.send_message(channel_id, f"❌ User `{user_id}` not found")
            return
        created = datetime.fromtimestamp(((int(user_id) >> 22) + 1420070400000) / 1000)
        info = f"""📋 **USER INFO**
`Username:` {user['username']}#{user.get('discriminator', '0')}
`ID:` {user['id']}
`Created:` {created.strftime('%Y-%m-%d %H:%M:%S')}
`Bot:` {user.get('bot', False)}"""
        self.send_message(channel_id, info)
    
    def cmd_infotoken(self, channel_id):
        info = self.get_token_info()
        if info:
            token_info = f"""🔐 **TOKEN INFORMATION**
`Username:` {info['username']}
`User ID:` {info['id']}
`Created:` {info['created']}
`Verified:` {info['verified']}
`MFA Enabled:` {info['mfa']}
`Email:` {info['email']}"""
            self.send_message(channel_id, token_info)
        else:
            self.send_message(channel_id, "❌ Failed to get token info")
    
    def cmd_dm(self, channel_id, target_id, message):
        dm_id = self.create_dm(target_id)
        if dm_id:
            if self.send_message(dm_id, message):
                self.send_message(channel_id, f"✅ DM sent to `{target_id}`")
            else:
                self.send_message(channel_id, f"❌ Failed to send DM")
        else:
            self.send_message(channel_id, f"❌ Cannot create DM with `{target_id}`")
    
    def cmd_hide(self, channel_id, user_id):
        if self.block_user(user_id):
            self.send_message(channel_id, f"✅ User `{user_id}` is now blocked")
        else:
            self.send_message(channel_id, f"❌ Failed to block user")
    
    def cmd_afk(self, channel_id, reason):
        self.afk_reason = reason or "AFK"
        self.send_message(channel_id, f"✅ AFK set: {self.afk_reason}")
        def clear():
            time.sleep(AFK_TIMEOUT)
            self.afk_reason = None
        threading.Thread(target=clear, daemon=True).start()
    
    def cmd_gay(self, channel_id, user_id):
        random.seed(int(user_id) if user_id.isdigit() else hash(user_id))
        percent = random.randint(0, 100)
        pride = "🌈" * (percent // 10) + "⬛" * (10 - (percent // 10))
        msg = f"""🏳️‍🌈 **GAY CALCULATOR** 🏳️‍🌈
`User:` <@{user_id}>
`Gay Percentage:` **{percent}%**
`Pride Meter:` {pride}"""
        self.send_message(channel_id, msg)
    
    def cmd_love(self, channel_id, user1, user2):
        random.seed(int(user1) + int(user2))
        percent = random.randint(0, 100)
        hearts = "❤️" * (percent // 10) + "🖤" * (10 - (percent // 10))
        msg = f"""💕 **LOVE CALCULATOR** 💕
`<@{user1}> + <@{user2}>`
`Match:` **{percent}%**
{hearts}"""
        self.send_message(channel_id, msg)
    
    def cmd_sfinfo(self, channel_id):
        import socket
        info = f"""🖥️ **SYSTEM INFO**
`OS:` {os.uname().sysname if hasattr(os, 'uname') else 'Android'}
`Hostname:` {socket.gethostname()}
`Uptime:` {self.get_uptime()}
`Python:` {sys.version.split()[0]}"""
        self.send_message(channel_id, info)
    
    def cmd_doxxer(self, channel_id, user_id):
        user = self.get_user_info(user_id)
        name = user['username'] if user else user_id
        msg = f"""⚠️ **DOX FORMAT (MOCK DATA)**
`Discord:` {name}
`User ID:` {user_id}
`IP:` 192.168.xxx.xxx
`Location:` [REDACTED]
`Email:` [REDACTED]

{R}⚠️ Educational purposes only{RS}"""
        self.send_message(channel_id, msg)
    
    def cmd_dumperrorlogs(self, channel_id):
        filename = self.dump_errors()
        if filename:
            self.send_message(channel_id, f"📁 Error logs dumped to `{filename}`")
        else:
            self.send_message(channel_id, "✅ No errors logged!")
    
    def cmd_thx(self, channel_id):
        msg = f"""⭐ **CREDITS** ⭐

{BD}{W}NOX Self-Bot v4.0{RS}

{Y}Made with ❤️ by NOX{RS}
{P}Powered by Aetherbark AI - The All-Knowing Deity{RS}

{G}Join the journey. Stay dangerous.{RS}"""
        self.send_message(channel_id, msg)
    
    def cmd_spoof(self, channel_id):
        self.spoofing = not self.spoofing
        if self.spoofing:
            self.send_message(channel_id, "✅ **Display name spoofing ENABLED**\nChanging name every 5 seconds...")
            def spoof_loop():
                while self.spoofing:
                    guilds = self.get_guilds()
                    name = random.choice(self.spoof_names)
                    for guild in guilds:
                        self.change_display_name(guild['id'], name)
                    time.sleep(5)
            threading.Thread(target=spoof_loop, daemon=True).start()
        else:
            self.send_message(channel_id, "❌ Display name spoofing DISABLED")
    
    # ============= MESSAGE HANDLER =============
    def check_commands(self):
        try:
            dms = self.get_dm_channels()
            for dm in dms:
                channel_id = dm['id']
                messages = self.get_messages(channel_id, limit=3)
                for msg in messages:
                    msg_id = msg['id']
                    if msg_id in self.processed:
                        continue
                    content = msg.get('content', '')
                    author_id = str(msg['author']['id'])
                    if author_id == str(self.user['id']) and content.startswith(self.prefix):
                        self.processed.add(msg_id)
                        if len(self.processed) > 50:
                            self.processed.clear()
                        parts = content[len(self.prefix):].split()
                        if not parts:
                            continue
                        cmd = parts[0].lower()
                        args = parts[1:] if len(parts) > 1 else []
                        print(f"{G}[CMD]{RS} {cmd}")
                        if cmd == "help": self.cmd_help(channel_id)
                        elif cmd == "sniped": self.cmd_sniped(channel_id)
                        elif cmd == "info" and args: self.cmd_info(channel_id, args[0])
                        elif cmd == "infotoken": self.cmd_infotoken(channel_id)
                        elif cmd == "dm" and len(args) >= 2: self.cmd_dm(channel_id, args[0], " ".join(args[1:]))
                        elif cmd == "hide" and args: self.cmd_hide(channel_id, args[0])
                        elif cmd == "afk": self.cmd_afk(channel_id, " ".join(args) if args else None)
                        elif cmd == "gay" and args: self.cmd_gay(channel_id, args[0])
                        elif cmd == "love" and len(args) >= 2: self.cmd_love(channel_id, args[0], args[1])
                        elif cmd == "sfinfo": self.cmd_sfinfo(channel_id)
                        elif cmd == "doxxer" and args: self.cmd_doxxer(channel_id, args[0])
                        elif cmd == "dumperrorlogs": self.cmd_dumperrorlogs(channel_id)
                        elif cmd == "thx": self.cmd_thx(channel_id)
                        elif cmd == "spoof": self.cmd_spoof(channel_id)
                        else: self.send_message(channel_id, f"❌ Unknown command")
        except Exception as e:
            self.log_error(str(e))
    
    def login(self):
        try:
            r = self.session.get("https://discord.com/api/v9/users/@me")
            if r.status_code == 200:
                self.user = r.json()
                return True
            return False
        except:
            return False
    
    def run(self):
        print(CL, end="")
        print(BANNER)
        if not self.login():
            print(f"{R}❌ INVALID TOKEN! Edit config.py{R}")
            return
        print(f"{G}✅ Logged in as: {self.user['username']}#{self.user.get('discriminator', '0')}{RS}")
        print(f"{G}┌─────────────────────────────────────────────────────────────────┐")
        print(f"│ {BD}⚡ NOX SELF-BOT ACTIVE{R}{G}                                                │")
        print(f"├─────────────────────────────────────────────────────────────────┤")
        print(f"│ {C}🤖 Bot:{RS} {W}{BOT_NAME}{RS}                                                      │")
        print(f"│ {C}📡 Status:{RS} {G}● ONLINE{RS}                                                   │")
        print(f"│ {C}💬 Prefix:{RS} {W}{self.prefix}{RS}                                                    │")
        print(f"└─────────────────────────────────────────────────────────────────┘{RS}")
        print(f"{Y}💡 Send '{self.prefix}help' in a DM to yourself{RS}\n")
        try:
            while self.running:
                self.check_commands()
                time.sleep(2)
        except KeyboardInterrupt:
            print(f"\n{Y}⚠️ Shutting down...{RS}")

if __name__ == "__main__":
    bot = NOXSelfBot()
    bot.run()
