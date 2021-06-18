from django.urls import path
from .import views


urlpatterns=[

    path('',views.index, name='index'),   #route of index page
    path('login/',views.login, name='login'),   #route of index page
    path('register',views.register, name='register'),   #route of index page
    path('purpose/',views.purpose,name='purpose'), #route of the purpose page
    path('profile/',views.profile,name='profile'), #route of the purpose page
    path('logout',views.logout,name='logout'), #route of the logout page
    path('card2/',views.matches,name='matches'), #route of the matches page
    path('del',views.delt,name='delete'), #route of the matches page
    

]