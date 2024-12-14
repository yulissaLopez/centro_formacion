from django.urls import path
from .views import EstudianteListCreateView, EstudianteManageView, NotaCreateView

urlpatterns = [
    path('', EstudianteListCreateView.as_view(), name = 'estudiantes-list-create'),
    path('<str:documento_identidad>/manage', EstudianteManageView.as_view(), name = 'estudiante-manage'),
    path('notas', NotaCreateView.as_view(), name = 'notas-registro'),
    
    ]
