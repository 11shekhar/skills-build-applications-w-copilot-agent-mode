from djongo import models
from django.utils import timezone


class User(models.Model):
    _id = models.ObjectIdField()
    username = models.CharField(max_length=150, unique=True)
    email = models.EmailField(unique=True)
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    password = models.CharField(max_length=255)
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'users'

    def __str__(self):
        return self.username


class Team(models.Model):
    _id = models.ObjectIdField()
    name = models.CharField(max_length=150, unique=True)
    description = models.TextField(blank=True)
    members = models.JSONField(default=list)  # List of user IDs
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'teams'

    def __str__(self):
        return self.name


class Activity(models.Model):
    ACTIVITY_TYPES = [
        ('running', 'Running'),
        ('cycling', 'Cycling'),
        ('swimming', 'Swimming'),
        ('walking', 'Walking'),
        ('weightlifting', 'Weightlifting'),
    ]

    _id = models.ObjectIdField()
    user = models.CharField(max_length=150)  # username reference
    activity_type = models.CharField(max_length=20, choices=ACTIVITY_TYPES)
    duration = models.IntegerField()  # in minutes
    distance = models.FloatField(null=True, blank=True)  # in kilometers
    calories_burned = models.IntegerField(null=True, blank=True)
    date = models.DateField(default=timezone.now)
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'activities'

    def __str__(self):
        return f"{self.user} - {self.activity_type}"


class Leaderboard(models.Model):
    _id = models.ObjectIdField()
    user = models.CharField(max_length=150, unique=True)  # username
    team = models.CharField(max_length=150)
    total_activities = models.IntegerField(default=0)
    total_duration = models.IntegerField(default=0)  # in minutes
    total_distance = models.FloatField(default=0)  # in kilometers
    total_calories = models.IntegerField(default=0)
    rank = models.IntegerField(default=0)
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'leaderboard'

    def __str__(self):
        return f"{self.user} - Rank {self.rank}"


class Workout(models.Model):
    _id = models.ObjectIdField()
    user = models.CharField(max_length=150)  # username reference
    name = models.CharField(max_length=255)
    description = models.TextField()
    exercises = models.JSONField(default=list)  # List of exercises
    duration = models.IntegerField()  # in minutes
    difficulty = models.CharField(max_length=20, choices=[('easy', 'Easy'), ('medium', 'Medium'), ('hard', 'Hard')])
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'workouts'

    def __str__(self):
        return self.name
