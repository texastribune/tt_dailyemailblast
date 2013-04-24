from django.core.mail import EmailMultiAlternatives


def send_email(subject, bodies, from_email, to, headers):
    msg = EmailMultiAlternatives(subject, bodies['text'], from_email, to,
            headers=headers)
    msg.attach_alternative(bodies['html'], 'text/html')
    msg.send(fail_silently=False)
