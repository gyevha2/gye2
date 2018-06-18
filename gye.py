# -*- coding: utf-8 -*-

from gyevha import *
from datetime import datetime
from time import sleep
from bs4 import BeautifulSoup
from humanfriendly import format_timespan, format_size, format_number, format_length
import time, random, sys, json, codecs, threading, glob, re, string, os, requests, subprocess, six, ast, pytz, urllib, urllib.parse
from gtts import gTTS
from googletrans import Translator
#==============================================================================#
botStart = time.time()

gye = LINE()
ais = LINE()

KAC = [gye,ais]
GUE = [gye,ais] # ini jangan luh hapus peak inj fungsi Ciak alias kick
#maksudnya agak bot sb/induk gak ikutan nge kick Mudeng ora
gyeMID = gye.profile.mid
aisMID = ais.profile.mid

Bots = [gyeMID,aisMID]
creator = ["u2821289b2f0cb7ba14e19c92bdbcfacc"]
Owner = ["u2821289b2f0cb7ba14e19c92bdbcfacc"]                
admin = ["u2821289b2f0cb7ba14e19c92bdbcfacc"]

gyeProfile = gye.getProfile()
aisProfile = ais.getProfile()

lineSettings = gye.getSettings()
aisSettings = ais.getSettings()

oepoll = OEPoll(gye)
oepoll1 = OEPoll(ais)

responsename = gye.getProfile().displayName
responsename1 = ais.getProfile().displayName
#==============================================================================#




with open('Owner.json', 'r') as fp:
    Owner = json.load(fp)
    
with open('admin.json', 'r') as fp:
    admin = json.load(fp)
    
myProfile = {
	"displayName": "",
	"statusMessage": "",
	"pictureStatus": ""
}

myProfile["displayName"] = gyeProfile.displayName
myProfile["statusMessage"] = gyeProfile.statusMessage
myProfile["pictureStatus"] = gyeProfile.pictureStatus

readOpen = codecs.open("read.json","r","utf-8")
settingsOpen = codecs.open("temp.json","r","utf-8")

#==============================================================================#

read = json.load(readOpen)
settings = json.load(settingsOpen)

def restartBot():
    print ("[ INFO ] BOT RESETTED")
    backupData()
    python = sys.executable
    os.execl(python, python, *sys.argv)
    
def logError(text):
    gye.log("[ Suscsses ] " + str(text))
    time_ = datetime.now()
    with open("errorLog.txt","a") as error:
        error.write("\n[%s] %s" % (str(time), text))
        
def sendMessageWithMention(to, mid):
    try:
        aa = '{"S":"0","E":"3","M":'+json.dumps(mid)+'}'
        text_ = '@x '
        gye.sendMessage(to, text_, contentMetadata={'MENTION':'{"MENTIONEES":['+aa+']}'}, contentType=0)
    except Exception as error:
        logError(error)
        
def helpmessage():
    helpMessage = "╭════════╬🔛╬════════╮" + "\n" + \
                  "║͜͡☆➣ Ǥﾘ乇 Џんﾑ 乃Ծｲ丂" + "\n" + \
                  "╰════════╬🔛╬════════╯" + "\n" + \
                  "╭════════╬🔛╬════════╮" + "\n" + \
                  "║͜͡☆➣ HELP" + "\n" + \
                  "╰════════╬🔛╬════════╯" + "\n" + \
                  "╭════════╬🔛╬════════╮" + "\n" + \
                  "║͜͡☆➣☯ Help 1" + "\n" + \
                  "║͜͡☆➣☯ Help 2" + "\n" + \
                  "║͜͡☆➣☯ Tag" + "\n" + \
                  "║͜͡☆➣☯ Halo ( panggil bot ) " + "\n" + \
                  "║͜͡☆➣☯ Absen" + "\n" + \
                  "║͜͡☆➣☯ @pamit ( keluar Semua ) " + "\n" + \
                  "║͜͡☆➣☯ Balik ( usir bot ) " + "\n" + \
                  "║͜͡☆➣☯ Bye " + "\n" + \
                  "║͜͡☆➣☯ Cekk ( cek semua bot )" + "\n" + \
                  "║͜͡☆➣☯ Me" + "\n" + \
                  "║͜͡☆➣☯  Sp" + "\n" + \
                  "║͜͡☆➣☯ Status" + "\n" + \
                  "║͜͡☆➣☯ Ciak @" + "\n" + \
                  "║͜͡☆➣☯ Kickallmember" + "\n" + \
                  "╰════════╬🔛╬════════╯" + "\n" + \
                  "╭════════╬🔛╬════════╮" + "\n" + \
                  "║͜͡☆➣ Ǥﾘ乇 Џんﾑ 乃Ծｲ丂" + "\n" + \
                  "╰════════╬🔛╬════════╯"
    return helpMessage
    
def helptexttospeech():
    helpTextToSpeech =   "╭════════╬🔛╬════════╮" + "\n" + \
                  "║͜͡☆➣ Ǥﾘ乇 Џんﾑ 乃Ծｲ丂" + "\n" + \
                  "╰════════╬🔛╬════════╯" + "\n" + \
                  "╭════════╬🔛╬════════╮" + "\n" + \
                  "║͜͡☆➣ HELP1" + "\n" + \
                  "╰════════╬🔛╬════════╯" + "\n" + \
                  "╭════════╬🔛╬════════╮" + "\n" + \
                  "║͜͡☆➣☯ Help 1" + "\n" + \
                  "║͜͡☆➣☯ Help 2" + "\n" + \
                  "║͜͡☆➣☯ Protect on/off" + "\n" + \
                  "║͜͡☆➣☯ QrProtect on/off" + "\n" + \
                  "║͜͡☆➣☯ InviteProtect on/off" + "\n" + \
                  "║͜͡☆➣☯ CancelProtect on/off" + "\n" + \
                  "║͜͡☆➣☯ AutoAdd on/off" + "\n" + \
                  "║͜͡☆➣☯ AutoJoin on/off" + "\n" + \
                  "║͜͡☆➣☯ AutoLeave on/off" + "\n" + \
                  "║͜͡☆➣☯ CheckSticker on/off" + "\n" + \
                  "║͜͡☆➣☯ AutoRead on/off" + "\n" + \
                  "║͜͡☆➣☯ DetectMention on/off" + "\n" + \
                  "║͜͡☆➣☯ Join link on/off" + "\n" + \
                  "║͜͡☆➣☯ GroupCreator" + "\n" + \
                  "║͜͡☆➣☯ GroupId" + "\n" + \
                  "║͜͡☆➣☯ GroupName" + "\n" + \
                  "║͜͡☆➣☯ GroupPicture" + "\n" + \
                  "║͜͡☆➣☯ GroupList" + "\n" + \
                  "║͜͡☆➣☯ GroupMemberList" + "\n" + \
                  "║͜͡☆➣☯ GroupInfo" + "\n" + \
                  "║͜͡☆➣☯ Gt" + "\n" + \
                  "║͜͡☆➣☯ Gt on/off" + "\n" + \
                  "║͜͡☆➣☯ Mimic on" + "\n" + \
                  "║͜͡☆➣☯ Mimic off" + "\n" + \
                  "║͜͡☆➣☯ MimicAdd" + "\n" + \
                  "║͜͡☆➣☯ MimicDel" + "\n" + \
                  "║͜͡☆➣☯ Lurking on/off" + "\n" + \
                  "║͜͡☆➣☯ Lurking" + "\n" + \
                  "╰════════╬🔛╬════════╯" + "\n" + \
                  "╭════════╬🔛╬════════╮" + "\n" + \
                  "║͜͡☆➣ Ǥﾘ乇 Џんﾑ 乃Ծｲ丂" + "\n" + \
                  "╰════════╬🔛╬════════╯"
    return helpTextToSpeech
    
