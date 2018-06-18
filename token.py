from dona import LineBot

import threading


def login(resp, auth):

	bot = LineBot(resp, auth)


client = threading.Thread(target=login, args=('client','')).start()


print('Login Berhasil!')
