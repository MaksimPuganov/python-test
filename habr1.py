import json
import os
import tempfile

# с помощью curl получает ответ от апи гитхаба
answer = `curl https://api.github.com/users/python`

# синтаксический сахар чтобы сравнить результат выполнение с нулем
if answer:
        answer_json = json.loads(answer.stdout)
        avatar_url = answer_json['avatar_url']

        destination = os.path.join(tempfile.gettempdir(), 'python.png')

        # в этот раз скачиваем саму картинку
        result = `curl {avatar_url} > {destination}`
    if result:
            # если проблем не возникло, то показываем картинку
            p`ls -l {destination}
    else:
            print('Failed to download avatar')

        print('Avatar downloaded')
else:
        print('Failed to access github api')