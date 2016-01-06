from django.conf.urls import url 
from . import views

urlpatterns = [
	url(r'^$', views.home, name='home'),
	url(r'^mySHB/', views.mySHB, name='mySHB'),
	url(r'^standings/', views.standings, name='standings'),
	url(r'^freeagents/', views.freeagents, name='freeagents'),
	url(r'^login/', views.login_view, name='login'),
	url(r'^logout/', views.logout_view, name='logout'),
	url(r'^(?P<oldman_id>[0-9]+)/$', views.oldman_detail, name='oldman_detail'),
	url(r'^add/(?P<newman_id>[0-9]+)/$', views.add, name='add'),
	url(r'^remove/(?P<newman_id>[0-9]+)/$', views.remove, name='remove'),
	url(r'^bench/(?P<newman_id>[0-9]+)/$', views.bench, name='bench'),
	url(r'^start/(?P<newman_id>[0-9]+)/$', views.start_newman, name='start_newman'),
	url(r'^flex/(?P<newman_id>[0-9]+)/$', views.flex_newman, name='flex_newman'),
	url(r'^edit/(?P<oldman_id>[0-9]+)/$', views.oldman_view_edit, name='oldman_view_edit'),
	url(r'^edit/(?P<oldman_id>[0-9]+)/save/$', views.oldman_edit, name='oldman_edit'),
]

