"""
URL configuration for expense_calculator project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
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
from django.db import router
from django.urls import path, include
from django.views.generic import TemplateView

# create a router for expenses
from rest_framework.routers import DefaultRouter
from expenses import views
router = DefaultRouter()
router.register(r'expenses', views.ExpenseViewSet)

urlpatterns = [
    path('', TemplateView.as_view(template_name='index.html'), name='home'),
    # add api url
    # include the rest_framework urls for browsable API
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('api/', include(router.urls)),
    path('admin/', admin.site.urls),
]

admin.site.site_header = "Expense Calculator"