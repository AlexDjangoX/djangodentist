from django.shortcuts import render
from django.core.mail import send_mail

def home(request):
	return render(request, 'home.html', {})

def contact(request):
	if request.method == "POST":
		message_name = request.POST['message-name']
		message_email = request.POST['message-email']
		message = request.POST['message']

		# send an email
		send_mail(
			'Message from ' + message_name, # subject
			message, 						# message
			message_email, 					# from
			['alexmonk17@gmail.com'], 		# To email, add more to list if wanted
			)

		return render(request, 'contact.html', {'message_name':message_name})

	else:
		return render(request, 'contact.html', {})

def about(request):
	return render(request, 'about.html', {})

def pricing(request):
	return render(request, 'pricing.html', {})

def service(request):
	return render(request, 'service.html', {})

def appointment(request):
	if request.method == "POST":
		your_name = request.POST['your-name']
		your_phone = request.POST['your-phone']
		your_email = request.POST['your-email']
		your_schedule = request.POST['your-schedule']
		your_time = request.POST['your-time']
		your_message = request.POST['your-message']

		callback = your_name + ' thank you for booking a callback, our secretary will contact you to set an appointment.'

		# send an email
		send_mail(
			'Callback from Dr AlexDjangoX for ' + your_name, # subject
			callback, 											# message
			your_email, 										# from
			['alexmonk17@gmail.com', your_email], 							# To email, add more to list if wanted
			)

		return render(request, 'appointment.html', {
			'your_name': your_name,
			'your_phone': your_phone,
			'your_email': your_email,
			'your_schedule': your_schedule,
			'your_time':your_time,
			'your_message':your_message,
			})

	else:
		return render(request, 'home.html', {})