from django.urls import path

from . import views

app_name = 'api'
urlpatterns = [
    path('test', views.test_page, name="test_page"),
    path('user/create', views.user_create, name='user_create'),
    path('user/search', views.user_search, name='user_search'),
    path('user/update', views.user_update, name='user_update'),
    path('user/delete', views.user_delete, name='user_delete'),
    path('organization/create', views.organization_create, name='organization_create'),
    path('organization/search', views.organization_search, name='organization_search'),
    path('organization/update', views.organization_update, name='organization_update'),
    path('organization/delete', views.organization_delete, name='organization_delete'),
    path('event/create', views.event_create, name='event_create'),
    path('event/search', views.event_search, name='event_search'),
    path('event/update', views.event_update, name='event_update'),
    path('event/delete', views.event_delete, name='event_delete'),
    path('team/create', views.team_create, name='team_create'),
    path('team/search', views.team_search, name='team_search'),
    path('team/update', views.team_update, name='team_update'),
    path('team/delete', views.team_delete, name='team_delete'),
    path('category/create', views.category_create, name='category_create'),
    path('category/search', views.category_search, name='category_search'),
    path('category/update', views.category_update, name='category_update'),
    path('category/delete', views.category_delete, name='category_delete'),
    path('category/add_team', views.category_add_team, name='category_add_team'),
    path('category/remove_team', views.category_remove_team, name='category_remove_team'),
    path('criteria/create', views.criteria_create, name='criteria_create'),
    path('criteria/search', views.criteria_search, name='criteria_search'),
    path('criteria/update', views.criteria_update, name='criteria_update'),
    path('criteria/delete', views.criteria_delete, name='criteria_delete'),
    path('criteria_label/create', views.criteria_label_create, name='criteria_label_create'),
    path('criteria_label/search', views.criteria_label_search, name='criteria_label_search'),
    path('criteria_label/update', views.criteria_label_update, name='criteria_label_update'),
    path('criteria_label/delete', views.criteria_label_delete, name='criteria_label_delete'),
]
