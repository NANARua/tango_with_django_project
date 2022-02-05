from django.urls import path
from rango import views

app_name = 'rango'

urlpatterns = [
    path('', views.index, name='index'),
    # first parameter is the string to match. empty string '', only match if there is nothing after
    # second parameter tells Django what view to call if matched
    # third and optional parameter is called name
    path('about/', views.about, name='about'),
    path('category/<slug:category_name_slug>/',views.show_category, name='show_category'),
]