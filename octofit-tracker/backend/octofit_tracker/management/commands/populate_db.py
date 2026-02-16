from django.core.management.base import BaseCommand
from api.models import User, Team, Activity, Leaderboard, Workout
from datetime import datetime, timedelta
import random


class Command(BaseCommand):
    help = 'Populate the octofit_db database with test data'


    def handle(self, *args, **kwargs):
        print('Populating octofit_db using djongo...')
        self.stdout.write(self.style.SUCCESS('Starting database population...'))

        # Clear existing data
        User.objects.all().delete()
        Team.objects.all().delete()
        Activity.objects.all().delete()
        Leaderboard.objects.all().delete()
        Workout.objects.all().delete()
        self.stdout.write(self.style.SUCCESS('Cleared existing data'))

        # Create Teams
        team_marvel = Team.objects.create(
            name='Team Marvel',
            description='Marvel superheroes team',
            members=[]
        )
        team_dc = Team.objects.create(
            name='Team DC',
            description='DC superheroes team',
            members=[]
        )
        self.stdout.write(self.style.SUCCESS('Created teams'))

        # Marvel superheroes
        marvel_heroes = [
            ('ironman', 'Iron Man', 'tony@stark.com', 'Tony', 'Stark'),
            ('captainamerica', 'Captain America', 'steve@rogers.com', 'Steve', 'Rogers'),
            ('thor', 'Thor', 'thor@asgard.com', 'Thor', 'Odinson'),
            ('blackwidow', 'Black Widow', 'natasha@romanoff.com', 'Natasha', 'Romanoff'),
            ('hawkeye', 'Hawkeye', 'clint@barton.com', 'Clint', 'Barton'),
        ]

        # DC superheroes
        dc_heroes = [
            ('superman', 'Superman', 'clark@kent.com', 'Clark', 'Kent'),
            ('batman', 'Batman', 'bruce@wayne.com', 'Bruce', 'Wayne'),
            ('wonderwoman', 'Wonder Woman', 'diana@prince.com', 'Diana', 'Prince'),
            ('theflash', 'The Flash', 'barry@allen.com', 'Barry', 'Allen'),
            ('greenlantern', 'Green Lantern', 'hal@jordan.com', 'Hal', 'Jordan'),
        ]

        # Create Marvel users
        marvel_users = []
        team_marvel.members = []
        for username, display_name, email, first_name, last_name in marvel_heroes:
            user = User.objects.create(
                username=username,
                email=email,
                first_name=first_name,
                last_name=last_name,
                password='password123'
            )
            marvel_users.append(user)
            team_marvel.members.append(str(user._id))

        # Create DC users
        dc_users = []
        team_dc.members = []
        for username, display_name, email, first_name, last_name in dc_heroes:
            user = User.objects.create(
                username=username,
                email=email,
                first_name=first_name,
                last_name=last_name,
                password='password123'
            )
            dc_users.append(user)
            team_dc.members.append(str(user._id))

        team_marvel.save()
        team_dc.save()
        self.stdout.write(self.style.SUCCESS('Created users and updated teams'))

        # Create activities for Marvel users
        activity_types = ['running', 'cycling', 'swimming', 'walking', 'weightlifting']
        for i, user in enumerate(marvel_users):
            for j in range(random.randint(3, 7)):
                date = datetime.now() - timedelta(days=random.randint(0, 30))
                activity = Activity.objects.create(
                    user=user.username,
                    activity_type=random.choice(activity_types),
                    duration=random.randint(20, 120),
                    distance=random.uniform(1.0, 10.0) if random.choice([True, False]) else None,
                    calories_burned=random.randint(100, 500),
                    date=date.date()
                )

        # Create activities for DC users
        for i, user in enumerate(dc_users):
            for j in range(random.randint(3, 7)):
                date = datetime.now() - timedelta(days=random.randint(0, 30))
                activity = Activity.objects.create(
                    user=user.username,
                    activity_type=random.choice(activity_types),
                    duration=random.randint(20, 120),
                    distance=random.uniform(1.0, 10.0) if random.choice([True, False]) else None,
                    calories_burned=random.randint(100, 500),
                    date=date.date()
                )

        self.stdout.write(self.style.SUCCESS('Created activities'))

        # Create leaderboard entries
        all_users = marvel_users + dc_users
        rank = 1
        for user in sorted(all_users, key=lambda x: sum(1 for _ in Activity.objects.filter(user=x.username)), reverse=True):
            activities = Activity.objects.filter(user=user.username)
            total_activities = activities.count()
            total_duration = sum(a.duration for a in activities) if activities else 0
            total_distance = sum(a.distance or 0 for a in activities) if activities else 0
            total_calories = sum(a.calories_burned or 0 for a in activities) if activities else 0

            team_name = 'Team Marvel' if user in marvel_users else 'Team DC'

            leaderboard = Leaderboard.objects.create(
                user=user.username,
                team=team_name,
                total_activities=total_activities,
                total_duration=total_duration,
                total_distance=total_distance,
                total_calories=total_calories,
                rank=rank
            )
            rank += 1

        self.stdout.write(self.style.SUCCESS('Created leaderboard entries'))

        # Create workouts
        workout_templates = [
            {
                'name': 'Full Body Workout',
                'description': 'A comprehensive full body workout',
                'exercises': ['Squats', 'Bench Press', 'Deadlifts', 'Pull-ups', 'Rows'],
                'difficulty': 'hard',
                'duration': 90
            },
            {
                'name': 'Cardio Blast',
                'description': 'High intensity cardio training',
                'exercises': ['Running', 'Burpees', 'Jump Rope', 'Mountain Climbers'],
                'difficulty': 'hard',
                'duration': 45
            },
            {
                'name': 'Upper Body Strength',
                'description': 'Focus on upper body muscle building',
                'exercises': ['Bench Press', 'Shoulder Press', 'Bicep Curls', 'Tricep Dips'],
                'difficulty': 'medium',
                'duration': 60
            },
            {
                'name': 'Lower Body Burn',
                'description': 'Intense lower body workout',
                'exercises': ['Squats', 'Leg Press', 'Leg Curls', 'Calf Raises'],
                'difficulty': 'medium',
                'duration': 60
            },
            {
                'name': 'Beginner Basics',
                'description': 'Basic workout for beginners',
                'exercises': ['Walking', 'Stretching', 'Light Weights'],
                'difficulty': 'easy',
                'duration': 30
            },
        ]

        for user in all_users:
            for _ in range(random.randint(1, 3)):
                template = random.choice(workout_templates)
                workout = Workout.objects.create(
                    user=user.username,
                    name=template['name'],
                    description=template['description'],
                    exercises=template['exercises'],
                    difficulty=template['difficulty'],
                    duration=template['duration']
                )

        self.stdout.write(self.style.SUCCESS('Created workouts'))
        self.stdout.write(self.style.SUCCESS('Database population completed successfully!'))
