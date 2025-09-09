from django.shortcuts import render
from django.contrib.auth import logout

# Logout view
def logout_view(request):
    logout(request)
    return render(request, "relationship_app/logout.html")