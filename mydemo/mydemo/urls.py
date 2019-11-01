from django.urls import path
from django.contrib import admin
from . import testdb, search, register, login

urlpatterns = [
    path('admin/', admin.site.urls),
    path('list-emp/', testdb.query_emp),
    path('search/', search.search_post),
    path('register/', register.register_user),
    path('index/', login.login_index),
    path('login/', login.login_check),

]
