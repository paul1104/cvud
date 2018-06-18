from LINE import *
from ThriftService.ttypes import *
import time, asyncio, json, threading, codecs, sys, os, re, urllib, requests, wikipedia, html5lib, timeit, pafy, youtube_dl, requests
from bs4 import BeautifulSoup
#import urllib3.contrib.pyopenssl

RASadmin = ["uc34ef1087f001add7ca83b96211177be","uabab32583a1252539e052e3afb93d42d","u90b1c62dc5551c0c1433bd9c885903e4","u195e8e61256e69348dad97a3d8e1e35b","ubf0f729ee3667846ce10204febdbb4cc","ue3682515c7fdf1f8f214eb9b75867a97","ua5e3f84c97b698a23ba44d0c503aca62","u51dc207f9c470ae5f9c9ac44c18ce32a"]
RAKey = "NH "

mulai = time.time()

def waktu(secs):
    mins, secs = divmod(secs,60)
    hours, mins = divmod(mins,60)
    days, hours = divmod(hours, 24)
    return '%02d Hari %02d Jam %02d Menit %02d Detik' % (days, hours, mins, secs)
    
class LineBot(object):
    
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
        akun = open('RAwait.json','r')
        self.wait = json.load(akun)
        setting = open('RAset.json','r')
        self.RAset = json.load(setting)
        
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
        
    def bot(self, op):
        cl = self.client
        wait = self.wait
        try:
            if op.type == 0:
                return
            
            if op.type == 11:
                if op.param1 in self.RAset["RAprotqr"]:
                    if cl.getGroup(op.param1).preventedJoinByTicket == False:
                        if op.param2 not in RASadmin and op.param2 not in self.wait["RAAdmin"] and op.param2 not in self.wait["RAStaff"] and op.param2 not in self.wait["RABots"]:
                            cl.reissueGroupTicket(op.param1)
                            X = cl.getGroup(op.param1)
                            X.preventedJoinByTicket = True
                            cl.updateGroup(X)
                            
                if op.param2 in self.wait["RAblacklist"]:
                    if cl.getGroup(op.param1).preventedJoinByTicket == False:
                        if op.param2 not in RASadmin and op.param2 not in self.wait["RAAdmin"] and op.param2 not in self.wait["RAStaff"] and op.param2 not in self.wait["RABots"]:
                            cl.reissueGroupTicket(op.param1)
                            X = cl.getGroup(op.param1)
                            X.preventedJoinByTicket = True
                            cl.updateGroup(X)
                            cl.kickoutFromGroup(op.param1,[op.param2])
            
            if op.type == 13:
                if self.mid in op.param3:
                    if self.wait["RAautojoin"] == True:
                        if op.param2 not in RASadmin and op.param2 not in self.wait["RAAdmin"] and op.param2 not in self.wait["RABots"]:
                            cl.acceptGroupInvitation(op.param1)
                            ginfo = cl.getGroup(op.param1)
                            cl.sendText(op.param1,"Selamat Tinggal\n " +str(ginfo.name))
                            cl.leaveGroup(op.param1)
                        else:
                            cl.acceptGroupInvitation(op.param1)
                            ginfo = cl.getGroup(op.param1)
                            cl.sendText(op.param1,"Hai " + str(ginfo.name))
            
            if op.type == 13:
                if op.param2 in self.wait["RAblacklist"]:
                    try:
                        cl.cancelGroupInvitation(op.param1,[op.param3])
                        cl.kickoutFromGroup(op.param1,[op.param2])
                    except:
                        try:
                            group = cl.getGroup(op.param1)
                            gMembMids = [contact.mid for contact in group.invitee]
                            for op.param2 in gMembMids:
                                cl.cancelGroupInvitation(op.param1,[op.param2])
                        except:
                            cl.cancelGroupInvitation(op.param1,[op.param3])
                            cl.kickoutFromGroup(op.param1,[op.param2])
                    
                if op.param1 in self.RAset["RAprotinvite"]:
                    if op.param2 not in RASadmin and op.param2 not in self.wait["RAAdmin"] and op.param2 not in self.wait["RAStaff"] and op.param2 not in self.wait["RABots"]:
                        group = cl.getGroup(op.param1)
                        gMembMids = [contact.mid for contact in group.invitee]
                        for _mid in gMembMids:
                            cl.cancelGroupInvitation(op.param1,[_mid])
                        
                if op.param3 in self.wait["RAblacklist"]:
                    group = cl.getGroup(op.param1)
                    gMembMids = [contact.mid for contact in group.invitee]
                    for _mid in gMembMids:
                        if op.param2 not in RASadmin and op.param2 not in self.wait["RAAdmin"] and op.param2 not in self.wait["RAStaff"] and op.param2 not in self.wait["RABots"]:
                            cl.cancelGroupInvitation(op.param1,[_mid])
                            self.wait["RAblacklist"][op.param2] = True
                            f=codecs.open('RAwait.json','w','utf-8')
                            json.dump(self.wait, f, sort_keys=True, indent=4,ensure_ascii=False)
                            cl.kickoutFromGroup(op.param1,[op.param2])
                
            if op.type == 17:
                if op.param2 in self.wait["RAblacklist"]:
                    cl.kickoutFromGroup(op.param1,[op.param2])
                    
                if op.param1 in self.RAset["RAgreet"]:
                    if op.param2 not in RASadmin and op.param2 not in self.wait["RAAdmin"] and op.param2 not in self.wait["RAStaff"] and op.param2 not in self.wait["RABots"]:
                        ginfo = cl.getGroup(op.param1)
                        user = cl.getContact(op.param2)
                        cl.sendText(op.param1,"Welcome at" + str(ginfo.name))
            
            if op.type == 19:
                if op.param1 in self.RAset["RAprotkick"]:
                    if op.param2 not in RASadmin and op.param2 not in self.wait["RAAdmin"] and op.param2 not in self.wait["RAStaff"] and op.param2 not in self.wait["RABots"]:
                        self.wait["RAblacklist"][op.param2] = True
                        f=codecs.open('RAwait.json','w','utf-8')
                        json.dump(self.wait, f, sort_keys=True, indent=4,ensure_ascii=False)
                        user = cl.getContact(op.param2)
                        cl.sendText(op.param1,"No Kick Member " + str(user.displayName))
                        try:
                            cl.findAndAddContactsByMid(op.param3)
                            cl.inviteIntoGroup(op.param1,[op.param3])
                        except:
                            pass
                
                if op.param2 not in RASadmin and op.param2 not in self.wait["RAAdmin"] and op.param2 not in self.wait["RAStaff"] and op.param2 not in self.wait["RABots"] and op.param3 in RASadmin:
                    self.wait["RAblacklist"][op.param2] = True
                    f=codecs.open('RAwait.json','w','utf-8')
                    json.dump(self.wait, f, sort_keys=True, indent=4,ensure_ascii=False)
                    cl.findAndAddContactsByMid(op.param3)
                    cl.kickoutFromGroup(op.param1,[op.param2])
                    cl.inviteIntoGroup(op.param1,[op.param3])
                    
                if op.param2 not in RASadmin and op.param2 not in self.wait["RAAdmin"] and op.param2 not in self.wait["RAStaff"] and op.param2 not in self.wait["RABots"] and op.param3 in self.wait["RAAdmin"]:
                    self.wait["RAblacklist"][op.param2] = True
                    f=codecs.open('RAwait.json','w','utf-8')
                    json.dump(self.wait, f, sort_keys=True, indent=4,ensure_ascii=False)
                    cl.findAndAddContactsByMid(op.param3)
                    cl.kickoutFromGroup(op.param1,[op.param2])
                    cl.inviteIntoGroup(op.param1,[op.param3])
                    
                if op.param2 not in RASadmin and op.param2 not in self.wait["RAAdmin"] and op.param2 not in self.wait["RAStaff"] and op.param2 not in self.wait["RABots"] and op.param3 in self.wait["RAStaff"]:
                    self.wait["RAblacklist"][op.param2] = True
                    f=codecs.open('RAwait.json','w','utf-8')
                    json.dump(self.wait, f, sort_keys=True, indent=4,ensure_ascii=False)
                    cl.findAndAddContactsByMid(op.param3)
                    cl.kickoutFromGroup(op.param1,[op.param2])
                    cl.inviteIntoGroup(op.param1,[op.param3])
                    
            if op.type == 19:
                if op.param3 in self.wait["RABots"]:
                    cl.findAndAddContactsByMid(op.param3)
                    cl.inviteIntoGroup(op.param1,[op.param3])
                    if op.param2 not in RASadmin and op.param2 not in self.wait["RAAdmin"] and op.param2 not in self.wait["RAStaff"] and op.param2 not in self.wait["RABots"]:
                        self.wait["RAblacklist"][op.param2] = True
                        f=codecs.open('RAwait.json','w','utf-8')
                        json.dump(self.wait, f, sort_keys=True, indent=4,ensure_ascii=False)
                        cl.kickoutFromGroup(op.param1,[op.param2])
            
            if op.type == 32:
                if op.param1 in self.RAset["RAprotcancel"]:
                    if op.param2 not in RASadmin and op.param2 not in self.wait["RAAdmin"] and op.param2 not in self.wait["RAStaff"] and op.param2 not in self.wait["RABots"]:
                        cl.kickoutFromGroup(op.param1,[op.param2])
                        self.wait["RAblacklist"][op.param2] = True
                        f=codecs.open('RAwait.json','w','utf-8')
                        json.dump(self.wait, f, sort_keys=True, indent=4,ensure_ascii=False)
                        try:
                            if op.param3 not in self.wait["RAblacklist"]:
                                cl.findAndAddContactsByMid(op.param3)
                                cl.inviteIntoGroup(op.param1,[op.param3])
                        except:
                            if op.param3 not in self.wait["RAblacklist"]:
                                cl.findAndAddContactsByMid(op.param3)
                                cl.inviteIntoGroup(op.param1,[op.param3])
            
            if op.type == 46:
                if op.param2 in self.wait["RABots"]:
                    cl.removeAllMessages()
                
            if op.type == 55:
                if op.param1 in self.RAset["RAreadPoint"]:
                    if op.param2 in self.RAset["RAreadMember"][op.param1]:
                        pass
                    else:
                        self.RAset["RAreadMember"][op.param1][op.param2] = True
                else:
                    pass
                
            if op.type == 26:
                msg = op.message
                if msg.to in self.RAset["RAreadPoint"]:
                    if msg.from_ in self.RAset["RAreadMember"][msg.to]:
                        pass
                    else:
                        self.RAset["RAreadMember"][msg.to][msg.from_] = True
                else:
                    pass
            
            if op.type == 26:
                if self.wait["RAautoread"] == True:
                    msg = op.message
                    if msg.toType == 2:
                        msg.to = msg.to
                        msg.from_ = msg.from_
                        cl.sendChatChecked(msg.to,msg.id)
                
            if op.type == 26:
                msg = op.message
                if msg.contentType == 13:
                    if msg.from_ in RASadmin or msg.from_ in self.wait["RAAdmin"] or msg.from_ in self.wait["RAStaff"]:
                        if self.wait["RAwblacklist"] == True:
                            if msg.contentMetadata["mid"] in self.wait["RAblacklist"]:
                                cl.sendText(msg.to,"Akun sudah terblacklist")
                            else:
                                self.wait["RAblacklist"][msg.contentMetadata["mid"]] = True
                                f=codecs.open('RAwait.json','w','utf-8')
                                json.dump(self.wait, f, sort_keys=True, indent=4,ensure_ascii=False)
                                cl.sendText(msg.to,"Akun terblacklist")
                        elif self.wait["RAdblacklist"] == True:
                            if msg.contentMetadata["mid"] in self.wait["RAblacklist"]:
                                del self.wait["RAblacklist"][msg.contentMetadata["mid"]]
                                f=codecs.open('RAwait.json','w','utf-8')
                                json.dump(self.wait, f, sort_keys=True, indent=4,ensure_ascii=False)
                                cl.sendText(msg.to,"Akun dihapus dari blacklist")
                            else:
                                cl.sendText(msg.to,"Akun tidak ada di blacklist")
                        elif self.wait["RAautoscan"] == True:
                            msg.contentType = 0
                            cl.sendText(msg.to,msg.contentMetadata["mid"])
                            
                    if msg.from_ in RASadmin or msg.from_ in self.wait["RAAdmin"]:         
                        if self.wait["RASadmin"] == True:
                            if msg.contentMetadata["mid"] in self.wait["RAAdmin"]:
                                cl.sendText(msg.to,"Akun sudah menjadi admin")
                            else:
                                self.wait["RAAdmin"][msg.contentMetadata["mid"]] = True
                                f=codecs.open('RAwait.json','w','utf-8')
                                json.dump(self.wait, f, sort_keys=True, indent=4,ensure_ascii=False)
                                cl.sendText(msg.to,"Terdaftar menjadi admin")
                        elif self.wait["RASDadmin"] == True:
                            if msg.contentMetadata["mid"] in self.wait["RAAdmin"]:
                                del self.wait["RAAdmin"][msg.contentMetadata["mid"]]
                                f=codecs.open('RAwait.json','w','utf-8')
                                json.dump(self.wait, f, sort_keys=True, indent=4,ensure_ascii=False)
                                cl.sendText(msg.to,"Akun dihapus dari adminlist")
                            else:
                                cl.sendText(msg.to,"Akun tidak ada di adminlist")
                        elif self.wait["RASstaff"] == True:
                            if msg.contentMetadata["mid"] in self.wait["RAStaff"]:
                                cl.sendText(msg.to,"Akun sudah menjadi staff")
                            else:
                                self.wait["RAStaff"][msg.contentMetadata["mid"]] = True
                                f=codecs.open('RAwait.json','w','utf-8')
                                json.dump(self.wait, f, sort_keys=True, indent=4,ensure_ascii=False)
                                cl.sendText(msg.to,"Terdaftar menjadi staff")
                        elif self.wait["RASDstaff"] == True:
                            if msg.contentMetadata["mid"] in self.wait["RAStaff"]:
                                del self.wait["RAStaff"][msg.contentMetadata["mid"]]
                                f=codecs.open('RAwait.json','w','utf-8')
                                json.dump(self.wait, f, sort_keys=True, indent=4,ensure_ascii=False)
                                cl.sendText(msg.to,"Akun dihapus dari stafflist")
                            else:
                                cl.sendText(msg.to,"Akun tidak ada di stafflist")
                                
                    if msg.from_ in RASadmin:
                        if self.wait["RASbot"] == True:
                            if msg.contentMetadata["mid"] in self.wait["RABots"]:
                                cl.sendText(msg.to,"Bot sudah masuk list")
                            else:
                                self.wait["RABots"][msg.contentMetadata["mid"]] = True
                                f=codecs.open('RAwait.json','w','utf-8')
                                json.dump(self.wait, f, sort_keys=True, indent=4,ensure_ascii=False)
                                cl.sendText(msg.to,"Bot masuk dalam list")
                        elif self.wait["RASDbot"] == True:
                            if msg.contentMetadata["mid"] in self.wait["RABots"]:
                                del self.wait["RABots"][msg.contentMetadata["mid"]]
                                f=codecs.open('RAwait.json','w','utf-8')
                                json.dump(self.wait, f, sort_keys=True, indent=4,ensure_ascii=False)
                                cl.sendText(msg.to,"Bot keluar dari list")
                            else:
                                cl.sendText(msg.to,"Bot tidak ada di list")
                    
                elif msg.contentType == 1:
                    if msg.from_ in RASadmin:
                        if self.mid in self.RAset["RAfoto"]:
                            path = cl.downloadObjectMsg(msg.id)
                            del self.RAset["RAfoto"][self.mid]
                            cl.updateProfilePicture(path)
                            cl.sendMessage(msg.to,"Foto berhasil dirubah")
                        elif msg.to in self.RAset["RAfoto"]:
                            path = cl.downloadObjectMsg(msg.id)
                            cl.updateProfilePicture(path)
                            del self.RAset["RAfoto"][msg.to]
                            cl.sendMessage(msg.to,"Foto berhasil diperbaharui")
                        if msg.toType == 2:
                            if msg.to in self.RAset["RAGfoto"]:
                                path = cl.downloadObjectMsg(msg.id)
                                del self.RAset["RAGfoto"][msg.to]
                                cl.updateGroupPicture(msg.to, path)
                                cl.sendMessage(msg.to,"Foto grup diperbaharui")
                elif None == msg.text:
                    return
                
