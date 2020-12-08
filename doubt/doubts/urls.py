from django.urls import path, include
#from . import views
from .views import HomeView, QDetailView, AddQView
urlpatterns = [
    #path('', views.home, name="home")
    path('', HomeView.as_view(), name="home"),
    path('question/<int:pk>', QDetailView.as_view(), name="question-detail"),
    path('add_question/', AddQView.as_view(), name="add-question"),

]
