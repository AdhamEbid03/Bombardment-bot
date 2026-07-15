# 💣 Bombardment Bot

Bombardment Bot is a simple Discord soundboard bot built in Python that exists for one reason:

> Cause complete and utter chaos in your Discord voice channels.

Inspired by those random meme compilations where absolute silence is suddenly interrupted by an airhorn, vine boom, or some other ridiculous sound effect, this bot lets you recreate that experience with your friends.

---

## ✨ Features

- 🎵 Play random meme sounds
- 🎙️ Join and leave Discord voice channels
- 📁 Easily add your own custom sound effects
- 🐍 Lightweight and easy to modify

---

# 🛠️ Tech Stack

- Python 3.12.10
- FFmpeg

### Libraries Used

- discord.py
- python-dotenv
- PyNaCl

---

# 📦 Installation

## 1. Clone the repository

```bash
git clone https://github.com/YOUR_USERNAME/Bombardment-Bot.git
cd Bombardment-Bot
```

---

## 2. Install Python dependencies

```bash
pip install -r requirements.txt
```

---

## 3. Install FFmpeg

Download FFmpeg and add the **bin** folder to your Windows PATH.

Once installed, verify it by running:

```bash
ffmpeg -version
```

If you see the version information, you're good to go.

---

## 4. Create a `.env` file

Create a file called:

```text
.env
```

Inside it, add your Discord Bot Token:

```env
DISCORD_TOKEN=YOUR_DISCORD_BOT_TOKEN
```

> ⚠️ Never share your bot token or upload your `.env` file to GitHub.

---

# 🚀 Running the Bot

Simply run:

```bash
python main.py
```

If everything has been configured correctly, your bot should come online.

---

# 🎮 Usage

Once the bot is online:

1. Invite it to your Discord server.
2. Make sure you're connected to a voice channel.
3. Wake the bot up using:

```text
wake up bomb
```
If messages on discord don't work, try the following steps
### Enable Message Content Intent

In the Discord Developer Portal:

1. Open your application.
2. Select **Bot**.
3. Scroll to **Privileged Gateway Intents**.
4. Enable **Message Content Intent**.
5. Save your changes.

4. Use:

```text
/join
```

(or your configured join command)

5. Start the bombardment.

---

# 📂 Adding Your Own Sounds

Want to make your friends regret inviting you to the server?

Simply add your own sound files to the sounds folder.

The bot automatically selects compatible audio files from the "sounds" folder.

Supported formats include:

- mp3
- wav
- ogg

---

# ⚠️ Known Issues

Discord voice quality can vary depending on your internet connection and region.

Users in regions where Discord voice traffic is restricted (such as the UAE) may experience delayed or choppy audio playback. This is a network limitation rather than an issue with the bot itself.

---

# 🤝 Contributing

Feel free to fork the repository, improve the code, add commands, or expand the sound library.

Pull Requests are always welcome.

---

# 📜 License

This project is licensed under the MIT License.

Feel free to modify it, learn from it, or make your own chaotic version.

---

# ❤️ Acknowledgements

Huge thanks to the developers behind:

- discord.py
- FFmpeg
- python-dotenv

Without their work, this project wouldn't exist.

---

## Have fun...

...and please use your newfound power responsibly.

Or don't.

I'm not your dad.