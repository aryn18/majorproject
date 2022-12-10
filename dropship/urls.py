from django.contrib import admin
from django.urls import path, include
from core import views
from django.contrib.auth import views as auth_views


from core.customer import views as customer_view;
from core.courier import views as courier_view;

customer_urlpatterns=[
    path('', customer_view.home, name='home'),
    path('profile/', customer_view.profile_page, name="profile"),

]

courier_urlpatterns=[
    path('', courier_view.home, name='home')
]

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home),

        path('', include('social_django.urls', namespace='social')),


    path('sign-in/', auth_views.LoginView.as_view(template_name="sign_in.html")),
    path('sign-out/', auth_views.LogoutView.as_view(next_page="/")),
    path('sign-up/', views.sign_up),

    path('customer/', include((customer_urlpatterns, 'customer'))),
    path('courier/', include((courier_urlpatterns, 'courier'))),

]
