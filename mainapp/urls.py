from django.urls import path
from . import views

app_name="mainapp"
urlpatterns = [
    path('', views.home, name='homepage'),
    path('allcategories', views.all_categories, name='allcategories'),
    path('search', views.search_results, name='search_results'),
    path('challenges', views.challenges, name='challenges'),
    path('open-challenges', views.open_challenges, name='open-challenges'),
    path('coming-soon', views.coming_soon_challenges, name='coming-soon'),
    path('tags/<int:id>', views.tagged, name='tagged'),
    path('submit-challenge', views.submit_a_challenge, name='submit-a-challenge'),
    path('archived-challenges', views.archived_challenges, name='archived'),
    path('rolling-challenges', views.rolling_challenges, name='rolling'),
    path('detail/<int:id>/<slug:slug>/', views.challenge_detail, name='detail'),
    path('about', views.about, name="about"),
    path('privacy-policy', views.privacy_policy, name="privacy_policy"),
]
