
from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', views.dashboard, name='Home'),
# for signup
    path('signup/', views.register, name='Signup'),
    path('login/', views.login, name='Login'),

    path('reset_password/', auth_views.PasswordResetView.as_view(template_name="dashboard/password_reset.html"),
         name="reset_password"),
    path('reset_password_sent/',
         auth_views.PasswordResetDoneView.as_view(template_name="dashboard/password_reset_sent.html"),
         name="password_reset_done"),
    path('reset/<uidb64>/<token>',
         auth_views.PasswordResetConfirmView.as_view(template_name="dashboard/password_reset_form.html"),
         name="password_reset_confirm"),
    path('reset_password_complete/',
         auth_views.PasswordResetCompleteView.as_view(template_name="dashboard/password_reset_done.html"),
         name="password_reset_complete"),
     #     url for category 
    path('demo/', views.category, name='category'),
    path('postComment', views.postComment, name="postComment"),
    path('service-deatils/<int:id>', views.servicedetail, name="Service_details"),
    path('<int:service_id>/like', views.toggleLike, name='like'),
    
# api for cart
    path('cart/', views.cart, name="cart"),
    path('checkout/', views.checkout, name="checkout"),
    path('update_item/', views.updateItem, name="update_item"),
    path('process_order/', views.processOrder, name="process_order"),

    path('mylist/', views.mylist, name="mylist"),

    path('test/', views.test, name="home"),
    path('celery/', views.celeryt, name="home"),
    path('search/', views.search, name="Search"),
    path('logout/', views.logout_request, name="Logout"),
    path('about/', views.aboutus, name="About"),


]



