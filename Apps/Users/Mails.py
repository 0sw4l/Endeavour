__author__ = 'osw4l'
from django.core.mail import EmailMultiAlternatives

url = 'http://localhost:8010/users/confirm-user'
mail_admin = 'ioswxd@gmail.com'


def enviar_token(**kwargs):

    nombre = kwargs.get('nombre')
    mail = kwargs.get('email')
    token = kwargs.get('token')

    titulo = "Confirma Tu cuenta - Endeavour"

    mensaje = '<h1 style="font-size: 2em">Hola sr <span style="color: CornflowerBlue ">{0}</span> </h1> ' \
              '<div style="font-size: 1.5em">' \
              '<br>Gracias por registrarte en <strong>Endeavour</strong>. ' \
              '<br>Para Activar tu cuenta toca <a href="{1}/{2}/">este vinculo</a>.' \
              '<br>Equipo <strong>Endeavour</strong>.' \
              '<br>' \
              '<br>Funcion creada por <strong>0sw4l</strong>.' \
              '</div>'.format(nombre, url, token)

    correo = EmailMultiAlternatives(titulo, mensaje, mail_admin, [mail])
    correo.attach_alternative(mensaje, "text/html")
    correo.send()



