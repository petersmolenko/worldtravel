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
from django.urls import path
from worldtravelapp import views
from django.conf.urls.static import static
from django.conf import settings
from django.contrib.auth import views as auth_views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),
    path('auth/sign-in/', auth_views.login, {'template_name': 'worldtravelapp/admin/sign_in.html'}, name='auth_login'),
    path('auth/sign-up/', views.sign_up, name='auth_sign_up'),
    path('auth/logout/', auth_views.logout, {'next_page': '/'}, name='auth_logout'),

    path('admin/room/', views.admin_room, name='admin_room'),
    path('admin/news/', views.admin_news, name='admin_news'),
    path('admin/news/ok/', views.admin_news_ok, name='admin_news_ok'),
    path('admin/news/drafts/', views.admin_news_draft, name='admin_news_draft'),
    path('admin/tours/', views.admin_tours, name='admin_tours'),
    path('admin/tours/new/', views.admin_tours_new, name='admin_tours_new'),
    path('admin/tours/<int:pk>/edit/', views.admin_tours_edit, name='admin_tours_edit'),
    path('admin/tours/date/<int:pk>/edit/', views.admin_tours_edit_date, name='admin_tours_edit_date'),
    path('admin/tours/date/<int:pk>/remove/', views.admin_tours_date_remove, name='admin_tours_date_remove'),
    path('admin/tours/day/<int:pk>/new', views.admin_tours_day_new, name='admin_tours_day_new'),
    path('admin/tours/day/<int:pk>/edit', views.admin_tours_day_edit, name='admin_tours_day_edit'),
    path('admin/tours/day/<int:pk>/remove/', views.admin_tours_day_remove, name='admin_tours_day_remove'),
    path('admin/tours/<int:pk>/remove/', views.admin_tours_remove, name='admin_tours_remove'),
    path('admin/orders/', views.admin_orders, name='admin_orders'),
    path('admin/orders/order/<int:pk>/approve', views.admin_order_approve, name='admin_order_approve'),
    path('admin/orders/order/<int:pk>/deny', views.admin_order_deny, name='admin_order_deny'),
    path('admin/workers/', views.admin_workers, name='admin_workers'),
    path('admin/workers/new/', views.admin_workers_new, name='admin_workers_new'),
    path('admin/workers/<int:pk>/edit/', views.admin_workers_edit, name='admin_workers_edit'),
    path('admin/workers/<int:pk>/remove/', views.admin_workers_remove, name='admin_workers_remove'),
    path('admin/countrys/', views.admin_countrys, name='admin_countrys'),
    path('admin/countrys/new/', views.admin_countrys_new, name='admin_countrys_new'),
    path('admin/countrys/<int:pk>/edit/', views.admin_countrys_edit, name='admin_countrys_edit'),
    path('admin/countrys/<int:pk>/remove/', views.admin_countrys_remove, name='admin_countrys_remove'),
    path('admin/citys/', views.admin_citys, name='admin_citys'),
    path('admin/citys/new/', views.admin_citys_new, name='admin_citys_new'),
    path('admin/citys/<int:pk>/edit/', views.admin_citys_edit, name='admin_citys_edit'),
    path('admin/citys/<int:pk>/remove/', views.admin_citys_remove, name='admin_citys_remove'),
    path('admin/hottours/', views.admin_hottours, name='admin_hottours'),
    path('admin/hottours/new/', views.admin_hottours_new, name='admin_hottours_new'),
    path('admin/hottours/<int:pk>/edit/', views.admin_hottours_edit, name='admin_hottours_edit'),
    path('admin/hottours/<int:pk>/remove/', views.admin_hottours_remove, name='admin_hottours_remove'),
    path('admin/messages/', views.admin_messages, name='admin_messages'),
    path('admin/messages/<int:pk>/remove/', views.admin_messages_remove, name='admin_messages_remove'),

    path('user/room/', views.user_room, name='user_room'),
    path('user/desire/', views.user_desire, name='user_desire'),
    path('user/desire/<int:pk>/remove/', views.user_order_desire_remove, name='order_desire_remove'),
    path('user/order/', views.user_order, name='user_order'),
    path('user/order/<int:pk>/new', views.user_order_new, name='order_new'),
    path('user/order/<int:pk>/cancel/', views.user_order_cancel, name='user_order_cancel'),
    path('user/history/', views.user_history, name='user_history'),
    path('user/history/clean/', views.user_history_clean, name='user_history_clean'),
    path('user/settings/', views.user_settings, name='user_settings'),


    path('tours/', views.tours, name='tours'),
    path('tours/tour/<int:pk>/', views.tour_detail, name='tour_detail'),
    path('tours/tour/<int:pk>/review/new', views.add_review_to_tour, name='add_review_to_tour'),
    path('tours/tour/<int:pk>/review/approve/', views.review_approve, name='review_approve'),
    path('tours/tour/<int:pk>/review/remove/', views.review_remove, name='review_remove'),
    path('tours/exc', views.tours_exc, name='tours_exc'),
    path('tours/wee', views.tours_wee, name='tours_wee'),
    path('tours/act', views.tours_act, name='tours_act'),
    path('tours/bea', views.tours_bea, name='tours_bea'),
    
    path('post_list/', views.post_list, name='post_list'),
    path('post/<int:pk>/', views.post_detail, name='post_detail'),
    path('post/<int:pk>/comment/', views.add_comment_to_post, name='add_comment_to_post'),
    path('post/<int:pk>/publish/', views.post_publish, name='post_publish'),
    path('post/<int:pk>/remove/', views.post_remove, name='post_remove'),
    path('post/new/', views.post_new, name='post_new'),
    path('post/<int:pk>/edit', views.post_edit, name='post_edit'),
    path('post/tag/<str:tag>/', views.tag_post, name='tag_post'),

    path('comment/<int:pk>/approve/', views.comment_approve, name='comment_approve'),
    path('comment/<int:pk>/remove/', views.comment_remove, name='comment_remove'),

    path('about_us/', views.about_us, name='about_us'),
    path('contacts/', views.contacts, name='contacts'),
]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
