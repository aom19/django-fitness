from django.conf import settings
from rest_framework.routers import DefaultRouter, SimpleRouter

from django_fitness.users.api.views import UserViewSet
from django_fitness.fitness.views import WorkoutViewSet, ExerciseViewSet, SetViewSet

if settings.DEBUG:
    router = DefaultRouter()
else:
    router = SimpleRouter()

router.register("users", UserViewSet)
router.register("workouts", WorkoutViewSet)
router.register("exercises", ExerciseViewSet)
router.register("sets", SetViewSet)



app_name = "api"
urlpatterns = router.urls
