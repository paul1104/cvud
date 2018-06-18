# -*- coding: utf-8 -*-

from LINE import *
from ThriftService.ttypes import *
from gtts import gTTS
from time import sleep
from datetime import datetime, timedelta
from bs4 import BeautifulSoup
from googletrans import Translator
from multiprocessing import Pool, Process
from humanfriendly import format_timespan, format_size, format_number, format_length
import time, random, asyncio, timeit, sys, json, codecs, threading, glob, re, string, os, requests, subprocess, six, urllib, urllib.parse, ast, pafy, youtube_dl, pytz, traceback, atexit

botStart = time.time()
	
def __init__(self, resp, authQR=None):
    self.resp = resp
    self.resp = self.resp+' '
    self.authQR = authQR
    self.login(authQR)
    self.fetch()
	
def login(self, auth):
    if auth == None:
        self.client = LineClient()
    else:
        self.client = LineClient(authToken=auth)
    self.client_ch = LineChannel(self.client, channelId="1341209850")
    self.client.log("Auth Token : " + str(self.client.authToken))
    self.client.log("Channel Token : " + str(self.client_ch.channelAccessToken))
    self.mid = self.client.getProfile().mid
	
clientMid = self.client.getProfile().mid
clientProfile = self.client.getProfile()
clientSettings = self.client.getSettings()

msg_dict={}

helpmess = """╔══『 мenυ ĸaneĸι 』 
╠ ⌬ 「/ѕιderѕ」 
╠ ⌬ 「/ѕearcн」 
╠ ⌬ 「/aвoυт」 
╠ ⌬ 「/groυp」 
╠ ⌬ 「/ᴋᴇʟᴜᴀʀ」 
╚══『 мenυ ĸaneĸι 』\n @!"""

sidersmess = """╔══『 мenυ ѕιderѕ 』 
╠ ⌬ 「lυrĸιng on」= nyalaĸan dυlυ 
╠ ⌬ 「lυrĸιng」 = мelιнaтĸan ѕιderѕ 
╠ ⌬ 「lυrĸιng oғғ」= мaтιĸan 
╠════════════════ 
╠ ⌬ 「ѕιder on」= oтoмaтιѕ 
╠ ⌬ 「ѕιder oғғ」= oтoмaтιѕ 
╚══『 мenυ ĸaneĸι 』\n @!"""

searchmess = """╔══『 мenυ ѕearcн 』 
╠ ⌬ 「ayaт: [ayaт ĸeвerapa]」 
╠ ⌬ 「jadwal: [naмa cнannel]」 
╠ ⌬ 「call: [noмor нp]」 
╠ ⌬ 「мeмe: [тeхт 1] [тeхт 2]」 
╠ ⌬ 「reтro: [тeхт 1] [тeхт 2]」 
╠ ⌬ 「neon: [тeхт]」 
╠ ⌬ 「yтмp3: [lιnĸ vιd yт]」 
╠═══════════════ 
╠ ⌬ 「ттѕ」= вerвιcara ѕeѕυaι вaнaѕa 
╠ ⌬ 「тranѕlaтe」 = тranѕlaтe 
╠ ⌬ 「ѕpeed」= ĸecepaтan вoт 
╠ ⌬ 「rυnтιмe」= вoт вerjalan ѕelaмa 
╠═══════════════ 
╠ ⌬ 「/ѕcreen [lιnĸ nya] 」 
╠ ⌬ 「/ceĸ [тgl-вln-тнn]」 
╠ ⌬ 「/ιмage [naмa тargeт]」 
╠ ⌬ 「/мυѕιc [naмa lagυ]」 
╠ ⌬ 「/yт [naмa vιdeo]」 
╠═══════════════ 
╠ ⌬ 「ιnѕтapoѕт υѕernaмe|ĸeвerapa」 
╠ ⌬ 「ιnѕтaѕтory υѕernaмe|ĸeвerapa」  
╚══『 мenυ ĸaneĸι 』\n @!"""

groupmess = """╔══『 мenυ groυp 』 
╠ ⌬ 「cgp」= cнange ғoтo groυp 
╠ ⌬ 「мenтιon」= тag all 
╠═══════════════ 
╠ ⌬ 「pcιd: [ιd тargeт] [ιѕι peѕan]」 
╠ ⌬ 「apaĸaн [perтanyaan]?」 
╠ ⌬ 「doѕa @[тag тargeт]」 
╠ ⌬ 「paнala @[тag тargeт]」 
╠═══════════════ 
╠ ⌬ 「gcreaтor」 
╠ ⌬ 「groυppιcтυre」 
╠ ⌬ 「groυpтιcĸeт」 
╠ ⌬ 「groυpιnғo」 
╠ ⌬ 「lιѕтмeмвer」 
╠ ⌬ 「reѕυlт」 
╠════════════════ 
╠ ⌬ 「/cυrιdp @[тag тargeт]」 
╠ ⌬ 「/cυrιcover @[тag тargeт]」 
╚══『 мenυ ĸaneĸι 』\n @!"""

limit = {
    'batas': "5",
    'user':{}
    }

wait = {
    'limit':{},
    'contact':False,
    'autoJoin':True,
    'sticker':False,
    'autoCancel':{"on":True,"members":10},
    "spam":{},
    "detectMention":False,
    "Members":1,
    "wordban":{},
    'leaveRoom':True,
    'likeOn':True,
    'comment1':"Auto Like By http://line.me/ti/p/%40ish7215m",
    'timeline':True,
    'autoAdd':True,
    'atjointicket':True,
    "alwaysRead":True,
    "linkticket":False,
    "cpp":False,
    "cpg":False,
    'message':"тнαикѕ fσя α∂∂ мє! му ¢яєαтσя ιѕ http://line.me/ti/p/%40ish7215m",
    "lang":"JP",
    "comment":"тнαикѕ fσя α∂∂ мє! му ¢яєαтσя ιѕ http://line.me/ti/p/%40ish7215m",
    "commenty":"Auto Like by кєи кαиєкι\n\nhttp://line.me/ti/p/%40ish7215m",
    "commentOn":True,
    "commentBlack":{},
    "wblack":False,
    "dblack":False,
    "clock":False,
    "cName":" ",
    "blacklist":{},
    "whitelist":{},
    "wblacklist":False,
    "dblacklist":False,
    "teman":{},
    "winvite":False,
    "likeOn":True,
    "protection":False,
    "welcomemsg":True,
    "welmsg":" welcome to ",
    "pname":{},
    "pro_name":{},
    "Pap":{}
    }

wait2 = {
    'readPoint':{},
    'readMember':{},
    'setTime':{},
    'ROM':{}
    }

cctv = {
    "cyduk":{},
    "point":{},
    "sidermem":{}
}    
   
hasil = {
    "result":False,
    "posts":False,
    "postInfo":False,
    "liked":{}
    }
    
wordban = {
    "kontol":{},
    "kontl":{},
    "kntl":{},
    "memek":{},
    "anjing":{},
    "njing":{},
    "anjeng":{}
}

setTime = {}
setTime = wait2['setTime']

settings = {
    "limituser": {},
    "autoAdd": True,
    "autoJoin": True,
    "autoLeave": False,
    "welcomemsg": True,
    "autoCancel":{"on":True,"members":10},
    "autoRead": False,
    "autoRespon": False,
    "autoJoinTicket": True,
    "checkContact": False,
    "checkPost": False,
    "checkSticker": False,
    "changePictureProfile": False,
    "changeGroupPicture": [],
    "keyCommand": "",
    "myProfile": {
        "displayName": "",
        "coverId": "",
        "pictureStatus": "",
        "statusMessage": ""
    },
    "mimic": {
        "copy": False,
        "status": False,
        "target": {}
    },
    "setKey": False,
    "unsendMessage": False,
    "restartPoint": {},
    "server": "VPS",
    "target": {},
    "timeRestart": "1200",
    "userAgent": [
        "Mozilla/5.0 (X11; U; Linux i586; de; rv:5.0) Gecko/20100101 Firefox/5.0",
        "Mozilla/5.0 (X11; U; Linux amd64; rv:5.0) Gecko/20100101 Firefox/5.0 (Debian)",
        "Mozilla/5.0 (X11; U; Linux amd64; en-US; rv:5.0) Gecko/20110619 Firefox/5.0",
        "Mozilla/5.0 (X11; Linux) Gecko Firefox/5.0",
        "Mozilla/5.0 (X11; Linux x86_64; rv:5.0) Gecko/20100101 Firefox/5.0 FirePHP/0.5",
        "Mozilla/5.0 (X11; Linux x86_64; rv:5.0) Gecko/20100101 Firefox/5.0 Firefox/5.0",
        "Mozilla/5.0 (X11; Linux x86_64) Gecko Firefox/5.0",
        "Mozilla/5.0 (X11; Linux ppc; rv:5.0) Gecko/20100101 Firefox/5.0",
        "Mozilla/5.0 (X11; Linux AMD64) Gecko Firefox/5.0",
        "Mozilla/5.0 (X11; FreeBSD amd64; rv:5.0) Gecko/20100101 Firefox/5.0",
        "Mozilla/5.0 (Windows NT 6.2; WOW64; rv:5.0) Gecko/20100101 Firefox/5.0",
        "Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:5.0) Gecko/20110619 Firefox/5.0",
        "Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:5.0) Gecko/20100101 Firefox/5.0",
        "Mozilla/5.0 (Windows NT 6.1; rv:6.0) Gecko/20100101 Firefox/5.0",
        "Mozilla/5.0 (Windows NT 6.1.1; rv:5.0) Gecko/20100101 Firefox/5.0",
        "Mozilla/5.0 (Windows NT 5.2; WOW64; rv:5.0) Gecko/20100101 Firefox/5.0",
        "Mozilla/5.0 (Windows NT 5.1; U; rv:5.0) Gecko/20100101 Firefox/5.0",
        "Mozilla/5.0 (Windows NT 5.1; rv:2.0.1) Gecko/20100101 Firefox/5.0",
        "Mozilla/5.0 (Windows NT 5.0; WOW64; rv:5.0) Gecko/20100101 Firefox/5.0",
        "Mozilla/5.0 (Windows NT 5.0; rv:5.0) Gecko/20100101 Firefox/5.0"
    ]
}

#if settings["restartPoint"] != None:
#    client.sendMessage(settings["restartPoint"], "Bot kembali aktif")

read = {
    "ROM": {},
    "readPoint": {},
    "readMember": {},
    "readTime": {}
}

cctv = {
    "cyduk":{},
    "point":{},
    "sidermem":{}
}   

list_language = {
    "list_textToSpeech": {
        "id": "Indonesia",
        "af" : "Afrikaans",
        "sq" : "Albanian",
        "ar" : "Arabic",
        "hy" : "Armenian",
        "bn" : "Bengali",
        "ca" : "Catalan",
        "zh" : "Chinese",
        "zh-cn" : "Chinese (Mandarin/China)",
        "zh-tw" : "Chinese (Mandarin/Taiwan)",
        "zh-yue" : "Chinese (Cantonese)",
        "hr" : "Croatian",
        "cs" : "Czech",
        "da" : "Danish",
        "nl" : "Dutch",
        "en" : "English",
        "en-au" : "English (Australia)",
        "en-uk" : "English (United Kingdom)",
        "en-us" : "English (United States)",
        "eo" : "Esperanto",
        "fi" : "Finnish",
        "fr" : "French",
        "de" : "German",
        "el" : "Greek",
        "hi" : "Hindi",
        "hu" : "Hungarian",
        "is" : "Icelandic",
        "id" : "Indonesian",
        "it" : "Italian",
        "ja" : "Japanese",
        "km" : "Khmer (Cambodian)",
        "ko" : "Korean",
        "la" : "Latin",
        "lv" : "Latvian",
        "mk" : "Macedonian",
        "no" : "Norwegian",
        "pl" : "Polish",
        "pt" : "Portuguese",
        "ro" : "Romanian",
        "ru" : "Russian",
        "sr" : "Serbian",
        "si" : "Sinhala",
        "sk" : "Slovak",
        "es" : "Spanish",
        "es-es" : "Spanish (Spain)",
        "es-us" : "Spanish (United States)",
        "sw" : "Swahili",
        "sv" : "Swedish",
        "ta" : "Tamil",
        "th" : "Thai",
        "tr" : "Turkish",
        "uk" : "Ukrainian",
        "vi" : "Vietnamese",
        "cy" : "Welsh"
    },
    "list_translate": {    
        "af": "afrikaans",
        "sq": "albanian",
        "am": "amharic",
        "ar": "arabic",
        "hy": "armenian",
        "az": "azerbaijani",
        "eu": "basque",
        "be": "belarusian",
        "bn": "bengali",
        "bs": "bosnian",
        "bg": "bulgarian",
        "ca": "catalan",
        "ceb": "cebuano",
        "ny": "chichewa",
        "zh-cn": "chinese (simplified)",
        "zh-tw": "chinese (traditional)",
        "co": "corsican",
        "hr": "croatian",
        "cs": "czech",
        "da": "danish",
        "nl": "dutch",
        "en": "english",
        "eo": "esperanto",
        "et": "estonian",
        "tl": "filipino",
        "fi": "finnish",
        "fr": "french",
        "fy": "frisian",
        "gl": "galician",
        "ka": "georgian",
        "de": "german",
        "el": "greek",
        "gu": "gujarati",
        "ht": "haitian creole",
        "ha": "hausa",
        "haw": "hawaiian",
        "iw": "hebrew",
        "hi": "hindi",
        "hmn": "hmong",
        "hu": "hungarian",
        "is": "icelandic",
        "ig": "igbo",
        "id": "indonesian",
        "ga": "irish",
        "it": "italian",
        "ja": "japanese",
        "jw": "javanese",
        "kn": "kannada",
        "kk": "kazakh",
        "km": "khmer",
        "ko": "korean",
        "ku": "kurdish (kurmanji)",
        "ky": "kyrgyz",
        "lo": "lao",
        "la": "latin",
        "lv": "latvian",
        "lt": "lithuanian",
        "lb": "luxembourgish",
        "mk": "macedonian",
        "mg": "malagasy",
        "ms": "malay",
        "ml": "malayalam",
        "mt": "maltese",
        "mi": "maori",
        "mr": "marathi",
        "mn": "mongolian",
        "my": "myanmar (burmese)",
        "ne": "nepali",
        "no": "norwegian",
        "ps": "pashto",
        "fa": "persian",
        "pl": "polish",
        "pt": "portuguese",
        "pa": "punjabi",
        "ro": "romanian",
        "ru": "russian",
        "sm": "samoan",
        "gd": "scots gaelic",
        "sr": "serbian",
        "st": "sesotho",
        "sn": "shona",
        "sd": "sindhi",
        "si": "sinhala",
        "sk": "slovak",
        "sl": "slovenian",
        "so": "somali",
        "es": "spanish",
        "su": "sundanese",
        "sw": "swahili",
        "sv": "swedish",
        "tg": "tajik",
        "ta": "tamil",
        "te": "telugu",
        "th": "thai",
        "tr": "turkish",
        "uk": "ukrainian",
        "ur": "urdu",
        "uz": "uzbek",
        "vi": "vietnamese",
        "cy": "welsh",
        "xh": "xhosa",
        "yi": "yiddish",
        "yo": "yoruba",
        "zu": "zulu",
        "fil": "Filipino",
        "he": "Hebrew"
    }
}

#Bots=[mid]
boty = ["u1869dc950cf9211164a150d91aa150db","u9ed37b221ed5b78a46d6209d93159bef","u3a354e28238fabd00ebfdbcac12e5973"]
admin=["ub8530f15ff4020c3cc2d1ad2f066aa4b","u5601bdfbc2c67e7adcb95f790127b193"]
owner=["ub8530f15ff4020c3cc2d1ad2f066aa4b","u5601bdfbc2c67e7adcb95f790127b193"]
settings["myProfile"]["displayName"] = nadyaProfile.displayName
settings["myProfile"]["statusMessage"] = nadyaProfile.statusMessage
settings["myProfile"]["pictureStatus"] = nadyaProfile.pictureStatus
coverId = client.getProfileDetail()["result"]["objectId"]
settings["myProfile"]["coverId"] = coverId
	
def fetch(self):
    while True:
        try:
            self.operations = self.client._client.fetchOps(self.client.revision, 10, 0, 0)
            for op in self.operations:
                if (op.type != OpType.END_OF_OPERATION):
                    self.client.revision = max(self.client.revision, op.revision)
                    self.bot(op)
        except KeyboardInterrupt:
            print('Selamat Tinggal!')
            exit()
		
def autoRestart():
    if time.time() - botStart > int(settings["timeRestart"]):
        backupData()
        time.sleep(5)
        restartBot()
	
def restartBot():
    print ("[ INFO ] BOT RESTART")
    python = sys.executable
    os.execl(python, python, *sys.argv)
    
def logError(text):
    client.log("[ ERROR ] {}".format(str(text)))
    tz = pytz.timezone("Asia/Jakarta")
    timeNow = datetime.now(tz=tz)
    timeHours = datetime.strftime(timeNow,"(%H:%M)")
    day = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday","Friday", "Saturday"]
    hari = ["Minggu", "Senin", "Selasa", "Rabu", "Kamis", "Jumat", "Sabtu"]
    bulan = ["Januari", "Februari", "Maret", "April", "Mei", "Juni", "Juli", "Agustus", "September", "Oktober", "November", "Desember"]
    inihari = datetime.now(tz=tz)
    hr = inihari.strftime('%A')
    bln = inihari.strftime('%m')
    for i in range(len(day)):
        if hr == day[i]: hasil = hari[i]
    for k in range(0, len(bulan)):
        if bln == str(k): bln = bulan[k-1]
    time = "{}, {} - {} - {} | {}".format(str(hasil), str(inihari.strftime('%d')), str(bln), str(inihari.strftime('%Y')), str(inihari.strftime('%H:%M:%S')))
    with open("logError.txt","a") as error:
        error.write("\n[ {} ] {}".format(str(time), text))

