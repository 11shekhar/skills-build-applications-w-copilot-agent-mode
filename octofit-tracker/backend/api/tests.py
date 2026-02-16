from django.test import TestCase
from rest_framework.test import APITestCase
from rest_framework import status
from .models import User, Team, Activity, Leaderboard, Workout


class UserAPITestCase(APITestCase):
    def setUp(self):
        self.user_data = {
            'username': 'testuser',
            'email': 'testuser@example.com',
            'first_name': 'Test',
            'last_name': 'User',
            'password': 'testpass123'
        }

    def test_create_user(self):
        response = self.client.post('/api/users/', self.user_data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_list_users(self):
        response = self.client.get('/api/users/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)


class TeamAPITestCase(APITestCase):
    def setUp(self):
        self.team_data = {
            'name': 'Team Marvel',
            'description': 'Marvel superheroes team',
            'members': []
        }

    def test_create_team(self):
        response = self.client.post('/api/teams/', self.team_data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_list_teams(self):
        response = self.client.get('/api/teams/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)


class ActivityAPITestCase(APITestCase):
    def setUp(self):
        self.activity_data = {
            'user': 'testuser',
            'activity_type': 'running',
            'duration': 30,
            'distance': 5.0,
            'calories_burned': 300
        }

    def test_create_activity(self):
        response = self.client.post('/api/activities/', self.activity_data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_list_activities(self):
        response = self.client.get('/api/activities/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)


class LeaderboardAPITestCase(APITestCase):
    def setUp(self):
        self.leaderboard_data = {
            'user': 'testuser',
            'team': 'Team Marvel',
            'total_activities': 5,
            'total_duration': 150,
            'total_distance': 25.0,
            'total_calories': 1500,
            'rank': 1
        }

    def test_create_leaderboard(self):
        response = self.client.post('/api/leaderboard/', self.leaderboard_data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_list_leaderboard(self):
        response = self.client.get('/api/leaderboard/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)


class WorkoutAPITestCase(APITestCase):
    def setUp(self):
        self.workout_data = {
            'user': 'testuser',
            'name': 'Full Body Workout',
            'description': 'A comprehensive full body workout',
            'exercises': ['Squats', 'Bench Press', 'Deadlifts'],
            'duration': 60,
            'difficulty': 'hard'
        }

    def test_create_workout(self):
        response = self.client.post('/api/workouts/', self.workout_data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_list_workouts(self):
        response = self.client.get('/api/workouts/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
