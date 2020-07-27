from datetime import datetime, timedelta

def convertTime(data_google):

    dto = datetime.strptime(data_google,'%Y-%m-%dT%H:%M:%S.%fZ')
    dto = dto - timedelta(hours=3)
    return [dto.strftime('%d/%m'),dto.strftime('%H:%M')]
