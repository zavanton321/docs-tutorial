from django.urls import path

from student.views import vote, IndexView, DetailedView, ResultsView

app_name = 'student'

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('<int:pk>', DetailedView.as_view(), name='detail'),
    path('<int:pk>/vote/', vote, name='vote'),
    path('<int:pk>/results/', ResultsView.as_view(), name='results'),
]
