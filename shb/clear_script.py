from shb.models import *
def clear():
	for newman in Newman.objects.all():
		newman.owner = None
		newman.save()
	return "All newman owner have been cleared"