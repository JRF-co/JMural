from __future__ import print_function
from auth import oauth
## lista os cursos, retorna id e nome dos cursos ativos

def coursesList():
    service = oauth()
    results = service.courses().list().execute()
    courses = results.get('courses', [])

    if not courses:
        print('No courses found.')
        return ['No courses found']
    else:
        lc = []
        for l in courses:
            if l['courseState'] == 'ACTIVE':
                lc.append({l['name']:l['id']})
            else:
                pass
        return lc