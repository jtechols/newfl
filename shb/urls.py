from django.conf.urls import url 
from . import views

urlpatterns = [
	url(r'^$', views.home, name='home'),
	url(r'^mySHB/', views.mySHB, name='mySHB'),
	url(r'^standings/', views.standings, name='standings'),
	url(r'^freeagents/(?P<sort>\w+)/$', views.freeagents, name='freeagents'),
	url(r'^login/', views.login_view, name='login'),
	url(r'^logout/', views.logout_view, name='logout'),
	url(r'^oldman/(?P<oldman_id>[0-9]+)/$', views.oldman_detail, name='oldman_detail'),
	url(r'^add/(?P<newman_id>[0-9]+)/$', views.add, name='add'),
	url(r'^remove/(?P<newman_id>[0-9]+)/$', views.remove, name='remove'),
	url(r'^bench/(?P<newman_id>[0-9]+)/$', views.bench, name='bench'),
	url(r'^start/(?P<newman_id>[0-9]+)/$', views.start_newman, name='start_newman'),
	url(r'^flex/(?P<newman_id>[0-9]+)/$', views.flex_newman, name='flex_newman'),
	url(r'^edit/(?P<oldman_id>[0-9]+)/$', views.oldman_edit, name='oldman_view_edit'),
	url(r'^edit/(?P<oldman_id>[0-9]+)/save/$', views.oldman_edit_save, name='oldman_edit_save'),
	url(r'^newman/(?P<newman_id>[0-9]+)/$', views.newman_detail, name='newman_detail'),
	url(r'^lock_lineups/$', views.lock_lineups, name='lock_lineups'),
	url(r'^unlock_lineups/$', views.unlock_lineups, name='unlock_lineups'),
	url(r'^bank_points/$', views.bank_points, name='bank_points'),
]


