from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import LanguageView, ParadigmView, ProgrammerView

router = DefaultRouter()
router.register('languages', LanguageView)
router.register('paradigms', ParadigmView)
router.register('programmers', ProgrammerView)

urlpatterns = [
	path('', include(router.urls)),
	path('api-auth/', include('rest_framework.urls'))

]
    