def helptranslate():
    helpTranslate =    "╭════════╬🔛╬════════╮" + "\n" + \
                  "║͜͡☆➣ Ǥﾘ乇 Џんﾑ 乃Ծｲ丂" + "\n" + \
                  "╰════════╬🔛╬════════╯" + "\n" + \
                  "╭════════╬🔛╬════════╮" + "\n" + \
                  "║͜͡☆➣ HELP2" + "\n" + \
                  "╰════════╬🔛╬════════╯" + "\n" + \
                  "╭════════╬🔛╬════════╮" + "\n" + \
                  "║͜͡☆➣☯ AdminLit" + "\n" + \
                  "║͜͡☆➣☯ OwnerList" + "\n" + \
                  "║͜͡☆➣☯ BanContact" + "\n" + \
                  "║͜͡☆➣☯ UnbanContact" + "\n" + \
                  "║͜͡☆➣☯ BanList" + "\n" + \
                  "║͜͡☆➣☯ Clearban" + "\n" + \
                  "║͜͡☆➣☯ Restart" + "\n" + \
                  "║͜͡☆➣☯ About" + "\n" + \
                  "║͜͡☆➣☯ Me" + "\n" + \
                  "║͜͡☆➣☯ MyMid" + "\n" + \
                  "║͜͡☆➣☯ Midnya @" + "\n" + \
                  "║͜͡☆➣☯ MyName" + "\n" + \
                  "║͜͡☆➣☯MyBio" + "\n" + \
                  "║͜͡☆➣☯MyPicture" + "\n" + \
                  "║͜͡☆➣☯ MyVideoProfile" + "\n" + \
                  "║͜͡☆➣☯MyCover" + "\n" + \
                  "║͜͡☆➣☯ StealContact @" + "\n" + \
                  "║͜͡☆➣☯ StealMid @" + "\n" + \
                  "║͜͡☆➣☯ StealName「Mention」" + "\n" + \
                  "║͜͡☆➣☯ StealBio @" + "\n" + \
                  "║͜͡☆➣☯ StealPicture @" + "\n" + \
                  "║͜͡☆➣☯ StealVideoProfile @" + "\n" + \
                  "║͜͡☆➣☯ StealCover @" + "\n" + \
                  "║͜͡☆➣☯ CloneProfile @" + "\n" + \
                  "║͜͡☆➣☯ RestoreProfile" + "\n" + \
                  "║͜͡☆➣☯ GroupCreator" + "\n" + \
                  "║͜͡☆➣☯ GroupId" + "\n" + \
                  "║͜͡☆➣☯ GroupName" + "\n" + \
                  "║͜͡☆➣☯ GroupPicture" + "\n" + \
                  "║͜͡☆➣☯ Gt" + "\n" + \
                  "║͜͡☆➣☯ Gt「On/Off」" + "\n" + \
                  "║͜͡☆➣☯ GroupList" + "\n" + \
                  "║͜͡☆➣☯ GroupMemberList" + "\n" + \
                  "║͜͡☆➣☯ GroupInfo" + "\n" + \
                  "║͜͡☆➣☯ Ciak @" + "\n" + \
                  "║͜͡☆➣☯  KickAllMember"+ "\n" + \
                  "╰════════╬🔛╬════════╯" + "\n" + \
                  "╭════════╬🔛╬════════╮" + "\n" + \
                  "║͜͡☆➣ Ǥﾘ乇 Џんﾑ 乃Ծｲ丂" + "\n" + \
                  "╰════════╬🔛╬════════╯"
    return helpTranslate
#==============================================================================#
def backupData():
    try:
        backup = settings
        f = codecs.open('temp.json','w','utf-8')
        json.dump(backup, f, sort_keys=True, indent=4, ensure_ascii=False)
        backup = read
        f = codecs.open('read.json','w','utf-8')
        json.dump(backup, f, sort_keys=True, indent=4, ensure_ascii=False)
        return True
    except Exception as error:
        logError(error)
        return False
        
def command(text):
    pesan = text.lower()
    if pesan.startswith(settings["keyCommand"]):
        cmd = pesan.replace(settings["keyCommand"],"")
    else:
        cmd = "Undefined command"
    return cmd        


def lineBot(op):
    try:
        if op.type == 0:
            print ("[ 0 ] GYEVHA BOTS SATU")
            return
#-------------------------------------------------------------------------------
        if op.type == 25:
            msg = op.message
            if msg.contentType == 13:
                if settings["wblack"] == True:
                    if msg.contentMetadata["mid"] in settings["commentBlack"]:
                        gye.sendMessage(msg.to,"sudah masuk daftar hitam")
                        settings["wblack"] = False
                    else:
                        settings["commentBlack"][msg.contentMetadata["mid"]] = True
                        settings["wblack"] = False
                        gye.sendMessage(msg.to,"Itu tidak berkomentar")
                elif settings["dblack"] == True:
                    if msg.contentMetadata["mid"] in settings["commentBlack"]:
                        del settings["commentBlack"][msg.contentMetadata["mid"]]
                        gye.sendMessage(msg.to,"Done")
                        settings["dblack"] = False
                    else:
                        settings["dblack"] = False
                        gye.sendMessage(msg.to,"Tidak ada dalam daftar hitam")
#-------------------------------------------------------------------------------
                elif settings["wblacklist"] == True:
                    if msg.contentMetadata["mid"] in settings["blacklist"]:
                        gye.sendMessage(msg.to,"sudah masuk daftar hitam")
                        settings["wblacklist"] = False
                    else:
                        settings["blacklist"][msg.contentMetadata["mid"]] = True
                        settings["wblacklist"] = False
                        gye.sendMessage(msg.to,"Done")
                        
                elif settings["dblacklist"] == True:
                    if msg.contentMetadata["mid"] in settings["blacklist"]:
                        del settings["blacklist"][msg.contentMetadata["mid"]]
                        gye.sendMessage(msg.to,"Done")
                        settings["dblacklist"] = False
                    else:
                        settings["dblacklist"] = False
                        gye.sendMessage(msg.to,"Done")
                        
                       
#-------------------------------------------------------------------------------
        if op.type == 25:
            print ("[ 25 ] GYEVHA BOTS TIGA")
            msg = op.message
            text = msg.text
            msg_id = msg.id
            receiver = msg.to
            sender = msg._from
            if msg.toType == 0:
                if sender != gye.profile.mid:
                    to = sender
                else:
                    to = receiver
            else:
                to = receiver
            if msg.contentType == 0:
                if text is None:
                    return
#==============================================================================#
                if text.lower() == 'help':
                    helpMessage = helpmessage()
                    gye.sendMessage(to, str(helpMessage))
                    gye.sendContact(to, "u104e95aaefb53cf411f77353f6a96ece")
                    gye.sendMessage(to,"Jangan Songong Ye Pake Sc Orang 􀰂􀰂􀰂􀰂􀠁✍͡Gye􏿿􀌂􀆭✯➣􏿿")
                elif text.lower() == 'help1':
                    helpTextToSpeech = helptexttospeech()
                    gye.sendMessage(to, str(helpTextToSpeech))
                    ais.sendMessage(to, "Jangan Songong Ye Pake Bot Orang 􀰂􀰂􀰂􀰂􀠁✍͡Gye􏿿􀌂􀆭✯➣􏿿")
                elif text.lower() == 'help2':
                    helpTranslate = helptranslate()
                    gye.sendMessage(to, str(helpTranslate))
                    gye.sendMessage(to, "Jangan Songong Ye Pake Bot Orang 􀰂􀰂􀰂􀰂􀠁✍͡Gye􏿿􀌂􀆭✯➣􏿿")
