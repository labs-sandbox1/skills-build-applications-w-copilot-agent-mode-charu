from djongo import models

class Team(models.Model):
    _id = models.ObjectIdField(primary_key=True, editable=False)
    name = models.CharField(max_length=100, unique=True, default="")
    class Meta:
        db_table = 'teams'

class User(models.Model):
    _id = models.ObjectIdField(primary_key=True, editable=False)
    name = models.CharField(max_length=100, default="")
    email = models.EmailField(unique=True, default="")
    team = models.ForeignKey(Team, on_delete=models.CASCADE, related_name='members', null=True, default=None, to_field='_id')
    class Meta:
        db_table = 'users'

class Activity(models.Model):
    _id = models.ObjectIdField(primary_key=True, editable=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='activities', null=True, default=None, to_field='_id')
    type = models.CharField(max_length=100, default="")
    duration = models.IntegerField(default=0)  # minutes
    calories = models.IntegerField(default=0)
    date = models.DateField(null=True, default=None)
    class Meta:
        db_table = 'activities'

class Workout(models.Model):
    _id = models.ObjectIdField(primary_key=True, editable=False)
    name = models.CharField(max_length=100, default="")
    description = models.TextField(default="")
    difficulty = models.CharField(max_length=50, default="")
    class Meta:
        db_table = 'workouts'

class Leaderboard(models.Model):
    _id = models.ObjectIdField(primary_key=True, editable=False)
    team = models.ForeignKey(Team, on_delete=models.CASCADE, related_name='leaderboard_entries', null=True, default=None, to_field='_id')
    points = models.IntegerField(default=0)
    class Meta:
        db_table = 'leaderboard'
