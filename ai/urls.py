from django.urls import path
from . import views

urlpatterns = [
    path(
        '',
        view= views.ProcessData.as_view(),
        name='formulario_ai',
    ),
    path(
        'cnn',
        view= views.CNN.as_view(),
        name='cnn',
    ),
    path(
        'prediction/',
        views.ShowData.as_view(),
        name="show_data"
    ),
    path(
        'rf',
        view= views.RF.as_view(),
        name='rf',
    ),
    path(
        'comments',
        view= views.comments,
        name='comments',
    ),

]
