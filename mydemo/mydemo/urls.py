from django.urls import path
from django.contrib import admin
from . import view, testdb, search, search2

urlpatterns = [
    path('admin/', admin.site.urls),
    path('hello/', view.hello),
    path('list-emp/', testdb.query_emp),
    path('search-form/', search.search_form),
    path('search/', search.search),
    path('search2/', search2.search_post),
]
