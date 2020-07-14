"""organization URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from management import views

urlpatterns = [
    path('admin/', admin.site.urls),

    path('organizations/', views.IndexView.as_view(), name='first_page'),

    path('organizations/<int:pk>', views. DetailView.as_view(), name='detail'),

    path('organizations/<int:pk>/branches', views.DetailView1.as_view(), name='second_page'),

    path('organizations/users', views.IndexView2.as_view(), name='third_page'),

    path('organizations/ser', views.ORGList.as_view()),
    path('organizations/ser/<int:id>/', views.ORGlist_edit.as_view()),

    path('branches/ser', views.BRNList.as_view()),
    path('users/ser', views.USRList.as_view()),
    path('co_relation/ser', views.FINALTBL.as_view()),

    #path('organizations/<int:pk>/users', views.DetailView2.as_view(), name='third_page'),

]
