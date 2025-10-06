from django.urls import path
from contact_book_app.views import index,signup_view,login_view,logout_view,add_contact,view_profile,delete_contact,edit_contact,search

urlpatterns = [
    path('', index),
    path('index/', index),
    path('signup_view/', signup_view),
    path('login_view/', login_view),
    path('logout_view/', logout_view),
    path('add_contact/', add_contact),
    path('view_profile/<int:id>/', view_profile),
    path('delete_contact/<int:id>/', delete_contact),
    path('edit_contact/<int:id>/', edit_contact),
    path('search/', search),
]

