from django.urls import path

from . import views

app_name='polls'

urlpatterns = [
    path('', views.index, name='index'),
    path('<int:ques_id>/vote/', views.vote, name='vote'),
    path('<int:ques_id>/', views.detail, name='detail'),
    # ex: /polls/5/results/
    path('<int:ques_id>/results/', views.results, name='results'),
    # ex: /polls/5/vote/
    path('<int:ques_id>/vote/', views.vote, name='vote'),
]
