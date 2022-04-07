from django.urls import path
from . import views
urlpatterns = [
    path('', views.home, name = 'home'),
    path('accounts/profile/',views.book_list),
    path('add/',views.add_book),
    path('update/<int:id>/',views.update_book),
    path('delete/<int:id>/',views.delete_book),


]