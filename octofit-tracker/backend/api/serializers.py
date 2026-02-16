from rest_framework import serializers
from .models import User, Team, Activity, Leaderboard, Workout


class UserSerializer(serializers.ModelSerializer):
    _id = serializers.SerializerMethodField()

    class Meta:
        model = User
        fields = ['_id', 'username', 'email', 'first_name', 'last_name', 'created_at', 'updated_at']
        read_only_fields = ['_id', 'created_at', 'updated_at']

    def get__id(self, obj):
        return str(obj._id) if obj._id else None


class TeamSerializer(serializers.ModelSerializer):
    _id = serializers.SerializerMethodField()

    class Meta:
        model = Team
        fields = ['_id', 'name', 'description', 'members', 'created_at', 'updated_at']
        read_only_fields = ['_id', 'created_at', 'updated_at']

    def get__id(self, obj):
        return str(obj._id) if obj._id else None


class ActivitySerializer(serializers.ModelSerializer):
    _id = serializers.SerializerMethodField()

    class Meta:
        model = Activity
        fields = ['_id', 'user', 'activity_type', 'duration', 'distance', 'calories_burned', 'date', 'created_at', 'updated_at']
        read_only_fields = ['_id', 'created_at', 'updated_at']

    def get__id(self, obj):
        return str(obj._id) if obj._id else None


class LeaderboardSerializer(serializers.ModelSerializer):
    _id = serializers.SerializerMethodField()

    class Meta:
        model = Leaderboard
        fields = ['_id', 'user', 'team', 'total_activities', 'total_duration', 'total_distance', 'total_calories', 'rank', 'created_at', 'updated_at']
        read_only_fields = ['_id', 'created_at', 'updated_at']

    def get__id(self, obj):
        return str(obj._id) if obj._id else None


class WorkoutSerializer(serializers.ModelSerializer):
    _id = serializers.SerializerMethodField()

    class Meta:
        model = Workout
        fields = ['_id', 'user', 'name', 'description', 'exercises', 'duration', 'difficulty', 'created_at', 'updated_at']
        read_only_fields = ['_id', 'created_at', 'updated_at']

    def get__id(self, obj):
        return str(obj._id) if obj._id else None
