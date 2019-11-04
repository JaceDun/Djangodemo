from django.urls import path
from django.contrib import admin
from . import login, user_manage

urlpatterns = [
    path('admin/', admin.site.urls),
    path('add_user/', user_manage.add_user),
    path('index/', login.login_index),
    path('login/', login.login_check),
    path('edit_user/', user_manage.edit_user),
    path('edit_save/', user_manage.edit_user_handler),
    path('delete_user/', user_manage.delete_user),

]
