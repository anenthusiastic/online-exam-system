from django.urls import include, path
from django.contrib.auth import views as auth_views

from .views import classroom, students, teachers

urlpatterns = [
    path('', classroom.home, name='home'),
    # change password
    path('password_change/', auth_views.PasswordChangeView.as_view(), name='password_change'),
    path('password_change/done', auth_views.PasswordChangeDoneView.as_view(), name='password_change_done'),  # success message
    # reset password
    path('password_reset/', auth_views.PasswordResetView.as_view(), name='password_reset'),  # enter email for password
    path('password_reset/done', auth_views.PasswordResetDoneView.as_view(), name='password_reset_done'),  # we have sent you mail
    path('reset/<uidb64>/<token>', auth_views.PasswordResetDoneView.as_view(), name='password_reset_done'),  # enter new password
    path('reset/done', auth_views.PasswordResetDoneView.as_view(), name='password_reset_complete'),   # password reset successfull

    path('students/', include(([
        path('', students.QuizListView.as_view(), name='quiz_list'),
        path('taken/', students.TakenQuizListView.as_view(), name='taken_quiz_list'),
        path('quiz/<int:pk>/', students.take_quiz, name='take_quiz'),        
    ], 'classroom'), namespace='students')),

    path('teachers/', include(([
        path('', teachers.QuizListView.as_view(), name='quiz_change_list'),
        path('quiz/add/', teachers.QuizCreateView.as_view(), name='quiz_add'),
        path('quiz/<int:pk>/', teachers.QuizUpdateView.as_view(), name='quiz_change'),
        path('quiz/<int:pk>/delete/', teachers.QuizDeleteView.as_view(), name='quiz_delete'),
        path('quiz/<int:pk>/question/add/', teachers.question_add, name='question_add'),
        path('quiz/<int:quiz_pk>/question/<int:question_pk>/', teachers.question_change, name='question_change'),
        path('quiz/<int:quiz_pk>/question/<int:question_pk>/delete/', teachers.QuestionDeleteView.as_view(), name='question_delete'),
    ], 'classroom'), namespace='teachers')),
]