def cTime_to_datetime(unixtime):
    return datetime.fromtimestamp(int(str(unixtime)[:len(str(unixtime))-3]))
def dt_to_str(dt):
    return dt.strftime('%H:%M:%S')

def delete_log():
    ndt = datetime.now()
    for data in msg_dict:
        if (datetime.utcnow() - cTime_to_datetime(msg_dict[data]["createdTime"])) > timedelta(1):
            if "path" in msg_dict[data]:
                client.deleteFile(msg_dict[data]["path"])
            del msg_dict[data]
            
def sendMention(to, text="", mids=[]):
    arrData = ""
    arr = []
    mention = "@zeroxyuuki "
    if mids == []:
        raise Exception("Invalid mids")
    if "@!" in text:
        if text.count("@!") != len(mids):
            raise Exception("Invalid mids")
        texts = text.split("@!")
        textx = ""
        for mid in mids:
            textx += str(texts[mids.index(mid)])
            slen = len(textx)
            elen = len(textx) + 15
            arrData = {'S':str(slen), 'E':str(elen - 4), 'M':mid}
            arr.append(arrData)
            textx += mention
        textx += str(texts[len(mids)])
    else:
        textx = ""
        slen = len(textx)
        elen = len(textx) + 15
        arrData = {'S':str(slen), 'E':str(elen - 4), 'M':mids[0]}
        arr.append(arrData)
        textx += mention + str(text)
    client.sendMessage(to, textx, {'MENTION': str('{"MENTIONEES":' + json.dumps(arr) + '}')}, 0)

def command(text):
    pesan = text.lower()
    if settings["setKey"] == True:
        if pesan.startswith(settings["keyCommand"]):
            cmd = pesan.replace(settings["keyCommand"],"")
        else:
            cmd = "Undefined command"
    else:
        cmd = text.lower()
    return cmd
    
def download_page(url):
    try:
        headers = {}
        headers['User-Agent'] = random.choice(settings["userAgent"])
        req = urllib.request.Request(url, headers = headers)
        resp = urllib.request.urlopen(req)
        respData = str(resp.read())
        return respData
    except Exception as e:
        logError(e)
def _images_get_next_item(s):
    start_line = s.find('rg_di')
    if start_line == -1:    #If no links are found then give an error!
        end_quote = 0
        link = "no_links"
        return link, end_quote
    else:
        start_line = s.find('"class="rg_meta"')
        start_content = s.find('"ou"',start_line+70)
        end_content = s.find(',"ow"',start_content-70)
        content_raw = str(s[start_content+6:end_content-1])
        return content_raw, end_content
#Getting all links with the help of '_images_get_next_image'
def _images_get_all_items(page):
    items = []
    while True:
        item, end_content = _images_get_next_item(page)
        if item == "no_links":
            break
        else:
            items.append(item)      #Append all the links in the list named 'Links'
            page = page[end_content:]
    return items

def backupData():
    try:
        backup = settings
        f = codecs.open('kaneki.json','w','utf-8')
        json.dump(backup, f, sort_keys=True, indent=4, ensure_ascii=False)
        return True
    except Exception as error:
        logError(error)
        return False

def helptexttospeech():
    if settings['setKey'] == True:
        key = settings['keyCommand']
    else:
        key = ''
    helpTextToSpeech =  "╔══[ Help TextToSpeech ]" + "\n" + \
                        "╠ " + key + "af : Afrikaans" + "\n" + \
                        "╠ " + key + "sq : Albanian" + "\n" + \
                        "╠ " + key + "ar : Arabic" + "\n" + \
                        "╠ " + key + "hy : Armenian" + "\n" + \
                        "╠ " + key + "bn : Bengali" + "\n" + \
                        "╠ " + key + "ca : Catalan" + "\n" + \
                        "╠ " + key + "zh : Chinese" + "\n" + \
                        "╠ " + key + "zhcn : Chinese (Mandarin/China)" + "\n" + \
                        "╠ " + key + "zhtw : Chinese (Mandarin/Taiwan)" + "\n" + \
                        "╠ " + key + "zhyue : Chinese (Cantonese)" + "\n" + \
                        "╠ " + key + "hr : Croatian" + "\n" + \
                        "╠ " + key + "cs : Czech" + "\n" + \
                        "╠ " + key + "da : Danish" + "\n" + \
                        "╠ " + key + "nl : Dutch" + "\n" + \
                        "╠ " + key + "en : English" + "\n" + \
                        "╠ " + key + "enau : English (Australia)" + "\n" + \
                        "╠ " + key + "enuk : English (United Kingdom)" + "\n" + \
                        "╠ " + key + "enus : English (United States)" + "\n" + \
                        "╠ " + key + "eo : Esperanto" + "\n" + \
                        "╠ " + key + "fi : Finnish" + "\n" + \
                        "╠ " + key + "fr : French" + "\n" + \
                        "╠ " + key + "de : German" + "\n" + \
                        "╠ " + key + "el : Greek" + "\n" + \
                        "╠ " + key + "hi : Hindi" + "\n" + \
                        "╠ " + key + "hu : Hungarian" + "\n" + \
                        "╠ " + key + "is : Icelandic" + "\n" + \
                        "╠ " + key + "id : Indonesian" + "\n" + \
                        "╠ " + key + "it : Italian" + "\n" + \
                        "╠ " + key + "ja : Japanese" + "\n" + \
                        "╠ " + key + "km : Khmer (Cambodian)" + "\n" + \
                        "╠ " + key + "ko : Korean" + "\n" + \
                        "╠ " + key + "la : Latin" + "\n" + \
                        "╠ " + key + "lv : Latvian" + "\n" + \
                        "╠ " + key + "mk : Macedonian" + "\n" + \
                        "╠ " + key + "no : Norwegian" + "\n" + \
                        "╠ " + key + "pl : Polish" + "\n" + \
                        "╠ " + key + "pt : Portuguese" + "\n" + \
                        "╠ " + key + "ro : Romanian" + "\n" + \
                        "╠ " + key + "ru : Russian" + "\n" + \
                        "╠ " + key + "sr : Serbian" + "\n" + \
                        "╠ " + key + "si : Sinhala" + "\n" + \
                        "╠ " + key + "sk : Slovak" + "\n" + \
                        "╠ " + key + "es : Spanish" + "\n" + \
                        "╠ " + key + "eses : Spanish (Spain)" + "\n" + \
                        "╠ " + key + "esus : Spanish (United States)" + "\n" + \
                        "╠ " + key + "sw : Swahili" + "\n" + \
                        "╠ " + key + "sv : Swedish" + "\n" + \
                        "╠ " + key + "ta : Tamil" + "\n" + \
                        "╠ " + key + "th : Thai" + "\n" + \
                        "╠ " + key + "tr : Turkish" + "\n" + \
                        "╠ " + key + "uk : Ukrainian" + "\n" + \
                        "╠ " + key + "vi : Vietnamese" + "\n" + \
                        "╠ " + key + "cy : Welsh" + "\n" + \
                        "╚══[ Kaneki Public Bot ]" + "\n" + "\n\n" + \
                        "Contoh : " + key + "say-id Kaneki"
    return helpTextToSpeech

def helptranslate():
    if settings['setKey'] == True:
        key = settings['keyCommand']
    else:
        key = ''
    helpTranslate = "╔══[ Help Translate ]" + "\n" + \
                    "╠ " + key + "af : afrikaans" + "\n" + \
                    "╠ " + key + "sq : albanian" + "\n" + \
                    "╠ " + key + "am : amharic" + "\n" + \
                    "╠ " + key + "ar : arabic" + "\n" + \
                    "╠ " + key + "hy : armenian" + "\n" + \
                    "╠ " + key + "az : azerbaijani" + "\n" + \
                    "╠ " + key + "eu : basque" + "\n" + \
                    "╠ " + key + "be : belarusian" + "\n" + \
                    "╠ " + key + "bn : bengali" + "\n" + \
                    "╠ " + key + "bs : bosnian" + "\n" + \
                    "╠ " + key + "bg : bulgarian" + "\n" + \
                    "╠ " + key + "ca : catalan" + "\n" + \
                    "╠ " + key + "ceb : cebuano" + "\n" + \
                    "╠ " + key + "ny : chichewa" + "\n" + \
                    "╠ " + key + "zhcn : chinese (simplified)" + "\n" + \
                    "╠ " + key + "zhtw : chinese (traditional)" + "\n" + \
                    "╠ " + key + "co : corsican" + "\n" + \
                    "╠ " + key + "hr : croatian" + "\n" + \
                    "╠ " + key + "cs : czech" + "\n" + \
                    "╠ " + key + "da : danish" + "\n" + \
                    "╠ " + key + "nl : dutch" + "\n" + \
                    "╠ " + key + "en : english" + "\n" + \
                    "╠ " + key + "eo : esperanto" + "\n" + \
                    "╠ " + key + "et : estonian" + "\n" + \
                    "╠ " + key + "tl : filipino" + "\n" + \
                    "╠ " + key + "fi : finnish" + "\n" + \
                    "╠ " + key + "fr : french" + "\n" + \
                    "╠ " + key + "fy : frisian" + "\n" + \
                    "╠ " + key + "gl : galician" + "\n" + \
                    "╠ " + key + "ka : georgian" + "\n" + \
                    "╠ " + key + "de : german" + "\n" + \
                    "╠ " + key + "el : greek" + "\n" + \
                    "╠ " + key + "gu : gujarati" + "\n" + \
                    "╠ " + key + "ht : haitian creole" + "\n" + \
                    "╠ " + key + "ha : hausa" + "\n" + \
                    "╠ " + key + "haw : hawaiian" + "\n" + \
                    "╠ " + key + "iw : hebrew" + "\n" + \
                    "╠ " + key + "hi : hindi" + "\n" + \
                    "╠ " + key + "hmn : hmong" + "\n" + \
                    "╠ " + key + "hu : hungarian" + "\n" + \
                    "╠ " + key + "is : icelandic" + "\n" + \
                    "╠ " + key + "ig : igbo" + "\n" + \
                    "╠ " + key + "id : indonesian" + "\n" + \
                    "╠ " + key + "ga : irish" + "\n" + \
                    "╠ " + key + "it : italian" + "\n" + \
                    "╠ " + key + "ja : japanese" + "\n" + \
                    "╠ " + key + "jw : javanese" + "\n" + \
                    "╠ " + key + "kn : kannada" + "\n" + \
                    "╠ " + key + "kk : kazakh" + "\n" + \
                    "╠ " + key + "km : khmer" + "\n" + \
                    "╠ " + key + "ko : korean" + "\n" + \
                    "╠ " + key + "ku : kurdish (kurmanji)" + "\n" + \
                    "╠ " + key + "ky : kyrgyz" + "\n" + \
                    "╠ " + key + "lo : lao" + "\n" + \
                    "╠ " + key + "la : latin" + "\n" + \
                    "╠ " + key + "lv : latvian" + "\n" + \
                    "╠ " + key + "lt : lithuanian" + "\n" + \
                    "╠ " + key + "lb : luxembourgish" + "\n" + \
                    "╠ " + key + "mk : macedonian" + "\n" + \
                    "╠ " + key + "mg : malagasy" + "\n" + \
                    "╠ " + key + "ms : malay" + "\n" + \
                    "╠ " + key + "ml : malayalam" + "\n" + \
                    "╠ " + key + "mt : maltese" + "\n" + \
                    "╠ " + key + "mi : maori" + "\n" + \
                    "╠ " + key + "mr : marathi" + "\n" + \
                    "╠ " + key + "mn : mongolian" + "\n" + \
                    "╠ " + key + "my : myanmar (burmese)" + "\n" + \
                    "╠ " + key + "ne : nepali" + "\n" + \
                    "╠ " + key + "no : norwegian" + "\n" + \
                    "╠ " + key + "ps : pashto" + "\n" + \
                    "╠ " + key + "fa : persian" + "\n" + \
                    "╠ " + key + "pl : polish" + "\n" + \
                    "╠ " + key + "pt : portuguese" + "\n" + \
                    "╠ " + key + "pa : punjabi" + "\n" + \
                    "╠ " + key + "ro : romanian" + "\n" + \
                    "╠ " + key + "ru : russian" + "\n" + \
                    "╠ " + key + "sm : samoan" + "\n" + \
                    "╠ " + key + "gd : scots gaelic" + "\n" + \
                    "╠ " + key + "sr : serbian" + "\n" + \
                    "╠ " + key + "st : sesotho" + "\n" + \
                    "╠ " + key + "sn : shona" + "\n" + \
                    "╠ " + key + "sd : sindhi" + "\n" + \
                    "╠ " + key + "si : sinhala" + "\n" + \
                    "╠ " + key + "sk : slovak" + "\n" + \
                    "╠ " + key + "sl : slovenian" + "\n" + \
                    "╠ " + key + "so : somali" + "\n" + \
                    "╠ " + key + "es : spanish" + "\n" + \
                    "╠ " + key + "su : sundanese" + "\n" + \
                    "╠ " + key + "sw : swahili" + "\n" + \
                    "╠ " + key + "sv : swedish" + "\n" + \
                    "╠ " + key + "tg : tajik" + "\n" + \
                    "╠ " + key + "ta : tamil" + "\n" + \
                    "╠ " + key + "te : telugu" + "\n" + \
                    "╠ " + key + "th : thai" + "\n" + \
                    "╠ " + key + "tr : turkish" + "\n" + \
                    "╠ " + key + "uk : ukrainian" + "\n" + \
                    "╠ " + key + "ur : urdu" + "\n" + \
                    "╠ " + key + "uz : uzbek" + "\n" + \
                    "╠ " + key + "vi : vietnamese" + "\n" + \
                    "╠ " + key + "cy : welsh" + "\n" + \
                    "╠ " + key + "xh : xhosa" + "\n" + \
                    "╠ " + key + "yi : yiddish" + "\n" + \
                    "╠ " + key + "yo : yoruba" + "\n" + \
                    "╠ " + key + "zu : zulu" + "\n" + \
                    "╠ " + key + "fil : Filipino" + "\n" + \
                    "╠ " + key + "he : Hebrew" + "\n" + \
                    "╚══[ Kaneki Public Bot ]" + "\n" + "\n\n" + \
                    "Contoh : " + key + "tr-id Kaneki"
    return helpTranslate

