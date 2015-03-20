from django.conf.urls import patterns, url
from rugby import views

urlpatterns = patterns('',
	url(r'^$', views.index, name='index'),
	url(r'^coupon', views.coupon, name='coupon'),
	url(r'^leagueTable', views.leagueTable, name='leagueTable'),
)
