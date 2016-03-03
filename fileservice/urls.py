from django.conf.urls import url

urlpatterns = [
  url(r'^add-file/$', 'fileservice.views.add_file'), 
  url(r'^get-file/$', 'fileservice.views.get_file'),
  url(r'^download/$', 'fileservice.views.download_file'),
  url(r'^$', 'fileservice.views.home')
]