def bot(self, op):
    client = self.client
    global time
    global ast
    global groupParam
    try:
        if op.type == 0:
            print ("[ 0 ] END OF OPERATION")
            return

        if op.type == 5:
            if settings["autoAdd"] == True:
                Oa = 'ud4082219b6754e7b610f84d07d3b436b'
                client.sendContact(op.param1, Oa)
                client.findAndAddContactsByMid(op.param1)
            sendMention(op.param1, "Halo @!,Terimakasih telah menambahkan saya sebagai teman :3 Silahkan invite bot ini ke grup kamu~", [op.param1])

        if op.type == 17:
            if settings["welcomemsg"] == True:
                ginfo = client.getGroup(op.param1)
                contact = client.getContact(op.param2)
                client.sendContact(op.param1, contact.mid)
                sendMention(op.param1,"Hallo @! \nWelcome To ☞ " + str(ginfo.name) + " ☜" + "\nBudayakan Cek Note\nDan Semoga Betah Disini (ﾉ*>∀<)ﾉ♡", [op.param2])  
                                
        if op.type == 13:
            if clientMid in op.param3:
                G = client.getGroup(op.param1)
                if settings["autoJoin"] == True:
                    if settings["autoCancel"]["on"] == True:
                        if len(G.members) <= settings["autoCancel"]["members"]:
                            client.acceptGroupInvitation(op.param1)
                            Oa = 'ud4082219b6754e7b610f84d07d3b436b'
                            client.sendContact(op.param1, Oa)
                            sendMention(op.param1,"мaaғ @! ! мeмвer anda вelυм мencυĸυpι😊 ѕιlaнĸan нυвυngι oa dιaтaѕ!", [op.param2])
                            client.leaveGroup(op.param1)
                        else:
                            client.acceptGroupInvitation(op.param1)
                            xname = client.getContact(op.param2).displayName
                            Oa = 'ud4082219b6754e7b610f84d07d3b436b'
                            client.sendContact(op.param1, Oa)
                            sendMention(op.param1, "тerιмa ĸaѕιн @! тelaн мengυndang вoт ιnι!\n\nwajιв add oa dιaтaѕ! \nĸeтιĸ нelp υnтυĸ мelιнaт ғιтυre вoт ιnι!", [op.param2])


        if op.type in [22, 24]:
            if settings["autoLeave"] == True:
                sendMention(op.param1, "Oi asw @!,ngapain invite saya")
                client.leaveRoom(op.param1)

        if op.type == 26:
            try:
                print ("[ 26 ] SEND MESSAGE")
            #    msg_dict = msg._from
                msg = op.message
                text = msg.text
                msg_id = msg.id
                receiver = msg.to
                sender = msg._from
                setKey = settings["keyCommand"].title()
                if settings["setKey"] == False:
                    setKey = ''
                if msg.toType == 0 or msg.toType == 1 or msg.toType == 2:
                    if msg.toType == 0:
                        if sender != client.profile.mid:
                            to = sender
                        else:
                            to = receiver
                    elif msg.toType == 1:
                        to = receiver
                    elif msg.toType == 2:
                        to = receiver
                    if msg.contentType == 0:
                        if text is None:
                            return
                        else:
                            cmd = command(text)
                            if text.lower() == "help":
                             if sender not in settings["limituser"]:
                                  settings["limituser"][sender] = {'count':0,'limit':5}
                             if settings["limituser"][sender]['count'] == settings["limituser"][sender]["limit"]:
                                  sendMention(to, "@! anda terkena limit, ketik /open untuk membuka limit.", [sender])
                             else:
                                  sendMention(to, helpmess, [sender])
                                  Oa = 'ud4082219b6754e7b610f84d07d3b436b'
                                  client.sendContact(to, Oa)
                                  settings["limituser"][sender]["count"] = settings["limituser"][sender]["count"]+1

                            elif text.lower() == '/open':
                              if msg._from not in boty:
                                del settings["limituser"][sender]
                                sendMention(to, "@! limit anda sudah terbuka!", [sender])
				
                            elif text.lower() == 'limitlist':
                              if msg._from not in boty:
                                if settings["limituser"] == {}:
                                    client.sendMessage(to, "Kosong")
                                else:
                                    mc = "Daftar Limit："
                                    for mi_d in settings["limituser"]:
                                      if settings["limituser"][mi_d]["count"] == 5:
                                        mc += "\n->" + client.getContact(mi_d).displayName
                                    client.sendMessage(to, mc)
				
                    #        elif wait["limit"][msg._from] >= 5:
                     #           sendMention(to, "@! anda terkena limit! ketik /open untuk membuka limit!", [msg._from])
					    
                            elif cmd == "/siders":
                              if msg._from not in boty:
                                if sender not in settings["limituser"]:
                                  settings["limituser"][sender] = {'count':0,'limit':5}
                                if settings["limituser"][sender]['count'] == settings["limituser"][sender]["limit"]:
                                  sendMention(to, "@! anda terkena limit, ketik /open untuk membuka limit.", [sender])
                                else:
                                    sendMention(to, sidersmess, [sender])
                                    Oa = 'ud4082219b6754e7b610f84d07d3b436b'
                                    client.sendContact(to, Oa)
                                    settings["limituser"][sender]["count"] = settings["limituser"][sender]["count"]+1
				
                            elif cmd == "/search":
                              if msg._from not in boty:
                                if sender not in settings["limituser"]:
                                  settings["limituser"][sender] = {'count':0,'limit':5}
                                if settings["limituser"][sender]['count'] == settings["limituser"][sender]["limit"]:
                                  sendMention(to, "@! anda terkena limit, ketik /open untuk membuka limit.", [sender])
                                else:
                                    sendMention(to, searchmess, [sender])
                                    Oa = 'ud4082219b6754e7b610f84d07d3b436b'
                                    client.sendContact(to, Oa)
                                    settings["limituser"][sender]["count"] = settings["limituser"][sender]["count"]+1
				
                            elif cmd == "/group":
                              if msg._from not in boty:
                                if sender not in settings["limituser"]:
                                  settings["limituser"][sender] = {'count':0,'limit':5}
                                if settings["limituser"][sender]['count'] == settings["limituser"][sender]["limit"]:
                                  sendMention(to, "@! anda terkena limit, ketik /open untuk membuka limit.", [sender])
                                else:
                                    sendMention(to, groupmess, [sender])
                                    Oa = 'ud4082219b6754e7b610f84d07d3b436b'
                                    client.sendContact(to, Oa)
                                    settings["limituser"][sender]["count"] = settings["limituser"][sender]["count"]+1
				
                            elif cmd == "tts":
                              if msg._from not in boty:
                                if sender not in settings["limituser"]:
                                  settings["limituser"][sender] = {'count':0,'limit':5}
                                if settings["limituser"][sender]['count'] == settings["limituser"][sender]["limit"]:
                                  sendMention(to, "@! anda terkena limit, ketik /open untuk membuka limit.", [sender])
                                else:
                                    helpTextToSpeech = helptexttospeech()
                                    client.sendMessage(to, str(helpTextToSpeech))
                                    settings["limituser"][sender]["count"] = settings["limituser"][sender]["count"]+1
				
                            elif cmd == "translate":
                              if msg._from not in boty:
                                if sender not in settings["limituser"]:
                                  settings["limituser"][sender] = {'count':0,'limit':5}
                                if settings["limituser"][sender]['count'] == settings["limituser"][sender]["limit"]:
                                  sendMention(to, "@! anda terkena limit, ketik /open untuk membuka limit.", [sender])
                                else:
                                    helpTranslate = helptranslate()
                                    client.sendMessage(to, str(helpTranslate))
                                    settings["limituser"][sender]["count"] = settings["limituser"][sender]["count"]+1
				
                            elif cmd == "speed":
                              if msg._from not in boty:
                                if sender not in settings["limituser"]:
                                  settings["limituser"][sender] = {'count':0,'limit':5}
                                if settings["limituser"][sender]['count'] == settings["limituser"][sender]["limit"]:
                                  sendMention(to, "@! anda terkena limit, ketik /open untuk membuka limit.", [sender])
                                else:
                                    start = time.time()
                                    client.sendMessage(to, "Benchmarking...")
                                    elapsed_time = time.time() - start
                                    client.sendMessage(to, "[ Speed ]\nKecepatan mengirim pesan {} detik".format(str(elapsed_time)))
                                    settings["limituser"][sender]["count"] = settings["limituser"][sender]["count"]+1
				
                            elif cmd == "runtime":
                              if msg._from not in boty:
                                if sender not in settings["limituser"]:
                                  settings["limituser"][sender] = {'count':0,'limit':5}
                                if settings["limituser"][sender]['count'] == settings["limituser"][sender]["limit"]:
                                  sendMention(to, "@! anda terkena limit, ketik /open untuk membuka limit.", [sender])
                                else:
                                    timeNow = time.time()
                                    runtime = timeNow - botStart
                                    runtime = format_timespan(runtime)
                                    client.sendMessage(to, "Bot sudah berjalan selama {}".format(str(runtime)))
                                    settings["limituser"][sender]["count"] = settings["limituser"][sender]["count"]+1
				
                            elif cmd == "restart":
                              if msg._from in admin:
                                client.sendMessage(to, "Berhasil merestart Bot")
                                restartBot()
                            
                            elif cmd == "/curidp":
                              if msg._from not in boty:
                                if sender not in settings["limituser"]:
                                  settings["limituser"][sender] = {'count':0,'limit':5}
                                if settings["limituser"][sender]['count'] == settings["limituser"][sender]["limit"]:
                                  sendMention(to, "@! anda terkena limit, ketik /open untuk membuka limit.", [sender])
                                else:
                                    settings["limituser"][sender]["count"] = settings["limituser"][sender]["count"]+1
                                    key = eval(msg.contentMetadata["MENTION"])
                                    u = key["MENTIONEES"][0]["M"]
                                    a = client.getContact(u).pictureStatus
                                    if client.getContact(u).videoProfile != None:
                                        client.sendVideoWithURL(receiver, 'http://dl.profile.line.naver.jp/'+a+'/vp.small')
                                    else:
                                        client.sendImageWithURL(receiver, 'http://dl.profile.line.naver.jp/'+a)
                                    
                            elif cmd == "/curicover":
                              if msg._from not in boty:
                                if sender not in settings["limituser"]:
                                  settings["limituser"][sender] = {'count':0,'limit':5}
                                if settings["limituser"][sender]['count'] == settings["limituser"][sender]["limit"]:
                                  sendMention(to, "@! anda terkena limit, ketik /open untuk membuka limit.", [sender])
                                else:
                                    settings["limituser"][sender]["count"] = settings["limituser"][sender]["count"]+1
                                    key = eval(msg.contentMetadata["MENTION"])
                                    u = key["MENTIONEES"][0]["M"]
                                    a = client.getProfileCoverURL(mid=u)
                                    client.sendImageWithURL(receiver, a)
                                    
                            elif cmd == "oa": 
                              if msg._from in admin:
                                Oa = 'ud4082219b6754e7b610f84d07d3b436b'
                                client.sendContact(msg.to, Oa)
                                
                            elif "ayat:" in msg.text.lower():
                             if msg._from not in boty:
                                if sender not in settings["limituser"]:
                                  settings["limituser"][sender] = {'count':0,'limit':5}
                                if settings["limituser"][sender]['count'] == settings["limituser"][sender]["limit"]:
                                  sendMention(to, "@! anda terkena limit, ketik /open untuk membuka limit.", [sender])
                                else:
                                   sep = msg.text.split(" ")
                                   ayat = msg.text.lower().replace(sep[0] + " ","")
                                   path = "http://islamcdn.com/quran/media/audio/ayah/ar.alafasy/" + ayat
                                   sendMention(msg.to, "@! ini ayat yang kamu cari..", [sender])
                                   client.sendAudioWithURL(msg.to, path)
                                   settings["limituser"][sender]["count"] = settings["limituser"][sender]["count"]+1
					
                            elif "jadwal: " in msg.text.lower():
                              if msg._from not in boty:
                                if sender not in settings["limituser"]:
                                  settings["limituser"][sender] = {'count':0,'limit':5}
                                if settings["limituser"][sender]['count'] == settings["limituser"][sender]["limit"]:
                                  sendMention(to, "@! anda terkena limit, ketik /open untuk membuka limit.", [sender])
                                else:
                                        txt = msg.text.split(" ")
                                        teks = msg.text.lower().replace("jadwal: "+txt[1]+" ","")
                                        response = requests.get("https://farzain.xyz/api/premium/acaratv.php?apikey=kanekipubot&id="+txt[1]+"")
                                        data = response.json()
                                        pictig = str(data['status'])
                                        hasil = str(data['url'])
                                        text = "Status : "+pictig+"\n"+hasil+""
                                        client.sendMessage(msg.to, text)
                                        settings["limituser"][sender]["count"] = settings["limituser"][sender]["count"]+1
   
                            elif "call: " in msg.text.lower():
                              if msg._from not in boty:
                                if sender not in settings["limituser"]:
                                  settings["limituser"][sender] = {'count':0,'limit':5}
                                if settings["limituser"][sender]['count'] == settings["limituser"][sender]["limit"]:
                                  sendMention(to, "@! anda terkena limit, ketik /open untuk membuka limit.", [sender])
                                else:
                                    no = msg.text.lower().replace("call: ","")
                                    r = requests.get("http://apisora.herokuapp.com/prank/call/?no="+str(no))
                                    data = r.json()
                                    result = data["result"].replace('</br>', '\n')
                                    tgb = "[ Prank Call ]\n\n"
                                    tgb += "Status: "+str(data["status"])+"\n"
                                    tgb += "Result "+str(result)+"\n\n[ Finish ]"
                                    client.sendMessage(msg.to,str(tgb))
                                    Oa = 'ud4082219b6754e7b610f84d07d3b436b'
                                    client.sendContact(msg.to, Oa)
                                    settings["limituser"][sender]["count"] = settings["limituser"][sender]["count"]+1
		
                            elif "sms: " in msg.text.lower():
                              if msg._from not in boty:
                                if sender not in settings["limituser"]:
                                  settings["limituser"][sender] = {'count':0,'limit':5}
                                if settings["limituser"][sender]['count'] == settings["limituser"][sender]["limit"]:
                                  sendMention(to, "@! anda terkena limit, ketik /open untuk membuka limit.", [sender])
                                else:
                                    try:
                                        txt = msg.text.split(" ")
                                        teks = msg.text.lower().replace("sms: "+txt[1]+" ","")
                                        response = requests.get("http://leert.corrykalam.gq/sms.php?no="+txt[1]+"&text="+teks+"")
                                        data = response.json()
                                        pictig = str(data['status'])
                                        hasil = str(data['detail'])
                                        text = "Status : "+pictig+"\n\n"+hasil+""
                                        client.sendMessage(msg.to, text)
                                        Oa = 'ud4082219b6754e7b610f84d07d3b436b'
                                        client.sendContact(msg.to, Oa)
                                        settings["limituser"][sender]["count"] = settings["limituser"][sender]["count"]+1
                                    except Exception as e:
                                        client.sendMessage(msg.to, str(e))
                                        
                            elif msg.text in ["Accept invite"]:
                                if msg._from in admin:
                                    gid = client.getGroupIdsInvited()
                                    _list = ""
                                    for i in gid:
                                        if i is not None:
                                            gids = client.getGroup(i)
                                            _list += gids.name
                                            client.acceptGroupInvitation(i)
                                        else:
                                            break
                                    if gid is not None:
                                        client.sendMessage(msg.to,"Berhasil terima semua undangan dari grup :\n" + _list)
                                    else:
                                        client.sendMessage(msg.to,"Tidak ada grup yang tertunda saat ini")
                            
                            elif msg.text in ["Result"]:
                              if msg._from not in boty:
                                if sender not in settings["limituser"]:
                                  settings["limituser"][sender] = {'count':0,'limit':5}
                                if settings["limituser"][sender]['count'] == settings["limituser"][sender]["limit"]:
                                  sendMention(to, "@! anda terkena limit, ketik /open untuk membuka limit.", [sender])
                                else:
                                    mE = client.getProfile()
                                    gT = client.getGroupIdsJoined()
                                    fT = client.getAllContactIds()
                                    ginv = client.getGroupIdsInvited()
                                    client.sendMessage(msg.to,"「"+mE.displayName+"」 \n\nGroup total : " + str(len(gT))+ "\nFriend total: " +str(len(fT))+ "\nPending Group: " + str(len(ginv)))       
                                    settings["limituser"][sender]["count"] = settings["limituser"][sender]["count"]+1
				
                            elif "Gbcont" in msg.text:
                                if msg._from in admin:
                                  n = client.getGroupIdsJoined()                
                                  Oa = 'ud4082219b6754e7b610f84d07d3b436b'
                                  for people in n:                	
                                  	client.sendContact(people, Oa)
                        
                            elif "Gbc " in msg.text:
                                if msg._from in admin:
                                  bctxt = msg.text.replace("Gbc ","")
                                  n = client.getGroupIdsJoined()                
                                  Oa = 'ud4082219b6754e7b610f84d07d3b436b'
                                  for people in n:                	
                                        client.sendMessage(people, bctxt)
                                  #      client.sendContact(people, Oa)
                    
                            elif "Sider on" in msg.text:
                             if msg._from not in boty:
                                if sender not in settings["limituser"]:
                                  settings["limituser"][sender] = {'count':0,'limit':5}
                                if settings["limituser"][sender]['count'] == settings["limituser"][sender]["limit"]:
                                  sendMention(to, "@! anda terkena limit, ketik /open untuk membuka limit.", [sender])
                                else:
                                    try:
                                        del cctv['point'][msg.to]
                                        del cctv['sidermem'][msg.to]
                                        del cctv['cyduk'][msg.to]
                                    except:
                                        pass
                                    cctv['point'][msg.to] = msg.id
                                    cctv['sidermem'][msg.to] = ""
                                    cctv['cyduk'][msg.to]=True
                                    wait["Sider"] = True
                                    client.sendMessage(msg.to,"Siap On Cek Sider")
                                    settings["limituser"][sender]["count"] = settings["limituser"][sender]["count"]+1
                
                            elif "Sider off" in msg.text:
                             if msg._from not in boty:
                                if sender not in settings["limituser"]:
                                  settings["limituser"][sender] = {'count':0,'limit':5}
                                if settings["limituser"][sender]['count'] == settings["limituser"][sender]["limit"]:
                                  sendMention(to, "@! anda terkena limit, ketik /open untuk membuka limit.", [sender])
                                else:
                                    ginfo = client.getGroup(msg.to)
                                    gCreator = ginfo.creator.mid
                                    if msg.to in cctv['point']:
                                        cctv['cyduk'][msg.to]=False
                                        wait["Sider"] = False
                                        client.sendMessage(msg.to, "Cek Sider Off")
                                        settings["limituser"][sender]["count"] = settings["limituser"][sender]["count"]+1
                                    else:
                                        client.sendMessage(msg.to, "Heh Belom Di Set")
                    
                            elif "Sider on" in msg.text:
                              if msg._from not in boty:
                                if sender not in settings["limituser"]:
                                  settings["limituser"][sender] = {'count':0,'limit':5}
                                if settings["limituser"][sender]['count'] == settings["limituser"][sender]["limit"]:
                                  sendMention(to, "@! anda terkena limit, ketik /open untuk membuka limit.", [sender])
                                else:
                                    try:
                                        del cctv['point'][msg.to]
                                        del cctv['sidermem'][msg.to]
                                        del cctv['cyduk'][msg.to]
                                    except:
                                        pass
                                    cctv['point'][msg.to] = msg.id
                                    cctv['sidermem'][msg.to] = ""
                                    cctv['cyduk'][msg.to]=True
                                    wait["Sider"] = True
                                    client.sendMessage(msg.to,"Siap On Cek Sider")
                                    settings["limituser"][sender]["count"] = settings["limituser"][sender]["count"]+1
                
                            elif "Sider off" in msg.text:
                              if msg._from not in boty:
                                if sender not in settings["limituser"]:
                                  settings["limituser"][sender] = {'count':0,'limit':5}
                                if settings["limituser"][sender]['count'] == settings["limituser"][sender]["limit"]:
                                  sendMention(to, "@! anda terkena limit, ketik /open untuk membuka limit.", [sender])
                                else:
                                  if msg.to in cctv['point']:
                                      cctv['cyduk'][msg.to]=False
                                      wait["Sider"] = False
                                      client.sendMessage(msg.to, "Cek Sider Off")
                                      settings["limituser"][sender]["count"] = settings["limituser"][sender]["count"]+1
                                  else:
                                      client.sendMessage(msg.to, "Heh Belom Di Set")
                    
                            elif text.lower() == '/about':
                              if msg._from not in boty:
                                if sender not in settings["limituser"]:
                                  settings["limituser"][sender] = {'count':0,'limit':5}
                                if settings["limituser"][sender]['count'] == settings["limituser"][sender]["limit"]:
                                  sendMention(to, "@! anda terkena limit, ketik /open untuk membuka limit.", [sender])
                                else:
                                    try:
                                        settings["limituser"][sender]["count"] = settings["limituser"][sender]["count"]+1
                                        arr = []
                                        owner = "ud4082219b6754e7b610f84d07d3b436b"
                                        creator = client.getContact(owner)
                                        contact = client.getContact(owner)
                                        grouplist = client.getGroupIdsJoined()
                                        contactlist = client.getAllContactIds()
                                        blockedlist = client.getBlockedContactIds()
                                        ret_ = "╔══[ About Public Bot ]"
                                        ret_ += "\n╠ Line : {}".format(contact.displayName)
                                        ret_ += "\n╠ Group : {}".format(str(len(grouplist)))
                                        ret_ += "\n╠ Friend : {}".format(str(len(contactlist)))
                                        ret_ += "\n╠ Blocked : {}".format(str(len(blockedlist)))
                                        ret_ += "\n╠═══════"
                                        ret_ += "\n╠ Version : Public Bot 1"
                                        ret_ += "\n╠ Creator : {}".format(creator.displayName)
                                        ret_ += "\n╚═══════"
                                        client.sendMessage(msg.to, str(ret_))
                                    except Exception as e:
                                        client.sendMessage(msg.to, str(e))
                                        
                            elif msg.text.lower() in ["hi","hai","apa","P"]:
                              if msg._from not in boty:
                                if sender not in settings["limituser"]:
                                  settings["limituser"][sender] = {'count':0,'limit':5}
                                if settings["limituser"][sender]['count'] == settings["limituser"][sender]["limit"]:
                                  sendMention(to, "@! anda terkena limit, ketik /open untuk membuka limit.", [sender])
                                else:
                                    settings["limituser"][sender]["count"] = settings["limituser"][sender]["count"]+1
                                    sendMention(msg.to, "Hi @! sayang", [sender])
                                    
                            elif "/removechat" in msg.text.lower():
                                if msg._from in admin:
                                    try:
                                        client.removeAllMessages(op.param2)
                                        client.sendMessage(msg.to,"Done")
                                    except Exception as error:
                                        client.sendMessage(msg.to,"Error")
                        
                            elif "Apakah " in msg.text:
                              if sender not in settings["limituser"]:
                                  settings["limituser"][sender] = {'count':0,'limit':5}
                              if settings["limituser"][sender]['count'] == settings["limituser"][sender]["limit"]:
                                  sendMention(to, "@! anda terkena limit, ketik /open untuk membuka limit.", [sender])
                              else:
                                    tanya = msg.text.replace("Apakah ","")
                                    jawab = ("Ya","Tidak")
                                    jawaban = random.choice(jawab)
                                    client.sendMessage(msg.to,jawaban)
                                    settings["limituser"][sender]["count"] = settings["limituser"][sender]["count"]+1
            
