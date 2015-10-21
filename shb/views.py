from django.shortcuts import render
from django.http import HttpResponse
from django.template import RequestContext, loader
from .models import Newman, Oldmen, SHB
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
# Create your views here.
def login(request):
	context = {}
	return render(request, 'shb/login.html', context)
@login_required
def home(request):
	all_newmen_list = Newman.objects.all()
	newmen_point_list = all_newmen_list.order_by('-points')[:10]
	context = {	'all_newmen_list': all_newmen_list, 'newmen_point_list': newmen_point_list}
	return render(request, 'shb/newfl.html', context)
@login_required
def mySHB(request):
	full_name = request.user.get_full_name()
	for oldmen in Oldmen.objects.all():
			if full_name == oldmen.team_owner:
				team_list = oldmen.newman_set.all()
				person = oldmen
	context = {'team_list': team_list, 'person': person}
	return render(request, 'shb/mySHB.html', context)
@login_required
def standings(request):
	position = 0
	oldmen_list = Oldmen.objects.order_by('-team_points')
	context = {'oldmen_list': oldmen_list, 'position':position}
	return render(request, 'shb/standings.html', context)
@login_required
def freeagents(request):
	free_agents = Newman.objects.filter(owner = None)
	context = {'free_agents': free_agents}
	return render(request, 'shb/freeagents.html', context)