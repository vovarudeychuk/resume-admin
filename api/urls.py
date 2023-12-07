from django.urls import path

from about.views import AboutListView
from account.views import CombinedAccountDataAPIView
from cv.views import CvApiView
from blog.views import BlogListView
from portfolio.views import PortfolioListView


from . import views

urlpatterns = [
    path('', views.getData),
    path('about/', AboutListView.as_view(), name='about-list'),
    path('account/', CombinedAccountDataAPIView.as_view(), name='account-list'),
    path('cv/', CvApiView.as_view(), name='cv-list'),
    path('blog/', BlogListView.as_view(), name='blog-list'),
    path('portfolio/', PortfolioListView.as_view(), name="portfolio-list")
]