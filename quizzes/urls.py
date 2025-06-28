from django.urls import path
from . import views

urlpatterns = [
    path('', views.quiz_list, name='quiz_list'),
    path('quiz/<int:quiz_id>/', views.quiz_detail, name='quiz_detail'),
    path('quiz/<int:quiz_id>/submit/', views.submit_quiz, name='submit_quiz'),
    path('quiz/results/<int:participacion_id>/', views.quiz_results, name='quiz_results'),
    path('register/', views.register, name='register'),
    path('profile/', views.profile, name='profile'),
    path('leaderboard/', views.leaderboard, name='leaderboard'),
    
    # URLs de administración
    path('admin-panel/', views.admin_dashboard, name='admin_dashboard'),
    path('admin-panel/quizzes/', views.admin_quiz_list, name='admin_quiz_list'),
    path('admin-panel/quiz/create/', views.admin_quiz_create, name='admin_quiz_create'),
    path('admin-panel/quiz/<int:quiz_id>/edit/', views.admin_quiz_edit, name='admin_quiz_edit'),
    path('admin-panel/quiz/<int:quiz_id>/delete/', views.admin_quiz_delete, name='admin_quiz_delete'),
    path('admin-panel/quiz/<int:quiz_id>/pregunta/create/', views.admin_pregunta_create, name='admin_pregunta_create'),
    path('admin-panel/pregunta/<int:pregunta_id>/edit/', views.admin_pregunta_edit, name='admin_pregunta_edit'),
    path('admin-panel/pregunta/<int:pregunta_id>/delete/', views.admin_pregunta_delete, name='admin_pregunta_delete'),
    path('admin-panel/pregunta/<int:pregunta_id>/opcion/create/', views.admin_opcion_create, name='admin_opcion_create'),
    path('admin-panel/opcion/<int:opcion_id>/edit/', views.admin_opcion_edit, name='admin_opcion_edit'),
    path('admin-panel/opcion/<int:opcion_id>/delete/', views.admin_opcion_delete, name='admin_opcion_delete'),
    path('admin-panel/participaciones/', views.admin_participaciones, name='admin_participaciones'),
    
    # URLs para subir archivos de quiz
    path('admin-panel/upload-quiz/', views.upload_quiz, name='upload_quiz'),
    path('admin-panel/download-example/', views.download_example_quiz, name='download_example_quiz'),
]
