from django.contrib import admin
from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
      path('',views.index,name = 'index'),
    path('locked/',views.locked_page,name = 'locked'),
    
    # user creation and authentication
    path('login/',auth_views.LoginView.as_view(),name = 'login'),
    path('logout/',auth_views.LogoutView.as_view(),name ='logout'),
    path('password_change/',auth_views.PasswordChangeView.as_view(template_name='registration/password_change.html'),name ='password_change'),
    path('password_change_done/',auth_views.PasswordChangeDoneView.as_view(template_name='registration/change-password_change.html'),name ='password_change_done'),
    path('password_reset/',auth_views.PasswordResetView.as_view(template_name='registration/password_reset_form.html'),name ='password_reset'),
    path('password_reset/done/',
auth_views.PasswordResetDoneView.as_view(template_name='registration/password_reset_done.html'),
name='password_reset_done'),
path('reset/<uidb64>/<token>/',
auth_views.PasswordResetConfirmView.as_view(template_name='registration/password_reset_confirm.html'),
name='password_reset_confirm'),
path('reset/done/',
auth_views.PasswordResetCompleteView.as_view(template_name='registration/password_reset_complete.html'),
name='password_reset_complete'),

path('register/',views.register,name='register'),

#posts views
path('<int:year>/<int:month>/<int:day>/<slug:post>/',
views.post_detail,
name='post_detail'),

]
