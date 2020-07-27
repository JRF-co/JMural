from auth import oauth

def getName(courseId, userId):
    service = oauth()
    list ={}
    try:
        list = service.courses().teachers().get(
            courseId=courseId,
            userId= userId
        ).execute()
        name = list.get('profile').get('name').get('fullName')
        return name
    except:
        return 'Não consegui identificar o professor'