#==============================================================================#
                elif text.lower() == 'sp':
                    start = time.time()
                    gye.sendMessage(to, "🔜 Cek Speed....")
                    elapsed_time = time.time() - start
                    gye.sendMessage(to,format(str(elapsed_time)))
                elif text.lower() == 'restart':    
                    gye.sendMessage(to, "Please Wait...")
                    time.sleep(5)
                    gye.sendMessage(to, "Restart Sukses")
                    restartBot()
                elif text.lower() == 'runtime':
                    timeNow = time.time()
                    runtime = timeNow - botStart
                    runtime = format_timespan(runtime)
                    gye.sendMessage(to, "login bot selama {}".format(str(runtime)))
                elif text.lower() == 'about':
                    try:
                        arr = []
                        owner = "u104e95aaefb53cf411f77353f6a96ece"
                        creator = gye.getContact(owner)
                        contact = gye.getContact(gyeMID)
                        grouplist = gye.getGroupIdsJoined()
                        contactlist = gye.getAllContactIds()
                        blockedlist = gye.getBlockedContactIds()
                        ret_ = "╭════════╬♥╬════════╮\nStatus Bots\n ╰════════╬♥╬════════╯\n ╭════════╬♥╬════════╮\n"
                        ret_ += "\n╠ akun : {}".format(contact.displayName)
                        ret_ += "\n╠ group : {}".format(str(len(grouplist)))
                        ret_ += "\n╠ teman : {}".format(str(len(contactlist)))
                        ret_ += "\n╠ Blokir : {}".format(str(len(blockedlist)))
                        ret_ += "\n╠══[ About Selfbot ]"
                        ret_ += "\n╠ Version : Premium"
                        ret_ += "\n╠ Creator : {}".format(creator.displayName)
                        ret_ += "\n╰════════╬♥╬════════╯\n\nǤﾘ乇 Џんﾑ 乃Ծｲ丂 ╭════════╬♥╬════════╮\n╰════════╬♥╬════════╯"
                        gye.sendMessage(to, str(ret_))
                    except Exception as e:
                        gye.sendMessage(msg.to, str(e))
#==============================================================================#
                elif text.lower() == 'status':
                    try:
                        ret_ = "╭════════╬🔛╬════════╮\n║͜͡☆➣ 🔛 丂ｲﾑｲЦ丂 乃Ծｲ丂 🔛\n ╰════════╬🔛╬════════╯\n ╭════════╬🔛╬════════╮\n"
                        if settings["protect"] == True: ret_ += "║͜͡☆➣ Protect ✅"
                        else: ret_ += "║͜͡☆➣  Protect ❌"
                        if settings["qrprotect"] == True: ret_ += "\n║͜͡☆➣ Qr Protect ✅"
                        else: ret_ += "\n║͜͡☆➣ Qr Protect ❌"
                        if settings["inviteprotect"] == True: ret_ += "\n║͜͡☆➣ Invite Protect ✅"
                        else: ret_ += "\n║͜͡☆➣ Invite Protect ❌"
                        if settings["cancelprotect"] == True: ret_ += "\n║͜͡☆➣ Cancel Protect ✅"
                        else: ret_ += "\n║͜͡☆➣ Cancel Protect ❌"
                        if settings["autoAdd"] == True: ret_ += "\n║͜͡☆➣ Auto Add ✅"
                        else: ret_ += "\n║͜͡☆➣ Auto Add ❌"
                        if settings["autoJoin"] == True: ret_ += "\n║͜͡☆➣ Auto Join ✅"
                        else: ret_ += "\n║͜͡☆➣ Auto Join ❌"
                        if settings["autoLeave"] == True: ret_ += "\n║͜͡☆➣ Auto Leave ✅"
                        else: ret_ += "\n║͜͡☆➣ Auto Leave ❌"
                        if settings["autoRead"] == True: ret_ += "\n║͜͡☆➣ Auto Read ✅"
                        else: ret_ += "\n║͜͡☆➣ Auto Read ❌"
                        if settings["checkSticker"] == True: ret_ += "\n║͜͡☆➣ Check Sticker ✅"
                        else: ret_ += "\n║͜͡☆➣ Check Sticker ❌"
                        if settings["detectMention"] == True: ret_ += "\n║͜͡☆➣ Detect Mention ✅"
                        else: ret_ += "\n║͜͡☆➣ Detect Mention ❌"
                        ret_ += "\n╰════════╬🔛╬════════╯\n╭════════╬🔛╬════════╮\n║͜͡☆➣ 🔛 Ǥﾘ乇 Џんﾑ 乃Ծｲ丂 🔛\n╰════════╬🔛╬════════╯"
                        gye.sendMessage(to, str(ret_))
                    except Exception as e:
                        gye.sendMessage(msg.to, str(e))
                        
                elif msg.text.lower().startswith("spaminvite "):
                   #if msg._from in admin:
                    dan = text.split("|")
                    userid = dan[0]
                    namagrup = dan[0]
                    jumlah = int(dan[0])
                    grups = gye.groups
                    tgb = gye.findContactsByUserid(userid)
                    if jumlah <= 10000000:
                        for var in range(0,jumlah):
                            try:
                                gye.createGroup(str(namagrup), [tgb.mid])
                                for i in grups:
                                    grup = gye.getGroup(i)
                                    if grup.name == namagrup:
                                        gye.inviteIntoGroup(grup.id, [tgb.mid])
                                        gye.sendMessage(to, "@! sukses spam grup!\n\nkorban: @!\njumlah: {}\nnama grup: {}".format(jumlah, str(namagrup)), [sender, tgb.mid])
                            except Exception as Nigga:
                                gye.sendMessage(to, str(Nigga))
                            #else:
                                gye.sendMessage(to, "@! kebanyakan njer!!", [sender])
#-------------------------------------------------------------------------------
                elif msg.text.lower().startswith("owneradd "):
                        key = eval(msg.contentMetadata["MENTION"])
                        key["MENTIONEES"][0]["M"]
                        targets = []
                        for x in key["MENTIONEES"]:
                            targets.append(x["M"])
                        for target in targets:
                            try:
                                Owner[target] = True
                                f=codecs.open('Owner.json','w','utf-8')
                                json.dump(Owner, f, sort_keys=True, indent=4,ensure_ascii=False)
                                gye.sendMessage(msg.to,"Owner ☢-Bot-☢\nAdd\nExecuted")
                            except:
                                pass
                    
                elif msg.text.lower().startswith("ownerdel "):
                        key = eval(msg.contentMetadata["MENTION"])
                        key["MENTIONEES"][0]["M"]
                        targets = []
                        for x in key["MENTIONEES"]:
                            targets.append(x["M"])
                        for target in targets:
                            try:
                                del Owner[target]
                                f=codecs.open('Owner.json','w','utf-8')
                                json.dump(Owner, f, sort_keys=True, indent=4,ensure_ascii=False)
                                gye.sendMessage(msg.to,"Owner ☢-Bot-☢\nRemove\nExecuted")
                            except:
                                pass
#-------------------------------------------------------------------------------
                elif text.lower() == 'ownerlist':
                        if Owner == []:
                            gye.sendMessage(msg.to,"The Ownerlist is empty")
                        else:
                            gye.sendMessage(msg.to,"Tunggu...")
                            mc = "╔═══════════\n║͜͡☆➣ ☯GYEVHA BOTS\n║͜͡☆➣ ☯〘 Owner List 〙\n║͜͡☆➣ ☯\n"
                            for mi_d in admin:
                                mc += "║͜͡☆➣ ☯ " +gye.getContact(mi_d).displayName + "\n"
                            gye.sendMessage(msg.to,mc + "╠════════════\n║͜͡☆➣ ☯〘 line.me/ti/p/~aisyagye 〙\n╚═════════════")
