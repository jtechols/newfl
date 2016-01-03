from django.shortcuts import render
from django.http import HttpResponse
from django.template import RequestContext, loader
from .models import Newman, Oldmen, SHB
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout, login, authenticate
# Create your views here.
def logout_view(request):
	logout(request)
	context = {}
	return render(request, 'registration/logout.html', context)
def login_view(request):
	username = request.POST['username']
	password = request.POST['password']
	user = authenticate(username=username, password=password)
	all_newmen_list = Newman.objects.all()
	newmen_point_list = all_newmen_list.order_by('-points')[:10]
	context = {	'all_newmen_list': all_newmen_list, 'newmen_point_list': newmen_point_list}
	if user:
		login(request, user)
		return render(request, 'shb/newfl.html', context)
	else:
		return render(request, 'registration/login.html', context)
@login_required
def home(request):
	all_newmen_list = Newman.objects.all()
	newmen_point_list = all_newmen_list.order_by('-points')[:10]
	context = {	'all_newmen_list': all_newmen_list, 'newmen_point_list': newmen_point_list}
	return render(request, 'shb/newfl.html', context)
@login_required
def mySHB(request):
	full_name = request.user.get_full_name()
	team_list = []
	for oldmen in Oldmen.objects.all():
			if full_name == oldmen.team_owner:
				team_list = oldmen.newman_set.all()
				person = oldmen
	context = {'team_list': team_list, 'person': person}
	return render(request, 'shb/mySHB.html', context)
@login_required(login_url='/shb/login/')
def standings(request):
	position = 0
	oldmen_list = Oldmen.objects.order_by('-team_points')
	context = {'oldmen_list': oldmen_list, 'position':position}
	return render(request, 'shb/standings.html', context)
@login_required(login_url='/shb/login/')
def freeagents(request):
	free_agents = Newman.objects.filter(owner = None)
	context = {'free_agents': free_agents}
	return render(request, 'shb/freeagents.html', context)