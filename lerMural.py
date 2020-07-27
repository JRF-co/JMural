from __future__ import print_function
from auth import oauth
from data import convertTime

def getAnnouncements(cId, pagesize=10):
    service = oauth()
    list = service.courses().announcements().list(
            courseId = cId,
            pageSize = pagesize
        ).execute()
    posts = list.get('announcements')
    list = []

    for p in posts:
        list.append([convertTime(p['creationTime']),p['text'],p['creatorUserId'],convertTime(p['updateTime'])])
    return  list