#-------------------------------------------------------------------------------
                elif msg.text.lower().startswith("adminadd "):
                        targets = []
                        key = eval(msg.contentMetadata["MENTION"])
                        key["MENTIONEES"][0]["M"]
                        for x in key["MENTIONEES"]:
                            targets.append(x["M"])
                        for target in targets:
                            try:
                                admin[target] = True
                                f=codecs.open('admin.json','w','utf-8')
                                json.dump(admin, f, sort_keys=True, indent=4,ensure_ascii=False)
                                gye.sendMessage(msg.to,"🔜Admin Berhasil Di Tambahkan")
                                ais.sendMessage(msg.to,"🔜Admin Berhasil Di Tambahkan")
                                break
                            except:
                                gye.sendMessage(msg.to,"Added Target Fail !")
                                break
                    
                elif msg.text.lower().startswith("admindel "):
                        targets = []
                        key = eval(msg.contentMetadata["MENTION"])
                        key["MENTIONEES"][0]["M"]
                        for x in key["MENTIONEES"]:
                            targets.append(x["M"])
                        for target in targets:
                            try:
                                del admin[target]
                                f=codecs.open('admin.json','w','utf-8')
                                json.dump(admin, f, sort_keys=True, indent=4,ensure_ascii=False)
                                gye.sendMessage(msg.to,"🔜Admin Berhasil Di hapus")
                                ais.sendMessage(msg.to,"🔜Admin Berhasil Di hapus")
                                break
                            except:
                                gye.sendMessage(msg.to,"Deleted Target Fail !")
                            break
              #      else:
               #         gye.sendMessage(msg.to,"Owner Permission Required")
#-------------------------------------------------------------------------------
                elif text.lower() == 'adminlist':
                #    if msg._from in Owner:
                        if admin == []:
                            gye.sendMessage(msg.to,"The Adminlist is empty")
                        else:
                            gye.sendMessage(msg.to,"Tunggu...")
                            mc = "╭════════╬🔛╬════════╮\n║͜͡☆➣ ?? 丂ｲﾑｲЦ丂 乃Ծｲ丂 🔛\n"
                            for mi_d in admin:
                                mc += "║͜͡☆➣ ☯ " +gye.getContact(mi_d).displayName + "\n"
                            gye.sendMessage(msg.to,mc + "╠═══════════════════\n║͜͡☆➣ ☯〘 line.me/ti/p/~aisyagye 〙\n╰════════╬🔛╬════════╯")
#-------------------------------------------------------------------------------
                elif text.lower() == 'protect on':
                        if settings["protect"] == True:
                            if settings["lang"] == "JP":
                                gye.sendMessage(msg.to,"🔜 Protection Already ✔")
                        else:
                            settings["protect"] = True
                            if settings["lang"] == "JP":
                                gye.sendMessage(msg.to,"🔜 Protection Set To ✔")
                                
                elif text.lower() == 'protect off':
                        if settings["protect"] == False:
                            if settings["lang"] == "JP":
                                gye.sendMessage(msg.to,"🔜 Protection Already ✖")
                        else:
                            settings["protect"] = False
                            if settings["lang"] == "JP":
                                gye.sendMessage(msg.to,"🔜 Protection Set To ✖")
#----------------------------------------------------------------------------------------                        
                elif text.lower() == 'qrprotect on':
                        if settings["qrprotect"] == True:
                            if settings["lang"] == "JP":
                                gye.sendMessage(msg.to,"🔜 Protection Qr Already ✔")
                            else:
                                gye.sendMessage(msg.to,"🔜 Protection Qr Set To ✔")
                        else:
                            settings["qrprotect"] = True
                            if settings["lang"] == "JP":
                                gye.sendMessage(msg.to,"🔜 Protection Qr Set To ✔")
                            else:
                                gye.sendMessage(msg.to,"🔜 Protection Qr Already ✔")
                                
                elif text.lower() == 'qrprotect off':
                        if settings["qrprotect"] == False:
                            if settings["lang"] == "JP":
                                gye.sendMessage(msg.to,"🔜 Protection Qr Already ✖")
                            else:
                                gye.sendMessage(msg.to,"🔜 Protection Qr Set To ✖")
                        else:
                            settings["qrprotect"] = False
                            if settings["lang"] == "JP":
                                gye.sendMessage(msg.to,"🔜 Protection Qr Set To ✖")
                            else:
                                gye.sendMessage(msg.to,"🔜 Protection Qr Already ✖")
#-------------------------------------------------------------------------------
                elif text.lower() == 'inviteprotect on':
                        if settings["inviteprotect"] == True:
                            if settings["lang"] == "JP":
                                gye.sendMessage(msg.to,"🔜 Protection Invite Already ✔")
                            else:
                                gye.sendMessage(msg.to,"🔜 Protection Invite Set To ✔")
                        else:
                            settings["inviteprotect"] = True
                            if settings["lang"] == "JP":
                                gye.sendMessage(msg.to,"🔜 Protection Invite Set To ✔")
                            else:
                                gye.sendMessage(msg.to,"🔜 Protection Invite Already ✔")
                                
                elif text.lower() == 'inviteprotect off':
                        if settings["inviteprotect"] == False:
                            if settings["lang"] == "JP":
                                gye.sendMessage(msg.to,"🔜 Protection Invite Already ✖")
                            else:
                                gye.sendMessage(msg.to,"🔜 Protection Invite Set To ✖")
                        else:
                            settings["inviteprotect"] = False
                            if settings["lang"] == "JP":
                                gye.sendMessage(msg.to,"🔜 Protection Invite Set To ✖")
                            else:
                                gye.sendMessage(msg.to,"🔜 Protection Invite Already ✖")
#-------------------------------------------------------------------------------
                elif text.lower() == 'cancelprotect on':
                        if settings["cancelprotect"] == True:
                            if settings["lang"] == "JP":
                                gye.sendMessage(msg.to,"🔜 Protection Cancel Invite Already ✔")
                            else:
                                gye.sendMessage(msg.to,"🔜 Protection Cancel Invite Set To ✔")
                        else:
                            settings["cancelprotect"] = True
                            if settings["lang"] == "JP":
                                gye.sendMessage(msg.to,"🔜 Protection Cancel Invite Set To ✔")
                            else:
                                gye.sendMessage(msg.to,"🔜 Protection Cancel Invite Already ✔")
                                
                elif text.lower() == 'cancelprotect off':
                        if settings["cancelprotect"] == False:
                            if settings["lang"] == "JP":
                                gye.sendMessage(msg.to,"🔜 Protection Cancel Invite Already ✖")
                            else:
                                gye.sendMessage(msg.to,"🔜 Protection Cancel Invite Set To ✖")
                        else:
                            settings["cancelprotect"] = False
                            if settings["lang"] == "JP":
                                gye.sendMessage(msg.to,"🔜 Protection Cancel Invite Set To ✖")
                            else:
                                gye.sendMessage(msg.to,"🔜 Protection Cancel Invite Already ✖")
