from django.shortcuts import render
from django.http import JsonResponse
from .utils import query_groq_api
from django.conf import settings
import os

def chat_view(request):
    if request.method == "POST":
        user_query = request.POST.get("query")
        response = query_groq_api(user_query)

        if "error" in response:
            return JsonResponse({"error": "Groq API failed"}, status=500)

        return JsonResponse({"response": response})

    return render(request, "index.html", {"api_key": settings.GROQ_API_KEY})

