"""worldtravel URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
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
from django.urls import path, include
from worldtravelapp import views
from django.conf.urls.static import static
from django.conf import settings
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('auth/sign-in/', auth_views.login, {'template_name': 'admin/sign_in.html'}, name='auth_login'),
    path('auth/sign-up/', views.sign_up, name='auth_sign_up'),
    path('auth/logout/', auth_views.logout, name='auth_logout'),
    path('admin/news/', views.admin_news, name='admin_news'),
    path('admin/comments/', views.admin_comments, name='admin_comments'),
    path('admin/tours/', views.admin_tours, name='admin_tours'),
    path('admin/mytours/', views.admin_mytours, name='admin_mytours'),
    path('admin/orders/', views.admin_orders, name='admin_orders'),
    path('admin/settings/', views.admin_settings, name='admin_settings'),
    path('', views.post_list, name='post_list'),
    path('post/<int:pk>/', views.post_detail, name='post_detail'),
    path('post/<int:pk>/comment/', views.add_comment_to_post, name='add_comment_to_post'),
    path('post/<int:pk>/publish/', views.post_publish, name='post_publish'),
    path('post/<int:pk>/remove/', views.post_remove, name='post_remove'),
    path('post/new/', views.post_new, name='post_new'),
    path('admin/news/ok/', views.admin_news_ok, name='admin_news_ok'),
    path('admin/news/drafts/', views.admin_news_draft, name='admin_news_draft'),
    path('post/<int:pk>/edit', views.post_edit, name='post_edit'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