#----------------------
                            elif "Dosa @" in msg.text:
                             if sender not in settings["limituser"]:
                                  settings["limituser"][sender] = {'count':0,'limit':5}
                             if settings["limituser"][sender]['count'] == settings["limituser"][sender]["limit"]:
                                  sendMention(to, "@! anda terkena limit, ketik /open untuk membuka limit.", [sender])
                             else:
                                   tanya = msg.text.replace("Dosa @","")
                                   jawab = ("60%","70%","80%","90%","100%","Tak terhingga")
                                   jawaban = random.choice(jawab)
                                   client.sendMessage(msg.to,"Dosanya " + tanya + "adalah " + jawaban + " Banyak banyak tobat Nak ")
                                   settings["limituser"][sender]["count"] = settings["limituser"][sender]["count"]+1
#----------------------
                            elif "Pahala @" in msg.text:
                             if sender not in settings["limituser"]:
                                  settings["limituser"][sender] = {'count':0,'limit':5}
                             if settings["limituser"][sender]['count'] == settings["limituser"][sender]["limit"]:
                                  sendMention(to, "@! anda terkena limit, ketik /open untuk membuka limit.", [sender])
                             else:
                                   tanya = msg.text.replace("Pahala @","")
                                   jawab = ("0%","20%","40%","50%","60%","Tak ada")
                                   jawaban = random.choice(jawab)
                                   client.sendMessage(msg.to,"Pahalanya " + tanya + "adalah " + jawaban + "\nTobatlah nak")
                                   settings["limituser"][sender]["count"] = settings["limituser"][sender]["count"]+1
                
                            elif "/Spam: " in msg.text:
                             if sender not in settings["limituser"]:
                                  settings["limituser"][sender] = {'count':0,'limit':5}
                             if settings["limituser"][sender]['count'] == settings["limituser"][sender]["limit"]:
                                  sendMention(to, "@! anda terkena limit, ketik /open untuk membuka limit.", [sender])
                             else:
                                     settings["limituser"][sender]["count"] = settings["limituser"][sender]["count"]+1
                                     cond = msg.text.split(" ")
                                     value = int(cond[2])
                                     text = msg.text.replace("/Spam: " + str(cond[1]) + " " + str(value) + " ","")
                                     ballon1 = value * (text + "\n")
                                     if cond[1] == "on":
                                         if value <= 20:
                                             for x in range(value):
                                                 client.sendMessage(msg.to, text)
                                         else:
                                             client.sendMessage(msg.to,"Jumlah spamming melebihi batas. Max 10")
                                     elif cond[1] == "off":
                                         if value <= 20:
                                             client.sendMessage(msg.to,ballon1)
                                         else:
                                             client.sendMessage(msg.to,"Jumlah spamming melebihi batas")
                                     else:
                                         client.sendMessage(msg.to,"Error condition")
                        
                            elif "Setlastpoint" in msg.text:
                             if sender not in settings["limituser"]:
                                  settings["limituser"][sender] = {'count':0,'limit':5}
                             if settings["limituser"][sender]['count'] == settings["limituser"][sender]["limit"]:
                                  sendMention(to, "@! anda terkena limit, ketik /open untuk membuka limit.", [sender])
                             else:
                                   if msg.to in wait2['readPoint']:
                                           try:
                                               settings["limituser"][sender]["count"] = settings["limituser"][sender]["count"]+1
                                               del wait2['readPoint'][msg.to]
                                               del wait2['readMember'][msg.to]
                                               del wait2['setTime'][msg.to]
                                           except:
                                               pass
                                           wait2['readPoint'][msg.to] = msg.id
                                           wait2['readMember'][msg.to] = ""
                                           wait2['setTime'][msg.to] = datetime.now().strftime('%H:%M:%S')
                                           wait2['ROM'][msg.to] = {}
                                           with open('sider.json', 'w') as fp:
                                            json.dump(wait2, fp, sort_keys=True, indent=4)
                                            client.sendMessage(msg.to,"Set the lastseens' point(｀・ω・´)\n\n" + datetime.now().strftime('%H:%M:%S'))
                                   else:
                                       try:
                                               del wait2['readPoint'][msg.to]
                                               del wait2['readMember'][msg.to]
                                               del wait2['setTime'][msg.to]
                                       except:
                                             pass
                                       wait2['readPoint'][msg.to] = msg.id
                                       wait2['readMember'][msg.to] = ""
                                       wait2['setTime'][msg.to] = datetime.now().strftime('%H:%M:%S')
                                       wait2['ROM'][msg.to] = {}
                                       with open('sider.json', 'w') as fp:
                                        json.dump(wait2, fp, sort_keys=True, indent=4)
                                        client.sendMessage(msg.to, "Set reading point:\n" + datetime.now().strftime('%H:%M:%S'))
                    
                            elif "Viewlastseen" in msg.text:
                             if sender not in settings["limituser"]:
                                  settings["limituser"][sender] = {'count':0,'limit':5}
                             if settings["limituser"][sender]['count'] == settings["limituser"][sender]["limit"]:
                                  sendMention(to, "@! anda terkena limit, ketik /open untuk membuka limit.", [sender])
                             else:
                                    if msg.to in wait2['readPoint']:
                                        if wait2["ROM"][msg.to].items() == []:
                                             client.sendMessage(msg.to, "Sider:\nNone")
                                             settings["limituser"][sender]["count"] = settings["limituser"][sender]["count"]+1
                                        else:
                                            chiya = []
                                            for rom in wait2["ROM"][msg.to].items():
                                                chiya.append(rom[1])
                               
                                            cmem = client.getContacts(chiya)
                                            zx = ""
                                            zxc = ""
                                            zx2 = []
                                            xpesan = 'Lurkers:\n'
                                        for x in range(len(cmem)):
                                                xname = str(cmem[x].displayName)
                                                pesan = ''
                                                pesan2 = pesan+"@a\n"
                                                xlen = str(len(zxc)+len(xpesan))
                                                xlen2 = str(len(zxc)+len(pesan2)+len(xpesan)-1)
                                                zx = {'S':xlen, 'E':xlen2, 'M':cmem[x].mid}
                                                zx2.append(zx)
                                                zxc += pesan2
                                                msg.contentType = 0
          
                                        msg.text = xpesan+ zxc + "\nLurking time: %s\nCurrent time: %s"%(wait2['setTime'][msg.to],datetime.now().strftime('%H:%M:%S'))
                                        lol ={'MENTION':str('{"MENTIONEES":'+json.dumps(zx2).replace(' ','')+'}')}
                                        msg.contentMetadata = lol
                                        try:
                                          client.sendMessage(msg)
                                        except Exception as error:
                                              pass
                                        pass
               
           
                                    else:
                                        client.sendMessage(msg.to, "Lurking has not been set.")
                    
                            elif "Gbcpict " in msg.text:
                                if msg._from in admin:
                                  txt = msg.text.split(" ")
                                  bcteks = msg.text.replace("Gbcpict "+txt[1]+" "+txt[2]+" ","")
                                  n = client.getGroupIdsJoined()
                                  client.sendImageWithURL(to, txt[2])	
                                  client.sendMessage(to, bcteks)
                                  client.sendContact(to, txt[1])

                            elif "/keluar" in msg.text:
                             if sender not in settings["limituser"]:
                                  settings["limituser"][sender] = {'count':0,'limit':5}
                             if settings["limituser"][sender]['count'] == settings["limituser"][sender]["limit"]:
                                  sendMention(to, "@! anda terkena limit, ketik /open untuk membuka limit.", [sender])
                             else:
                                    if msg.toType == 2:
                                        ginfo = client.getGroup(msg.to)
                                        try:
                                            settings["limituser"][sender]["count"] = settings["limituser"][sender]["count"]+1
                                            Oa= 'ud4082219b6754e7b610f84d07d3b436b'
                                            client.sendContact(msg.to, Oa)
                                            client.leaveGroup(msg.to)
                                        except:
                                            pass
                                    
                            elif msg.text in ["Woy","woy","Woi","woi","bot","Bot"]:
                             if sender not in settings["limituser"]:
                                  settings["limituser"][sender] = {'count':0,'limit':5}
                             if settings["limituser"][sender]['count'] == settings["limituser"][sender]["limit"]:
                                  sendMention(to, "@! anda terkena limit, ketik /open untuk membuka limit.", [sender])
                             else:
                                  settings["limituser"][sender]["count"] = settings["limituser"][sender]["count"]+1
                                  quote = ['Istri yang baik itu Istri yang Mengizinkan Suaminya untuk Poligami 😂😂😂.','Kunci Untuk Bikin Suami Bahagia itu cuma satu..\nIzinkan Suamimu Untuk Selingkuh Coyyy ','Ah Kupret Lu','Muka Lu Kaya Jamban','Ada Orang kah disini?','Sange Euy','Ada Perawan Nganggur ga Coy?']
                                  psn = random.choice(quote)
                                  client.sendMessage(msg.to,psn)
                
                            elif "detectout" in msg.text:
                               if msg._from in admin:
                                groups = client.getGroupIdsJoined()
                                for group in groups:               	
                                    G = client.getGroup(group)
                                    if len(G.members) <= wait["autoCancel"]["members"]:
                                        Oa = 'ud4082219b6754e7b610f84d07d3b436b'
                                        owner = 'u5601bdfbc2c67e7adcb95f790127b193'
                                  #      sendMention(msg.to, "Halo @! detect group dibawah 10 members akan dimulai.", [sender])
                                        client.sendContact(group, Oa)
                                        client.sendMessage(group,"мaaғ! мeмвer anda вelυм мencυĸυpι😊 ѕιlaнĸan нυвυngι oa dιaтaѕ!")
                                        client.leaveGroup(group)
					
                            elif "meme: " in msg.text.lower():
                              if msg._from not in boty:
                                if sender not in settings["limituser"]:
                                     settings["limituser"][sender] = {'count':0,'limit':5}
                                if settings["limituser"][sender]['count'] == settings["limituser"][sender]["limit"]:
                                     sendMention(to, "@! anda terkena limit, ketik /open untuk membuka limit.", [sender])
                                else:
                                    try:
                                        txt = msg.text.split(" ")
                                        teks = msg.text.lower().replace("meme: "+txt[1]+" ","")
                                        data = []
                                        r = requests.get("http://ofckaneki.dynu.net/bot.php")
                                        r = eval(r.text)
                                        for a in r:
                                            data.append(a)
                                        c = random.choice(data)
                                        foto = "https://memegen.link/"+c+"/"+txt[1]+"/"+teks+".jpg"
                                        client.sendImageWithURL(msg.to, foto)
                                        settings["limituser"][sender]["count"] = settings["limituser"][sender]["count"]+1
                                    except Exception as e:
                                        client.sendMessage(msg.to, str(e))
                                        
                            elif "retro: " in msg.text.lower():
                              if msg._from not in boty:
                                if sender not in settings["limituser"]:
                                     settings["limituser"][sender] = {'count':0,'limit':5}
                                if settings["limituser"][sender]['count'] == settings["limituser"][sender]["limit"]:
                                     sendMention(to, "@! anda terkena limit, ketik /open untuk membuka limit.", [sender])
                                else:
                                    try:
                                        txt = msg.text.split(" ")
                                        teks = msg.text.lower().replace("retro: "+txt[1]+" ","")
                                        satu = ["1","2","3","4","5"]
                                        dua = ["1","2","3","4"]
                                        k = random.choice(satu)
                                        w = random.choice(dua)
                                        response = requests.get("http://leert.corrykalam.gq/retrowave.php?text1="+txt[1]+"&text2="+teks+"&text3=&btype="+k+"&ttype="+w+"")
                                        data = response.json()
                                        hasil = str(data['image'])
                                        download = str(data['image'])                      
                                        client.sendMessage(receiver, download)
                                        client.sendImageWithURL(receiver, hasil)
                                        Oa = 'ud4082219b6754e7b610f84d07d3b436b'
                                        client.sendContact(receiver, Oa)
                                        settings["limituser"][sender]["count"] = settings["limituser"][sender]["count"]+1
                                    except Exception as e:
                                        client.sendMessage(receiver, str(e))
			
                            elif "pcid: " in msg.text.lower():
                              if msg._from not in boty:
                                if sender not in settings["limituser"]:
                                     settings["limituser"][sender] = {'count':0,'limit':5}
                                if settings["limituser"][sender]['count'] == settings["limituser"][sender]["limit"]:
                                     sendMention(to, "@! anda terkena limit, ketik /open untuk membuka limit.", [sender])
                                else:
                                   txt = msg.text.split(" ")
                                   teks = msg.text.lower().replace("pcid: "+txt[1]+" ","")
                                   x = client.findContactsByUserid(txt[1])
                                   a = client.getContact(msg._from)
                                   sendMention(x.mid,"Anda mendapatkan pesan dari @!\n\n "+teks+"", [a.mid])
                                   sendMention(msg.to,"Sukses mengirim pesan ke "+x.displayName+"\nDari: @!\nPesan: "+teks+"", [a.mid])
                                   Oa = 'ud4082219b6754e7b610f84d07d3b436b'
                                   client.sendContact(msg.to, Oa)
                                   settings["limituser"][sender]["count"] = settings["limituser"][sender]["count"]+1

                            elif "saran: " in msg.text.lower():
                              if msg._from not in boty:
                                if sender not in settings["limituser"]:
                                     settings["limituser"][sender] = {'count':0,'limit':5}
                                if settings["limituser"][sender]['count'] == settings["limituser"][sender]["limit"]:
                                     sendMention(to, "@! anda terkena limit, ketik /open untuk membuka limit.", [sender])
                                else:
                                   settings["limituser"][sender]["count"] = settings["limituser"][sender]["count"]+1
                                   txt = msg.text.split(" ")
                                   teks = msg.text.lower().replace("saran: ","")
                                   line = 'syahraqa'
                                   x = client.findContactsByUserid(line)
                                   a = client.getContact(msg._from)
                                   sendMention(x.mid,"Anda mendapatkan pesan dari @!\n\nSaran:\n"+teks+"", [a.mid])
                                   sendMention(msg.to,"Sukses mengirim saran ke "+x.displayName+"\nDari: @!\nSaran : "+teks+"", [a.mid])
                                   Oa = 'ud4082219b6754e7b610f84d07d3b436b'
                                   client.sendContact(msg.to, Oa)
				
                            elif "Gbcon: " in msg.text:
                              if msg._from in admin:
                                n = client.getGroupIdsJoined()   
                                y = msg.text.split(" ")
                                k = msg.text.replace("Gbcon: "+y[1]+" ","")
                                Oa = y[1]
                                for people in n:                	
                                	client.sendContact(people, Oa)

                            elif "fs: " in msg.text.lower():
                              if msg._from not in boty:
                                if sender not in settings["limituser"]:
                                     settings["limituser"][sender] = {'count':0,'limit':5}
                                if settings["limituser"][sender]['count'] == settings["limituser"][sender]["limit"]:
                                     sendMention(to, "@! anda terkena limit, ketik /open untuk membuka limit.", [sender])
                                else:
                                    try:
                                        txt = msg.text.split(" ")
                                        teks = msg.text.lower().replace("fs: "+txt[1]+" ","")
                                        response = requests.get("https://farzain.com/api/premium/fs.php?apikey=kanekipubot&id="+txt[1]+"")
                                        data = response.json()
                                        pictig = str(data['status'])
                                        hasil = str(data['url'])
                                        text = "Status : "+pictig+""
                                        client.sendMessage(msg.to, text)
                                        client.sendImageWithURL(msg.to, hasil)
                                        Oa = 'ud4082219b6754e7b610f84d07d3b436b'
                                        client.sendContact(msg.to, Oa)
                                        settings["limituser"][sender]["count"] = settings["limituser"][sender]["count"]+1
                                    except Exception as e:
                                        client.sendMessage(msg.to, str(e))

                            elif msg.text.lower() in ["gcreator"]:
                             if msg._from not in boty:
                                if sender not in settings["limituser"]:
                                     settings["limituser"][sender] = {'count':0,'limit':5}
                                if settings["limituser"][sender]['count'] == settings["limituser"][sender]["limit"]:
                                     sendMention(to, "@! anda terkena limit, ketik /open untuk membuka limit.", [sender])
                                else:
                                    msg.contentType = 13
                                    ginfo = client.getGroup(msg.to)
                                    gCreator = ginfo.creator.mid
                                    try:
                                        msg.contentMetadata = {'mid': gCreator}
                                        gCreator1 = ginfo.creator.displayName
                                        settings["limituser"][sender]["count"] = settings["limituser"][sender]["count"]+1
                        
                                    except:
                                        gCreator = "Error"
                                    client.sendMessage(msg.to, "Group Creator : " + gCreator1)
                                    client.sendContact(msg.to, gCreator)

                            elif "gimage " in msg.text.lower():
                              if msg._from not in boty:
                                if sender not in settings["limituser"]:
                                     settings["limituser"][sender] = {'count':0,'limit':5}
                                if settings["limituser"][sender]['count'] == settings["limituser"][sender]["limit"]:
                                     sendMention(to, "@! anda terkena limit, ketik /open untuk membuka limit.", [sender])
                                else:
                                      googl = msg.text.lower().replace("gimage ","")
                                      url = 'https://www.google.com/search?hl=en&biw=1366&bih=659&tbm=isch&sa=1&ei=vSD9WYimHMWHvQTg_53IDw&q=' + googl
                                      raw_html = (download_page(url))
                                      items = []
                                      items = items + (_images_get_all_items(raw_html))
                                      path = random.choice(items)
                                      try:
                                          start = time.time()
                                          client.sendImageWithURL(msg.to,random.choice(items))
                                          client.sendImageWithURL(msg.to,random.choice(items))
                                          client.sendImageWithURL(msg.to,random.choice(items))
                                          client.sendMessage(msg.to,"Total Image Links ="+str(len(items)))
                                          settings["limituser"][sender]["count"] = settings["limituser"][sender]["count"]+1
                                      except Exception as njer:
                                            client.sendMessage(msg.to, str(njer))
				
                            elif "info saya" in msg.text.lower():
                             if msg._from not in boty:
                                if sender not in settings["limituser"]:
                                     settings["limituser"][sender] = {'count':0,'limit':5}
                                if settings["limituser"][sender]['count'] == settings["limituser"][sender]["limit"]:
                                     sendMention(to, "@! anda terkena limit, ketik /open untuk membuka limit.", [sender])
                                else:
                                  settings["limituser"][sender]["count"] = settings["limituser"][sender]["count"]+1
                                  kelamin = ("Waria","Laki-laki","Perempuan","Tidak Diketahui","Bencong")
                                  wajah = ("Standar","Ganteng","Cantik","Beruk","Hancur")
                                  status = ("Menikah","Pacaran","Jones")
                                  k = random.choice(kelamin)
                                  w = random.choice(wajah)
                                  s = random.choice(status)
                                  client.sendMessage(msg.to,"• Nama : @!\n• Kelamin : "+k+"\n• Wajah : "+w+"\n• Status Kehidupan : "+s, [sender])
