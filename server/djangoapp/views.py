from django.http import JsonResponse
from django.contrib.auth import login, authenticate, logout
from django.views.decorators.csrf import csrf_exempt
import json
import logging

# Logger instance
logger = logging.getLogger(__name__)

@csrf_exempt
def login_user(request):
    """
    Handles login requests. Authenticates the user and logs them in.
    """
    if request.method == "POST":
        try:
            # Parse the JSON request body
            data = json.loads(request.body)
            username = data.get('userName')
            password = data.get('password')

            
            # Validate the input
            if not username or not password:
                return JsonResponse({"status": "failure", "message": "Missing username or password"}, status=400)

            # Authenticate the user
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return JsonResponse({"userName": username, "status": "Authenticated"})
            else:
                return JsonResponse({"status": "failure", "message": "Invalid credentials"}, status=401)
        except json.JSONDecodeError:
            return JsonResponse({"status": "failure", "message": "Invalid JSON format"}, status=400)
    return JsonResponse({"status": "failure", "message": "Invalid request method"}, status=405)

@csrf_exempt
def logout_user(request):
    """
    Handles logout requests. Logs the user out and clears session data.
    """
    logout(request)
    data = {"userName": ""}
    return JsonResponse(data)

@csrf_exempt
def register_user(request):
    """
    Handles registration requests. Creates a new user and logs them in.
    """
    if request.method == "POST":
        try:
            data = json.loads(request.body)
            username = data.get('userName')
            password = data.get('password')
            first_name = data.get('firstName')
            last_name = data.get('lastName')
            email = data.get('email')
            
            # Check if the username already exists
            if User.objects.filter(username=username).exists():
                return JsonResponse({"userName": username, "error": "Already Registered"}, status=400)
            
            # Create a new user
            user = User.objects.create_user(
                username=username,
                password=password,
                first_name=first_name,
                last_name=last_name,
                email=email
            )
            
            # Log the user in
            login(request, user)
            return JsonResponse({"userName": username, "status": "Authenticated"})
        
        except json.JSONDecodeError:
            return JsonResponse({"status": "failure", "message": "Invalid JSON format"}, status=400)
        except Exception as e:
            return JsonResponse({"status": "failure", "message": str(e)}, status=500)
    
    return JsonResponse({"status": "failure", "message": "Invalid request method"}, status=405)

# Placeholder for dealer reviews view
# def get_dealer_reviews(request, dealer_id):
#     """
#     Retrieves and renders dealer reviews for a specific dealer.
#     """
#     ...

# Placeholder for adding a review
# @csrf_exempt
# def add_review(request, dealer_id):
#     """
#     Handles adding a review for a specific dealer.
#     """
#     ...
