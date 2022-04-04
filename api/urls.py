from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns

# from api.views import notes_list, notes_detail
from api.views import NoteListView, NoteDetailView

urlpatterns = [
    path('notes/', NoteListView.as_view()),
    # path('notes/', notes_list),
    path('notes/<int:pk>/', NoteDetailView.as_view(), name='notes-detail'),
    # path('notes/<int:pk>/', notes_detail),
]

urlpatterns = format_suffix_patterns(urlpatterns)