#-------------Fungsi Pap-----------------------------#
# Pembatas Script #
                            elif "Surat:" in msg.text:
                             if msg._from not in boty:
                                if sender not in settings["limituser"]:
                                     settings["limituser"][sender] = {'count':0,'limit':5}
                                if settings["limituser"][sender]['count'] == settings["limituser"][sender]["limit"]:
                                     sendMention(to, "@! anda terkena limit, ketik /open untuk membuka limit.", [sender])
                                else:
                                  try:
                                     settings["limituser"][sender]["count"] = settings["limituser"][sender]["count"]+1
                                     sep = msg.text.split(" ")
                                     surah = int(text.replace(sep[0] + " ",""))
                                     if 0 < surah < 115:
                                         if surah not in [2, 3, 4, 5, 6, 7, 9, 10, 11, 12, 16, 17, 18, 20, 21, 23, 26, 37]:
                                             if len(str(surah)) == 1:
                                                 audionya = "https://audio5.qurancentral.com/mishary-rashid-alafasy/mishary-rashid-alafasy-00" + str(surah) + "-muslimcentral.com.mp3"
                                                 sendMention(msg.to, "@! ini surat yang kamu minta..", [msg._from])
                                                 client.sendAudioWithURL(msg.to, audionya)
                                             elif len(str(surah)) == 2:
                                                 audionya = "https://audio5.qurancentral.com/mishary-rashid-alafasy/mishary-rashid-alafasy-0" + str(surah) + "-muslimcentral.com.mp3"
                                                 sendMention(msg.to, "@! ini surat yang kamu minta..", [msg._from])
                                                 client.sendAudioWithURL(msg.to, audionya)
                                             else:
                                                 audionya = "https://audio5.qurancentral.com/mishary-rashid-alafasy/mishary-rashid-alafasy-" + str(surah) + "-muslimcentral.com.mp3"
                                                 sendMention(msg.to, "@! ini surat yang kamu minta..", [msg._from])
                                                 client.sendAudioWithURL(msg.to, audionya)
                                         else:
                                             sendMention(msg.to, "@! Surah yang kamu minta terlalu panjang", [msg._from])
                                     else:
                                         sendMention(msg.to, "@! Quran hanya 114 surah", [msg._from])
                                  except Exception as error:
                                      client.sendMessage(msg.to, "error\n"+str(error))
                              
                            elif "neon: " in msg.text.lower():
                              if msg._from not in boty:
                                if sender not in settings["limituser"]:
                                     settings["limituser"][sender] = {'count':0,'limit':5}
                                if settings["limituser"][sender]['count'] == settings["limituser"][sender]["limit"]:
                                     sendMention(to, "@! anda terkena limit, ketik /open untuk membuka limit.", [sender])
                                else:
                                    try:
                                        settings["limituser"][sender]["count"] = settings["limituser"][sender]["count"]+1
                                        txt = msg.text.split(" ")
                                        teks = msg.text.lower().replace("neon: ","")
                                        color = ["red","yellow","green","purple","violet","blue"]
                                        k = random.choice(color)
                                        foto = "https://ari-api.herokuapp.com/neon?text="+teks+"&color="+k+""
                                        sendMention(msg.to, "@! ini foto neon pesanan kamu..", [msg._from])
                                        client.sendImageWithURL(msg.to, foto)
                                    except Exception as e:
                                        client.sendMessage(msg.to, str(e))
                
                            elif 'ytmp3: ' in text.lower():
                              if msg._from not in boty:
                                if sender not in settings["limituser"]:
                                     settings["limituser"][sender] = {'count':0,'limit':5}
                                if settings["limituser"][sender]['count'] == settings["limituser"][sender]["limit"]:
                                     sendMention(to, "@! anda terkena limit, ketik /open untuk membuka limit.", [sender])
                                else:
                                    url_= text.lower().replace('ytmp3: ','')
                                    params = {'key':'betakey','q':url_}
                                    path = 'http://rahandiapi.herokuapp.com/youtubeapi?'
                                    r = requests.get(path,params=params).json()
                                    client.sendMessage(msg.to, r['result']['audiolist'][4]['url'])
                                    settings["limituser"][sender]["count"] = settings["limituser"][sender]["count"]+1
                            
                            
                            elif msg.text.lower().startswith("sholat "):
                              if msg._from not in boty:
                                if sender not in settings["limituser"]:
                                     settings["limituser"][sender] = {'count':0,'limit':5}
                                if settings["limituser"][sender]['count'] == settings["limituser"][sender]["limit"]:
                                     sendMention(to, "@! anda terkena limit, ketik /open untuk membuka limit.", [sender])
                                else:
                                    location = msg.text.lower().replace("sholat ","")
                                    params = {'lokasi':location}
                                    with requests.session() as web:
                                        r = requests.get("http://leert.corrykalam.gq/praytime.php?location="+location+"")                      
                                        data = r.text
                                        data = json.loads(data)
                                        if data[1] != "Subuh : " and data[2] != "Dzuhur : " and data[3] != "Ashr : " and data[4] != "Maghrib : " and data[5] != "Isha : ":
                                            ret_ = "[ Prayer Schedule ]"
                                            ret_ += "\n\nLocation : " + data[0]
                                            ret_ += "\n" + data[1]
                                            ret_ += "\n" + data[2]
                                            ret_ += "\n" + data[3]               
                                            ret_ += "\n" + data[4]
                                            ret_ += "\n" + data[5]
                                        else:
                                               ret_ = "[ Prayer Schedule ] Error : Location not found" 
                                        client.sendMessage(msg.to, str(ret_))
                                        settings["limituser"][sender]["count"] = settings["limituser"][sender]["count"]+1
                                    
                            elif cmd == "autoadd on":
                              if msg._from in admin:
                                settings["autoAdd"] = True
                                client.sendMessage(to, "Berhasil mengaktifkan auto add")
                            elif cmd == "autoadd off":
                              if msg._from in admin:
                                settings["autoAdd"] = False
                                client.sendMessage(to, "Berhasil menonaktifkan auto add")
                            elif cmd == "autojoin on":
                              if msg._from in admin:
                                settings["autoJoin"] = True
                                client.sendMessage(to, "Berhasil mengaktifkan auto join")
                            elif cmd == "autojoin off":
                              if msg._from in admin:
                                settings["autoJoin"] = False
                                client.sendMessage(to, "Berhasil menonaktifkan auto join")
                            elif cmd == "autoleave on":
                              if msg._from in admin:
                                settings["autoLeave"] = True
                                client.sendMessage(to, "Berhasil mengaktifkan auto leave")
                            elif cmd == "autoleave off":
                              if msg._from in admin:
                                settings["autoLeave"] = False
                                client.sendMessage(to, "Berhasil menonaktifkan auto leave")
                            elif cmd == "autorespon on":
                              if msg._from in admin:
                                settings["autoRespon"] = True
                                client.sendMessage(to, "Berhasil mengaktifkan auto respon")
                            elif cmd == "autorespon off":
                              if msg._from in admin:
                                settings["autoRespon"] = False
                                client.sendMessage(to, "Berhasil menonaktifkan auto respon")
                            elif cmd == "autoread on":
                              if msg._from in admin:
                                settings["autoRead"] = True
                                client.sendMessage(to, "Berhasil mengaktifkan auto read")
                            elif cmd == "autoread off":
                              if msg._from in admin:
                                settings["autoRead"] = False
                                client.sendMessage(to, "Berhasil menonaktifkan auto read")
                            elif cmd == "autojointicket on":
                              if msg._from in admin:
                                settings["autoJoinTicket"] = True
                                client.sendMessage(to, "Berhasil mengaktifkan auto join by ticket")
                            elif cmd == "autoJoinTicket off":
                              if msg._from in admin:
                                settings["autoJoin"] = False
                                client.sendMessage(to, "Berhasil menonaktifkan auto join by ticket")
                            elif cmd == "checkcontact on":
                              if msg._from in admin:
                                settings["checkContact"] = True
                                client.sendMessage(to, "Berhasil mengaktifkan check details contact")
                            elif cmd == "checkcontact off":
                              if msg._from in admin:
                                settings["checkContact"] = False
                                client.sendMessage(to, "Berhasil menonaktifkan check details contact")
                            elif cmd == "checkpost on":
                              if msg._from in admin:
                                settings["checkPost"] = True
                                client.sendMessage(to, "Berhasil mengaktifkan check details post")
                            elif cmd == "checkpost off":
                              if msg._from in admin:
                                settings["checkPost"] = False
                                client.sendMessage(to, "Berhasil menonaktifkan check details post")
                            elif cmd == "checksticker on":
                              if msg._from in admin:
                                settings["checkSticker"] = True
                                client.sendMessage(to, "Berhasil mengaktifkan check details sticker")
                            elif cmd == "checksticker off":
                              if msg._from in admin:
                                settings["checkSticker"] = False
                                client.sendMessage(to, "Berhasil menonaktifkan check details sticker")
                            elif cmd == "unsendchat on":
                              if msg._from in admin:
                                settings["unsendMessage"] = True
                                client.sendMessage(to, "Berhasil mengaktifkan unsend message")
                            elif cmd == "unsendchat off":
                              if msg._from in admin:
                                settings["unsendMessage"] = False
                                client.sendMessage(to, "Berhasil menonaktifkan unsend message")
                            elif cmd == "status":
                              if msg._from in admin:
                                try:
                                    ret_ = "╔══[ Status ]"
                                    if settings["autoAdd"] == True: ret_ += "\n╠══[ ON ] Auto Add"
                                    else: ret_ += "\n╠══[ OFF ] Auto Add"
                                    if settings["autoJoin"] == True: ret_ += "\n╠══[ ON ] Auto Join"
                                    else: ret_ += "\n╠══[ OFF ] Auto Join"
                                    if settings["autoLeave"] == True: ret_ += "\n╠══[ ON ] Auto Leave Room"
                                    else: ret_ += "\n╠══[ OFF ] Auto Leave Room"
                                    if settings["autoJoinTicket"] == True: ret_ += "\n╠══[ ON ] Auto Join Ticket"
                                    else: ret_ += "\n╠══[ OFF ] Auto Join Ticket"
                                    if settings["autoRead"] == True: ret_ += "\n╠══[ ON ] Auto Read"
                                    else: ret_ += "\n╠══[ OFF ] Auto Read"
                                    if settings["autoRespon"] == True: ret_ += "\n╠══[ ON ] Detect Mention"
                                    else: ret_ += "\n╠══[ OFF ] Detect Mention"
                                    if settings["checkContact"] == True: ret_ += "\n╠══[ ON ] Check Contact"
                                    else: ret_ += "\n╠══[ OFF ] Check Contact"
                                    if settings["checkPost"] == True: ret_ += "\n╠══[ ON ] Check Post"
                                    else: ret_ += "\n╠══[ OFF ] Check Post"
                                    if settings["checkSticker"] == True: ret_ += "\n╠══[ ON ] Check Sticker"
                                    else: ret_ += "\n╠══[ OFF ] Check Sticker"
                                    if settings["setKey"] == True: ret_ += "\n╠══[ ON ] Set Key"
                                    else: ret_ += "\n╠══[ OFF ] Set Key"
                                    if settings["unsendMessage"] == True: ret_ += "\n╠══[ ON ] Unsend Message"
                                    else: ret_ += "\n╠══[ OFF ] Unsend Message"
                                    ret_ += "\n╚══[ Status ]"
                                    client.sendMessage(to, str(ret_))
                                except Exception as e:
                                    client.sendMessage(msg.to, str(e))
