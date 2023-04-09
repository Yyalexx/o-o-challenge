"""
URL configuration for estate_objects app.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from django.urls import path
from estate_objects.views import *

urlpatterns = [
    path('', ObjectsList.as_view(), name='objects_list'),
    path('search/', ObjectSearch.as_view(), name='search'),
    path('<int:pk>', ObjectDetails.as_view(), name='object_details'),
    path('add/', ObjectCreate.as_view(), name='object_create'),
    path('<int:pk>/edit/', ObjectUpdate.as_view(), name='object_update'),
    path('<int:pk>/delete/', ObjectDelete.as_view(), name='object_delete'),
    path('solutions/<int:pk>/edit/', SolutionUpdate.as_view(), name='solution_update')

]