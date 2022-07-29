from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns=[
    path('',views.HomeView.as_view(),name='index'), #as_view() is used because it is class based view
    path('<int:pk>',views.CandidateView.as_view(),name='candidate') #<int:pk> gives the id for the url
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)