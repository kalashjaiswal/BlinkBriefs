from django.urls import path
from summarizer import views

urlpatterns = [
    path("summarize-text", views.SummarizerView.as_view()),
    path("summarize-youtube", views.YoutubeSummarizerView.as_view()),
    path("summarize-news-articles", views.NewsArticleSummarizerView.as_view()),
    path("summarize-wikipedia", views.WikipediaSummarizerView.as_view()),
]