#-------------------------------------------------------------------------------
                elif text.lower() == 'allpro on':
                        settings["protect"] = True
                        settings["qrprotect"] = True
                        settings["inviteprotect"] = True
                        settings["cancelprotect"] = True
                        settings["join link"] = True
                        gye.sendMessage(msg.to,"Join link on")
                        gye.sendMessage(msg.to,"Qrprotect on")
                        gye.sendMessage(msg.to,"Protect on")
                        gye.sendMessage(msg.to,"Inviteprotect on")
                        gye.sendMessage(msg.to,"Cancelprotect on")
                        gye.sendMessage(msg.to,"Bot on")
                        gye.sendMessage(msg.to,"🔜 All Protect Set To On")
                        		            
                elif text.lower() == 'allpro off':
             #       if msg._from in Owner:
                        settings["protect"] = False
                        settings["qrprotect"] = False
                        settings["inviteprotect"] = False
                        settings["cancelprotect"] = False
                        gye.sendMessage(msg.to,"Qrprotect Off")
                        gye.sendMessage(msg.to,"Protect Off")
                        gye.sendMessage(msg.to,"Inviteprotect Off")
                        gye.sendMessage(msg.to,"Cancelprotect Off")
                        gye.sendMessage(msg.to,"bot off")
                        #gye.sendMessage(msg.to,"anti js off")
                        gye.sendMessage(msg.to,"🔜 All Protect Set To Modar")
            #        else:
             #           gye.sendMessage(msg.to,"Just for Owner")
#-------------------------------------------------------------------------------
                elif text.lower() == 'autoadd on':
                    settings["autoAdd"] = True
                    gye.sendMessage(to, "🔜Berhasil mengaktifkan Auto Add")
                elif text.lower() == 'autoadd off':
                    settings["autoAdd"] = False
                    gye.sendMessage(to, "🔜Berhasil menonaktifkan Auto Add")
                elif text.lower() == 'autojoin on':
             #     if msg._from in Owner:    
                    settings["autoJoin"] = True
                    gye.sendMessage(to, "🔜Berhasil mengaktifkan Auto Join")
                elif text.lower() == 'autojoin off':
                #  if msg._from in Owner:    
                    settings["autoJoin"] = False
                    gye.sendMessage(to, "🔜Berhasil menonaktifkan Auto Join")
                elif text.lower() == 'autoleave on':
               #   if msg._from in Owner:
                    settings["autoLeave"] = True
                    gye.sendMessage(to, "🔜Berhasil mengaktifkan Auto Leave")
                elif text.lower() == 'autoleave off':
             #     if msg._from in Owner:
                    settings["autoLeave"] = False
                    gye.sendMessage(to, "🔜Berhasil menonaktifkan Auto Leave")
                elif text.lower() == 'autoread on':
                    settings["autoRead"] = True
                    gye.sendMessage(to, "🔜Berhasil mengaktifkan Auto Read")
                elif text.lower() == 'autoread off':
                    settings["autoRead"] = False
                    gye.sendMessage(to, "🔜Berhasil menonaktifkan Auto Read")
                elif text.lower() == 'checksticker on':
                    settings["checkSticker"] = True
                    gye.sendMessage(to, "🔜Berhasil mengaktifkan Check Details Sticker")
                elif text.lower() == 'checksticker off':
                    settings["checkSticker"] = False
                    gye.sendMessage(to, "🔜Berhasil menonaktifkan Check Details Sticker")
                elif text.lower() == 'detectmention on':
                    settings["datectMention"] = True
                    gye.sendMessage(to, "🔜Berhasil mengaktifkan Detect Mention")
                elif text.lower() == 'detectmention off':
                    settings["datectMention"] = False
                    gye.sendMessage(to, "🔜Berhasil menonaktifkan Detect Mention")
                elif text.lower() == 'join link on':
                    settings["autoJoinTicket"] = True
                    gye.sendMessage(to, "🔜Berhasil mengaktifkan Auto Join Link")
                elif text.lower() == 'join link off':
                    settings["autoJoinTicket"] = False
                    gye.sendMessage(to, "🔜Berhasil menonaktifkan Auto Join Link")                    
#==============================================================================#
                elif text.lower() == "respon":
                        gye.sendMessage(msg.to,responsename)
                        ais.sendMessage(msg.to,responsename2)
                elif msg.text.lower() == 'absen':
                        ais.sendContact(to, aisMID)
                        
                elif text.lower() in ["bye"]:
                    ais.leaveGroup(msg.to)    
                        
                elif text.lower() in ["@pamit"]:
                    gye.leaveGroup(msg.to)
                    ais.leaveGroup(msg.to)
                    
                elif text.lower() in ["halo"]:    
                    G = gye.getGroup(msg.to)
                    ginfo = gye.getGroup(msg.to)
                    G.preventedJoinByTicket = False
                    gye.updateGroup(G)
                    invsend = 0
                    Ticket = gye.reissueGroupTicket(msg.to)
                    ais.acceptGroupInvitationByTicket(msg.to,Ticket)
                    G = gye.getGroup(msg.to)
                    G.preventedJoinByTicket = True
                    gye.updateGroup(G)
                    G.preventedJoinByTicket(G)
                    gye.updateGroup(G)
                
                elif text.lower() == 'me':
                    sendMessageWithMention(to, gyeMID)
                    gye.sendContact(to, gyeMID)
                elif text.lower() == 'mymid':
                    gye.sendMessage(msg.to,"[MID]\n" +  gyeMID)
                elif text.lower() == 'myname':
                    me = gye.getContact(gyeMID)
                    gye.sendMessage(msg.to,"[DisplayName]\n" + me.displayName)
                elif text.lower() == 'mybio':
                    me = gye.getContact(gyeMID)
                    gye.sendMessage(msg.to,"[StatusMessage]\n" + me.statusMessage)
                elif text.lower() == 'mypicture':
                    me = gye.getContact(gyeMID)
                    gye.sendImageWithURL(msg.to,"http://dl.profile.line-cdn.net/" + me.pictureStatus)
                elif text.lower() == 'myvideoprofile':
                    me = gye.getContact(gyeMID)
                    gye.sendVideoWithURL(msg.to,"http://dl.profile.line-cdn.net/" + me.pictureStatus + "/vp")
                elif text.lower() == 'mycover':
                    me = gye.getContact(gyeMID)
                    cover = gye.getProfileCoverURL(gyeMID)    
                    gye.sendImageWithURL(msg.to, cover)
                elif msg.text.lower().startswith("stealcontact "):
                    if 'MENTION' in msg.contentMetadata.keys()!= None:
                        names = re.findall(r'@(\w+)', text)
                        mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                        mentionees = mention['MENTIONEES']
                        lists = []
                        for mention in mentionees:
                            if mention["M"] not in lists:
                                lists.append(mention["M"])
                        for ls in lists:
                            contact = gye.getContact(ls)
                            mi_d = contact.mid
                            gye.sendContact(msg.to, mi_d)
                elif msg.text.lower().startswith("midnya "):
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
                            ret_ += "\n{}" + ls
                        gye.sendMessage(msg.to, str(ret_))
                elif msg.text.lower().startswith("stealname "):
                    if 'MENTION' in msg.contentMetadata.keys()!= None:
                        names = re.findall(r'@(\w+)', text)
                        mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                        mentionees = mention['MENTIONEES']
                        lists = []
                        for mention in mentionees:
                            if mention["M"] not in lists:
                                lists.append(mention["M"])
                        for ls in lists:
                            contact = gye.getContact(ls)
                            gye.sendMessage(msg.to, "[ Display Name ]\n" + contact.displayName)
                elif msg.text.lower().startswith("stealbio "):
                    if 'MENTION' in msg.contentMetadata.keys()!= None:
                        names = re.findall(r'@(\w+)', text)
                        mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                        mentionees = mention['MENTIONEES']
                        lists = []
                        for mention in mentionees:
                            if mention["M"] not in lists:
                                lists.append(mention["M"])
                        for ls in lists:
                            contact = gye.getContact(ls)
                            gye.sendMessage(msg.to, "[ Status Message ]\n{}" + contact.statusMessage)
                elif msg.text.lower().startswith("stealpicture "):
                    if 'MENTION' in msg.contentMetadata.keys()!= None:
                        names = re.findall(r'@(\w+)', text)
                        mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                        mentionees = mention['MENTIONEES']
                        lists = []
                        for mention in mentionees:
                            if mention["M"] not in lists:
                                lists.append(mention["M"])
                        for ls in lists:
                            path = "http://dl.profile.gye.naver.jp/" + gye.getContact(ls).pictureStatus
                            gye.sendImageWithURL(msg.to, str(path))
                elif msg.text.lower().startswith("stealvideoprofile "):
                    if 'MENTION' in msg.contentMetadata.keys()!= None:
                        names = re.findall(r'@(\w+)', text)
                        mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                        mentionees = mention['MENTIONEES']
                        lists = []
                        for mention in mentionees:
                            if mention["M"] not in lists:
                                lists.append(mention["M"])
                        for ls in lists:
                            path = "http://dl.profile.gye.naver.jp/" + gye.getContact(ls).pictureStatus + "/vp"
                            gye.sendImageWithURL(msg.to, str(path))
                elif msg.text.lower().startswith("stealcover "):
                    if line != None:
                        if 'MENTION' in msg.contentMetadata.keys()!= None:
                            names = re.findall(r'@(\w+)', text)
                            mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                            mentionees = mention['MENTIONEES']
                            lists = []
                            for mention in mentionees:
                                if mention["M"] not in lists:
                                    lists.append(mention["M"])
                            for ls in lists:
                                path = gye.getProfileCoverURL(ls)
                                gye.sendImageWithURL(msg.to, str(path))
                elif msg.text.lower().startswith("cloneprofile "):    
                    if 'MENTION' in msg.contentMetadata.keys()!= None:
                        names = re.findall(r'@(\w+)', text)
                        mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                        mentionees = mention['MENTIONEES']
                        for mention in mentionees:
                            contact = mention["M"]
                            break
                        try:
                            gye.cloneContactProfile(contact)
                            gye.sendMessage(msg.to, "Berhasil clone member tunggu beberapa saat sampai profile berubah")
                        except:
                            gye.sendMessage(msg.to, "Gagal clone member")
                elif text.lower() == 'restoreprofile':    
                    try:
                        gyeProfile.displayName = str(myProfile["displayName"])
                        gyeProfile.statusMessage = str(myProfile["statusMessage"])
                        gyeProfile.pictureStatus = str(myProfile["pictureStatus"])
                        gye.updateProfileAttribute(8, gyeProfile.pictureStatus)
                        gye.updateProfile(gyeProfile)
                        gye.sendMessage(msg.to, "Berhasil restore profile tunggu beberapa saat sampai profile berubah")
                    except:
                        gye.sendMessage(msg.to, "Gagal restore profile")
