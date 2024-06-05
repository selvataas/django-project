from datetime import date,datetime
from django.shortcuts import get_object_or_404, redirect, render

from courses.forms import CourseCreateForm, UploadForm
from .models import Course, Category, UploadModel
from django.core.paginator import Paginator
import random, os
from django.contrib.auth.decorators import login_required, user_passes_test

data = {
    "programlama":"programlama kategorisine ait kurslar",
    "web-gelistirme":"web gelistirme kategorisine ait kurslar",
    "mobil":"mobil kategorisine ait kurslar",
}

db = {
    "courses": [
        {
            "title":"javascript kursu",
            "description":"javascript kurs açıklaması",
            "imageUrl":"https://th.bing.com/th/id/OIP.jRmiVqe48aRlay0NUb_r2QAAAA?rs=1&pid=ImgDetMain",
            "slug":"javascript-kursu",
            "date":datetime.now(),
            "isActive": True,
            "isUpdated": False
        },
        {
            "title":"python kursu",
            "description":"python kurs açıklaması",
            "imageUrl":"https://th.bing.com/th/id/OIP.ujO3LNmVkgw8umROCXKx4QHaEK?rs=1&pid=ImgDetMain",
            "slug":"python-kursu",
            "date":datetime.now(),
            "isActive":  False,
            "isUpdated": False

        },
        {
             "title":"web geliştirme kursu",
            "description":"web geliştirme kurs açıklaması",
            "imageUrl":"https://th.bing.com/th/id/R.57e269d772efb557362226367e9e2a63?rik=4E4g719M7vqo1w&pid=ImgRaw&r=0",
            "slug":"web-gelistirme-kursu",
            "date":datetime.now(),
            "isActive": True,
            "isUpdated": True
        },
    ],
    "categories": [
        { "id":1, "name":"programlama", "slug":"programlama" }, 
        { "id":2, "name":"web geliştirme", "slug":"web-gelistirme" },
        { "id":3, "name":"mobil uygulamalar", "slug":"mobil-uygulamalar" },        
        ]
}

def index(request):
    # list comphension
    kurslar = Course.objects.filter(isActive=1, isHome=1)
    kategoriler = Category.objects.all()
    #  for kurs in db["courses"]:
    #      if kurs ["isActive"] == True:
    #          kurslar.append(kurs)
    return render(request, 'courses/index.html', {
         'categories': kategoriler,
         'courses': kurslar
     })

def isAdmin(user):
    return user.is_superuser

@user_passes_test(isAdmin)
def create_course(request):
    if not request.user.is_superuser:
        return redirect('index')
    
    if request.method == "POST":
        form = CourseCreateForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect("/kurslar")
    else:
        form = CourseCreateForm()
    return render(request, "courses/create_course.html", {"form": form})

@user_passes_test(isAdmin)
def course_list(request):
    kurslar = Course.objects.all()
    return render(request, 'courses/index.html', {
         'courses': kurslar
     })

        # kurs = Course(
            #     title=form.cleaned_data[" title"],
            #     description=form.cleaned_data["description"],
            #     imageUrl=form.cleaned_data["imageUrl"],
            #     slug=form.cleaned_data["slug"])
            # kurs.save()   


        # kurs=Course(title=title, imageUrl=imageUrl, description=description, slug=slug, isActive=isActive, isHome=isHome)
        # kurs.save()
        # return redirect("/kurslar")

 

def upload(request):
    if request.method == "POST":
        form = UploadForm(request.POST, request.FILES)

        if form.is_valid(): 
            model = UploadModel(image=request.FILES["image"])
            model.save()
        # print(uploaded_image)
            return render(request, "courses/success.html")
    else:
        form = UploadForm()
    return render(request, "courses/upload.html", {"form": form})



def search(request):
    if "q" in request.GET and request.GET["q"] != "": 
        q = request.GET["q"]
        kurslar = Course.objects.filter(isActive=True, title__contains=q).order_by("date")
        kategoriler = Category.objects.all()
    else:
        return redirect("/kurslar")

    # paginator = Paginator(kurslar, 3)
    # page = request.GET.get('page', 1)
    # page_obj = paginator.page(page)

    # print(page_obj.paginator.count)
    # print(page_obj.paginator.num_pages)

    return render(request, 'courses/search.html',{
        'categories': kategoriler,
        'courses':kurslar,
    })


def details(request, slug):
    course = get_object_or_404(Course, slug=slug) 

    context = {
        'course ': course
    }
    return render(request, 'courses/details.html', context)

def getCoursesByCategory(request, slug):
    kurslar = Course.objects.filter(categories__slug=slug, isActive=True).order_by("date")
    kategoriler = Category.objects.all()

    paginator = Paginator(kurslar, 3)
    page = request.GET.get('page', 1)
    page_obj = paginator.page(page)

    return render(request, 'courses/list.html', {
        'categories': kategoriler,
        'page_obj': page_obj,
        'seciliKategori': slug
    })













    # try:
    #     category_text = data[category_name];
    #     return render(request, 'courses/kurslar.html', {
    #         'category': category_name,
    #         'category_text': category_text

    #     })
    # except:
    #      return HttpResponseNotFound("<h1>yanlış kategori seçimi</h1>")

# def  getCoursesByCategoryId(request, category_id):
#     # 1-2-3 =>
#     category_list = list(data.keys()) 
#     if(category_id > len(category_list)):
#         return HttpResponseNotFound("yanlış kategori seçimi")
    
#     category_name = category_list[category_id-1]

#     redirect_url = reverse('courses_by_category', args=[category_name])

#     return redirect(redirect_url)





