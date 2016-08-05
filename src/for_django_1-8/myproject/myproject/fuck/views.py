# -*- coding: utf-8 -*-
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse

from myproject.myapp.models import Document
from myproject.myapp.forms import DocumentForm
# from .forms import UploadFileForm


# def handle_uploaded_file(f):
#     with open('some/file/name.txt', 'wb+') as destination:
#         for chunk in f.chunks():
#             destination.write(chunk)

# def upload_file(request):
    # if request.method == 'POST':
    #     form = UploadFileForm(request.POST, request.FILES)
    #     if form.is_valid():
    #         handle_uploaded_file(request.FILES['file'])
    #         return HttpResponseRedirect('/success/url/')
    # else:
    #     form = UploadFileForm()
    # return render_to_response('upload.html', {'form': form})







# @csrf_exempt
def fuck(request):
    print "FFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF"
    # print request.uploaded_file

    if request.method == 'POST':
        form = DocumentForm(request.POST, request.FILES)
        print "//////////////////////////////////////////"
        # print request
        # print form


        print "//////////////////////////////////////////"

        if form.is_valid():
            newdoc = Document(docfile=request.FILES['docfile'])
            newdoc.save()
            # logger.debug(request)
            # logger.debug(request.POST)

            # Redirect to the document list after POST
            return HttpResponseRedirect(reverse('myproject.myapp.views.list_fuck'))
            # return render_to_response(
            #     'fuck.html',
            #     {'documents': documents, 'form': form},
            #     context_instance=RequestContext(request)
            # )
    else:
        form = DocumentForm()  # A empty, unbound form

    # Load documents for the list page
    documents = Document.objects.all()

    # Render list page with the documents and the form
    return render_to_response(
        'list.html',
        {'documents': documents, 'form': form},
        context_instance=RequestContext(request)
    )
