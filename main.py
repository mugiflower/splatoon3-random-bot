import discord
import random
import os

TOKEN = os.getenv("TOKEN")

intents = discord.Intents.default()
intents.message_content = True
client = discord.Client(intents=intents)

weapons = [
    "わかばシューター", "スプラシューター", "ボールドマーカー",
    "N-ZAP85", "プロモデラーMG", "シャープマーカー",
    "ホットブラスター", "ロングブラスター", "クラッシュブラスター",
    "スプラスコープ", "スクイックリンα", "リッター4K",
    "スプラローラー", "カーボンローラー", "ダイナモローラー",
    "バケットスロッシャー", "ヒッセン", "スクリュースロッシャー",
    "スプラスピナー", "バレルスピナー", "ノーチラス47",
    "パブロ", "ホクサイ", "クーゲルシュライバー",
    "スパッタリー", "ケルビン525", "デュアルスイーパー"
]

@client.event
async def on_ready():
    print(f"BOTが起動しました: {client.user}")

@client.event
async def on_message(message):
    if message.author.bot:
        return
    if message.content == "!weapon":
        weapon = random.choice(weapons)
        await message.channel.send(f"今日の武器は: **{weapon}** 🎯")

client.run(TOKEN)