#==============================================================================#
                elif msg.text.lower().startswith("mimicadd "):
                    targets = []
                    key = eval(msg.contentMetadata["MENTION"])
                    key["MENTIONEES"][0]["M"]
                    for x in key["MENTIONEES"]:
                        targets.append(x["M"])
                    for target in targets:
                        try:
                            settings["mimic"]["target"][target] = True
                            gye.sendMessage(msg.to,"Target ditambahkan!")
                            break
                        except:
                            gye.sendMessage(msg.to,"Added Target Fail !")
                            break
                elif msg.text.lower().startswith("mimicdel "):
                    targets = []
                    key = eval(msg.contentMetadata["MENTION"])
                    key["MENTIONEES"][0]["M"]
                    for x in key["MENTIONEES"]:
                        targets.append(x["M"])
                    for target in targets:
                        try:
                            del settings["mimic"]["target"][target]
                            gye.sendMessage(msg.to,"Target dihapuskan!")
                            break
                        except:
                            gye.sendMessage(msg.to,"Deleted Target Fail !")
                            break
                elif text.lower() == 'mimiclist':
                    if settings["mimic"]["target"] == {}:
                        gye.sendMessage(msg.to,"Tidak Ada Target")
                    else:
                        mc = "╔══[ Mimic List ]"
                        for mi_d in settings["mimic"]["target"]:
                            mc += "\n╠ "+gye.getContact(mi_d).displayName
                        gye.sendMessage(msg.to,mc + "\n╚══[ Finish ]")
                    
                elif "mimic" in msg.text.lower():
                    sep = text.split(" ")
                    mic = text.replace(sep[0] + " ","")
                    if mic == "on":
                        if settings["mimic"]["status"] == False:
                            settings["mimic"]["status"] = True
                            gye.sendMessage(msg.to,"Reply Message on")
                    elif mic == "off":
                        if settings["mimic"]["status"] == True:
                            settings["mimic"]["status"] = False
                            gye.sendMessage(msg.to,"Reply Message off")
#==============================================================================#
                elif text.lower() == 'groupcreator':
                    group = gye.getGroup(to)
                    GS = group.creator.mid
                    gye.sendContact(to, GS)
                elif text.lower() == 'groupid':
                    gid = gye.getGroup(to)
                    gye.sendMessage(to, "[ID Group : ]\n" + gid.id)
                elif text.lower() == 'grouppicture':
                    group = gye.getGroup(to)
                    path = "http://dl.profile.line-cdn.net/" + group.pictureStatus
                    gye.sendImageWithURL(to, path)
                elif text.lower() == 'groupname':
                    gid = gye.getGroup(to)
                    gye.sendMessage(to, "[Nama Group : ]\n" + gid.name)
                elif text.lower() == 'gt':
                    if msg.toType == 2:
                        group = gye.getGroup(to)
                        if group.preventedJoinByTicket == False:
                            ticket = gye.reissueGroupTicket(to)
                            gye.sendMessage(to, "[ Group Ticket ]\nhttps://line.me/R/ti/g/{}".format(str(ticket)))
                        else:
                            gye.sendMessage(to, "Grup qr tidak terbuka silahkan buka terlebih dahulu dengan perintah {}openqr".format(str(settings["keyCommand"])))
                elif text.lower() == 'gt on':
                    if msg.toType == 2:
                        group = gye.getGroup(to)
                        if group.preventedJoinByTicket == False:
                            gye.sendMessage(to, "Grup qr sudah terbuka")
                        else:
                            group.preventedJoinByTicket = False
                            gye.updateGroup(group)
                            gye.sendMessage(to, "Berhasil membuka grup qr")
                elif text.lower() == 'gt off':
                    if msg.toType == 2:
                        group = gye.getGroup(to)
                        if group.preventedJoinByTicket == True:
                            gye.sendMessage(to, "Grup qr sudah tertutup")
                        else:
                            group.preventedJoinByTicket = True
                            gye.updateGroup(group)
                            gye.sendMessage(to, "Berhasil menutup grup qr")
                elif text.lower() == 'groupinfo':
                    group = gye.getGroup(to)
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
                        gTicket = "https://line.me/R/ti/g/{}".format(str(gye.reissueGroupTicket(group.id)))
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
                    gye.sendMessage(to, str(ret_))
                    gye.sendImageWithURL(to, path)
                elif text.lower() == 'groupmemberlist':
                    if msg.toType == 2:
                        group = gye.getGroup(to)
                        ret_ = "╔══[ Member List ]"
                        no = 0 + 1
                        for mem in group.members:
                            ret_ += "\n╠ {}. {}".format(str(no), str(mem.displayName))
                            no += 1
                        ret_ += "\n╚══[ Total {} ]".format(str(len(group.members)))
                        gye.sendMessage(to, str(ret_))
                elif text.lower() == 'grouplist':
                        groups = gye.groups
                        ret_ = "╔══[ Group List ]"
                        no = 0 + 1
                        for gid in groups:
                            group = gye.getGroup(gid)
                            ret_ += "\n╠ {}. {} | {}".format(str(no), str(group.name), str(len(group.members)))
                            no += 1
                        ret_ += "\n╚══[ Total {} Groups ]".format(str(len(groups)))
                        gye.sendMessage(to, str(ret_))
