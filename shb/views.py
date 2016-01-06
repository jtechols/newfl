from django.shortcuts import render
from django.http import HttpResponse, HttpRedirect
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
		return HttpRedirect('/shb/')
@login_required
def home(request):
	match = True
	all_newmen_list = Newman.objects.all()
	newmen_point_list = all_newmen_list.order_by('-points')[:10]
	context = {	'all_newmen_list': all_newmen_list, 'newmen_point_list': newmen_point_list, 'match':match}
	return render(request, 'shb/newfl.html', context)
@login_required
def mySHB(request):
	full_name = request.user.get_full_name()
	team_list = []
	person = None
	for oldmen in Oldmen.objects.all():
			if full_name == oldmen.team_owner:
				team_list = oldmen.newman_set.all()
				person = oldmen
				person.team_total()
	for newman in team_list:
		newman.section()
	for each_new in Newman.objects.all():
		each_new.calc_points()
	if team_list:
		ww_list = team_list.filter(woodwind=True, bench=False, flex=False)
		sax_list = team_list.filter(saxophone=True, bench=False, flex=False)
		hb_list = team_list.filter(highbrass=True, bench=False, flex=False)
		lb_list = team_list.filter(lowbrass=True, bench=False, flex=False)
		p_list = team_list.filter(perc=True, bench=False, flex=False)
		b_list = team_list.filter(bench=True)
		f_list = team_list.filter(flex=True)
	else:
		ww_list = []
		sax_list = []
		hb_list = []
		lb_list = []
		p_list = []
		b_list = []
		f_list = []
	context = {'team_list': team_list, 'person': person, 'ww_list': ww_list, 'sax_list':sax_list, 'hb_list': hb_list, 'lb_list':lb_list, 'p_list':p_list, 'b_list':b_list, 'f_list':f_list}
	return render(request, 'shb/mySHB.html', context)
@login_required
def standings(request):
	for oldman in Oldmen.objects.all():
		oldman.team_total()
	oldmen_list = Oldmen.objects.order_by('-team_points')
	person = None
	full_name = request.user.get_full_name()
	for oldmen in oldmen_list:
		if full_name == oldmen.team_owner:
			person = oldmen
	context = {'oldmen_list': oldmen_list, 'person': person}
	return render(request, 'shb/standings.html', context)
@login_required
def freeagents(request):
	free_agents = Newman.objects.filter(owner = None)
	free_agents = free_agents.order_by('-points')
	context = {'free_agents': free_agents}
	for newman in Newman.objects.all():
		newman.section()
	return render(request, 'shb/freeagents.html', context)
@login_required
def oldman_detail(request, oldman_id):
	oldman = Oldmen.objects.filter(id=oldman_id)[0]
	team_list = oldman.newman_set.all()
	for newman in team_list:
		newman.section()
	for each_new in Newman.objects.all():
		each_new.calc_points()
	if team_list:
		ww_list = team_list.filter(woodwind=True, bench=False, flex=False)
		sax_list = team_list.filter(saxophone=True, bench=False, flex=False)
		hb_list = team_list.filter(highbrass=True, bench=False, flex=False)
		lb_list = team_list.filter(lowbrass=True, bench=False, flex=False)
		p_list = team_list.filter(perc=True, bench=False, flex=False)
		b_list = team_list.filter(bench=True, flex=False)
		f_list = team_list.filter(flex=True, bench=False)
	else:
		ww_list = []
		sax_list = []
		hb_list = []
		lb_list = []
		p_list = []
		b_list = []
		f_list = []
	oldman.team_total()
	context  = {'oldman': oldman, 'team_list':team_list, 'ww_list': ww_list, 'sax_list':sax_list, 'hb_list': hb_list, 'lb_list':lb_list, 'p_list':p_list, 'b_list':b_list, 'f_list':f_list}
	return render(request, 'shb/oldman_detail.html', context)
@login_required
def add(request, newman_id):
	full_name = request.user.get_full_name()
	for oldmen in Oldmen.objects.all():
			if full_name == oldmen.team_owner:
				person = oldmen
				person.add_newman(newman_id)
	return mySHB(request)
@login_required
def remove(request, newman_id):
	full_name = request.user.get_full_name()
	for oldmen in Oldmen.objects.all():
			if full_name == oldmen.team_owner:
				person = oldmen
				person.remove_newman(newman_id)
	return mySHB(request)
@login_required
def bench(request, newman_id):
	full_name = request.user.get_full_name()
	for oldmen in Oldmen.objects.all():
			if full_name == oldmen.team_owner:
				person = oldmen
				person.bench_newman(newman_id)
	return mySHB(request)
@login_required
def start_newman(request, newman_id):
	full_name = request.user.get_full_name()
	for oldmen in Oldmen.objects.all():
			if full_name == oldmen.team_owner:
				person = oldmen
				person.start_newman(newman_id)
	return mySHB(request)
@login_required
def flex_newman(request, newman_id):
	full_name = request.user.get_full_name()
	for oldmen in Oldmen.objects.all():
			if full_name == oldmen.team_owner:
				person = oldmen
				person.flex_newman(newman_id)
	return mySHB(request)