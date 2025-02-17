"""
URL configuration for oz_django_7 project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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
from django.urls import URLPattern, URLResolver, path

# from ninja import NinjaAPI
#
# from tabom.services.like_service import do_like

# api = NinjaAPI()
#
#
# @api.get("/like")
# def like(request, article_id: int, user_id: int) -> None:
#     do_like(article_id, user_id)
#     return None


urlpatterns: list[URLResolver | URLPattern] = [
    path("admin/", admin.site.urls),
    # path("api/", api.urls),
]
