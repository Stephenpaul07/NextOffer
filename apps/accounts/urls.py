from django.urls import path

from .views import RegisterView, UserListView

urlpatterns = [
    path("users/", UserListView.as_view(), name="accounts-user-list"),
    path("register/", RegisterView.as_view(), name="accounts-register"),
]