# Pembatas Script #
                            elif cmd == "crash":
                              if msg._from in admin:
                                client.sendContact(to, "u1f41296217e740650e0448b96851a3e2',")
                            elif cmd.startswith("changename:"):
                              if msg._from in admin:
                                sep = text.split(" ")
                                string = text.replace(sep[0] + " ","")
                                if len(string) <= 20:
                                    profile = client.getProfile()
                                    profile.displayName = string
                                    client.updateProfile(profile)
                                    client.sendMessage(to,"Berhasil mengganti display name menjadi{}".format(str(string)))
                            elif cmd.startswith("changebio:"):
                              if msg._from in admin:
                                sep = text.split(" ")
                                string = text.replace(sep[0] + " ","")
                                if len(string) <= 500:
                                    profile = client.getProfile()
                                    profile.statusMessage = string
                                    client.updateProfile(profile)
                                    client.sendMessage(to,"Berhasil mengganti status message menjadi{}".format(str(string)))
                            elif cmd == "me":
                                sendMention(to, "Hai @! ini contact kamu..", [sender])
                                client.sendContact(to, sender)
                            elif cmd == "mymid":
                                client.sendMessage(to, "[ MID ]\n{}".format(sender))
                            elif cmd == "myname":
                                contact = client.getContact(sender)
                                client.sendMessage(to, "[ Display Name ]\n{}".format(contact.displayName))
                            elif cmd == "mybio":
                                contact = client.getContact(sender)
                                client.sendMessage(to, "[ Status Message ]\n{}".format(contact.statusMessage))
                            elif cmd == "mypicture":
                                contact = client.getContact(sender)
                                client.sendImageWithURL(to,"http://dl.profile.line-cdn.net/{}".format(contact.pictureStatus))
                            elif cmd == "myvideoprofile":
                                contact = client.getContact(sender)
                                client.sendVideoWithURL(to,"http://dl.profile.line-cdn.net/{}/vp".format(contact.pictureStatus))
                            elif cmd == "mycover":
                                channel = client.getProfileCoverURL(sender)          
                                path = str(channel)
                                client.sendImageWithURL(to, path)
                            elif cmd.startswith("cloneprofile "):
                              if msg._from in admin:
                                if 'MENTION' in msg.contentMetadata.keys()!= None:
                                    names = re.findall(r'@(\w+)', text)
                                    mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                                    mentionees = mention['MENTIONEES']
                                    lists = []
                                    for mention in mentionees:
                                        if mention["M"] not in lists:
                                            lists.append(mention["M"])
                                    for ls in lists:
                                        contact = client.getContact(ls)
                                        client.cloneContactProfile(ls)
                                        client.sendMessage(to, "Berhasil mengclone profile {}".format(contact.displayName))
                            elif cmd == "restoreprofile":
                              if msg._from in admin:
                                try:
                                    clientProfile = client.getProfile()
                                    clientProfile.displayName = str(settings["myProfile"]["displayName"])
                                    clientProfile.statusMessage = str(settings["myProfile"]["statusMessage"])
                                    clientProfile.pictureStatus = str(settings["myProfile"]["pictureStatus"])
                                    client.updateProfileAttribute(8, clientProfile.pictureStatus)
                                    client.updateProfile(clientProfile)
                                    coverId = str(settings["myProfile"]["coverId"])
                                    client.updateProfileCoverById(coverId)
                                    client.sendMessage(to, "Berhasil restore profile tunggu beberapa saat sampai profile berubah")
                                except Exception as e:
                                    client.sendMessage(to, "Gagal restore profile")
                                    logError(error)
                            elif cmd == "backupprofile":
                              if msg._from in admin:
                                try:
                                    profile = client.getProfile()
                                    settings["myProfile"]["displayName"] = str(profile.displayName)
                                    settings["myProfile"]["statusMessage"] = str(profile.statusMessage)
                                    settings["myProfile"]["pictureStatus"] = str(profile.pictureStatus)
                                    coverId = client.getProfileDetail()["result"]["objectId"]
                                    settings["myProfile"]["coverId"] = str(coverId)
                                    client.sendMessage(to, "Berhasil backup profile")
                                except Exception as e:
                                    client.sendMessage(to, "Gagal backup profile")
                                    logError(error)
                            elif cmd.startswith("stealmid "):
                                if 'MENTION' in msg.contentMetadata.keys()!= None:
                                    names = re.findall(r'@(\w+)', text)
                                    mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                                    mentionees = mention['MENTIONEES']
                                    lists = []
                                    for mention in mentionees:
                                        if mention["M"] not in lists:
                                            lists.append(mention["M"])
                                    ret_ = "[ Mid User ]"
                                    for ls in lists:
                                        ret_ += "\n{}".format(str(ls))
                                    client.sendMessage(to, str(ret_))
                            elif cmd.startswith("stealname "):
                                if 'MENTION' in msg.contentMetadata.keys()!= None:
                                    names = re.findall(r'@(\w+)', text)
                                    mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                                    mentionees = mention['MENTIONEES']
                                    lists = []
                                    for mention in mentionees:
                                        if mention["M"] not in lists:
                                            lists.append(mention["M"])
                                    for ls in lists:
                                        contact = client.getContact(ls)
                                        client.sendMessage(to, "[ Display Name ]\n{}".format(str(contact.displayName)))
                            elif cmd.startswith("stealbio "):
                                if 'MENTION' in msg.contentMetadata.keys()!= None:
                                    names = re.findall(r'@(\w+)', text)
                                    mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                                    mentionees = mention['MENTIONEES']
                                    lists = []
                                    for mention in mentionees:
                                        if mention["M"] not in lists:
                                            lists.append(mention["M"])
                                    for ls in lists:
                                        contact = client.getContact(ls)
                                        client.sendMessage(to, "[ Status Message ]\n{}".format(str(contact.statusMessage)))
                            elif cmd.startswith("stealpicture"):
                                if 'MENTION' in msg.contentMetadata.keys()!= None:
                                    names = re.findall(r'@(\w+)', text)
                                    mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                                    mentionees = mention['MENTIONEES']
                                    lists = []
                                    for mention in mentionees:
                                        if mention["M"] not in lists:
                                            lists.append(mention["M"])
                                    for ls in lists:
                                        contact = client.getContact(ls)
                                        path = "http://dl.profile.line.naver.jp/{}".format(contact.pictureStatus)
                                        client.sendImageWithURL(to, str(path))
                            elif cmd.startswith("stealvideoprofile "):
                                if 'MENTION' in msg.contentMetadata.keys()!= None:
                                    names = re.findall(r'@(\w+)', text)
                                    mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                                    mentionees = mention['MENTIONEES']
                                    lists = []
                                    for mention in mentionees:
                                        if mention["M"] not in lists:
                                            lists.append(mention["M"])
                                    for ls in lists:
                                        contact = client.getContact(ls)
                                        path = "http://dl.profile.line.naver.jp/{}/vp".format(contact.pictureStatus)
                                        client.sendVideoWithURL(to, str(path))
                            elif cmd.startswith("stealcover "):
                                if client != None:
                                    if 'MENTION' in msg.contentMetadata.keys()!= None:
                                        names = re.findall(r'@(\w+)', text)
                                        mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                                        mentionees = mention['MENTIONEES']
                                        lists = []
                                        for mention in mentionees:
                                            if mention["M"] not in lists:
                                                lists.append(mention["M"])
                                        for ls in lists:
                                            channel = client.getProfileCoverURL(ls)
                                            path = str(channel)
                                            client.sendImageWithURL(to, str(path))
# Pembatas Script #
                            elif cmd == 'groupid':
                                gid = client.getGroup(to)
                                client.sendMessage(to, "[ID Group : ]\n" + gid.id)
                            elif cmd == 'grouppicture':
                                group = client.getGroup(to)
                                path = "http://dl.profile.line-cdn.net/" + group.pictureStatus
                                client.sendImageWithURL(to, path)
                            elif cmd == 'groupname':
                                gid = client.getGroup(to)
                                client.sendMessage(to, "[Nama Group : ]\n" + gid.name)
                            elif cmd == 'groupticket':
                                if msg.toType == 2:
                                    group = client.getGroup(to)
                                    if group.preventedJoinByTicket == False:
                                        ticket = client.reissueGroupTicket(to)
                                        client.sendMessage(to, "[ Group Ticket ]\nhttps://line.me/R/ti/g/{}".format(str(ticket)))
                                    else:
                                        client.sendMessage(to, "Grup qr tidak terbuka silahkan buka terlebih dahulu dengan perintah {}openqr".format(str(settings["keyCommand"])))
                            elif cmd == 'groupticket on':
                              if msg._from in admin:
                                if msg.toType == 2:
                                    group = client.getGroup(to)
                                    if group.preventedJoinByTicket == False:
                                        client.sendMessage(to, "Grup qr sudah terbuka")
                                    else:
                                        group.preventedJoinByTicket = False
                                        client.updateGroup(group)
                                        client.sendMessage(to, "Berhasil membuka grup qr")
                            elif cmd == 'groupticket off':
                              if msg._from in admin:
                                if msg.toType == 2:
                                    group = client.getGroup(to)
                                    if group.preventedJoinByTicket == True:
                                        client.sendMessage(to, "Grup qr sudah tertutup")
                                    else:
                                        group.preventedJoinByTicket = True
                                        client.updateGroup(group)
                                        client.sendMessage(to, "Berhasil menutup grup qr")
                            elif cmd == 'groupinfo':
                                group = client.getGroup(to)
                                try:
                                    gCreator = group.creator.displayName
                                except:
                                    gCreator = "Tidak ditemukan"
                                if group.invitee is None:
                                    gPending = "0"
                                else:
                                    gPending = str(len(group.invitee))
                                if group.preventedJoinByTicket == True:
                                    gQr = "Tertutup"
                                    gTicket = "Tidak ada"
                                else:
                                    gQr = "Terbuka"
                                    gTicket = "https://line.me/R/ti/g/{}".format(str(client.reissueGroupTicket(group.id)))
                                path = "http://dl.profile.line-cdn.net/" + group.pictureStatus
                                ret_ = "╔══[ Group Info ]"
                                ret_ += "\n╠ Nama Group : {}".format(str(group.name))
                                ret_ += "\n╠ ID Group : {}".format(group.id)
                                ret_ += "\n╠ Pembuat : {}".format(str(gCreator))
                                ret_ += "\n╠ Jumlah Member : {}".format(str(len(group.members)))
                                ret_ += "\n╠ Jumlah Pending : {}".format(gPending)
                                ret_ += "\n╠ Group Qr : {}".format(gQr)
                                ret_ += "\n╠ Group Ticket : {}".format(gTicket)
                                ret_ += "\n╚══[ Finish ]"
                                client.sendMessage(to, str(ret_))
                                client.sendImageWithURL(to, path)
                            elif cmd == 'listmember':
                                if msg.toType == 2:
                                    group = client.getGroup(to)
                                    ret_ = "╔══[ Member List ]"
                                    no = 0 + 1
                                    for mem in group.members:
                                        ret_ += "\n╠ {}. {}".format(str(no), str(mem.displayName))
                                        no += 1
                                    ret_ += "\n╚══[ Total {} ]".format(str(len(group.members)))
                                    client.sendMessage(to, str(ret_))
                            elif cmd == 'listgroup':
                              if msg._from in admin:
                                    groups = client.groups
                                    ret_ = "╔══[ Group List ]"
                                    no = 0 + 1
                                    for gid in groups:
                                        group = client.getGroup(gid)
                                        ret_ += "\n╠ {}. {} | {}".format(str(no), str(group.name), str(len(group.members)))
                                        no += 1
                                    ret_ += "\n╚══[ Total {} Groups ]".format(str(len(groups)))
                                    client.sendMessage(to, str(ret_))
# Pembatas Script #
                            elif cmd == "cpp":
                              if msg._from in admin:
                                settings["changePictureProfile"] = True
                                client.sendMessage(to, "Silahkan kirim gambarnya")
                            elif cmd == "cgp":
                                if sender not in settings["limituser"]:
                                     settings["limituser"][sender] = {'count':0,'limit':5}
                                if settings["limituser"][sender]['count'] == settings["limituser"][sender]["limit"]:
                                     sendMention(to, "@! anda terkena limit, ketik /open untuk membuka limit.", [sender])
                                else:
                                   if msg.toType == 2:
                                         if to not in settings["changeGroupPicture"]:
                                             settings["changeGroupPicture"].append(to)
                                         client.sendMessage(to, "Silahkan kirim gambarnya")
                                         settings["limituser"][sender]["count"] = settings["limituser"][sender]["count"]+1
				
                            elif cmd == 'mention':
                             if msg._from not in boty:
                                if sender not in settings["limituser"]:
                                     settings["limituser"][sender] = {'count':0,'limit':5}
                                if settings["limituser"][sender]['count'] == settings["limituser"][sender]["limit"]:
                                     sendMention(to, "@! anda terkena limit, ketik /open untuk membuka limit.", [sender])
                                else:
                                    settings["limituser"][sender]["count"] = settings["limituser"][sender]["count"]+1
                                    group = client.getGroup(msg.to)
                                    nama = [contact.mid for contact in group.members]
                                    k = len(nama)//100
                                    for a in range(k+1):
                                        txt = u''
                                        s=0
                                        b=[]
                                        for i in group.members[a*100 : (a+1)*100]:
                                            b.append({"S":str(s), "E" :str(s+6), "M":i.mid})
                                            s += 7
                                            txt += u'@Zero \n'
                                        client.sendMessage(to, text=txt, contentMetadata={u'MENTION': json.dumps({'MENTIONEES':b})}, contentType=0)
                                        client.sendMessage(to, "Total {} Mention".format(str(len(nama))))  
                            elif cmd == "lurking on":
                                    tz = pytz.timezone("Asia/Jakarta")
                                    timeNow = datetime.now(tz=tz)
                                    day = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday","Friday", "Saturday"]
                                    hari = ["Minggu", "Senin", "Selasa", "Rabu", "Kamis", "Jumat", "Sabtu"]
                                    bulan = ["Januari", "Februari", "Maret", "April", "Mei", "Juni", "Juli", "Agustus", "September", "Oktober", "November", "Desember"]
                                    hr = timeNow.strftime("%A")
                                    bln = timeNow.strftime("%m")
                                    for i in range(len(day)):
                                        if hr == day[i]: hasil = hari[i]
                                    for k in range(0, len(bulan)):
                                        if bln == str(k): bln = bulan[k-1]
                                    readTime = hasil + ", " + timeNow.strftime('%d') + " - " + bln + " - " + timeNow.strftime('%Y') + "\nJam : [ " + timeNow.strftime('%H:%M:%S') + " ]"
                                    if receiver in read['readPoint']:
                                        try:
                                            del read['readPoint'][receiver]
                                            del read['readMember'][receiver]
                                            del read['readTime'][receiver]
                                        except:
                                            pass
                                        read['readPoint'][receiver] = msg_id
                                        read['readMember'][receiver] = ""
                                        read['readTime'][receiver] = readTime
                                        read['ROM'][receiver] = {}
                                        client.sendMessage(receiver,"Lurking telah diaktifkan")
                                    else:
                                        try:
                                            del read['readPoint'][receiver]
                                            del read['readMember'][receiver]
                                            del read['readTime'][receiver]
                                        except:
                                            pass
                                        read['readPoint'][receiver] = msg_id
                                        read['readMember'][receiver] = ""
                                        read['readTime'][receiver] = readTime
                                        read['ROM'][receiver] = {}
                                        client.sendMessage(receiver,"Set reading point : \n" + readTime)
                            elif cmd == "lurking off":                             
                                    tz = pytz.timezone("Asia/Jakarta")
                                    timeNow = datetime.now(tz=tz)
                                    day = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday","Friday", "Saturday"]
                                    hari = ["Minggu", "Senin", "Selasa", "Rabu", "Kamis", "Jumat", "Sabtu"]
                                    bulan = ["Januari", "Februari", "Maret", "April", "Mei", "Juni", "Juli", "Agustus", "September", "Oktober", "November", "Desember"]
                                    hr = timeNow.strftime("%A")
                                    bln = timeNow.strftime("%m")
                                    for i in range(len(day)):
                                        if hr == day[i]: hasil = hari[i]
                                    for k in range(0, len(bulan)):
                                        if bln == str(k): bln = bulan[k-1]
                                    readTime = hasil + ", " + timeNow.strftime('%d') + " - " + bln + " - " + timeNow.strftime('%Y') + "\nJam : [ " + timeNow.strftime('%H:%M:%S') + " ]"
                                    if receiver not in read['readPoint']:
                                        client.sendMessage(receiver,"Lurking telah dinonaktifkan")
                                    else:
                                        try:
                                            del read['readPoint'][receiver]
                                            del read['readMember'][receiver]
                                            del read['readTime'][receiver]
                                        except:
                                            pass
                                        client.sendMessage(receiver,"Delete reading point : \n" + readTime)
        
                            elif cmd == "lurking reset":                                    
                                    tz = pytz.timezone("Asia/Jakarta")
                                    timeNow = datetime.now(tz=tz)
                                    day = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday","Friday", "Saturday"]
                                    hari = ["Minggu", "Senin", "Selasa", "Rabu", "Kamis", "Jumat", "Sabtu"]
                                    bulan = ["Januari", "Februari", "Maret", "April", "Mei", "Juni", "Juli", "Agustus", "September", "Oktober", "November", "Desember"]
                                    hr = timeNow.strftime("%A")
                                    bln = timeNow.strftime("%m")
                                    for i in range(len(day)):
                                        if hr == day[i]: hasil = hari[i]
                                    for k in range(0, len(bulan)):
                                        if bln == str(k): bln = bulan[k-1]
                                    readTime = hasil + ", " + timeNow.strftime('%d') + " - " + bln + " - " + timeNow.strftime('%Y') + "\nJam : [ " + timeNow.strftime('%H:%M:%S') + " ]"
                                    if msg.to in read["readPoint"]:
                                        try:
                                            del read["readPoint"][msg.to]
                                            del read["readMember"][msg.to]
                                            del read["readTime"][msg.to]
                                            del read["ROM"][msg.to]
                                        except:
                                            pass
                                        read['readPoint'][receiver] = msg_id
                                        read['readMember'][receiver] = ""
                                        read['readTime'][receiver] = readTime
                                        read['ROM'][receiver] = {}
                                        client.sendMessage(msg.to, "Reset reading point : \n" + readTime)
                                    else:
                                        client.sendMessage(msg.to, "Lurking belum diaktifkan ngapain di reset?")
                                    
                            elif cmd == "lurking":
                                tz = pytz.timezone("Asia/Jakarta")
                                timeNow = datetime.now(tz=tz)
                                day = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday","Friday", "Saturday"]
                                hari = ["Minggu", "Senin", "Selasa", "Rabu", "Kamis", "Jumat", "Sabtu"]
                                bulan = ["Januari", "Februari", "Maret", "April", "Mei", "Juni", "Juli", "Agustus", "September", "Oktober", "November", "Desember"]
                                hr = timeNow.strftime("%A")
                                bln = timeNow.strftime("%m")
                                for i in range(len(day)):
                                    if hr == day[i]: hasil = hari[i]
                                for k in range(0, len(bulan)):
                                    if bln == str(k): bln = bulan[k-1]
                                readTime = hasil + ", " + timeNow.strftime('%d') + " - " + bln + " - " + timeNow.strftime('%Y') + "\nJam : [ " + timeNow.strftime('%H:%M:%S') + " ]"
                                if receiver in read['readPoint']:
                                    if read["ROM"][receiver].items() == []:
                                        client.sendMessage(receiver,"Tidak Ada Sider")
                                    else:
                                        chiya = []
                                        for rom in read["ROM"][receiver].items():
                                            chiya.append(rom[1])
                                        cmem = client.getContacts(chiya) 
                                        zx = ""
                                        zxc = ""
                                        zx2 = []
                                        xpesan = '[R E A D E R ]\n'
                                    for x in range(len(cmem)):
                                        xname = str(cmem[x].displayName)
                                        pesan = ''
                                        pesan2 = pesan+"@c\n"
                                        xlen = str(len(zxc)+len(xpesan))
                                        xlen2 = str(len(zxc)+len(pesan2)+len(xpesan)-1)
                                        zx = {'S':xlen, 'E':xlen2, 'M':cmem[x].mid}
                                        zx2.append(zx)
                                        zxc += pesan2
                                    text = xpesan+ zxc + "\n" + readTime
                                    try:
                                        client.sendMessage(receiver, text, contentMetadata={'MENTION':str('{"MENTIONEES":'+json.dumps(zx2).replace(' ','')+'}')}, contentType=0)
                                    except Exception as error:
                                        print (error)
                                    pass
                                else:
                                    client.sendMessage(receiver,"Lurking belum diaktifkan")
                            
