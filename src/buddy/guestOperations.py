from models import GuestEntry
import datetime

def saveGuestEntry(boozprofileId,userId,likeStatus,joiningtime):
    print "boozprofileId:", boozprofileId, "userId::", userId,  "joiningtime::", joiningtime
    g = GuestEntry(boozprofileId,userId,1,datetime.datetime.now())
    g.save()

def getAllJoingList():
    allJoingList = GuestEntry.objects.all()
    print "allJoingList::", allJoingList
    return allJoingList


