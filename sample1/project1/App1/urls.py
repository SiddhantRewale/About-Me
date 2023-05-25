from django.contrib import admin
from django.urls import path
from.import views

# urlpatterns = [
#     path('admin/', admin.site.urls),
#     path('',views.index,name='index'),
#     path('about/',views.about,name='about')
# ]


urlpatterns = [

    path('',views.index,name='index'),
    path('removepunc/',views.removepunc,name='rempunc'),
    path('Captializefirst/',views.capfirst,name="capfirst"),
    path('newline/',views.newline,name="newline"),
    path('spaceremover/',views.spaceremover,name="spaceremover"),
    path('Charcount/',views.Charcount,name="Charcount"),
    path('Analyze/',views.analyze,name="analyze"),
    path('project/<str:pk>/',views.project,name='project'),
    path('projects/',views.projects,name='projects')


]