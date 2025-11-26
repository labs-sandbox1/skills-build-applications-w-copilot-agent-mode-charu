from django.contrib import admin
from .models import Team, User, Activity, Workout, Leaderboard

@admin.register(Team)
class TeamAdmin(admin.ModelAdmin):
    list_display = ['_id', 'name']
    search_fields = ['name']

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ['_id', 'name', 'email', 'team']
    list_filter = ['team']
    search_fields = ['name', 'email']

@admin.register(Activity)
class ActivityAdmin(admin.ModelAdmin):
    list_display = ['_id', 'user', 'type', 'duration', 'calories', 'date']
    list_filter = ['type', 'date']
    search_fields = ['user__name', 'type']

@admin.register(Workout)
class WorkoutAdmin(admin.ModelAdmin):
    list_display = ['_id', 'name', 'difficulty']
    list_filter = ['difficulty']
    search_fields = ['name', 'description']

@admin.register(Leaderboard)
class LeaderboardAdmin(admin.ModelAdmin):
    list_display = ['_id', 'team', 'points']
    list_filter = ['team']
    search_fields = ['team__name']
