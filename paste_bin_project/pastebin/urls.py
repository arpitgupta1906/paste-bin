from django.urls import path
from .views import PasteCreate,PasteList,PasteDetail

urlpatterns=[
    path('',PasteCreate.as_view(),name="create"),
    path('paste/<int:pk>',PasteDetail.as_view(),name='pastebin_paste_detail'),
]
