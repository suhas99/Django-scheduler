import schedule
import time
from django.contrib.auth.models import User
from django_mail_admin import mail, model


def trig_email():
	print("This is to send email")
	libr = []

	users = User.objects.all()
	for i in users:
		libr = User.objects.get(username=i).email

	mail.send(
		'suhaskashyap2@gmail.com',
		'recipient@example.com',  # List of email addresses also accepted
		subject='My email',
		message='Hi there!',
		priority=models.PRIORITY.now,
		html_message='Hi <strong>there</strong>!',
	)

schedule.every(1).hour.do(trig_email)

while True:
	schedule.run_pending()
	time.sleep(1)
