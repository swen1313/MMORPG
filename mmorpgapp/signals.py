from django.db.models.signals import post_save
from django.dispatch import receiver # импортируем нужный декоратор
from django.core.mail import send_mail
from .models import Response, Advert


@receiver(post_save, sender=Response)
def notify_userWho(sender, instance, created, **kwargs):
    if created:
        subject = f'{instance.userTo} {instance.datetime}'
    else:
        subject = f'R changed for {instance.userTo} {instance.datetime}'

    send_mail(
        subject=subject,
        message=instance.message,
        from_email='yyulyul1@yandex.ru',  # здесь указываете почту, с которой будете отправлять (об этом попозже)
        recipient_list=[instance.advertResponse.userWho.email] # здесь список получателей. Например, секретарь, сам врач и так далее
    )
