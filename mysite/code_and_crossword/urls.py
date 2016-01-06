from django.conf.urls import url

from . import views

app_name = 'code_and_crossword'
urlpatterns = [
	url(r'^$', views.index, name='index'),
    url(r'^(?P<level>[0-9]+)/code/$', views.code, name='code'),
    url(r'^(?P<level>[0-9]+)/crossword/$', views.crossword, name='crossword'),    
    url(r'^leaderboard', views.leaderboard, name='leaderboard'),
]

