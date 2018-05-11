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

    path('', views.post_list, name='post_list'),

    path('auth/sign-in/', auth_views.login, {'template_name': 'worldtravelapp/admin/sign_in.html'}, name='auth_login'),
    path('auth/sign-up/', views.sign_up, name='auth_sign_up'),
    path('auth/logout/', auth_views.logout, name='auth_logout'),

    path('admin/room/', views.admin_room, name='admin_room'),
    path('admin/news/', views.admin_news, name='admin_news'),
    path('admin/news/ok/', views.admin_news_ok, name='admin_news_ok'),
    path('admin/news/drafts/', views.admin_news_draft, name='admin_news_draft'),
    path('admin/tours/', views.admin_tours, name='admin_tours'),
    path('admin/orders/', views.admin_orders, name='admin_orders'),
    path('admin/workers/', views.admin_workers, name='admin_workers'),
    path('admin/workers/new/', views.admin_workers_new, name='admin_workers_new'),
    path('admin/workers/<int:pk>/edit/', views.admin_workers_edit, name='admin_workers_edit'),
    path('admin/workers/<int:pk>/remove/', views.admin_workers_remove, name='admin_workers_remove'),
    path('admin/messages/', views.admin_messages, name='admin_messages'),

    path('user/room/', views.user_room, name='user_room'),
    path('user/comments/', views.user_comments, name='user_comments'),
    path('user/mytours/', views.user_mytours, name='user_mytours'),
    path('user/settings/', views.user_settings, name='user_settings'),
    
    path('post/<int:pk>/', views.post_detail, name='post_detail'),
    path('post/<int:pk>/comment/', views.add_comment_to_post, name='add_comment_to_post'),
    path('post/<int:pk>/publish/', views.post_publish, name='post_publish'),
    path('post/<int:pk>/remove/', views.post_remove, name='post_remove'),
    path('post/new/', views.post_new, name='post_new'),
    path('post/<int:pk>/edit', views.post_edit, name='post_edit'),

    path('comment/<int:pk>/approve/', views.comment_approve, name='comment_approve'),
    path('comment/<int:pk>/remove/', views.comment_remove, name='comment_remove'),

    path('about_us/', views.about_us, name='about_us'),
    path('contacts/', views.contacts, name='contacts'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
