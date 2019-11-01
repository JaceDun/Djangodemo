from django.urls import path
from django.contrib import admin
from . import users_manage, testdb, search, register, logion

urlpatterns = [
    path('admin/', admin.site.urls),
    #path('index/', users_manage.list_users),
    path('list-emp/', testdb.query_emp),
    path('search/', search.search_post),
    path('register/', register.register_user),
    path('check/', logion.index),
    path('login/', logion.logion_check),

]