# Pembatas Script #   
                            elif cmd.startswith("/screen"):
                             if msg._from not in boty:
                                if sender not in settings["limituser"]:
                                     settings["limituser"][sender] = {'count':0,'limit':5}
                                if settings["limituser"][sender]['count'] == settings["limituser"][sender]["limit"]:
                                     sendMention(to, "@! anda terkena limit, ketik /open untuk membuka limit.", [sender])
                                else:
                                   try:
                                       sep = text.split(" ")
                                       query = text.replace(sep[0] + " ","")
                                       r = requests.get("http://rahandiapi.herokuapp.com/sswebAPI?key=betakey&link={}".format(urllib.parse.quote(query)))
                                       data = r.text
                                       data = json.loads(data)
                                       client.sendImageWithURL(to, data["result"])
                                       settings["limituser"][sender]["count"] = settings["limituser"][sender]["count"]+1
                                   except Exception as error:
                                       logError(error)
                            elif cmd.startswith("/cek"):
                             if msg._from not in boty:
                                if sender not in settings["limituser"]:
                                     settings["limituser"][sender] = {'count':0,'limit':5}
                                if settings["limituser"][sender]['count'] == settings["limituser"][sender]["limit"]:
                                     sendMention(to, "@! anda terkena limit, ketik /open untuk membuka limit.", [sender])
                                else:
                                   try:
                                       settings["limituser"][sender]["count"] = settings["limituser"][sender]["count"]+1
                                       sep = msg.text.split(" ")
                                       tanggal = msg.text.replace(sep[0] + " ","")
                                       r = requests.get('https://script.google.com/macros/exec?service=AKfycbw7gKzP-WYV2F5mc9RaR7yE3Ve1yN91Tjs91hp_jHSE02dSv9w&nama=ervan&tanggal='+tanggal)
                                       data=r.text
                                       data=json.loads(data)
                                       ret_ = "[ D A T E ]"
                                       ret_ += "\nDate Of Birth : {}".format(str(data["data"]["lahir"]))
                                       ret_ += "\nAge : {}".format(str(data["data"]["usia"]))
                                       ret_ += "\nBirthday : {}".format(str(data["data"]["ultah"]))
                                       ret_ += "\nZodiak : {}".format(str(data["data"]["zodiak"]))
                                       client.sendMessage(to, str(ret_))
                                   except Exception as error:
                                       logError(error)
                            elif cmd.startswith("/shalat "):
                             if msg._from not in boty:
                                if sender not in settings["limituser"]:
                                     settings["limituser"][sender] = {'count':0,'limit':5}
                                if settings["limituser"][sender]['count'] == settings["limituser"][sender]["limit"]:
                                     sendMention(to, "@! anda terkena limit, ketik /open untuk membuka limit.", [sender])
                                else:
                                   settings["limituser"][sender]["count"] = settings["limituser"][sender]["count"]+1
                                   separate = msg.text.split(" ")
                                   location = msg.text.replace(separate[0] + " ","")
                                   r = requests.get("http://leert.corrykalam.gq/praytime.php?location={}".format(location))
                                   data = r.text
                                   data = json.loads(data)
                                   tz = pytz.timezone("Asia/Jakarta")
                                   timeNow = datetime.now(tz=tz)
                                   if data[1] != "Subuh : " and data[2] != "Dzuhur : " and data[3] != "Ashar : " and data[4] != "Maghrib : " and data[5] != "Isya : ":
                                       ret_ = "╔══[ Jadwal Sholat Sekitar " + data[0] + " ]"
                                       ret_ += "\n╠ Tanggal : " + datetime.strftime(timeNow,'%Y-%m-%d')
                                       ret_ += "\n╠ Jam : " + datetime.strftime(timeNow,'%H:%M:%S')
                                       ret_ += "\n╠ " + data[1]
                                       ret_ += "\n╠ " + data[2]
                                       ret_ += "\n╠ " + data[3]
                                       ret_ += "\n╠ " + data[4]
                                       ret_ += "\n╠ " + data[5]
                                       ret_ += "\n╚══[ Success ]"
                                       client.sendMessage(msg.to, str(ret_))
                            elif cmd.startswith("/cuaca "):
                             if msg._from not in boty:
                                if sender not in settings["limituser"]:
                                     settings["limituser"][sender] = {'count':0,'limit':5}
                                if settings["limituser"][sender]['count'] == settings["limituser"][sender]["limit"]:
                                     sendMention(to, "@! anda terkena limit, ketik /open untuk membuka limit.", [sender])
                                else:
                                   try:
                                       settings["limituser"][sender]["count"] = settings["limituser"][sender]["count"]+1
                                       sep = text.split(" ")
                                       location = text.replace(sep[0] + " ","")
                                       r = requests.get("https://farzain.com/api/cuaca.php?id={}".format(location))
                                       data = r.text
                                       data = json.loads(data)
                                       tz = pytz.timezone("Asia/Jakarta")
                                       timeNow = datetime.now(tz=tz)
                                       if "result" not in data:
                                           ret_ = "╔══[ Weather Status ]"
                                           ret_ += "\n╠ Location : " + data[0].replace("Temperatur di kota ","")
                                           ret_ += "\n╠ Suhu : " + data[1].replace("Suhu : ","") + "°C"
                                           ret_ += "\n╠ Kelembaban : " + data[2].replace("Kelembaban : ","") + "%"
                                           ret_ += "\n╠ Tekanan udara : " + data[3].replace("Tekanan udara : ","") + "HPa"
                                           ret_ += "\n╠ Kecepatan angin : " + data[4].replace("Kecepatan angin : ","") + "m/s"
                                           ret_ += "\n╠══[ Time Status ]"
                                           ret_ += "\n╠ Tanggal : " + datetime.strftime(timeNow,'%Y-%m-%d')
                                           ret_ += "\n╠ Jam : " + datetime.strftime(timeNow,'%H:%M:%S') + " WIB"
                                           ret_ += "\n╚══[ Success ]"
                                           client.sendMessage(to, str(ret_))
                                   except Exception as error:
                                       logError(error)
                            elif cmd.startswith("/lokasi "):
                             if msg._from not in boty:
                                if sender not in settings["limituser"]:
                                     settings["limituser"][sender] = {'count':0,'limit':5}
                                if settings["limituser"][sender]['count'] == settings["limituser"][sender]["limit"]:
                                     sendMention(to, "@! anda terkena limit, ketik /open untuk membuka limit.", [sender])
                                else:
                                   try:
                                       settings["limituser"][sender]["count"] = settings["limituser"][sender]["count"]+1
                                       sep = text.split(" ")
                                       location = text.replace(sep[0] + " ","")
                                       r = requests.get("http://leert.corrykalam.gq/location.php?location={}".format(location))
                                       data = r.text
                                       data = json.loads(data)
                                       if data[0] != "" and data[1] != "" and data[2] != "":
                                           link = "https://www.google.co.id/maps/@{},{},15z".format(str(data[1]), str(data[2]))
                                           ret_ = "╔══[ Location Status ]"
                                           ret_ += "\n╠ Location : " + data[0]
                                           ret_ += "\n╠ Google Maps : " + link
                                           ret_ += "\n╚══[ Success ]"
                                           client.sendMessage(to, str(ret_))
                                   except Exception as error:
                                       logError(error)
                            elif cmd.startswith("instainfo"):
                             if msg._from not in boty:
                                if sender not in settings["limituser"]:
                                     settings["limituser"][sender] = {'count':0,'limit':5}
                                if settings["limituser"][sender]['count'] == settings["limituser"][sender]["limit"]:
                                     sendMention(to, "@! anda terkena limit, ketik /open untuk membuka limit.", [sender])
                                else:
                                   try:
                                       settings["limituser"][sender]["count"] = settings["limituser"][sender]["count"]+1
                                       sep = text.split(" ")
                                       search = text.replace(sep[0] + " ","")
                                       r = requests.get("https://www.instagram.com/{}/?__a=1".format(search))
                                       data = r.text
                                       data = json.loads(data)
                                       if data != []:
                                           ret_ = "╔══[ Profile Instagram ]"
                                           ret_ += "\n╠ Nama : {}".format(str(data["graphql"]["user"]["full_name"]))
                                           ret_ += "\n╠ Username : {}".format(str(data["graphql"]["user"]["username"]))
                                           ret_ += "\n╠ Bio : {}".format(str(data["graphql"]["user"]["biography"]))
                                           ret_ += "\n╠ Pengikut : {}".format(str(data["graphql"]["user"]["edge_followed_by"]["count"]))
                                           ret_ += "\n╠ Diikuti : {}".format(str(data["graphql"]["user"]["edge_follow"]["count"]))
                                           if data["graphql"]["user"]["is_verified"] == True:
                                               ret_ += "\n╠ Verifikasi : Sudah"
                                           else:
                                               ret_ += "\n╠ Verifikasi : Belum"
                                           if data["graphql"]["user"]["is_private"] == True:
                                               ret_ += "\n╠ Akun Pribadi : Iya"
                                           else:
                                               ret_ += "\n╠ Akun Pribadi : Tidak"
                                           ret_ += "\n╠ Total Post : {}".format(str(data["graphql"]["user"]["edge_owner_to_timeline_media"]["count"]))
                                           ret_ += "\n╚══[ https://www.instagram.com/{} ]".format(search)
                                           path = data["graphql"]["user"]["profile_pic_url_hd"]
                                           client.sendImageWithURL(to, str(path))
                                           client.sendMessage(to, str(ret_))
                                   except Exception as error:
                                       logError(error)
                            elif cmd.startswith("instapost"):
                             if msg._from not in boty:
                                if sender not in settings["limituser"]:
                                     settings["limituser"][sender] = {'count':0,'limit':5}
                                if settings["limituser"][sender]['count'] == settings["limituser"][sender]["limit"]:
                                     sendMention(to, "@! anda terkena limit, ketik /open untuk membuka limit.", [sender])
                                else:
                                   try:
                                       settings["limituser"][sender]["count"] = settings["limituser"][sender]["count"]+1
                                       sep = text.split(" ")
                                       text = text.replace(sep[0] + " ","")   
                                       cond = text.split("|")
                                       username = cond[0]
                                       no = cond[1] 
                                       r = requests.get("http://rahandiapi.herokuapp.com/instapost/{}/{}?key=betakey".format(str(username), str(no)))
                                       data = r.text
                                       data = json.loads(data)
                                       if data["find"] == True:
                                           if data["media"]["mediatype"] == 1:
                                               client.sendImageWithURL(msg.to, str(data["media"]["url"]))
                                           if data["media"]["mediatype"] == 2:
                                               client.sendVideoWithURL(msg.to, str(data["media"]["url"]))
                                           ret_ = "╔══[ Info Post ]"
                                           ret_ += "\n╠ Jumlah Like : {}".format(str(data["media"]["like_count"]))
                                           ret_ += "\n╠ Jumlah Comment : {}".format(str(data["media"]["comment_count"]))
                                           ret_ += "\n╚══[ Caption ]\n{}".format(str(data["media"]["caption"]))
                                           client.sendMessage(to, str(ret_))
                                   except Exception as error:
                                       logError(error)
                            elif cmd.startswith("instastory"):
                             if msg._from not in boty:
                                if sender not in settings["limituser"]:
                                     settings["limituser"][sender] = {'count':0,'limit':5}
                                if settings["limituser"][sender]['count'] == settings["limituser"][sender]["limit"]:
                                     sendMention(to, "@! anda terkena limit, ketik /open untuk membuka limit.", [sender])
                                else:
                                   try:
                                       settings["limituser"][sender]["count"] = settings["limituser"][sender]["count"]+1
                                       sep = text.split(" ")
                                       text = text.replace(sep[0] + " ","")
                                       cond = text.split("|")
                                       search = str(cond[0])
                                       if len(cond) == 2:
                                           r = requests.get("http://rahandiapi.herokuapp.com/instastory/{}?key=betakey".format(search))
                                           data = r.text
                                           data = json.loads(data)
                                           if data["url"] != []:
                                               num = int(cond[1])
                                               if num <= len(data["url"]):
                                                   search = data["url"][num - 1]
                                                   if search["tipe"] == 1:
                                                       client.sendImageWithURL(to, str(search["link"]))
                                                   if search["tipe"] == 2:
                                                       client.sendVideoWithURL(to, str(search["link"]))
                                   except Exception as error:
                                       logError(error)
                                    
                            elif cmd.startswith("say-"):
                             if msg._from not in boty:
                                if sender not in settings["limituser"]:
                                     settings["limituser"][sender] = {'count':0,'limit':5}
                                if settings["limituser"][sender]['count'] == settings["limituser"][sender]["limit"]:
                                     sendMention(to, "@! anda terkena limit, ketik /open untuk membuka limit.", [sender])
                                else:
                                   sep = text.split("-")
                                   sep = sep[1].split(" ")
                                   lang = sep[0]
                                   say = text.replace("say-" + lang + " ","")
                                   if lang not in list_language["list_textToSpeech"]:
                                       return client.sendMessage(to, "Language not found")
                                   tts = gTTS(text=say, lang=lang)
                                   tts.save("hasil.mp3")
                                   client.sendAudio(to,"hasil.mp3")
                                   settings["limituser"][sender]["count"] = settings["limituser"][sender]["count"]+1
                                
                            elif cmd.startswith("/image"):
                             if msg._from not in boty:
                                if sender not in settings["limituser"]:
                                     settings["limituser"][sender] = {'count':0,'limit':5}
                                if settings["limituser"][sender]['count'] == settings["limituser"][sender]["limit"]:
                                     sendMention(to, "@! anda terkena limit, ketik /open untuk membuka limit.", [sender])
                                else:
                                   try:
                                       settings["limituser"][sender]["count"] = settings["limituser"][sender]["count"]+1
                                       separate = msg.text.split(" ")
                                       search = msg.text.replace(separate[0] + " ","")
                                       r = requests.get("http://rahandiapi.herokuapp.com/imageapi?key=betakey&q={}".format(search))
                                       data = r.text
                                       data = json.loads(data)
                                       if data["result"] != []:
                                           items = data["result"]
                                           path = random.choice(items)
                                           a = items.index(path)
                                           b = len(items)
                                           client.sendImageWithURL(to, str(path))
                                   except Exception as error:
                                       logError(error)
                            elif cmd.startswith("/music "):
                             if msg._from not in boty:
                                if sender not in settings["limituser"]:
                                     settings["limituser"][sender] = {'count':0,'limit':5}
                                if settings["limituser"][sender]['count'] == settings["limituser"][sender]["limit"]:
                                     sendMention(to, "@! anda terkena limit, ketik /open untuk membuka limit.", [sender])
                                else:
                                   settings["limituser"][sender]["count"] = settings["limituser"][sender]["count"]+1
                                   sep = msg.text.split(" ")
                                   query = msg.text.replace(sep[0] + " ","")
                                   cond = query.split("|")
                                   search = str(cond[0])
                                   result = requests.get("http://api.ntcorp.us/joox/search?q={}".format(str(search)))
                                   data = result.text
                                   data = json.loads(data)
                                   if len(cond) == 1:
                                       num = 0
                                       ret_ = "╔══[ Result Music ]"
                                       for music in data["result"]:
                                           num += 1
                                           ret_ += "\n╠ {}. {}".format(str(num), str(music["single"]))
                                       ret_ += "\n╚══[ Total {} Music ]".format(str(len(data["result"])))
                                       ret_ += "\n\nUntuk Melihat Details Music, silahkan gunakan command /music {}|「nomor」\nContoh: /music {}|1".format(str(search), str(search))
                                       client.sendMessage(to, str(ret_))
                                   elif len(cond) == 2:
                                       num = int(cond[1])
                                       if num <= len(data["result"]):
                                           music = data["result"][num - 1]
                                           result = requests.get("http://api.ntcorp.us/joox/song_info?sid={}".format(str(music["sid"])))
                                           data = result.text
                                           data = json.loads(data)
                                           if data["result"] != []:
                                               ret_ = "╔══[ Music ]"
                                               ret_ += "\n╠ Title : {}".format(str(data["result"]["song"]))
                                               ret_ += "\n╠ Album : {}".format(str(data["result"]["album"]))
                                               ret_ += "\n╠ Size : {}".format(str(data["result"]["size"]))
                                               ret_ += "\n╠ Link : {}".format(str(data["result"]["mp3"][0]))
                                               ret_ += "\n╚══[ Finish ]"
                                               client.sendImageWithURL(to, str(data["result"]["img"]))
                                               client.sendMessage(to, str(ret_))
                                               client.sendAudioWithURL(to, str(data["result"]["mp3"][0]))
                            elif cmd.startswith("/lirik"):
                             if msg._from not in boty:
                                if sender not in settings["limituser"]:
                                     settings["limituser"][sender] = {'count':0,'limit':5}
                                if settings["limituser"][sender]['count'] == settings["limituser"][sender]["limit"]:
                                     sendMention(to, "@! anda terkena limit, ketik /open untuk membuka limit.", [sender])
                                else:
                                   settings["limituser"][sender]["count"] = settings["limituser"][sender]["count"]+1
                                   sep = msg.text.split(" ")
                                   query = msg.text.replace(sep[0] + " ","")
                                   cond = query.split("|")
                                   search = cond[0]
                                   api = requests.get("http://api.secold.com/joox/cari/{}".format(str(search)))
                                   data = api.text
                                   data = json.loads(data)
                                   if len(cond) == 1:
                                       num = 0
                                       ret_ = "╔══[ Result Lyric ]"
                                       for lyric in data["results"]:
                                           num += 1
                                           ret_ += "\n╠ {}. {}".format(str(num), str(lyric["single"]))
                                       ret_ += "\n╚══[ Total {} Music ]".format(str(len(data["results"])))
                                       ret_ += "\n\nUntuk Melihat Details Lyric, silahkan gunakan command {}SearchLyric {}|「number」".format(str(setKey), str(search))
                                       client.sendMessage(to, str(ret_))
                                   elif len(cond) == 2:
                                       num = int(cond[1])
                                       if num <= len(data["results"]):
                                           lyric = data["results"][num - 1]
                                           api = requests.get("http://api.secold.com/joox/sid/{}".format(str(lyric["songid"])))
                                           data = api.text
                                           data = json.loads(data)
                                           lyrics = data["results"]["lyric"]
                                           lyric = lyrics.replace('ti:','Title - ')
                                           lyric = lyric.replace('ar:','Artist - ')
                                           lyric = lyric.replace('al:','Album - ')
                                           removeString = "[1234567890.:]"
                                           for char in removeString:
                                               lyric = lyric.replace(char,'')
                                           client.sendMessage(msg.to, str(lyric))
                            elif cmd.startswith("/yt"):
                             if msg._from not in boty:
                                if sender not in settings["limituser"]:
                                     settings["limituser"][sender] = {'count':0,'limit':5}
                                if settings["limituser"][sender]['count'] == settings["limituser"][sender]["limit"]:
                                     sendMention(to, "@! anda terkena limit, ketik /open untuk membuka limit.", [sender])
                                else:
                                   settings["limituser"][sender]["count"] = settings["limituser"][sender]["count"]+1
                                   sep = text.split(" ")
                                   search = text.replace(sep[0] + " ","")
                                   params = {"search_query": search}
                                   r = requests.get("https://www.youtube.com/results", params = params)
                                   soup = BeautifulSoup(r.content, "html5lib")
                                   ret_ = "╔══[ Youtube Result ]"
                                   datas = []
                                   for data in soup.select(".yt-lockup-title > a[title]"):
                                       if "&lists" not in data["href"]:
                                           datas.append(data)
                                   for data in datas:
                                       ret_ += "\n╠══[ {} ]".format(str(data["title"]))
                                       ret_ += "\n╠ https://www.youtube.com{}".format(str(data["href"]))
                                   ret_ += "\n╚══[ Total {} ]".format(len(datas))
                                   client.sendMessage(to, str(ret_))
                            elif cmd.startswith("tr-"):
                             if msg._from not in boty:
                                if sender not in settings["limituser"]:
                                     settings["limituser"][sender] = {'count':0,'limit':5}
                                if settings["limituser"][sender]['count'] == settings["limituser"][sender]["limit"]:
                                     sendMention(to, "@! anda terkena limit, ketik /open untuk membuka limit.", [sender])
                                else:
                                   settings["limituser"][sender]["count"] = settings["limituser"][sender]["count"]+1
                                   sep = text.split("-")
                                   sep = sep[1].split(" ")
                                   lang = sep[0]
                                   say = text.replace("tr-" + lang + " ","")
                                   if lang not in list_language["list_translate"]:
                                       return client.sendMessage(to, "Language not found")
                                   translator = Translator()
                                   hasil = translator.translate(say, dest=lang)
                                   A = hasil.text
                                   client.sendMessage(to, str(A))