#-------------------------------------------------------------------------------
                elif text.lower() == 'clearban':
                        settings["blacklist"] = {}
                        gye.sendMessage(msg.to,"🔜 Done ✔")
                        ais.sendMessage(msg.to,"🔜 Done ✔")
                        gye.sendMessage(msg.to,"🔜 Blacklist Dibersihkan ✔")
                        ais.sendMessage(msg.to,"🔜 Blacklist Dibersihkan ✔")
                        
                elif text.lower() == 'bot on':
                        gye.sendMessage(msg.to,"➲ Gye 1")
                        ais.sendMessage(msg.to,"🔜 Asist 1 ✔ Protect")
                        
                elif text.lower() == 'bot off':
                        gye.sendMessage(msg.to,"➲ Gye 1")
                        ais.sendMessage(msg.to,"🔜 Asist 1 ✖ Protect")
 
                elif text.lower() == 'bancontact':
                        settings["wblacklist"] = True
                        gye.sendMessage(msg.to,"Send Contact")
                        
                elif msg.text in ["unbancontact"]:
                        settings["dblacklist"] = True
                        gye.sendMessage(msg.to,"Send Contact")
#-------------------------------------------------------------------------------
                elif text.lower() == 'banlist':
                        if settings["blacklist"] == {}:
                            gye.sendMessage(msg.to,"Tidak Ada Banlist")
                        else:
                            gye.sendMessage(msg.to,"Daftar Banlist")
                            num=1
                            msgs="═══T E R S A N G K A═══"
                            for mi_d in settings["blacklist"]:
                                msgs+="\n[%i] %s" % (num, gye.getContact(mi_d).displayName)
                                num=(num+1)
                            msgs+="\n═══T E R S A N G K A═══\n\nTotal Tersangka :  %i" % len(settings["blacklist"])
                            gye.sendMessage(msg.to, msgs)
#=======================================================================================
                elif msg.text.lower().startswith("ciak "):
                       targets = []
                       key = eval(msg.contentMetadata["MENTION"])
                       key["MENTIONEES"][0]["M"]
                       for x in key["MENTIONEES"]:
                           targets.append(x["M"])
                       for target in targets:
                           try:
                               random.choice(GUE).kickoutFromGroup(msg.to,[target])
                           except:
                               random.choice(GUE).sendText(msg.to,"Error")
#-------------------------------------------------------------------------------
                elif text.lower() == 'ciak all member':
                 #   if msg._from in Owner:
                        if msg.toType == 2:
                            print ("[ 19 ] KICK ALL MEMBER")
                            _name = msg.text.replace("kickallmember","")
                            #gs = gye.getGroup(msg.to)
                            gs = ais.getGroup(msg.to)
                            gs = ki2.getGroup(msg.to)
                           #gye.sendMessage(msg.to,"「 Bye All 」")
                           #gye.sendMessage(msg.to,"「 Sory guys 」")
                            targets = []
                            for g in gs.members:
                                if _name in g.displayName:
                                    targets.append()
                            if targets == []:
                                gye.sendMessage(msg.to,"Not Found")
                            else:
                                for target in targets:
                                    if not target in Bots:
                                        if not target in Owner:
                                            if not target in admin:
                                                try:
                                                    klist=[line,ais,ki2]
                                                    kicker=random.choice(klist)
                                                    kicker.kickoutFromGroup(msg.to,[target])
                                                    print (msg.to,[g.mid])
                                                except:
                                                    gye.sendMessage(msg.to,"") 
#==============================================================================#          
                elif text.lower() == 'tag':
                    group = gye.getGroup(msg.to)
                    nama = [contact.mid for contact in group.members]
                    k = len(nama)//100
                    for a in range(k+1):
                        txt = u''
                        s=0
                        b=[]
                        for i in group.members[a*100 : (a+1)*100]:
                            b.append({"S":str(s), "E" :str(s+6), "M":i.mid})
                            s += 7
                            txt += u'@Alin \n'
                        gye.sendMessage(to, text=txt, contentMetadata={u'MENTION': json.dumps({'MENTIONEES':b})}, contentType=0)
                        gye.sendMessage(to, "Total {} Mention".format(str(len(nama))))          
                elif text.lower() == 'lurking on':
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
                    if msg.to in read['readPoint']:
                            try:
                                del read['readPoint'][msg.to]
                                del read['readMember'][msg.to]
                                del read['readTime'][msg.to]
                            except:
                                pass
                            read['readPoint'][msg.to] = msg.id
                            read['readMember'][msg.to] = ""
                            read['readTime'][msg.to] = datetime.now().strftime('%H:%M:%S')
                            read['ROM'][msg.to] = {}
                            with open('read.json', 'w') as fp:
                                json.dump(read, fp, sort_keys=True, indent=4)
                                gye.sendMessage(msg.to,"Lurking already on")
                    else:
                        try:
                            del read['readPoint'][msg.to]
                            del read['readMember'][msg.to]
                            del read['readTime'][msg.to]
                        except:
                            pass
                        read['readPoint'][msg.to] = msg.id
                        read['readMember'][msg.to] = ""
                        read['readTime'][msg.to] = datetime.now().strftime('%H:%M:%S')
                        read['ROM'][msg.to] = {}
                        with open('read.json', 'w') as fp:
                            json.dump(read, fp, sort_keys=True, indent=4)
                            gye.sendMessage(msg.to, "Set reading point:\n" + readTime)
                            
                elif text.lower() == 'lurking off':
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
                    if msg.to not in read['readPoint']:
                        gye.sendMessage(msg.to,"Lurking already off")
                    else:
                        try:
                            del read['readPoint'][msg.to]
                            del read['readMember'][msg.to]
                            del read['readTime'][msg.to]
                        except:
                              pass
                        gye.sendMessage(msg.to, "Delete reading point:\n" + readTime)
    
                elif text.lower() == 'lurking reset':
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
                        except:
                            pass
                        gye.sendMessage(msg.to, "Reset reading point:\n" + readTime)
                    else:
                        gye.sendMessage(msg.to, "Lurking belum diaktifkan ngapain di reset?")
                        
                elif text.lower() == 'lurking':
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
                            gye.sendMessage(receiver,"[ Reader ]:\nNone")
                        else:
                            chiya = []
                            for rom in read["ROM"][receiver].items():
                                chiya.append(rom[1])
                            cmem = gye.getContacts(chiya) 
                            zx = ""
                            zxc = ""
                            zx2 = []
                            xpesan = '[ Reader ]:\n'
                        for x in range(len(cmem)):
                            xname = str(cmem[x].displayName)
                            pesan = ''
                            pesan2 = pesan+"@c\n"
                            xlen = str(len(zxc)+len(xpesan))
                            xlen2 = str(len(zxc)+len(pesan2)+len(xpesan)-1)
                            zx = {'S':xlen, 'E':xlen2, 'M':cmem[x].mid}
                            zx2.append(zx)
                            zxc += pesan2
                        text = xpesan+ zxc + "\n[ Lurking time ]: \n" + readTime
                        try:
                            gye.sendMessage(receiver, text, contentMetadata={'MENTION':str('{"MENTIONEES":'+json.dumps(zx2).replace(' ','')+'}')}, contentType=0)
                        except Exception as error:
                            print (error)
                        pass
                    else:
                        gye.sendMessage(receiver,"Lurking has not been set.")
                        
