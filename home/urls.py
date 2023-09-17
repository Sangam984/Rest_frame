
from django.urls import path
from .views import ListClass,ListSubjects,ListTitle,DetailContent,home
urlpatterns = [
        path('',home,name="home"),
        path('listClass/',ListClass.as_view(),name="grade"),
        path('subjects/<int:pk>',ListSubjects.as_view(),name="subs"),
        path('subject/title/<int:pk>',ListTitle.as_view(),name="title"),
        path('subject/title/content/<int:pk>',DetailContent.as_view(),name="content"),
]
