from celery import shared_task
from django.core.mail import send_mail
from django.conf import settings

@shared_task
def send_registration_email(user_email):
    subject = "Добро пожаловать в «Викторину»!"
    message = """Здравствуй, игрок!
    Спасибо, что зарегистрировались в нашем приложении «Викторина». Мы рады видеть вас в нашем сообществе любителей интеллектуальных игр! 🎉
    В нашем приложении у вас есть возможность:
    •	Создавать свои комнаты на разные тематики, от истории до спорта. Вы можете приглашать друзей и бросать вызов другим игрокам.
    •	Присоединяться к уже созданным комнатам, чтобы проверить свои знания и пообщаться с единомышленниками.
    Каждая викторина — это не только испытание вашего интеллекта, но и отличная возможность весело провести время!
    Мы желаем вам успехов и незабываемых побед. Пусть ваши знания и интуиция приводят вас к вершинам лидерборда! 🏆
    Чтобы быть в курсе последних новостей, обновлений и интересных статей, подписывайтесь на наш Телеграм-канал: https://t.me/success_victorina
    С нетерпением ждем ваших успехов!
    Команда «Викторина Success»
    """
    email_from = settings.EMAIL_HOST_USER
    recipient_list = [user_email]
    send_mail(subject, message, email_from, recipient_list)