#===DISINI GYE============================================================================[gyeMID - kiMID]
        if op.type == 19:
            print ("[ 19 ] GYEVHA BOTS KICK")
            try:
                if op.param3 in gyeMID:
                    if op.param2 in aisMID:
                        G = ais.getGroup(op.param1)
#                        ginfo = ki.getGroup(op.param1)
                        G.preventedJoinByTicket = False
                        ais.updateGroup(G)
                        invsend = 0
                        Ticket = ais.reissueGroupTicket(op.param1)
                        gye.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ais.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G = ais.getGroup(op.param1)
                        G.preventedJoinByTicket = True
                        ais.updateGroup(G)
                        G.preventedJoinByTicket(G)
                        ais.updateGroup(G)
                    else:
                        G = ais.getGroup(op.param1)
#                        ginfo = ais.getGroup(op.param1)
                        ais.kickoutFromGroup(op.param1,[op.param2])
                        G.preventedJoinByTicket = False
                        ais.updateGroup(G)
                        invsend = 0
                        Ticket = ais.reissueGroupTicket(op.param1)
                        gye.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ais.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G = ais.getGroup(op.param1)
                        G.preventedJoinByTicket = True
                        ais.updateGroup(G)
                        G.preventedJoinByTicket(G)
                        ais.updateGroup(G)
                        settings["blacklist"][op.param2] = True
#------- Ais - gye-----------------------------------------------------------------------[kiMID ki2MID]
                elif op.param3 in aisMID:
                    if op.param2 in gyeMID:
                        G = gye.getGroup(op.param1)
                        G.preventedJoinByTicket = False
                        gye.updateGroup(G)
                        invsend = 0
                        Ticket = gye.reissueGroupTicket(op.param1)
                        gye.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ais.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G = gye.getGroup(op.param1)
                        G.preventedJoinByTicket = True
                        gye.updateGroup(G)
                        G.preventedJoinByTicket(G)
                        gye.updateGroup(G)
                    else:
                        G = gye.getGroup(op.param1)
#                        ginfo = gye.getGroup(op.param1)
                        gye.kickoutFromGroup(op.param1,[op.param2])
                        G.preventedJoinByTicket = False
                        gye.updateGroup(G)
                        invsend = 0
                        Ticket = gye.reissueGroupTicket(op.param1)
                        gye.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ais.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G = gye.getGroup(op.param1)
                        G.preventedJoinByTicket = True
                        gye.updateGroup(G)
                        G.preventedJoinByTicket(G)
                        gye.updateGroup(G)
                        settings["blacklist"][op.param2] = True                        
                        
                elif op.param2 not in Bots:
                    if op.param2 in admin:
                        pass
                    elif settings["protect"] == True:
                        settings["blacklist"][op.param2] = True
                        random.choice(GUE).kickoutFromGroup(op.param1,[op.param2])
                        random.choice(GUE).inviteIntoGroup(op.param1,[op.param3])
                        random.choice(GUE).sendText(op.param1,"Don't Play bro...!")
                        
                else:
                    pass
            except:
                pass
#==============================================================================#
        if op.type == 13:
            if op.param2 not in Bots:
                if op.param2 in admin:
                    pass
                elif settings["inviteprotect"] == True:
                    settings["blacklist"][op.param2] = True
                    random.choice(GUE).cancelGroupInvitation(op.param1,[op.param3])
                    random.choice(GUE).kickoutFromGroup(op.param1,[op.param2])
                    if op.param2 not in Bots:
                        if op.param2 in admin:
                            pass
                        elif settings["cancelprotect"] == True:
                            settings["blacklist"][op.param2] = True
                            random.choice(GUE).cancelGroupInvitation(op.param1,[op.param3])	
#-------------------------------------------------------------------------------
        if op.type == 11:
            if op.param2 not in Bots:
                if op.param2 in admin and Bots and Owner:
                    pass
                elif settings["qrprotect"] == True:
                    settings["blacklist"][op.param2] = True
                    G = ais.getGroup(op.param1)
                    G.preventedJoinByTicket = True
                    ais.updateGroup(G)
                    random.choice(GUE).kickoutFromGroup(op.param1,[op.param2])
                else:
                    gye.sendMessage(op.param1,"")
            else:
                gye.sendMessage(op.param1,"")
                
#===============================================================================
# DISINI FUNGSI AUTO JOIN TICKET LINK BISA DI RUBAH HANYA
# DAN JUMBLAH ASIST KETIKA MAU NAMBAH ATAU MENGURANGI ASISIT
#===============================================================================
        if "/ti/g/" in msg.text.lower():
           if msg._from in admin:
            if settings["autoJoinTicket"] == True:
                link_re = re.compile('(?:line\:\/|line\.me\/R)\/ti\/g\/([a-zA-Z0-9_-]+)?')
                links = link_re.findall(text)
                n_links = []
                for l in links:
                    if l not in n_links:
                        n_links.append(l)
                for ticket_id in n_links:
                    group = gye.findGroupByTicket(ticket_id)
                    gye.acceptGroupInvitationByTicket(group.id,ticket_id)
                    gye.sendMessage(to, "🔜Berhasil masuk ke group %s" % str(group.name))
                    ais.acceptGroupInvitationByTicket(group.id,ticket_id)
                    ais.sendMessage(to, "🔜Berhasil masuk ke group %s" % str(group.name))              

        if op.type == 26:
            print ("[ 26 ] RECEIVE MESSAGE")
            msg = op.message
            text = msg.text
            msg_id = msg.id
            receiver = msg.to
            sender = msg._from
            if msg.toType == 0:
                if sender != gye.profile.mid:
                    to = sender
                else:
                    to = receiver
            else:
                to = receiver
                if settings["autoRead"] == True:
                    gye.sendChatChecked(to, msg_id)
                if to in read["readPoint"]:
                    if sender not in read["ROM"][to]:
                        read["ROM"][to][sender] = True
                if sender in settings["mimic"]["target"] and settings["mimic"]["status"] == True and settings["mimic"]["target"][sender] == True:
                    text = msg.text
                    if text is not None:
                        gye.sendMessage(msg.to,text)
                if msg.contentType == 0 and sender not in gyeMID and msg.toType == 2:
                    if 'MENTION' in msg.contentMetadata.keys()!= None:
                        names = re.findall(r'@(\w+)', text)
                        mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                        mentionees = mention['MENTIONEES']
                        lists = []
                        for mention in mentionees:
                            if gyeMID in mention["M"]:
                                if settings["detectMention"] == True:
                                    contact = gye.getContact(sender)
                                    gye.sendMessage(to, "sundala nu")
                                    sendMessageWithMention(to, contact.mid)
                                break
                        
    except Exception as error:
        logError(error)            
                        
   # except Exception as error:
    #    logError(error)
#==============================================================================#
# Auto join if BOT invited to group
def NOTIFIED_INVITE_INTO_GROUP(op):
    try:
        gye.acceptGroupInvitation(op.param1)
        ais.acceptGroupInvitation(op.param1)
    except Exception as e:
        gye.log("[NOTIFIED_INVITE_INTO_GROUP] ERROR : " + str(e))
# Auto kick if BOT out to group
def NOTIFIED_KICKOUT_FROM_GROUP(op):
    try:
        if op.param2 not in Bots:
            random.choice(KAC).kickoutFromGroup(op.param1,op.param2)
        else:
            pass
    except Exception as e:
        gye.log("[NOTIFIED_KICKOUT_FROM_GROUP] ERROR : " + str(e))

while True:
    try:
        ops = oepoll.singleTrace(count=50)
        if ops is not None:
            for op in ops:
                lineBot(op)
                oepoll.setRevision(op.revision)
    except Exception as e:
        logError(e)       
