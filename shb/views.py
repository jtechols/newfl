from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.template import RequestContext, loader
from .models import *
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout, login, authenticate
from .forms import *
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
		return HttpResponseRedirect('/shb/')
@login_required
def home(request):
	match = True
	all_newmen_list = Newman.objects.all()
	newmen_point_list = all_newmen_list.order_by('-career_points')[:10]
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
				person.current_total()
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
		oldman.current_total()
	oldmen_list = Oldmen.objects.order_by('-team_points')
	person = None
	full_name = request.user.get_full_name()
	for oldmen in oldmen_list:
		if full_name == oldmen.team_owner:
			person = oldmen
	context = {'oldmen_list': oldmen_list, 'person': person}
	return render(request, 'shb/standings.html', context)
@login_required
def freeagents(request, sort="-career_points"):
	oldmen_list = Oldmen.objects.all()
	full_name = request.user.get_full_name()
	for oldmen in oldmen_list:
		if full_name == oldmen.team_owner:
			person = oldmen
	free_agents = Newman.objects.filter(owner = None)
	if sort == 'career_points':
		sort = '-' + sort
	free_agents = free_agents.order_by(sort)
	context = {'free_agents': free_agents, 'person': person}
	for newman in Newman.objects.all():
		newman.section()
	return render(request, 'shb/freeagents.html', context)
@login_required
def newman_detail(request, newman_id):
	newman = Newman.objects.filter(id = newman_id)[0]
	shb_list = newman.shb_set.all()
	context={'newman': newman, 'shb_list': shb_list }
	return render(request, "shb/newman_detail.html", context)
@login_required
def oldman_detail(request, oldman_id):
	edit = False
	oldman = Oldmen.objects.filter(id=oldman_id)[0]
	full_name = request.user.get_full_name()
	for oldmen in Oldmen.objects.all():
			if full_name == oldmen.team_owner:
				person = oldmen
	if oldman == person:
		edit = True
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
	oldman.current_total()
	context  = {'oldman': oldman, 'team_list':team_list, 'ww_list': ww_list, 'sax_list':sax_list, 'hb_list': hb_list, 'lb_list':lb_list, 'p_list':p_list, 'b_list':b_list, 'f_list':f_list, 'edit':edit}
	return render(request, 'shb/oldman_detail.html', context)
@login_required
def oldman_edit(request, oldman_id):
	oldman = Oldmen.objects.filter(id=oldman_id)[0]
	full_name = request.user.get_full_name()
	for oldmen in Oldmen.objects.all():
			if full_name == oldmen.team_owner:
				person = oldmen
	if request.method == 'POST':
		form = UpdateTeam(request.POST)
		if form.is_valid():
			return oldman_detail(request,oldman_id)
	else:
		form = UpdateTeam()
	context = {'oldman':oldman, 'form':form}
	return render(request, 'shb/oldman_edit.html', context)
@login_required
def oldman_edit_save(request, oldman_id):
	team_name = request.POST['team_name']
	full_name = request.user.get_full_name()
	for oldmen in Oldmen.objects.all():
			if full_name == oldmen.team_owner:
				person = oldmen
	oldman = Oldmen.objects.filter(id=oldman_id)[0]
	if oldman == person:
		oldman.team_name = team_name
		oldman.save()
	context = {'oldman':oldman}
	return oldman_detail(request, oldman_id)
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
@login_required
def lock_lineups(request):
	if request.user.is_staff:
		for oldmen in Oldmen.objects.all():
			oldmen.locked = True 
			oldmen.save()
	return mySHB(request)
def unlock_lineups(request):
	if request.user.is_staff:
		for oldmen in Oldmen.objects.all():
			oldmen.locked = False
			oldmen.save()
	return mySHB(request)
def bank_points(request):
	if request.user.is_staff:
		for oldmen in Oldmen.objects.all():
			oldmen.bank_points()
	return mySHB(request)