import smtplib
import os
from dotenv import load_dotenv
load_dotenv()

from_address = os.getenv("EMAIL_ADDRESS")
password = os.getenv("EMAIL_PASSWORD")

to_address = 'full.development@yandex.com'
subject = 'Invitation!'
content_type = "text/plain; charset=UTF-8"

friend_name = "Тимур"
sender_name = "Сара"
website_name = "https://dvmn.org/profession-ref-program/shakaraizada/XtKm7/"

text_message = '''Привет, {friend_name}! {my_name} приглашает тебя на сайт {website}!

{website} — это новая версия онлайн-курса по программированию. 
Изучаем Python и не только. Решаем задачи. Получаем ревью от преподавателя.

Как будет проходить ваше обучение на {website}?

→ Попрактикуешься на реальных кейсах.
→ Будешь учиться без стресса и бессонных ночей.
→ Подготовишь крепкое резюме.

Регистрируйся → {website}
На курсы, которые еще не вышли, можно подписаться и получить уведомление на email.
'''.format(friend_name=friend_name, my_name=sender_name, website=website_name)

letter = "From: {}\nTo: {}\nSubject: {}\nContent-Type: {}\n\n{}".format(
    from_address, to_address, subject, content_type, text_message
)

letter = letter.encode("UTF-8")

server = smtplib.SMTP_SSL('smtp.yandex.ru', 465)
server.login(from_address, password)
server.sendmail(from_address, to_address, letter)
server.quit()