# Pembatas Script #
                    elif msg.contentType == 1:
                        if settings["changePictureProfile"] == True:
                            path = client.downloadObjectMsg(msg_id)
                            settings["changePictureProfile"] = False
                            client.updateProfilePicture(path)
                            client.sendMessage(to, "Berhasil mengubah foto profile")
                        if msg.toType == 2:
                            if to in settings["changeGroupPicture"]:
                                path = client.downloadObjectMsg(msg_id)
                                settings["changeGroupPicture"].remove(to)
                                client.updateGroupPicture(to, path)
                                client.sendMessage(to, "Berhasil mengubah foto group")
                    elif msg.contentType == 7:
                        if settings["checkSticker"] == True:
                            stk_id = msg.contentMetadata['STKID']
                            stk_ver = msg.contentMetadata['STKVER']
                            pkg_id = msg.contentMetadata['STKPKGID']
                            ret_ = "╔══[ Sticker Info ]"
                            ret_ += "\n╠ STICKER ID : {}".format(stk_id)
                            ret_ += "\n╠ STICKER PACKAGES ID : {}".format(pkg_id)
                            ret_ += "\n╠ STICKER VERSION : {}".format(stk_ver)
                            ret_ += "\n╠ STICKER URL : line://shop/detail/{}".format(pkg_id)
                            ret_ += "\n╚══[ Finish ]"
                            client.sendMessage(to, str(ret_))
                    elif msg.contentType == 13:
                        if settings["checkContact"] == True:
                            try:
                                contact = client.getContact(msg.contentMetadata["mid"])
                                if client != None:
                                    cover = client.getProfileCoverURL(msg.contentMetadata["mid"])
                                else:
                                    cover = "Tidak dapat masuk di line channel"
                                path = "http://dl.profile.line-cdn.net/{}".format(str(contact.pictureStatus))
                                try:
                                    client.sendImageWithURL(to, str(path))
                                except:
                                    pass
                                ret_ = "╔══[ Details Contact ]"
                                ret_ += "\n╠ Nama : {}".format(str(contact.displayName))
                                ret_ += "\n╠ MID : {}".format(str(msg.contentMetadata["mid"]))
                                ret_ += "\n╠ Bio : {}".format(str(contact.statusMessage))
                                ret_ += "\n╠ Gambar Profile : http://dl.profile.line-cdn.net/{}".format(str(contact.pictureStatus))
                                ret_ += "\n╠ Gambar Cover : {}".format(str(cover))
                                ret_ += "\n╚══[ Finish ]"
                                client.sendMessage(to, str(ret_))
                            except:
                                client.sendMessage(to, "Kontak tidak valid")
                    elif msg.contentType == 16:
                        if settings["checkPost"] == True:
                            try:
                                ret_ = "╔══[ Details Post ]"
                                if msg.contentMetadata["serviceType"] == "GB":
                                    contact = client.getContact(sender)
                                    auth = "\n╠ Penulis : {}".format(str(contact.displayName))
                                else:
                                    auth = "\n╠ Penulis : {}".format(str(msg.contentMetadata["serviceName"]))
                                purl = "\n╠ URL : {}".format(str(msg.contentMetadata["postEndUrl"]).replace("line://","https://line.me/R/"))
                                ret_ += auth
                                ret_ += purl
                                if "mediaOid" in msg.contentMetadata:
                                    object_ = msg.contentMetadata["mediaOid"].replace("svc=myhome|sid=h|","")
                                    if msg.contentMetadata["mediaType"] == "V":
                                        if msg.contentMetadata["serviceType"] == "GB":
                                            ourl = "\n╠ Objek URL : https://obs-us.line-apps.com/myhome/h/download.nhn?tid=612w&{}".format(str(msg.contentMetadata["mediaOid"]))
                                            murl = "\n╠ Media URL : https://obs-us.line-apps.com/myhome/h/download.nhn?{}".format(str(msg.contentMetadata["mediaOid"]))
                                        else:
                                            ourl = "\n╠ Objek URL : https://obs-us.line-apps.com/myhome/h/download.nhn?tid=612w&{}".format(str(object_))
                                            murl = "\n╠ Media URL : https://obs-us.line-apps.com/myhome/h/download.nhn?{}".format(str(object_))
                                        ret_ += murl
                                    else:
                                        if msg.contentMetadata["serviceType"] == "GB":
                                            ourl = "\n╠ Objek URL : https://obs-us.line-apps.com/myhome/h/download.nhn?tid=612w&{}".format(str(msg.contentMetadata["mediaOid"]))
                                        else:
                                            ourl = "\n╠ Objek URL : https://obs-us.line-apps.com/myhome/h/download.nhn?tid=612w&{}".format(str(object_))
                                    ret_ += ourl
                                if "stickerId" in msg.contentMetadata:
                                    stck = "\n╠ Stiker : https://line.me/R/shop/detail/{}".format(str(msg.contentMetadata["packageId"]))
                                    ret_ += stck
                                if "text" in msg.contentMetadata:
                                    text = "\n╠ Tulisan : {}".format(str(msg.contentMetadata["text"]))
                                    ret_ += text
                                ret_ += "\n╚══[ Finish ]"
                                client.sendMessage(to, str(ret_))
                            except:
                                client.sendMessage(to, "Post tidak valid")
                backupData()		
            except Exception as error:
                logError(error)
                traceback.print_tb(error.__traceback__)
                
        if op.type == 26:
            try:
                print ("[ 26 ] RECIEVE MESSAGE")
                msg = op.message
                text = msg.text
                msg_id = msg.id
                receiver = msg.to
                sender = msg._from
                if msg.toType == 0 or msg.toType == 1 or msg.toType == 2:
                    if msg.toType == 0:
                        if sender != client.profile.mid:
                            to = sender
                        else:
                            to = receiver
                    elif msg.toType == 1:
                        to = receiver
                    elif msg.toType == 2:
                        to = receiver
                    if settings["autoRead"] == True:
                        client.sendChatChecked(to, msg_id)
                    if to in read["readPoint"]:
                        if sender not in read["ROM"][to]:
                            read["ROM"][to][sender] = True
                    if sender in settings["mimic"]["target"] and settings["mimic"]["status"] == True and settings["mimic"]["target"][sender] == True:
                        text = msg.text
                        if text is not None:
                            client.sendMessage(msg.to,text)
                    if settings["unsendMessage"] == True:
                        try:
                            msg = op.message
                            if msg.toType == 0:
                                client.log("[{} : {}]".format(str(msg._from), str(msg.text)))
                            else:
                                client.log("[{} : {}]".format(str(msg.to), str(msg.text)))
                                msg_dict[msg.id] = {"text": msg.text, "from": msg._from, "createdTime": msg.createdTime, "contentType": msg.contentType, "contentMetadata": msg.contentMetadata}
                        except Exception as error:
                            logError(error)
                    if msg.contentType == 0:
                        if text is None:
                            return
                        if "/ti/g/" in msg.text.lower():
                         try:
                             if settings["autoJoinTicket"] == True:
                                 link_re = re.compile('(?:line\:\/|line\.me\/R)\/ti\/g\/([a-zA-Z0-9_-]+)?')
                                 links = link_re.findall(text)
                                 n_links = []
                                 for l in links:
                                     if l not in n_links:
                                         n_links.append(l)
                                 for ticket_id in n_links:
                                     group = client.findGroupByTicket(ticket_id)
                                     if group.preventedJoinByTicket == False:
                                       if len(group.members) >= 10:
                                         if len(group.members) <= 498:
                                             client.acceptGroupInvitationByTicket(group.id,ticket_id)
                                             client.sendMessage(to, "Berhasil masuk ke group %s" % str(group.name))
                                         else:
                                             client.sendMessage(to, "Tidak bisa bergabung ke group %s" % str(group.name))
                                       else:
                                           client.sendMessage(to, "QR group %s tertutup" % str(group.name))
                         except:
                               pass
		
                        if 'MENTION' in msg.contentMetadata.keys()!= None:
                            names = re.findall(r'@(\w+)', text)
                            mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                            mentionees = mention['MENTIONEES']
                            lists = []
                            for mention in mentionees:
                                if clientMid in mention["M"]:
                                    if settings["autoRespon"] == True:
                                        sendMention(sender, "Oi Asw @!,jangan main tag tag", [sender])
                                    break
                backupData()
            except Exception as error:
                logError(error)
                traceback.print_tb(error.__traceback__)
        
        if op.type == 55:
            try:
                if cctv['cyduk'][op.param1]==True:
                    if op.param1 in cctv['point']:
                        Name = client.getContact(op.param2).displayName
                        if Name in cctv['sidermem'][op.param1]:
                            pass
                        else:
                            cctv['sidermem'][op.param1] += "\n• " + Name
                            if " " in Name:
                                nick = Name.split(' ')
                                if len(nick) == 2:
                                    client.sendMessage(op.param1, "Haii " + "☞ " + nick[0] + " ☜" + "\nNgintip Aja Niih. . .\nChat Kek Idiih (-__-)   ")
                                else:
                                    client.sendMessage(op.param1, "Haii " + "☞ " + nick[1] + " ☜" + "\nBetah Banget Jadi Penonton. . .\nChat Napa (-__-)   ")
                            else:
                                client.sendMessage(op.param1, "Haii " + "☞ " + Name + " ☜" + "\nNgapain Kak Ngintip Aja?\nSini Gabung Chat...   ")
                    else:
                        pass
                else:
                    pass
            except:
                pass
                
        
        if op.type == 55:
            try:
                if op.param1 in wait2['readPoint']:
           
                    if op.param2 in wait2['readMember'][op.param1]:
                        pass
                    else:
                        wait2['readMember'][op.param1] += op.param2
                    wait2['ROM'][op.param1][op.param2] = op.param2
                    with open('sider.json', 'w') as fp:
                     json.dump(wait2, fp, sort_keys=True, indent=4)
                else:
                    pass
            except:
                pass  
                
        if op.type == 55:
            try:
                if op.param1 in wait2['readPoint']:
                    Name = client.getContact(op.param2).displayName
                    if Name in wait2['readMember'][op.param1]:
                        pass
                    else:
                        wait2['readMember'][op.param1] += "\n☀。" + Name
                        wait2['ROM'][op.param1][op.param2] = "☠。" + Name
                else:
                    client.sendMessage
            except:
                  pass
              
        if op.type == 26:
            msg = op.message
            msg.text = str(msg.text)
            text = msg.text
            try:
                if msg.contentType == 0:
                    try:
                        if msg.to in wait2['readPoint']:
                            if msg._from in wait2["ROM"][msg.to]:
                                del wait2["ROM"][msg.to][msg._from]
                        else:
                            pass
                    except:
                        pass
                else:
                    pass
            except KeyboardInterrupt:
                         sys.exit(0)
            except Exception as error:
                return
            
        if op.type == 55:
            print ("[ 55 ] NOTIFIED READ MESSAGE")
            try:
                if op.param1 in read['readPoint']:
                    if op.param2 in read['readMember'][op.param1]:
                        pass
                    else:
                        read['readMember'][op.param1] += op.param2
                    read['ROM'][op.param1][op.param2] = op.param2
                else:
                   pass
            except Exception as error:
                logError(error)
                traceback.print_tb(error.__traceback__)
    except Exception as error:
        logError(error)
        traceback.print_tb(error.__traceback__)

        if op.type == 26:
            msg = op.message
            text = msg.text
            msg_id = msg.id
            receiver = msg.to
            sender = msg._from
            if msg.toType == 0 or msg.toType == 2:
                if msg.toType == 0:
                    to = sender
        backupData()
    except Exception as error:
        logError(error)

#while True:
 #   try:
      #  autoRestart()
  #      delete_log()
  #      ops = clientPoll.singleTrace(count=50)
   #     if ops is not None:
     #       for op in ops:
                #clientBot(op)
         #       clientPoll.setRevision(op.revision)
      #          thread1 = threading.Thread(target=clientBot, args=(op,))#self.OpInterrupt[op.type], args=(op,)
                #thread1.daemon = True
              #  thread1.start()
      #          thread1.join()
 #   except Exception as error:
    #    logError(error)
