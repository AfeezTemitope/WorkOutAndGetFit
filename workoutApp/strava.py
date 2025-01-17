import os
import requests
from django.conf import settings
from django.http import JsonResponse
from django.shortcuts import redirect
from django.contrib.auth.models import AnonymousUser

STRAVA_API_URL = "https://www.strava.com/api/v3"


def strava_authenticate(request):
    """
    This view checks if the user has an existing Strava access token and fetches activities.
    If not, it starts the OAuth flow.
    """
    user = request.user

    # Check if the user already has a Strava access token
    if hasattr(user, 'strava_access_token') and user.strava_access_token:
        # Fetch Strava activities if the user is already authenticated
        return fetch_strava_activities(user.strava_access_token)
    else:
        # For anonymous users(user that is not logged in), store token in session
        if isinstance(user, AnonymousUser):
            strava_token = request.session.get('strava_access_token', None)
            if strava_token:
                return fetch_strava_activities(strava_token)

        # Redirect to Strava OAuth if no access token is found
        return redirect(
            f"{settings.STRAVA_AUTH_URL}?client_id={os.getenv('CLIENT_ID')}&redirect_uri={settings.STRAVA_REDIRECT_URI}&response_type=code&scope=activity:read")


def strava_callback(request):
    """
    This view handles the OAuth callback, exchanges the authorization code for an access token
    and stores the token either in the user's profile (if authenticated) or in the session (if anonymous).
    """
    code = request.GET.get('code')
    client_id = os.getenv('CLIENT_ID')
    client_secret = os.getenv('CLIENT_SECRET')
    redirect_uri = settings.STRAVA_REDIRECT_URI

    response = requests.post(
        'https://www.strava.com/oauth/token',
        data={
            'client_id': client_id,
            'client_secret': client_secret,
            'code': code,
            'grant_type': 'authorization_code',
            'redirect_uri': redirect_uri
        }
    )

    if response.status_code == 200:
        data = response.json()
        access_token = data['access_token']
        refresh_token = data['refresh_token']

        # Store the access token in the user's profile (if authenticated) or in session (if anonymous)
        user = request.user
        if user.is_authenticated:
            # Save the access token to the authenticated user's profile
            user.strava_access_token = access_token
            user.strava_refresh_token = refresh_token
            user.save()
        else:
            # Save the access token in the session for anonymous users
            request.session['strava_access_token'] = access_token
            request.session['strava_refresh_token'] = refresh_token

        return JsonResponse({"message": "Strava authentication successful."})
    else:
        return JsonResponse({"error": "Failed to authenticate with Strava."}, status=400)


def fetch_strava_activities(access_token):
    """
    Fetches the user's activities from Strava API using the provided access token.
    """
    response = requests.get(
        f"{STRAVA_API_URL}/athlete/activities",
        headers={"Authorization": f"Bearer {access_token}"}
    )

    if response.status_code == 200:
        activities = response.json()
        return JsonResponse({"activities": activities})
    return JsonResponse({"error": "Failed to fetch activities from Strava."}, status=400)
