from django.conf.urls import url 
from . import views

urlpatterns = [
	url(r'^$', views.home, name='home'),
	url(r'^mySHB/', views.mySHB, name='mySHB'),
	url(r'^standings/', views.standings, name='standings'),
	url(r'^freeagents/', views.freeagents, name='freeagents'),
]
