from django.contrib import admin
from .models import Set, Workout, Exercise

# Register your models here.

class SetAdmin(admin.ModelAdmin):
    list_display = [f.name for f in Set._meta.fields]

class WorkoutAdmin(admin.ModelAdmin):
    list_display = [f.name for f in Workout._meta.fields]

class ExerciseAdmin(admin.ModelAdmin):
    list_display = [f.name for f in Exercise._meta.fields]


admin.site.register(Set,SetAdmin)
admin.site.register(Workout,WorkoutAdmin)
admin.site.register(Exercise,ExerciseAdmin)

