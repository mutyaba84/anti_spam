from .models import BlockedEmail, BlockedIp, BlockedWord


def email_check(email):
	return BlockedEmail.objects.filter(email=email).exists()



def ip_check(ip):
	return BlockedIp.objects.filter(ip_address=ip).exists()


def get_ip(request):
	ip = request.META.get('HTTP_X_FORWARD_FOR')
	if ip:
		ip = ip.split(',')[0]
	else:
		ip = request.META.get('REMOTE_ADDR')
	return ip

def word_check(message):
	blocked_word = BlockedWord.objects.all()
	for item in blocked_word:
		if item.word.lower() in message.lower():
			return True
		else:
			return False
	
def add_spammer(email, ip_address):
    block_email = BlockedEmail(email=email)
    block_email.save()
    ip = BlockedIp(ip_address=ip_address)
    ip.save()