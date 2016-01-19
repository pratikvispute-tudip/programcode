from django.conf.urls import patterns, include, url
from django.contrib import admin
from userapp.views import UserFormView,UserLoginView,DashboardView,logoutView

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'userproject.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^register/',UserFormView.as_view()),
    url(r'^login/',UserLoginView.as_view(),name="login"),
    url(r'^dashboard/',DashboardView.as_view(),name="dashboard"),
    url(r'^logout/',logoutView.as_view(),name="logout")
)
