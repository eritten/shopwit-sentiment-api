from django.shortcuts import render
from .sentiment import analyze_sentiment
from .search import google_shopping_shop_search
from .specific_shop_search import google_shopping_shop_search as sp_search
from .assistant import product_query
from rest_framework.decorators import api_view
from rest_framework.response import Response
import os

# Create your views here.
open_ai_api_key = os.environ["OPEN_AI_KEY"]


api_key = 'd1bded552ea0e5d1a5c04c5794ad879e1ee3f5c3dff4626ac15de1b02c37e1c6'


@api_view(["GET"])
def analyze(request):
    message_content = request.GET.get("message")
    return Response({"message": analyze_sentiment(message_content)})


@api_view(["GET"])
def general_search(request):
    query = request.GET.get("query")
    products = google_shopping_shop_search(api_key, query)
    return Response(products)


@api_view(["GET"])
def search_shop(request):
    query = request.GET.get("query")
    shop = request.GET.get("shop")
    products = sp_search(api_key, query, shop)
    return Response(products)


@api_view(["GET"])
def ask_ai(request):
    product_details = request.GET.get("product_details")
    user_question = request.GET.get("user_question")
    answer = product_query(product_details, user_question, open_ai_api_key)
    return Response({"answer": answer})
