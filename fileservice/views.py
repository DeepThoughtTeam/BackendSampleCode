from django.shortcuts import render
from models import *
from django.http import Http404, HttpResponse
from django.utils.encoding import smart_str

def home(request):
  return render(request, 'file_upload_test.html')

def add_file(request, user_id=0):
  if 'file' not in request.FILES or 'name' not in request.POST:
    print "file post fail, lack name or file field"
    raise Http404
  file = request.FILES['file']
  name = request.POST['name']

  new_file = FileBase(file_content=file, file_name=name)
  new_file.save()
  return HttpResponse("OK")


def get_file(request):
  if request.method == 'GET':
    o = FileBase.objects.get(file_name=request.GET['name'])
    print o
    return HttpResponse("OK") 
  raise Http404


def download_file(request):
  if request.method != 'GET':
    raise Http404
  o = FileBase.objects.get(file_name='testfile')
  # filename = __file__ # Select your file here.
  # wrapper = FileWrapper(file(filename))
  # response = HttpResponse(wrapper, content_type='text/plain')
  # response['Content-Length'] = os.path.getsize(filename)
  # return response
  file_data = open("/Users/amaliujia/virenv/mysite/mysite/media/files/1.png").read()
  response = HttpResponse(file_data, content_type='application/force-download')
  response['Content-Disposition'] = 'attachment; filename=%s' % smart_str('1.png')
  #response['X-Sendfile'] = smart_str("../mysite/media/files/1.png")
  return response

  #file_path=request.GET['name']