#------------------------------- Start Menu ----------------------------------#
            
                elif msg.text == self.resp + 'msamenu':
                    if msg.from_ in RASadmin:
                        md = "🔰 |RA| Family Protection\n\n"
                        md += "🔰" +RAKey+ " absen\n"
                        md += "🔰" +RAKey+ " spbot\n"
                        md += "🔰" +RAKey+ " sprespon\n"
                        md += "🔰" +RAKey+ " cname 「text」\n"
                        md += "🔰" +RAKey+ " cbio 「text」\n"
                        md += "🔰" +RAKey+ " cfoto\n"
                        md += "🔰" +RAKey+ " cleanblacklist\n"
                        md += "🔰" +RAKey+ " byeall\n"
                        md += "🔰" +RAKey+ " leaveall\n"
                        md += "🔰" +RAKey+ " cleanmember\n"
                        md += "🔰" +RAKey+ " friend\n"
                        md += "🔰" +RAKey+ " spam「mid」「jumlah」\n"
                        md += "🔰" +RAKey+ " restart\n"
                        md += "🔰" +RAKey+ " masukin\n"
                        md += "🔰" +RAKey+ " removechat\n"
                        md += "🔰" +RAKey+ " leave「idgroup」\n"
                        md += "🔰" +RAKey+ " scblack 「on/off」\n"
                        md += "🔰" +RAKey+ " scublack 「on/off」\n"
                        md += "🔰" +RAKey+ " scadmin 「on/off」\n"
                        md += "🔰" +RAKey+ " scuadmin 「on/off」\n"
                        md += "🔰" +RAKey+ " scstaff 「on/off」\n"
                        md += "🔰" +RAKey+ " scustaff 「on/off」\n"
                        md += "🔰" +RAKey+ " autoread 「on/off」\n"
                        md += "🔰" +RAKey+ " ngebot 「on/off」\n"
                        md += "🔰" +RAKey+ " buangbot 「on/off」\n"
                        md += "🔰" +RAKey+ " 「block/allow」 invite\n"
                        md += "🔰" +RAKey+ " 「block/allow」 ourl\n"
                        md += "🔰" +RAKey+ " 「block/allow」 cancel\n"
                        md += "🔰" +RAKey+ " 「block/allow」 kick\n"
                        md += "🔰" +RAKey+ " 「block/allow」 semua\n"
                        md += "🔰" +RAKey+ " mspam\n"
                        md += "🔰" +RAKey+ " cspam「text」\n"
                        md += "🔰" +RAKey+ " bl「@」\n"
                        md += "🔰" +RAKey+ " ubl「@」\n"
                        md += "🔰" +RAKey+ " adadd「@」\n"
                        md += "🔰" +RAKey+ " addell「@」\n"
                        md += "🔰" +RAKey+ " stadd「@」\n"
                        md += "🔰" +RAKey+ " stdell「@」\n"
                        md += "🔰" +RAKey+ " nganubot「@」\n"
                        md += "🔰" +RAKey+ " cuekinbot「@」\n"
                        md += "Fungsi Diatas untuk semua Bot"
                        md += "\n\n"
                        md += "🔰" +self.resp+ " pengaturan\n"
                        md += "🔰" +self.resp+ " cekmid 「on/off」\n"
                        md += "🔰" +self.resp+ " 「allow/block」 greet\n"
                        md += "🔰" +self.resp+ " ourl / curl\n"
                        md += "🔰" +self.resp+ " informasi\n"
                        md += "🔰" +self.resp+ " listgroup\n"
                        md += "🔰" +self.resp+ " listidgroup\n"
                        md += "🔰" +self.resp+ " cname「text」\n"
                        md += "🔰" +self.resp+ " cbio「text」\n"
                        md += "🔰" +self.resp+ " cfoto\n"
                        md += "🔰" +self.resp+ " cfotogroup\n"
                        md += "🔰" +self.resp+ " cancel\n"
                        md += "🔰" +self.resp+ " masuk「idgroup」\n"
                        md += "🔰" +self.resp+ " bc「text」\n"
                        md += "🔰" +self.resp+ " kick「@」\n"
                        md += "🔰" +self.resp+ " listbl\n"
                        md += "🔰" +self.resp+ " limit 「jumlah」\n"
                        md += "🔰" +self.resp+ " panggil 「@」\n"
                        md += "🔰" +self.resp+ " listteam\n"
                        md += "🔰" +self.resp+ " listbot\n"
                        md += "🔰" +self.resp+ " listprotect\n"
                        md += "Fungsi Diatas untuk inisial Bot"
                        cl.sendText(msg.to,md)
                        
                elif msg.text == self.resp + 'mamenu':
                    if msg.from_ in RASadmin or msg.from_ in self.wait["RAAdmin"]:
                        md = "🔰 |RA| Admin Protection\n\n"
                        md += "🔰" +RAKey+ " absen\n"
                        md += "🔰" +RAKey+ " spbot\n"
                        md += "🔰" +RAKey+ " sprespon\n"
                        md += "🔰" +RAKey+ " cleanblacklist\n"
                        md += "🔰" +RAKey+ " byeall\n"
                        md += "🔰" +RAKey+ " scblack 「on/off」\n"
                        md += "🔰" +RAKey+ " scublack 「on/off」\n"
                        md += "🔰" +RAKey+ " scstaff 「on/off」\n"
                        md += "🔰" +RAKey+ " scustaff 「on/off」\n"
                        md += "🔰" +RAKey+ " 「block/allow」 invite\n"
                        md += "🔰" +RAKey+ " 「block/allow」 ourl\n"
                        md += "🔰" +RAKey+ " 「block/allow」 cancel\n"
                        md += "🔰" +RAKey+ " 「block/allow」 kick\n"
                        md += "🔰" +RAKey+ " 「block/allow」 semua\n"
                        md += "🔰" +RAKey+ " spam「mid」「jumlah」\n"
                        md += "🔰" +RAKey+ " mspam\n"
                        md += "🔰" +RAKey+ " cspam「text」\n"
                        md += "🔰" +RAKey+ " bl「@」\n"
                        md += "🔰" +RAKey+ " ubl「@」\n"
                        md += "🔰" +RAKey+ " stadd「@」\n"
                        md += "🔰" +RAKey+ " stdell「@」\n"
                        md += "Fungsi Diatas untuk semua Bot"
                        md += "\n\n"
                        md += "🔰" +self.resp+ " pengaturan\n"
                        md += "🔰" +self.resp+ " cekmid 「on/off」\n"
                        md += "🔰" +self.resp+ " 「allow/block」 greet\n"
                        md += "🔰" +self.resp+ " ourl / curl\n"
                        md += "🔰" +self.resp+ " informasi\n"
                        md += "🔰" +self.resp+ " listgroup\n"
                        md += "🔰" +self.resp+ " listidgroup\n"
                        md += "🔰" +self.resp+ " cfotogroup\n"
                        md += "🔰" +self.resp+ " cancel\n"
                        md += "🔰" +self.resp+ " masuk「idgroup」\n"
                        md += "🔰" +self.resp+ " bc「text」\n"
                        md += "🔰" +self.resp+ " kick「@」\n"
                        md += "🔰" +self.resp+ " listbl\n"
                        md += "🔰" +self.resp+ " listteam\n"
                        md += "🔰" +self.resp+ " listbot\n"
                        md += "🔰" +self.resp+ " listprotect\n"
                        cl.sendText(msg.to,md)
                        
                elif msg.text == self.resp + 'msmenu':
                    if msg.from_ in RASadmin or msg.from_ in self.wait["RAAdmin"] or msg.from_ in self.wait["RAStaff"]:
                        md = "🔰 |RA| Staff Protection\n\n"
                        md += "🔰" +RAKey+ " absen\n"
                        md += "🔰" +RAKey+ " spbot\n"
                        md += "🔰" +RAKey+ " sprespon\n"
                        md += "🔰" +RAKey+ " cleanblacklist\n"
                        md += "🔰" +RAKey+ " byeall\n"
                        md += "🔰" +RAKey+ " scblack 「on/off」\n"
                        md += "🔰" +RAKey+ " scublack 「on/off」\n"
                        md += "🔰" +RAKey+ " 「block/allow」 invite\n"
                        md += "🔰" +RAKey+ " 「block/allow」 ourl\n"
                        md += "🔰" +RAKey+ " 「block/allow」 cancel\n"
                        md += "🔰" +RAKey+ " 「block/allow」 kick\n"
                        md += "🔰" +RAKey+ " 「block/allow」 semua\n"
                        md += "🔰" +RAKey+ " bl「@」\n"
                        md += "🔰" +RAKey+ " ubl「@」\n"
                        md += "Fungsi Diatas untuk semua Bot"
                        md += "\n\n"
                        md += "🔰" +self.resp+ " pengaturan\n"
                        md += "🔰" +self.resp+ " cekmid 「on/off」\n"
                        md += "🔰" +self.resp+ " 「allow/block」 greet\n"
                        md += "🔰" +self.resp+ " ourl / curl\n"
                        md += "🔰" +self.resp+ " informasi\n"
                        md += "🔰" +self.resp+ " listgroup\n"
                        md += "🔰" +self.resp+ " cancel\n"
                        md += "🔰" +self.resp+ " kick「@」\n"
                        md += "🔰" +self.resp+ " listbl\n"
                        md += "🔰" +self.resp+ " listteam\n"
                        md += "🔰" +self.resp+ " listbot\n"
                        cl.sendText(msg.to,md)
                        
                elif msg.text == self.resp + 'mpublic':
                    md = " RA Family  Menu\n\n"
                    md += "🔰" +self.resp+ " cek「@」\n"
                    md += "🔰" +self.resp+ " gid\n"
                    md += "🔰" +self.resp+ " yid\n"
                    md += "🔰" +self.resp+ " lastseen「on/off」「lastseens」\n"
                    md += "🔰" +self.resp+ " tagall\n"
                    md += "🔰" +self.resp+ " yt-video「nama-judul」\n"
                    md += "🔰" +self.resp+ " yt-mp3「nama-judul」\n"
                    md += "🔰" +self.resp+ " film 「judul」 「tahun」\n"
                    md += "🔰" +self.resp+ " get-ig 「username」\n"
                    md += "🔰" +self.resp+ " igpost 「username」 「urutan」\n"
                    md += "🔰" +self.resp+ " wsholat 「nama lokasi」\n"
                    md += "🔰" +self.resp+ " ccuaca 「nama lokasi」\n"
                    md += "🔰" +self.resp+ " clokasi 「nama lokasi」\n"
                    cl.sendText(msg.to,md)
                    
                    
                    
                    
                        
                        
                elif msg.text == self.resp + 'pengaturan':
                    if msg.from_ in RASadmin or msg.from_ in self.wait["RAAdmin"] or msg.from_ in self.wait["RAStaff"]:
                        md = "🔰 |RA|Family Protection\n\n"
                        if self.wait["RASadmin"] == True: md+="✅ Add Admin\n"
                        else: md+="❎ Add Admin\n"
                        if self.wait["RASDadmin"] == True: md+="✅ Dell Admin\n"
                        else: md+="❎ Dell Admin\n"
                        if self.wait["RASstaff"] == True: md+="✅ Add Staff\n"
                        else: md+="❎ Add Staff\n"
                        if self.wait["RASDstaff"] == True: md+="✅ Dell Staff\n"
                        else: md+="❎ Dell Staff\n"
                        if self.wait["RAwblacklist"] == True: md+="✅ Blacklist\n"
                        else: md+="❎ Blacklist\n"
                        if self.wait["RAdblacklist"] == True: md+="✅ Unblacklist\n"
                        else: md+="❎ Unblacklist\n"
                        if self.wait["RAautoscan"] == True: md+="✅ Cek Mid\n"
                        else: md+="❎ Cek Mid\n"
                        if self.wait["RASbot"] == True: md+="✅ Tambahbot\n"
                        else: md+="❎ Tambahbot\n"
                        if self.wait["RASDbot"] == True: md+="✅ Buangbot\n"
                        else: md+="❎ Buangbot\n"
                        if self.wait["RAautojoin"] == True: md+="✅ Auto Join\n"
                        else: md+="❎ Auto Join\n"
                        if self.wait["RAautoread"] == True: md+="✅ Auto Read\n"
                        else: md+="❎ Auto Read\n"
                        if msg.to in self.RAset["RAprotinvite"]: md+="✅ Block inivte\n"
                        else: md+="❎ Block invite\n"
                        if msg.to in self.RAset["RAprotqr"]: md+="✅ Block ourl \n"
                        else: md+="❎ Block ourl\n"
                        if msg.to in self.RAset["RAprotkick"]: md+="✅ Block kick member \n"
                        else: md+="❎ Block kick member off\n" 
                        if msg.to in self.RAset["RAprotcancel"]: md+="✅ Block cancel member \n"
                        else: md+="❎ Block cancel member off\n"
                        if msg.to in self.RAset["RAgreet"]: md+="✅ Greet Message \n"
                        else: md+="❎ Greet off\n"
                        cl.sendText(msg.to,md)
                        
                
                elif msg.text == RAKey + "scblack on":
                    if msg.from_ in RASadmin or msg.from_ in self.wait["RAAdmin"] or msg.from_ in self.wait["RAStaff"]:
                        if self.wait["RAwblacklist"] == False:
                            self.wait["RAwblacklist"] = True
                            cl.sendText(msg.to, "kirim kontak untuk blacklist")
                        else:
                            cl.sendText(msg.to, "Sudah on")
                            
                elif msg.text == RAKey + "scblack off":
                    if msg.from_ in RASadmin or msg.from_ in self.wait["RAAdmin"] or msg.from_ in self.wait["RAStaff"]:
                        if self.wait["RAwblacklist"] == True:
                            self.wait["RAwblacklist"] = False
                            cl.sendText(msg.to, "Blacklist dinonaktifkan")
                        else:
                            cl.sendText(msg.to, "Sudah off")
                            
                elif msg.text == RAKey + "scublack on":
                    if msg.from_ in RASadmin or msg.from_ in self.wait["RAAdmin"] or msg.from_ in self.wait["RAStaff"]:
                        if self.wait["RAdblacklist"] == False:
                            self.wait["RAdblacklist"] = True
                            cl.sendText(msg.to, "kirim kontak untuk unblacklist")
                        else:
                            cl.sendText(msg.to, "Sudah on")
                            
                elif msg.text == RAKey + "scublack off":
                    if msg.from_ in RASadmin or msg.from_ in self.wait["RAAdmin"] or msg.from_ in self.wait["RAStaff"]:
                        if self.wait["RAdblacklist"] == True:
                            self.wait["RAdblacklist"] = False
                            cl.sendText(msg.to, "Unblacklist dinonaktifkan")
                        else:
                            cl.sendText(msg.to, "Sudah off")
                            
                elif msg.text == RAKey + "scadmin on":
                    if msg.from_ in RASadmin:
                        if self.wait["RASadmin"] == False:
                            self.wait["RASadmin"] = True
                            cl.sendText(msg.to, "kirim kontak untuk tambah admin")
                        else:
                            cl.sendText(msg.to, "Sudah on")
                            
                elif msg.text == RAKey + "scadmin off":
                    if msg.from_ in RASadmin:
                        if self.wait["RASadmin"] == True:
                            self.wait["RASadmin"] = False
                            cl.sendText(msg.to, "Tambah admin dinonaktifkan")
                        else:
                            cl.sendText(msg.to, "Sudah off")
                            
                elif msg.text == RAKey + "scuadmin on":
                    if msg.from_ in RASadmin:
                        if self.wait["RASDadmin"] == False:
                            self.wait["RASDadmin"] = True
                            cl.sendText(msg.to, "kirim kontak untuk hapus admin")
                        else:
                            cl.sendText(msg.to, "Sudah on")
                            
                elif msg.text == RAKey + "scuadmin off":
                    if msg.from_ in RASadmin:
                        if self.wait["RASDadmin"] == True:
                            self.wait["RASDadmin"] = False
                            cl.sendText(msg.to, "Hapus admin dinonaktifkan")
                        else:
                            cl.sendText(msg.to, "Sudah off")
                            
                            
                elif msg.text == RAKey + "scstaff on":
                    if msg.from_ in RASadmin or msg.from_ in self.wait["RAAdmin"]:
                        if self.wait["RASstaff"] == False:
                            self.wait["RASstaff"] = True
                            cl.sendText(msg.to, "kirim kontak untuk tambah staff")
                        else:
                            cl.sendText(msg.to, "Sudah on")
                            
                elif msg.text == RAKey + "scstaff off":
                    if msg.from_ in RASadmin or msg.from_ in self.wait["RAAdmin"]:
                        if self.wait["RASstaff"] == True:
                            self.wait["RASstaff"] = False
                            cl.sendText(msg.to, "Tambah staff dinonaktifkan")
                        else:
                            cl.sendText(msg.to, "Sudah off")
                            
                elif msg.text == RAKey + "scustaff on":
                    if msg.from_ in RASadmin or msg.from_ in self.wait["RAAdmin"]:
                        if self.wait["RASDstaff"] == False:
                            self.wait["RASDstaff"] = True
                            cl.sendText(msg.to, "kirim kontak untuk hapus staff")
                        else:
                            cl.sendText(msg.to, "Sudah on")
                            
                elif msg.text == RAKey + "scustaff off":
                    if msg.from_ in RASadmin or msg.from_ in self.wait["RAAdmin"]:
                        if self.wait["RASDstaff"] == True:
                            self.wait["RASDstaff"] = False
                            cl.sendText(msg.to, "Hapus staff dinonaktifkan")
                        else:
                            cl.sendText(msg.to, "Sudah off")
                            
                elif msg.text == RAKey + "autoread on":
                    if msg.from_ in RASadmin:
                        if self.wait["RAautoread"] == False:
                            self.wait["RAautoread"] = True
                            cl.sendText(msg.to, "Autoread diaktifkan")
                        else:
                            cl.sendText(msg.to, "Sudah on")
                            
                elif msg.text == RAKey + "autoread off":
                    if msg.from_ in RASadmin:
                        if self.wait["RAautoread"] == True:
                            self.wait["RAautoread"] = False
                            cl.sendText(msg.to, "Autoread dinonaktifkan")
                        else:
                            cl.sendText(msg.to, "Sudah off")
                            
                elif msg.text == self.resp + "cekmid on":
                    if msg.from_ in RASadmin or msg.from_ in self.wait["RAAdmin"] or msg.from_ in self.wait["RAStaff"]:
                        if self.wait["RAautoscan"] == False:
                            self.wait["RAautoscan"] = True
                            cl.sendText(msg.to, "Cek mid diaktifkan")
                        else:
                            cl.sendText(msg.to, "Sudah on")
                            
                elif msg.text == self.resp + "cekmid off":
                    if msg.from_ in RASadmin or msg.from_ in self.wait["RAAdmin"] or msg.from_ in self.wait["RAStaff"]:
                        if self.wait["RAautoscan"] == True:
                            self.wait["RAautoscan"] = False
                            cl.sendText(msg.to, "Cek mid dinonaktifkan")
                        else:
                            cl.sendText(msg.to, "Sudah off")
                            
                elif msg.text == RAKey + "ngebot on":
                    if msg.from_ in RASadmin:
                        if self.wait["RASbot"] == False:
                            self.wait["RASbot"] = True
                            cl.sendText(msg.to, "Tambah bot diaktifkan")
                        else:
                            cl.sendText(msg.to, "Sudah on")
                            
                elif msg.text == RAKey + "ngebot off":
                    if msg.from_ in RASadmin:
                        if self.wait["RASbot"] == True:
                            self.wait["RASbot"] = False
                            cl.sendText(msg.to, "Tambah bot dinonaktifkan")
                        else:
                            cl.sendText(msg.to, "Sudah off")            
                    
                elif msg.text == RAKey + "buangbot on":
                    if msg.from_ in RASadmin:
                        if self.wait["RASDbot"] == False:
                            self.wait["RASDbot"] = True
                            cl.sendText(msg.to, "Buang bot diaktifkan")
                        else:
                            cl.sendText(msg.to, "Sudah on")
                            
                elif msg.text == RAKey + "buangbot off":
                    if msg.from_ in RASadmin:
                        if self.wait["RASDbot"] == True:
                            self.wait["RASDbot"] = False
                            cl.sendText(msg.to, "Buang bot dinonaktifkan")
                        else:
                            cl.sendText(msg.to, "Sudah off")
                
                elif msg.text == RAKey + "block invite":
                    if msg.from_ in RASadmin or msg.from_ in self.wait["RAAdmin"] or msg.from_ in self.wait["RAStaff"]:
                        if msg.to in self.RAset["RAprotinvite"]:
                            cl.sendText(msg.to,"Block invite sudah diamankan")
                        else:
                            self.RAset["RAprotinvite"][msg.to] = True
                            f=codecs.open('RAset.json','w','utf-8')
                            json.dump(self.RAset, f, sort_keys=True, indent=4,ensure_ascii=False)
                            cl.sendText(msg.to,"Block invite telah di tutup")
                            
                elif msg.text == RAKey + "allow invite":
                    if msg.from_ in RASadmin or msg.from_ in self.wait["RAAdmin"] or msg.from_ in self.wait["RAStaff"]:
                        if msg.to not in self.RAset["RAprotinvite"]:
                            cl.sendText(msg.to,"Block invite belum diamankan")
                        else:
                            del self.RAset["RAprotinvite"][msg.to]
                            f=codecs.open('RAset.json','w','utf-8')
                            json.dump(self.RAset, f, sort_keys=True, indent=4,ensure_ascii=False)
                            cl.sendText(msg.to,"Block invite telah di buka")
                            
                elif msg.text == RAKey + "block ourl":
                    if msg.from_ in RASadmin or msg.from_ in self.wait["RAAdmin"] or msg.from_ in self.wait["RAStaff"]:
                        if msg.to in self.RAset["RAprotqr"]:
                            cl.sendText(msg.to,"Block ourl sudah diamankan")
                        else:
                            self.RAset["RAprotqr"][msg.to] = True
                            f=codecs.open('RAset.json','w','utf-8')
                            json.dump(self.RAset, f, sort_keys=True, indent=4,ensure_ascii=False)
                            cl.sendText(msg.to,"Block ourl telah di tutup")
                            
                elif msg.text == RAKey + "allow ourl":
                    if msg.from_ in RASadmin or msg.from_ in self.wait["RAAdmin"] or msg.from_ in self.wait["RAStaff"]:
                        if msg.to not in self.RAset["RAprotqr"]:
                            cl.sendText(msg.to,"Block ourl belum diamankan")
                        else:
                            del self.RAset["RAprotqr"][msg.to]
                            f=codecs.open('RAset.json','w','utf-8')
                            json.dump(self.RAset, f, sort_keys=True, indent=4,ensure_ascii=False)
                            cl.sendText(msg.to,"Block ourl telah di buka")
                            
                elif msg.text == RAKey + "block cancel":
                    if msg.from_ in RASadmin or msg.from_ in self.wait["RAAdmin"] or msg.from_ in self.wait["RAStaff"]:
                        if msg.to in self.RAset["RAprotcancel"]:
                            cl.sendText(msg.to,"Block cancel sudah diamankan")
                        else:
                            self.RAset["RAprotcancel"][msg.to] = True
                            f=codecs.open('RAset.json','w','utf-8')
                            json.dump(self.RAset, f, sort_keys=True, indent=4,ensure_ascii=False)
                            cl.sendText(msg.to,"Block cancel telah di tutup")
                            
                elif msg.text == RAKey + "allow cancel":
                    if msg.from_ in RASadmin or msg.from_ in self.wait["RAAdmin"] or msg.from_ in self.wait["RAStaff"]:
                        if msg.to not in self.RAset["RAprotcancel"]:
                            cl.sendText(msg.to,"Block cancel belum diamankan")
                        else:
                            del self.RAset["RAprotcancel"][msg.to]
                            f=codecs.open('RAset.json','w','utf-8')
                            json.dump(self.RAset, f, sort_keys=True, indent=4,ensure_ascii=False)
                            cl.sendText(msg.to,"Block cancel telah di buka")
                            
                elif msg.text == RAKey + "block kick":
                    if msg.from_ in RASadmin or msg.from_ in self.wait["RAAdmin"] or msg.from_ in self.wait["RAStaff"]:
                        if msg.to in self.RAset["RAprotkick"]:
                            cl.sendText(msg.to,"Block kick sudah diamankan")
                        else:
                            self.RAset["RAprotkick"][msg.to] = True
                            f=codecs.open('RAset.json','w','utf-8')
                            json.dump(self.RAset, f, sort_keys=True, indent=4,ensure_ascii=False)
                            cl.sendText(msg.to,"Block kick telah di tutup")
                            
                elif msg.text == RAKey + "allow kick":
                    if msg.from_ in RASadmin or msg.from_ in self.wait["RAAdmin"] or msg.from_ in self.wait["RAStaff"]:
                        if msg.to not in self.RAset["RAprotkick"]:
                            cl.sendText(msg.to,"Block kick belum diamankan")
                        else:
                            del self.RAset["RAprotkick"][msg.to]
                            f=codecs.open('RAset.json','w','utf-8')
                            json.dump(self.RAset, f, sort_keys=True, indent=4,ensure_ascii=False)
                            cl.sendText(msg.to,"Block kick telah di buka")
                            
                elif msg.text == RAKey + "block semua":
                    if msg.from_ in RASadmin or msg.from_ in self.wait["RAAdmin"] or msg.from_ in self.wait["RAStaff"]:
                        if msg.to in self.RAset["RAprotinvite"] or msg.to in self.RAset["RAprotqr"] or msg.to in self.RAset["RAprotcancel"] or msg.to in self.RAset["RAprotkick"]:
                            cl.sendText(msg.to,"Group sudah diamankan")
                        else:
                            self.RAset["RAprotinvite"][msg.to] = True
                            self.RAset["RAprotqr"][msg.to] = True
                            self.RAset["RAprotcancel"][msg.to] = True
                            self.RAset["RAprotkick"][msg.to] = True
                            f=codecs.open('RAset.json','w','utf-8')
                            json.dump(self.RAset, f, sort_keys=True, indent=4,ensure_ascii=False)
                            cl.sendText(msg.to,"Akses telah di tutup")
                            
                elif msg.text == RAKey + "allow semua":
                    if msg.from_ in RASadmin or msg.from_ in self.wait["RAAdmin"] or msg.from_ in self.wait["RAStaff"]:
                        if msg.to not in self.RAset["RAprotinvite"] or msg.to not in self.RAset["RAprotqr"] or msg.to not in self.RAset["RAprotcancel"] or msg.to not in self.RAset["RAprotkick"]:
                            cl.sendText(msg.to,"Group belum diamankan")
                        else:
                            del self.RAset["RAprotinvite"][msg.to]
                            del self.RAset["RAprotqr"][msg.to]
                            del self.RAset["RAprotcancel"][msg.to]
                            del self.RAset["RAprotkick"][msg.to]
                            f=codecs.open('RAset.json','w','utf-8')
                            json.dump(self.RAset, f, sort_keys=True, indent=4,ensure_ascii=False)
                            cl.sendText(msg.to,"Akses telah di buka")            
                            
                elif msg.text == self.resp + "allow greet":
                    if msg.from_ in RASadmin or msg.from_ in self.wait["RAAdmin"] or msg.from_ in self.wait["RAStaff"]:
                        if msg.to in self.RAset["RAgreet"]:
                            cl.sendText(msg.to,"Pesan sambutan sudah aktif")
                        else:
                            self.RAset["RAgreet"][msg.to] = True
                            f=codecs.open('RAset.json','w','utf-8')
                            json.dump(self.RAset, f, sort_keys=True, indent=4,ensure_ascii=False)
                            cl.sendText(msg.to,"Pesan sambutan diaktifkan")
                            
                elif msg.text == self.resp + "block greet":
                    if msg.from_ in RASadmin or msg.from_ in self.wait["RAAdmin"] or msg.from_ in self.wait["RAStaff"]:
                        if msg.to not in self.RAset["RAgreet"]:
                            cl.sendText(msg.to,"Pesan sambutan tidak aktif")
                        else:
                            del self.RAset["RAgreet"][msg.to]
                            f=codecs.open('RAset.json','w','utf-8')
                            json.dump(self.RAset, f, sort_keys=True, indent=4,ensure_ascii=False)
                            cl.sendText(msg.to,"Pesan sambutan dimatikan")            
                            
            #------------------- Protect Command Finish ------------------#
            
            
            #------------------- Main Command Start ------------------#
                        
                elif msg.text == self.resp + 'ourl':
                    if msg.from_ in RASadmin or msg.from_ in self.wait["RAAdmin"] or msg.from_ in self.wait["RAStaff"]:
                        if msg.toType == 2:
                            x = cl.getGroup(msg.to)
                            if x.preventedJoinByTicket == True:
                                x.preventedJoinByTicket = False
                                cl.updateGroup(x)
                            gurl = cl.reissueGroupTicket(msg.to)
                            cl.sendText(msg.to,"line://ti/g/" + gurl)
                            
                elif msg.text == self.resp + 'curl':
                    if msg.from_ in RASadmin or msg.from_ in self.wait["RAAdmin"] or msg.from_ in self.wait["RAStaff"]:
                        if msg.toType == 2:
                            X = cl.getGroup(msg.to)
                            X.preventedJoinByTicket = True
                            cl.updateGroup(X)
                            
                elif msg.text == self.resp + 'informasi':
                    if msg.from_ in RASadmin or msg.from_ in self.wait["RAAdmin"] or msg.from_ in self.wait["RAStaff"]:
                        profile = cl.getProfile()
                        gid = cl.getGroupIdsJoined()
                        total = str(len(gid))
                        eltime = time.time() - mulai
                        
                        cin = " "+waktu(eltime)
                        cl.sendText(msg.to,"[Name]\n" + profile.displayName + "\n\n[Mid]\n" + profile.mid + "\n\n[Total Group]\n" + str(total) + "\n\n[Command Menu]\n" +self.resp+ " mamenu\n" +self.resp+ " msmenu\n" +self.resp+ " mpublic" "\n\n[Runtime]\n" + cin)
                        
                elif msg.text == self.resp + 'listgroup':
                    if msg.from_ in RASadmin or msg.from_ in self.wait["RAAdmin"] or msg.from_ in self.wait["RAStaff"]:
                        gid = cl.getGroupIdsJoined()
                        h = "[List Groups]"
                        total = str(len(gid))
                        for i in gid:
                            if i is not None:
                                try:
                                    groups = cl.getGroup(i)
                                    if groups.members is not None:
                                        members = str(len(groups.members))
                                    else:
                                        members = "0"
                                    if groups.invitee is not None:
                                        pendings = str(len(groups.invitee))
                                    else:
                                        pendings = "0"
                                    h += "\n[" + groups.name + "]\n ->Members : " + members
                                except:
                                    break
                            else:
                                break
                        if gid is not None:
                            cl.sendText(msg.to,h + "\n|[Total Groups]| : " + str(total))
                        else:
                            cl.sendText(msg.to,"Tidak ada grup saat ini")
                        ginv = cl.getGroupIdsInvited()
                        j = "[List Groups Invited]"
                        totals = str(len(ginv))
                        for z in ginv:
                            if z is not None:
                                try:
                                    groups = cl.getGroup(z)
                                    if groups.members is not None:
                                        members = str(len(groups.members))
                                    else:
                                        members = "0"
                                    if groups.invitee is not None:
                                        pendings = str(len(groups.invitee))
                                    else:
                                        pendings = "0"
                                    j += "\n[" + groups.name + "]\n ->Members : " + members
                                except:
                                    break
                            else:
                                break
                        if ginv is not None:
                            cl.sendText(msg.to,j + "\n|[Total Groups Invited]| : " + str(totals))
                        else:
                            cl.sendText(msg.to,"Tidak ada grup tertunda saat ini")
                            
                elif msg.text == self.resp +'listidgroup':
                    if msg.from_ in RASadmin or msg.from_ in self.wait["RAAdmin"]:
                        gid = cl.getGroupIdsJoined()
                        h = ""
                        for i in gid:
                            h += "[%s]:\n%s\n" % (cl.getGroup(i).name,i)
                        cl.sendText(msg.to,h)
                        
                elif self.resp +"cname " in msg.text:
                    if msg.from_ in RASadmin:
                        string = msg.text.replace(self.resp + "cname ","")
                        profile_B = cl.getProfile()
                        profile_B.displayName = string
                        cl.updateProfile(profile_B)
                        cl.sendText(msg.to,"Berubah Menjadi " + string)
                            
                elif self.resp +"cbio " in msg.text:
                    if msg.from_ in RASadmin:
                        string = msg.text.replace(self.resp + "cbio ","")
                        profile_B = cl.getProfile()
                        profile_B.statusMessage = string
                        cl.updateProfile(profile_B)
                        cl.sendText(msg.to,"Berubah Menjadi " + string)
                            
                elif msg.text == self.resp +"cfoto":
                    if msg.from_ in RASadmin:
                        self.RAset["RAfoto"][self.mid] = True
                        cl.sendText(msg.to,"Kirim foto.....")
                        
                elif msg.text == self.resp +"cfotogroup":
                    if msg.from_ in RASadmin or msg.from_ in self.wait["RAAdmin"]:
                        self.RAset["RAGfoto"][msg.to] = True
                        cl.sendText(msg.to,"Kirim foto.....")
                        
                elif self.resp +"masuk " in msg.text:
                    if msg.from_ in RASadmin or msg.from_ in self.wait["RAAdmin"]:
                        gid = msg.text.replace(self.resp + "masuk ","")
                        if gid == "":
                            cl.sendText(msg.to,"id grup salah")
                        else:
                            try:
                                cl.findAndAddContactsByMid(msg.from_)
                                cl.inviteIntoGroup(gid,[msg.from_])
                            except Exception as e:
                                print(e)
                                
                elif self.resp +"bc " in msg.text:
                    if msg.from_ in RASadmin or msg.from_ in self.wait["RAAdmin"]:
                        text = msg.text.replace(self.resp + "bc ","")
                        gid = cl.getGroupIdsJoined()
                        if text == "":
                            cl.sendText(msg.to,"Tidak ada pesan")
                        else:
                            for i in gid:
                                cl.sendText(i,"✅ Broadcast\n\n" +text+ "\n\n http://line.me/ti/p/~kingharem12")
                                
                elif self.resp + "kick" in msg.text:
                    if msg.from_ in RASadmin or msg.from_ in self.wait["RAAdmin"] or msg.from_ in self.wait["RAStaff"]:
                        key = eval(msg.contentMetadata["MENTION"])
                        key["MENTIONEES"][0]["M"]
                        targets = []
                        for x in key["MENTIONEES"]:
                            targets.append(x["M"])
                        for target in targets:
                            if target in RASadmin or target in self.wait["RAAdmin"] or target in self.wait["RAStaff"]:
                                pass
                            else:
                                try:
                                    cl.kickoutFromGroup(msg.to,[target])
                                except:
                                    pass
                                
                elif RAKey + "bl" in msg.text:
                    if msg.from_ in RASadmin or msg.from_ in self.wait["RAAdmin"] or msg.from_ in self.wait["RAStaff"]:
                        key = eval(msg.contentMetadata["MENTION"])
                        key["MENTIONEES"][0]["M"]
                        targets = []
                        for x in key["MENTIONEES"]:
                            targets.append(x["M"])
                        for target in targets:
                            if target in RASadmin or target in self.wait["RAAdmin"] or target in self.wait["RAStaff"]:
                                pass
                            else:
                                try:
                                    self.wait["RAblacklist"][target] = True
                                    f=codecs.open('RAwait.json','w','utf-8')
                                    json.dump(self.wait, f, sort_keys=True, indent=4,ensure_ascii=False)
                                    cl.sendText(msg.to,"Akun terblacklist")
                                except:
                                    cl.sendText(msg.to,"Sudah terblacklist")
                                    
                elif RAKey + "ubl" in msg.text:
                    if msg.from_ in RASadmin or msg.from_ in self.wait["RAAdmin"] or msg.from_ in self.wait["RAStaff"]:
                        key = eval(msg.contentMetadata["MENTION"])
                        key["MENTIONEES"][0]["M"]
                        targets = []
                        for x in key["MENTIONEES"]:
                            targets.append(x["M"])
                        for target in targets:
                            if target in RASadmin or target in self.wait["RAAdmin"] or target in self.wait["RAStaff"]:
                                pass
                            else:
                                try:
                                    del self.wait["RAblacklist"][target]
                                    f=codecs.open('RAwait.json','w','utf-8')
                                    json.dump(self.wait, f, sort_keys=True, indent=4,ensure_ascii=False)
                                    cl.sendText(msg.to,"Akun bersih blacklist")
                                except:
                                    cl.sendText(msg.to,"Tidak terblacklist")
                                
                elif msg.text == RAKey +"mspam":
                    if msg.from_ in RASadmin or msg.from_ in self.wait["RAAdmin"]:
                        if self.wait["RAmessage"] is not None:
                            cl.sendText(msg.to,"Message \"" + str(self.wait['RAmessage']) + "\"")
                        else:
                            cl.sendText(msg.to,"Tidak ada pesan yang diatur")
                    
                elif msg.text == RAKey +"cspam ":
                    if msg.from_ in RASadmin or msg.from_ in self.wait["RAAdmin"]:
                        text = msg.text.replace(RAKey +"cspam ","")
                        try:
                            self.wait["RAmessage"] = text
                            cl.sendText(msg.to,"Berubah menjadi \"" + text + "\"")
                        except:
                            cl.sendText(msg.to,"Gagal mengganti pesan")
                            
                elif RAKey + "adadd" in msg.text:
                    if msg.from_ in RASadmin:
                        key = eval(msg.contentMetadata["MENTION"])
                        key["MENTIONEES"][0]["M"]
                        targets = []
                        for x in key["MENTIONEES"]:
                            targets.append(x["M"])
                        for target in targets:    
                            if target in self.wait["RAAdmin"]:
                                cl.sendText(msg.to,"Sudah terdaftar...")
                            else:
                                try:
                                    self.wait["RAAdmin"][target] = True
                                    f=codecs.open('RAwait.json','w','utf-8')
                                    json.dump(self.wait, f, sort_keys=True, indent=4,ensure_ascii=False)
                                    cl.sendText(msg.to,"Terdaftar menjadi admin")
                                except Exception as e:
                                    cl.sendText(msg.to,"Erorr....")
                                    
                elif RAKey + "addell" in msg.text:
                    if msg.from_ in RASadmin:
                        key = eval(msg.contentMetadata["MENTION"])
                        key["MENTIONEES"][0]["M"]
                        targets = []
                        for x in key["MENTIONEES"]:
                            targets.append(x["M"])
                        for target in targets:    
                            if target not in self.wait["RAAdmin"]:
                                cl.sendText(msg.to,"Sudah dihapus...")
                            else:
                                try:
                                    del self.wait["RAAdmin"][target]
                                    f=codecs.open('RAwait.json','w','utf-8')
                                    json.dump(self.wait, f, sort_keys=True, indent=4,ensure_ascii=False)
                                    cl.sendText(msg.to,"Dihapus menjadi admin")
                                except Exception as e:
                                    cl.sendText(msg.to,"Erorr...")
                                    
                elif RAKey + "stadd" in msg.text:
                    if msg.from_ in RASadmin or msg.from_ in self.wait["RAAdmin"]:
                        key = eval(msg.contentMetadata["MENTION"])
                        key["MENTIONEES"][0]["M"]
                        targets = []
                        for x in key["MENTIONEES"]:
                            targets.append(x["M"])
                        for target in targets:    
                            if target in self.wait["RAStaff"]:
                                cl.sendText(msg.to,"Sudah terdaftar...")
                                pass
                            else:
                                try:
                                    self.wait["RAStaff"][target] = True
                                    f=codecs.open('RAwait.json','w','utf-8')
                                    json.dump(self.wait, f, sort_keys=True, indent=4,ensure_ascii=False)
                                    cl.sendText(msg.to,"Terdaftar menjadi staff")
                                except Exception as e:
                                    cl.sendText(msg.to,"Erorr.....")
                                    
                elif RAKey + "stdell" in msg.text:
                    if msg.from_ in RASadmin or msg.from_ in self.wait["RAAdmin"]:
                        key = eval(msg.contentMetadata["MENTION"])
                        key["MENTIONEES"][0]["M"]
                        targets = []
                        for x in key["MENTIONEES"]:
                            targets.append(x["M"])
                        for target in targets:    
                            if target not in self.wait["RAStaff"]:
                                cl.sendText(msg.to,"Sudah dihapus...")
                                pass
                            else:
                                try:
                                    del self.wait["RAStaff"][target]
                                    f=codecs.open('RAwait.json','w','utf-8')
                                    json.dump(self.wait, f, sort_keys=True, indent=4,ensure_ascii=False)
                                    cl.sendText(msg.to,"Dihapus menjadi staff")
                                except Exception as e:
                                    cl.sendText(msg.to,"Erorr...")
                                    
                elif RAKey + "nganubot" in msg.text:
                    if msg.from_ in RASadmin:
                        key = eval(msg.contentMetadata["MENTION"])
                        key["MENTIONEES"][0]["M"]
                        targets = []
                        for x in key["MENTIONEES"]:
                            targets.append(x["M"])
                        for target in targets:    
                            if target in self.wait["RABots"]:
                                cl.sendText(msg.to,"Sudah terdaftar...")
                                pass
                            else:
                                try:
                                    self.wait["RABots"][target] = True
                                    f=codecs.open('RAwait.json','w','utf-8')
                                    json.dump(self.wait, f, sort_keys=True, indent=4,ensure_ascii=False)
                                    cl.sendText(msg.to,"Masuk kedalam keluarga")
                                except Exception as e:
                                    cl.sendText(msg.to,"Erorr.....")
                                    
                elif RAKey + "cuekinbot" in msg.text:
                    if msg.from_ in RASadmin:
                        key = eval(msg.contentMetadata["MENTION"])
                        key["MENTIONEES"][0]["M"]
                        targets = []
                        for x in key["MENTIONEES"]:
                            targets.append(x["M"])
                        for target in targets:    
                            if target not in self.wait["RABots"]:
                                cl.sendText(msg.to,"Sudah dihapus...")
                                pass
                            else:
                                try:
                                    del self.wait["RABots"][target]
                                    f=codecs.open('RAwait.json','w','utf-8')
                                    json.dump(self.wait, f, sort_keys=True, indent=4,ensure_ascii=False)
                                    cl.sendText(msg.to,"Dihapus dari listbot")
                                except Exception as e:
                                    cl.sendText(msg.to,"Erorr...")                    
                                    
                elif msg.text == self.resp +"listbl":
                    if msg.from_ in RASadmin or msg.from_ in self.wait["RAAdmin"] or msg.from_ in self.wait["RAStaff"]:
                        if self.wait["RAblacklist"] == {}:
                            cl.sendText(msg.to,"Tidak ada akun terblacklist")
                        else:
                            mc = "『User "
                            num=1
                            ragets = cl.getContacts(self.wait["RAblacklist"])
                            for mi_d in ragets:
                                mc+="\n%i. %s" % (num, mi_d.displayName)
                                num=(num+1)
                            mc+="\n\n Total %i Blacklist』 " % len(ragets)     
                            cl.sendText(msg.to, mc)
                            
                elif msg.text == self.resp +"listteam":
                    if msg.from_ in RASadmin or msg.from_ in self.wait["RAAdmin"] or msg.from_ in self.wait["RAStaff"]:
                        ma = ""
                        mb = ""
                        mc = ""
                        a = 0
                        b = 0
                        c = 0
                        for m_id in RASadmin:
                            a = a + 1
                            end = '\n'
                            ma += str(a) + ". " +cl.getContact(m_id).displayName + "\n"
                        for m_id in self.wait["RAAdmin"]:
                            b = b + 1
                            end = '\n'
                            mb += str(b) + ". " +cl.getContact(m_id).displayName + "\n"
                        for m_id in self.wait["RAStaff"]:
                            c = c + 1
                            end = '\n'
                            mc += str(c) + ". " +cl.getContact(m_id).displayName + "\n"
                        cl.sendText(msg.to,"🔰 |RA| Family:\n\nSuper admin:\n"+ma+"\nAdmin:\n"+mb+"\nStaff:\n"+mc+"\n\n『%s』 Bergabung menjadi family" %(str(len(RASadmin)+len(self.wait["RAStaff"])+len(self.wait["RAAdmin"]))))
                        
                elif msg.text == self.resp +"listbot":
                    if msg.from_ in RASadmin or msg.from_ in self.wait["RAAdmin"] or msg.from_ in self.wait["RAStaff"]:
                        if self.wait["RABots"] == {}:
                            cl.sendText(msg.to,"List bot kosong")
                        else:
                            mc = "『User "
                            num=1
                            ragets = cl.getContacts(self.wait["RABots"])
                            for mi_d in ragets:
                                mc+="\n%i. %s" % (num, mi_d.displayName)
                                num=(num+1)
                            mc+="\n\n Total %i botline』 " % len(ragets)     
                            cl.sendText(msg.to, mc)
                            
                elif msg.text == self.resp +"cancel":
                    if msg.from_ in RASadmin or msg.from_ in self.wait["RAAdmin"] or msg.from_ in self.wait["RAStaff"]:
                        if msg.toType == 2:
                            group = cl.getGroup(msg.to)
                            gMembMids = [contact.mid for contact in group.invitee]
                            for _mid in gMembMids:
                                cl.cancelGroupInvitation(msg.to,[_mid])
                            else:
                                cl.sendText(msg.to,"Selesai cancel member")
                                
                elif msg.text == self.resp +"listprotect":
                    if msg.from_ in RASadmin or msg.from_ in self.wait["RAAdmin"]:
                        ma = ""
                        a = 0
                        mb = ""
                        b = 0
                        mc = ""
                        c = 0
                        md = ""
                        d = 0
                        gid = self.RAset["RAprotinvite"]
                        for group in gid:
                            G = cl.getGroup(group)
                            a = a + 1
                            end = "\n"
                            ma += str(a) + ". " +G.name+ "\n"
                        gid = self.RAset["RAprotqr"]
                        for group in gid:
                            G = cl.getGroup(group)
                            b = b + 1
                            end = "\n"
                            mb += str(b) + ". " +G.name+ "\n"
                        gid = self.RAset["RAprotcancel"]
                        for group in gid:
                            G = cl.getGroup(group)
                            c = c + 1
                            end = "\n"
                            mc += str(c) + ". " +G.name+ "\n"
                        gid = self.RAset["RAprotkick"]
                        for group in gid:
                            G = cl.getGroup(group)
                            d = d + 1
                            end = "\n"
                            md += str(d) + ". " +G.name+ "\n"
                        cl.sendText(msg.to,"🔰Listprotect\n\nProtect Invite:\n"+ma+"\nProtect Ourl:\n"+mb+"\nProtect Cancel:\n"+mc+"\nProtect Kick:\n"+md)    
                                
                        
                        
                                
                elif msg.text == self.resp +"sprespon":
                    if msg.from_ in RASadmin or msg.from_ in self.wait["RAAdmin"] or msg.from_ in self.wait["RAStaff"]:
                        get_profile_time_start = time.time()
                        get_profile = cl.getProfile()
                        get_profile_time = time.time() - get_profile_time_start
                        get_group_time_start = time.time()
                        get_group = cl.getGroupIdsJoined()
                        get_group_time = time.time() - get_group_time_start
                        get_contact_time_start = time.time()
                        get_contact = cl.getContact(self.mid)
                        get_contact_time = time.time() - get_contact_time_start
                        cl.sendText(msg.to, "「speed respon」\n + Get Profile\n   %.10f\n + Get Contact\n   %.10f\n + Get Group\n   %.10f" % (get_profile_time/3,get_contact_time/3,get_group_time/3))
                    
                elif RAKey +"masukin" in msg.text:
                    if msg.from_ in RASadmin:
                        gs = cl.getGroup(msg.to)
                        targets = []
                        for x in gs.members:
                            targets.append(x.mid)
                        for a in self.wait["RABots"]:
                            if a in targets:
                                try:
                                    targets.remove(a)
                                except:
                                    pass
                        cl.sendText(msg.to,"Sudah masuk kedalam list")
                        for target in targets:
                            if target not in RASadmin:
                                if target not in self.wait["RAAdmin"]:
                                    if target not in self.wait["RAStaff"]:
                                        try:
                                            self.wait["RABots"][target] = True
                                            f=codecs.open('RAwait.json','w','utf-8')
                                            json.dump(self.wait, f, sort_keys=True, indent=4,ensure_ascii=False)
                                            cl.sendText(msg.to,"Berhasil..")
                                        except:
                                            pass    
        #---------------------- Multy Command ------------------------#
                
                elif msg.text == RAKey +'absen':
                    if msg.from_ in RASadmin or msg.from_ in self.wait["RAAdmin"] or msg.from_ in self.wait["RAStaff"]:
                        profile = cl.getProfile()
                        text = profile.displayName + ""
                        cl.sendText(msg.to, text)
                
                elif msg.text == RAKey + 'spbot':
                    if msg.from_ in RASadmin or msg.from_ in self.wait["RAAdmin"] or msg.from_ in self.wait["RAStaff"]:
                        start = time.time()
                        cl.sendText("u3b07c57b6239e5216aa4c7a02687c86d", 'kuota blum masuk 30GB tsel')
                        cl.sendText(msg.to, '%s Detik' % (time.time()-start))
                    
                elif RAKey +"cname " in msg.text:
                    if msg.from_ in RASadmin:
                        string = msg.text.replace(RAKey + "cname ","")
                        profile_B = cl.getProfile()
                        profile_B.displayName = string
                        cl.updateProfile(profile_B)
                        cl.sendText(msg.to,"Berubah Menjadi " + string)
                            
                elif RAKey +"cbio " in msg.text:
                    if msg.from_ in RASadmin:
                        string = msg.text.replace(RAKey + "cbio ","")
                        profile_B = cl.getProfile()
                        profile_B.statusMessage = string
                        cl.updateProfile(profile_B)
                        cl.sendText(msg.to,"Berubah Menjadi " + string)
                            
                elif msg.text == RAKey +"cfoto":
                    if msg.from_ in RASadmin:
                        self.RAset["RAfoto"][msg.to] = True
                        cl.sendText(msg.to,"Kirim foto.....")
                        
                elif msg.text == RAKey +'cleanblacklist':
                    if msg.from_ in RASadmin or msg.from_ in self.wait["RAAdmin"] or msg.from_ in self.wait["RAStaff"]:
                        group = cl.getGroup(msg.to)
                        gMembMids = [contact.mid for contact in group.members]
                        matched_list = []
                        if matched_list != []:
                            cl.sendText(msg.to,"Blacklisted contact noticed...")
                            cl.sendText(msg.to,"Begin Kicking contact")
                        for tag in self.wait["RAblacklist"]:
                            matched_list+=filter(lambda str: str == tag, gMembMids)
                        if matched_list == []:
                            cl.sendText(msg.to,"It looks empty here.")
                            return
                        for jj in matched_list:
                            cl.kickoutFromGroup(msg.to,[jj])
                
                elif msg.text == RAKey +'byeall':
                    if msg.from_ in RASadmin or msg.from_ in self.wait["RAAdmin"] or msg.from_ in self.wait["RAStaff"]:
                        if msg.toType == 2:
                            x = cl.getGroup(msg.to)
                            cl.leaveGroup(msg.to)
                            
                elif msg.text == RAKey +'leaveall':
                    if msg.from_ in RASadmin:
                        gid = cl.getGroupIdsJoined()
                        for i in gid:
                            cl.sendText(i,"Silahkan admin/staff invite kembali")
                            cl.leaveGroup(i)
                            
                elif RAKey + "cleanmember" in msg.text:
                    if msg.from_ in RASadmin:
                        gs = cl.getGroup(msg.to)
                        targets = []
                        for x in gs.members:
                            targets.append(x.mid)
                        for a in self.wait["RABots"]:
                            if a in targets:
                                try:
                                    targets.remove(a)
                                except:
                                    pass
                        for b in self.wait["RAAdmin"]:
                            if b in targets:
                                try:
                                    targets.remove(b)
                                except:
                                    pass
                        for c in RASadmin:
                            if c in targets:
                                try:
                                    targets.remove(c)
                                except:
                                    pass
                        for d in self.wait["RAStaff"]:
                            if d in targets:
                                try:
                                    targets.remove(d)
                                except:
                                    pass
                        cl.sendText(msg.to,"Byebye")
                        for target in targets:
                            try:
                                cl.kickoutFromGroup(msg.to,[target])
                            except:
                                pass            
                    
                elif msg.text == RAKey +'friend':
                    if msg.from_ in RASadmin:
                        ragets = cl.getAllContactIds()
                        racekcontact = cl.getContacts(ragets)
                        num=1
                        msgs=""
                        for ids in racekcontact:
                            msgs+="\n%i. %s" % (num, ids.displayName)
                            num=(num+1)
                        msgs+="\n\n「Total %i Friend's」 " % len(racekcontact)
                        cl.sendText(msg.to, msgs)
                        
                elif msg.text == RAKey +"spam ":
                    if msg.from_ in RASadmin or msg.from_ in self.wait["RAAdmin"]:
                        spm = msg.text.replace(self.resp + "spam ","")
                        sspm = spm.split()
                        midd = sspm[0]
                        jumlah = int(sspm[1])
                        if jumlah <= 100:
                            for var in range(0,jumlah):
                                if (self.wait["RAmessage"] in [" "," ","\n",None]):
                                    pass
                                else:
                                    cl.findAndAddContactsByMid(midd)
                                    cl.sendText(midd,str(self.wait["RAmessage"]))
                                    
                elif msg.text == RAKey + 'restart':
                    if msg.from_ in RASadmin:
                        cl.sendText(msg.to,"Tunggu Sebentar..")
                        python3 = sys.executable
                        os.execl(python3, python3, *sys.argv)
                
                elif msg.text == RAKey + 'removechat':
                    if msg.from_ in RASadmin:
                        try:
                            cl.removeAllMessages(op.param2)
                            cl.sendText(msg.to,"Chat Bersih....")
                        except:
                            pass
                                    
                elif RAKey +'leave ' in msg.text:
                    if msg.from_ in RASadmin:
                        ng = msg.text.replace(RAKey + 'leave ','')
                        gid = cl.getGroupIdsJoined()
                        for i in gid:
                            h = cl.getGroup(i).name
                            if h == ng:
                                cl.leaveGroup(i)
                    
                        
        #---------------------- Mix Command ------------------------#
        
                elif self.resp + "limit " in msg.text:
                    if msg.from_ in RASadmin or msg.from_ in self.wait["RAAdmin"] or msg.from_ in self.wait["RAStaff"]:
                        strnum = msg.text.replace(self.resp + "limit ","")
                        num =  int(strnum)
                        self.wait["RAlimit"] = num
                        cl.sendText(msg.to,"Total Diubah Menjadi " +strnum)
                        
                elif self.resp + "sc " in msg.text:
                    if msg.from_ in RASadmin or msg.from_ in self.wait["RAAdmin"] or msg.from_ in self.wait["RAStaff"]:
                        if 'MENTION' in msg.contentMetadata.keys()!=None:
                            key = eval(msg.contentMetadata["MENTION"])
                            key1 = key["MENTIONEES"][0]["M"]
                            jmlh = int(self.wait["RAlimit"])
                            if jmlh <= 1000:
                                for x in range(jmlh):
                                    try:
                                        msg.contentType = 13
                                        msg.contentMetadata = {'mid': key1}
                                        cl.sendMessage1(msg)
                                    except Exception as e:
                                        cl.sendText(msg.to,str(e))
                            else:
                                cl.sendText(msg.to,"Jumlah melebihi 1000")             
                elif self.resp + "panggil " in msg.text:
                    if msg.from_ in RASadmin or msg.from_ in self.wait["RAAdmin"] or msg.from_ in self.wait["RAStaff"]:
                        if 'MENTION' in msg.contentMetadata.keys()!=None:
                            key = eval(msg.contentMetadata["MENTION"])
                            key1 = key["MENTIONEES"][0]["M"]
                            zx = ""
                            zxc = " "
                            zx2 = []
                            pesan2 = "@a"" "
                            xlen = str(len(zxc))
                            xlen2 = str(len(zxc)+len(pesan2)-1)
                            zx = {'S':xlen, 'E':xlen2, 'M':key1}
                            zx2.append(zx)
                            zxc += pesan2
                            msg.contentType = 0
                            msg.text = zxc
                            lol = {'MENTION':str('{"MENTIONEES":'+json.dumps(zx2).replace(' ','')+'}')}
                            msg.contentMetadata = lol
                            jmlh = int(self.wait["RAlimit"])
                            if jmlh <= 1000:
                                for x in range(jmlh):
                                    try:
                                        cl.sendMessage1(msg)
                                    except Exception as e:
                                        cl.sendText(msg.to,str(e))
                            else:            
                                cl.sendText(msg.to,"Jumlah melebihi 1000")            
                                    
                            
                elif self.resp + "cek" in msg.text:
                    key = eval(msg.contentMetadata["MENTION"])
                    key1 = key["MENTIONEES"][0]["M"]
                    contact = cl.getContact(key1)
                    try:
                        path = "http://dl.profile.line-cdn.net/" + contact.pictureStatus
                        cl.sendImageWithURL(msg.to,path)
                        cl.sendText(msg.to,"[Name]\n" + contact.displayName + "\n\n[Mid]\n" + contact.mid + "\n\n[Status message]\n" + contact.statusMessage)
                    except:
                        path = "http://dl.profile.line-cdn.net/" + contact.pictureStatus
                        cl.sendImageWithURL(msg.to,path)
                        cl.sendText(msg.to,"[Name]\n" + contact.displayName + "\n\n[Mid]\n" + contact.mid + "\n\n[Status message]\n" + contact.statusMessage)
                        
                elif msg.text == self.resp +"gid":
                    cl.sendText(msg.to,msg.to)
                    
                elif msg.text == self.resp +"yid":
                    cl.sendText(msg.to,msg.from_)
                    
                elif msg.text == self.resp +"lastseen on":
                    self.RAset['RAreadPoint'][msg.to] = msg.id
                    self.RAset['RAreadMember'][msg.to] = {}
                    cl.sendText(msg.to, "lastseen diaktifkan")
                    
                elif msg.text == self.resp +"lastseen off":
                    del self.RAset['RAreadPoint'][msg.to]
                    del self.RAset['RAreadMember'][msg.to]
                    cl.sendText(msg.to, "lastseen dinonaktifkan")
                    
                elif msg.text == self.resp +"lastseens":
                    if msg.to in self.RAset['RAreadPoint']:
                        if self.RAset['RAreadMember'][msg.to] != {}:
                            aa = []
                            for x in self.RAset['RAreadMember'][msg.to]:
                                aa.append(x)
                            try:
                                arrData = ""
                                textx = "     [ Result {} lastseen ]    \n1. ".format(str(len(aa))) 
                                arr = []
                                no = 1
                                b = 1
                                for i in aa:
                                    b = b + 1
                                    end = "\n"
                                    mention = "@x\n"
                                    slen = str(len(textx))
                                    elen = str(len(textx) + len(mention) - 1)
                                    arrData = {'S':slen, 'E':elen, 'M':i}
                                    arr.append(arrData)
                                    textx += mention
                                    if no < len(aa):
                                        no += 1
                                        textx += str(b) + ". "
                                    else:
                                        try:
                                            no = "[ {} ]".format(str(cl.getGroup(msg.to).name))
                                        except:
                                            no = "  "
                                msg.to = msg.to
                                msg.text = textx
                                msg.contentMetadata = {'MENTION': str('{"MENTIONEES":' + json.dumps(arr) + '}')}
                                msg.contentType = 0
                                cl.sendMessage1(msg)
                            except:
                                pass
                            try:
                                del self.RAset['RAreadPoint'][msg.to]
                                del self.RAset['RAreadMember'][msg.to]
                            except:
                                pass
                            self.RAset['RAreadPoint'][msg.to] = msg.id
                            self.RAset['RAreadMember'][msg.to] = {}
                        else:
                            cl.sendText(msg.to, "User kosong...")
                    else:
                        cl.sendText(msg.to, "aktifkan lastseen")
        
                elif msg.text == self.resp +"tagall":
                    group = cl.getGroup(msg.to)
                    k = len(group.members)//100
                    for j in range(k+1):
                        aa = []
                        for x in group.members:
                            aa.append(x.mid)
                        try:
                            arrData = ""
                            textx = "     [ Mention {} Members ]    \n1. ".format(str(len(aa)))
                            arr = []
                            no = 1
                            b = 1
                            for i in aa:
                                b = b + 1
                                end = "\n"
                                mention = "@x\n"
                                slen = str(len(textx))
                                elen = str(len(textx) + len(mention) - 1)
                                arrData = {'S':slen, 'E':elen, 'M':i}
                                arr.append(arrData)
                                textx += mention
                                if no < len(aa):
                                    no += 1
                                    textx += str(b) + ". "
                                else:
                                    try:
                                        no = "[ {} ]".format(str(cl.getGroup(msg.to).name))

                                    except:
                                        no = " "
                            msg.to = msg.to
                            msg.text = textx
                            msg.contentMetadata = {'MENTION': str('{"MENTIONEES":' + json.dumps(arr) + '}')}
                            msg.contentType = 0
                            cl.sendMessage1(msg)
                        except Exception as e:
                            cl.sendText(msg.to,str(e))
                            
                elif self.resp + 'yt-video ' in msg.text:
                    try:
                        textToSearch = (msg.text).replace(self.resp + 'yt-video ', "").strip()
                        query = urllib.parse.quote(textToSearch)
                        url = "https://www.youtube.com/results?search_query=" + query
                        response = urllib.request.urlopen(url)
                        html = response.read()
                        soup = BeautifulSoup(html, "html.parser")
                        results = soup.find(attrs={'class':'yt-uix-tile-link'})
                        dl = 'https://www.youtube.com' + results['href']
                        start = timeit.timeit()
                        vid = pafy.new(dl)
                        stream = vid.streams
                        for s in stream:
                            vin = s.url
                            hasil = vid.title
                            hasil += '\n\nPenulis : ' +str(vid.author)
                            hasil += '\nDurasi   : ' +str(vid.duration)+ ' (' +s.quality+ ') '
                            hasil += '\nRating   : ' +str(vid.rating)
                            hasil += '\nDitonton    : ' +str(vid.viewcount)+ 'x '
                            hasil += '\nDiterbitkan : ' +vid.published
                            hasil += '\n\nTime taken : %s' % (start)
                            hasil += '\n\n Tunggu encoding selesai...'
                        cl.sendVideoWithURL(msg.to,vin)
                        cl.sendText(msg.to,hasil)
                    except:
                        cl.sendText(msg.to,"Informasi video gagal di cari")
                        
                elif self.resp + 'yt-mp3 ' in msg.text:
                    try:
                        textToSearch = (msg.text).replace(self.resp + 'yt-mp3 ', "").strip()
                        query = urllib.parse.quote(textToSearch)
                        url = "https://www.youtube.com/results?search_query=" + query
                        response = urllib.request.urlopen(url)
                        html = response.read()
                        soup = BeautifulSoup(html, "html.parser")
                        results = soup.find(attrs={'class':'yt-uix-tile-link'})
                        dl = 'https://www.youtube.com' + results['href']
                        start = timeit.timeit()
                        vid = pafy.new(dl)
                        stream = vid.audiostreams
                        for s in stream:
                            vin = s.url
                            path = vid.bigthumbhd
                            hasil = vid.title
                            hasil += '\n\nPenulis : ' +str(vid.author)
                            hasil += '\nDurasi   : ' +str(vid.duration)+ ' (' +s.quality+ ') '
                            hasil += '\nRating   : ' +str(vid.rating)
                            hasil += '\nDitonton    : ' +str(vid.viewcount)+ 'x '
                            hasil += '\nDiterbitkan : ' +vid.published
                            hasil += '\n\nTime taken : %s' % (start)
                            hasil += '\n\n Tunggu encoding selesai...'
                        cl.sendImageWithURL(msg.to, str(path))    
                        cl.sendAudioWithURL(msg.to,vin)
                        cl.sendText(msg.to,hasil)
                    except:
                        cl.sendText(msg.to,"Informasi Audio gagal di cari")
                        
                elif self.resp + 'film ' in msg.text:
                    proses = msg.text.replace(self.resp +'film ','')
                    prosess = proses.split()
                    title = prosess[0]
                    tahun = prosess[1]
                    r = requests.get('http://www.omdbapi.com/?t='+title+'&y='+tahun+'&plot=full&apikey=4bdd1d70')
                    start = timeit.timeit()
                    data=r.text
                    data=json.loads(data)
                    hasil = "Informasi \n" +str(data["Title"])+ " (" +str(data["Year"])+ ")"
                    hasil += "\n\n " +str(data["Plot"])
                    hasil += "\n\nDirector : " +str(data["Director"])
                    hasil += "\nActors   : " +str(data["Actors"])
                    hasil += "\nRelease : " +str(data["Released"])
                    hasil += "\nGenre    : " +str(data["Genre"])
                    hasil += "\nRuntime   : " +str(data["Runtime"])
                    path = data["Poster"]
                    cl.sendImageWithURL(msg.to, str(path))
                    cl.sendText(msg.to,hasil)
                    
                elif self.resp + 'get-ig ' in msg.text:
                    instagram = msg.text.replace(self.resp +'get-ig ','')
                    html = requests.get('https://www.instagram.com/' + instagram + '/')
                    soup = BeautifulSoup(html.text, 'html5lib')
                    data = soup.find_all('meta', attrs={'property':'og:description'})
                    text = data[0].get('content').split()
                    data1 = soup.find_all('meta', attrs={'property':'og:image'})
                    text1 = data1[0].get('content').split()
                    user = "Name: " + text[-2] + "\n"
                    user1 = "Username: " + text[-1] + "\n"
                    followers = "Followers: " + text[0] + "\n"
                    following = "Following: " + text[2] + "\n"
                    post = "Post: " + text[4] + "\n"
                    link = "Link: " + "https://instagram.com/" + instagram
                    cl.sendImageWithURL(msg.to, text1[0])
                    cl.sendText(msg.to, user + user1 + followers + following + post + link)
                    
                elif self.resp + 'igpost ' in msg.text:
                    instagram = msg.text.replace(self.resp +'igpost ','')
                    ig = instagram.split()
                    username = ig[0]
                    ke = ig[1]
                    r = requests.get('http://rahandiapi.herokuapp.com/instapost/'+username+'/'+ke+'?key=betakey', verify=True)
                    media = r.text
                    media = json.loads(media)
                    start = timeit.timeit()
                    hasil = "Informasi Post Instagram"
                    hasil += "\n\nLike       : " +str(media["media"]["like_count"])
                    hasil += "\nComment : " +str(media["media"]["comment_count"])
                    hasil += "\nCaption : \n\n" +str(media["media"]["caption"])
                    hasil += '\n\nTime taken : %s' % (start)
                    path = media["media"]["url"]
                    cl.sendImageWithURL(msg.to,path)
                    cl.sendText(msg.to,hasil)
                    
                #elif self.resp + 'igstory ' in msg.text:
                #    instagram = msg.text.replace(self.resp +'story ','')
                #    r = requests.get('http://rahandiapi.herokuapp.com/instastory/'+instagram'?key=betakey', verify=True)
                    
                    
                    
                elif self.resp + 'wsholat ' in msg.text:
                    location = msg.text.replace(self.resp +'wsholat ','')
                    with requests.session() as web:
                        web.headers["User-Agent"] = "Mozilla/5.0 (Windows NT 6.2; WOW64; rv:5.0) Gecko/20100101 Firefox/5.0"
                        r = web.get("http://api.corrykalam.net/apisholat.php?lokasi={}".format(urllib.parse.quote(location)))
                        data = r.text
                        data = json.loads(data)
                        if data[1] != "Subuh : " and data[2] != "Dzuhur : " and data[3] != "Ashr : " and data[4] != "Maghrib : " and data[5] != "Isha : ":
                            hasil = "Informasi Jadwal Sholat"
                            hasil += "\n\n╠ " + data[1]
                            hasil += "\n╠ " + data[2]
                            hasil += "\n╠ " + data[3]
                            hasil += "\n╠ " + data[4]
                            hasil += "\n╠ " + data[5]
                            hasil += "\n╠ Lokasi : " + data[0]
                            hasil += "\n "
                        else:
                            hasil = "Lokasi tidak ditemukan"
                        cl.sendText(msg.to, str(hasil))
                        
                elif self.resp + 'ccuaca ' in msg.text:
                    location = msg.text.replace(self.resp +'ccuaca ','')
                    with requests.session() as web:
                        web.headers["User-Agent"] = "Mozilla/5.0 (Windows NT 6.2; WOW64; rv:5.0) Gecko/20100101 Firefox/5.0"
                        r = web.get("http://api.corrykalam.net/apicuaca.php?kota={}".format(urllib.parse.quote(location)))
                        data = r.text
                        data = json.loads(data)
                        if "result" not in data:
                            hasil = "Informasi Cuaca"
                            hasil += "\n\n╠ Lokasi : " + data[0].replace("Temperatur di kota ","")
                            hasil += "\n╠ Suhu   : " + data[1].replace("Suhu : ","")
                            hasil += "\n╠ Kelembaban     : " + data[2].replace("Kelembaban : ","")
                            hasil += "\n╠ Tekanan Udara : " + data[3].replace("Tekanan udara : ","")
                            hasil += "\n╠ Kecepatan Angin : " + data[4].replace("Kecepatan angin : ","")
                            hasil += "\n "
                        else:
                            hasil = "Lokasi tidak ditemukan"
                        cl.sendText(msg.to, str(hasil))
                        
                elif self.resp + 'clokasi ' in msg.text:
                    location = msg.text.replace(self.resp +'clokasi ','')
                    with requests.session() as web:
                        web.headers["User-Agent"] = "Mozilla/5.0 (Windows NT 6.2; WOW64; rv:5.0) Gecko/20100101 Firefox/5.0"
                        r = web.get("http://api.corrykalam.net/apiloc.php?lokasi={}".format(urllib.parse.quote(location)))
                        data = r.text
                        data = json.loads(data)
                        if data[0] != "" and data[1] != "" and data[2] != "":
                            link = "https://www.google.co.id/maps/@{},{},15z".format(str(data[1]), str(data[2]))
                            hasil = "Informasi Lokasi"
                            hasil += "\n\n╠ Lokasi      : " + data[0]
                            hasil += "\n╠ Google Maps : " + link
                            hasil += "\n "
                        else:
                            hasil = "Lokasi tidak ditemukan"
                        cl.sendText(msg.to, str(hasil))
                    
                elif '/ti/g/' in msg.text.lower():
                    if msg.from_ in RASadmin or msg.from_ in self.wait["RAAdmin"] or msg.from_ in self.wait["RAStaff"]:
                        link_re = re.compile('(?:line\:\/|line\.me\/R)\/ti\/g\/([a-zA-Z0-9_-]+)?')
                        links = link_re.findall(msg.text)
                        n_links=[]
                        for l in links:
                            if l not in n_links:
                                n_links.append(l)
                        for ticket_id in n_links:
                            if self.wait["RAautojoin"] == True:
                                group=cl.findGroupByTicket(ticket_id)
                                cl.acceptGroupInvitationByTicket(group.id,ticket_id)
                                cl.sendText(msg.to,"Masuk %s" % str(group.name))
                    
                            
                    
                            
        except Exception as e:
            print(e)
                            
        
