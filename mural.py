from __future__ import print_function
#import pickle
#import os.path
#from googleapiclient.discovery import build
#from google_auth_oauthlib.flow import InstalledAppFlow
#from google.auth.transport.requests import Request
from auth import oauth

def publicar(cId, texto):
    service = oauth()
    publicacao =     {
        'courseId': cId,
        'text': texto,
        'state': 'PUBLISHED',
        'assigneeMode': 'ALL_STUDENTS',
        }
    try:
        sent = service.courses().announcements().create(
            courseId = cId,
            body = publicacao
        ).execute()
    except:
        return 'Algo deu errado'
    else:
        return 'Publicado'




if (__name__ == '__main__'):
    print(publicar(1,'a'))