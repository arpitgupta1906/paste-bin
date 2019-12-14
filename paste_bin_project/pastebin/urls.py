from django.urls import path
from .views import PasteCreate,PasteList,PasteDetail,PasteDelete,PasteUpdate

urlpatterns=[
    path('',PasteCreate.as_view(),name="create"),
    path('pastes/',PasteList.as_view(),name='pastebin_paste_list'),
    path('paste/<int:pk>',PasteDetail.as_view(),name='pastebin_paste_detail'),
    path('pasteupdate/<int:pk>',PasteUpdate.as_view(),name='pastebin_paste_edit'),
    path('pastedelete/<int:pk>',PasteDelete.as_view(),name='pastebin_paste_delete'),
]
