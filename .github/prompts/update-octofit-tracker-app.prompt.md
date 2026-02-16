```prompt
---
mode: 'agent'
model: 'GPT-4.1'
description: 'Update Django project and app files for the OctoFit Tracker application'
---

# Django App Updates

All Django project files are in the `octofit-tracker/backend/octofit_tracker` directory.

## Tasks

1. Update `octofit_tracker/settings.py`:
   - Configure MongoDB connection using Djongo with no authentication required
   - Ensure `octofit_tracker`, `rest_framework`, `corsheaders`, `djongo`, and `api` are in `INSTALLED_APPS`
   - Enable CORS to allow all origins, methods, and headers
   - Add CORS middleware configuration

2. Update `octofit_tracker/urls.py`:
   - Ensure `api/` points to the API routes
   - Include `api_root` view that serves as the API root endpoint
   - Use codespace environment variable for the base URL if available

3. Update `api/models.py`:
   - Create models for users, teams, activities, leaderboard, and workouts
   - Use Djongo's ObjectIdField for MongoDB object IDs
   - Add appropriate fields and metadata for each model

4. Update `api/serializers.py`:
   - Create serializers for each model
   - Convert ObjectId fields to strings in serializer output
   - Ensure proper serialization of all fields

5. Update `api/views.py`:
   - Create ViewSets for each model using REST framework
   - Implement `api_root` view that lists all available API endpoints
   - Ensure all CRUD operations are supported

6. Update `api/admin.py`:
   - Register all models with Django admin
   - Add appropriate list displays, search fields, and filters

7. Update `api/tests.py`:
   - Create test cases for API endpoints
   - Test CRUD operations for all models

## Notes
- Reference the instruction files in `.github/instructions/` for detailed guidelines
- All models use MongoDB collections instead of SQL tables
- The API should be accessible at `/api/` with a root endpoint at `/api/`
```
