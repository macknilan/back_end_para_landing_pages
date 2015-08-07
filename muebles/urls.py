from django.conf.urls import url
from .views import HomeView, ComedoresTemplateDetailView, CocinasTemplateDetailView, ChifoniersTemplateDetailView, CunasTemplateDetailView

urlpatterns = [

    url(r'^$', HomeView.as_view(), name='home'),
#    url(r'^comedores/$', ComedoresListView.as_view(), name='comedores'),
#    url(r'^cocinas/$', CocinasListView.as_view(), name='cocinas'),
#    url(r'^chifoniers/$', ChifoniersListView.as_view(), name='chifoniers'),
#    url(r'^cunas/$', CunasListView.as_view(), name='cunas'),
    url(r'^comedores/(?P<slug>[\w\-]+)/$', ComedoresTemplateDetailView.as_view(), name='detailcomedores'),
    url(r'^cocinas/(?P<slug>[\w\-]+)/$', CocinasTemplateDetailView.as_view(), name='detailcocinas'),
    url(r'^chifoniers/(?P<slug>[\w\-]+)/$', ChifoniersTemplateDetailView.as_view(), name='detailchifoniers'),
    url(r'^cunas/(?P<slug>[\w\-]+)/$', CunasTemplateDetailView.as_view(), name='detailcunas'),
#    url(r'^login/$', LoginView.as_view(), name='login'),
#    url(r'^logout/$', 'django.contrib.auth.views.logout', {'next_page': '/'}),
#    url(r'^profile/(?P<slug>[\w\-]+)/$', ProfileView.as_view(), name='profile'),
#    url(r'^perfil/$', PerfilRedirectView.as_view(), name='perfil'),
#    url(r'^edituseruserprofile/$', EditUser_UserProfileDef, name='edituseruserprofile'),
#    url(r'session_security/', include('session_security.urls')),
#    url(r'^userupdate/(?P<slug>[\w\-]+)/$', UserUpdateView.as_view(), name='userupdate'),
#    url(r'^userprofileupdate/(?P<slug>[\w\-]+)/$', UserProfileUpdateView.as_view(), name='userprofileupdate'),
#    url(r'^userprofiledetail/(?P<slug>[\w\-]+)/$', UserProfileDetailView.as_view(), name='userprofiledetail'),
]

