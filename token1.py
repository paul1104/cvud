from RAbotproses import LineBot

import threading


def login(resp, auth):

	bot = LineBot(resp, auth)


Za1 = threading.Thread(target=login, args=('ZA1','EpEOr45Q44Nw7zAJp2Qe.W07Xch8agT18QdUwirf3VG.nQxtOAP6bHMpCzwAvGNTPZIcooJBB9Nkl26ehBw8ZZo=')).start()

#Za2 = threading.Thread(target=login, args=('ZA2','Epw79hqLdN27XdxptSDe.VuY09tx4Ic8DEI6wDwthhG.HRhxxbXw6zvKlRforXlBtx71dYkyB2XcWv550alznac=')).start()

#Za3 = threading.Thread(target=login, args=('ZA3','EpGf91fVYbTjmY8u7nI6.ETj6hRGziqHm27jAQoasrG./UDSiJI74txcEyq7FQneyT7cOjPzFw78sSLTCrqMaag=')).start()

#Za4 = threading.Thread(target=login, args=('ZA4','EpH6qUUE4DZ36L4D8xY3.KG9UDe07YwMZYjG9spEuSW.1r0cYzSUcRy+OP+GSprQBU9iVrlpcfzxKxs7fRfQw4Y=')).start()

#Za5 = threading.Thread(target=login, args=('ZA5','EpTZiINnJ9nH8NF2Efs5.j11ZGOEADKe0fKENYQzRfq.7OoqPrtgcvzx9Wj+5A6xSSjzrCCsk59HgD1SftRGA50=')).start()

#Za6 = threading.Thread(target=login, args=('NH1','EpTYTMP6QHiSowEJAgb2.+zDSpxLAxOle23SAVoRb4G.mil69tCRyl8Xy2p1/3CSdNHehMpuJe0GMQ1AMg4Skv8=')).start()

#Za7 = threading.Thread(target=login, args=('NH2','Epxu1XSaMhxzLmcBu5Bd.Qr9F7O+ydsmvOoR8Wr5gdq.3kYM87P9/lJUIxotX1DWzyD4dwrErDUDpOeRx+6NtHc=')).start()

#Za8 = threading.Thread(target=login, args=('NH3','EpdhgJeYdCSzdOsBa7o8.WrKBtxeyfu++C0W31aalIa.aWkHBMk9e1kZx2WQ6FMg+lKNfPZPZR0/NySR/YeqkoE=')).start()



print('Login Berhasil!')
