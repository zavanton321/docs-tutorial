from django.urls import path

from student.views import detail, index, results, vote

app_name = 'student'

urlpatterns = [
    path('', index, name='index'),
    path('<int:question_id>', detail, name='detail'),
    path('<int:question_id>/vote/', vote, name='vote'),
    path('<int:question_id>/results/', results, name='results'),
]
