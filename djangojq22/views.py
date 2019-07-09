from django.shortcuts import render
from django.views.generic.edit import FormView,CreateView,UpdateView
from .forms import *
from django.http import  HttpResponseRedirect,HttpResponse
from django.conf import settings
from PIL import Image
from django.core.paginator import Paginator,EmptyPage,PageNotAnInteger
from django.views.generic import ListView

import os
# Create your views here.
def index(request):
    context_dict={}
#    return render(request, 'jqapp/checkbox_parameter.html', context=context_dict)
    return render(request, 'djangojq22/index.html', context=context_dict)

def save_picture_in_own_folder(self,form):
    self.object = form.save()
    category_pk = self.object.pk
    category = Category.objects.get(pk=category_pk)
    image_dir = settings.MEDIA_ROOT + '\images\\' + str(category_pk) + '\\'
    if not os.path.isdir(image_dir):
        os.mkdir(image_dir)
    myfile = category.picture.url
    filelist = myfile.split('/')
    filename = filelist[-1]
    im = Image.open(category.picture)
    im.save(image_dir + filename)
    category.picture = os.path.join(image_dir + filename)
    category.save()
    thumbnail=Thumbnail(category=category)
    size = (128, 128)
    im.thumbnail(size)
    im.save(image_dir + 'thumb.jpg')
    thumbnail.thumbpic=os.path.join(image_dir + 'thumb.jpg')
    thumbnail.save()

class CreateCategory(CreateView):
    template_name='djangojq22/Category.html'
    form_class = CategoryForm
    success_url = '/djangojq22/index'

    def form_valid(self, form):
        save_picture_in_own_folder(self,form)
        return HttpResponseRedirect(self.get_success_url())

class UpdateCategory(UpdateView):
    model = Category
    template_name='djangojq22/Category.html'
    form_class = CategoryForm
    success_url = '/djangojq22/index'
    def form_valid(self, form):
        save_picture_in_own_folder(self,form)
        return HttpResponseRedirect(self.get_success_url())

def show_category(request,category_pk):
    context_dict={}
    try:
        category=Category.objects.get(pk=category_pk)
        context_dict['category']=category
    except Category.DoesNotExist:
        context_dict['category']=None
        print("not exist")
    return render(request,'djangojq22/ShowCategory.html',context_dict)

def like_category(request):
    category_pk=None
    if request.method=='GET':
        category_pk=request.GET['category_pk']
        likes=0
        if category_pk:
            category=Category.objects.get(id=int(category_pk))
            if category:
                likes=category.likes+1
                category.likes=likes
                category.save()
    return HttpResponse(likes)

class CreateStudent(CreateView):
    template_name='djangojq22/Student.html'
    form_class = StudentForm
    success_url = '/djangojq22/index'

class CreateCategory2(CreateView):
    template_name='djangojq22/Category.html'
    form_class = CategoryFormM1
    success_url = '/djangojq22/index'

    def form_valid(self, form):
        save_picture_in_own_folder(self,form)
        return HttpResponseRedirect(self.get_success_url())

class CategoryList(ListView):
    model = Category
    context_object_name = 'my_favorite_categorys'
    paginate_by = 3

def listing(request):
    category_list = Category.objects.all()
    paginator = Paginator(category_list, 5) # Show 25 contacts per page

    page = request.GET.get('page')
    categorys = paginator.get_page(page)
    return render(request, 'djangojq22/list.html', {'categorys': categorys})