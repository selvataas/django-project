from datetime import date,datetime
from django.shortcuts import get_object_or_404, redirect, render
from .models import Course, Category
from django.core.paginator import Paginator

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
            "imageUrl":"https://www.bing.com/images/search?view=detailV2&ccid=jRmiVqe4&id=88887D85E76E91D304C542199E1881A5B877A1FF&thid=OIP.jRmiVqe48aRlay0NUb_r2QAAAA&mediaurl=https%3A%2F%2Fhoudoukyokucho.com%2Fwp-content%2Fuploads%2F2022%2F05%2FJavaScript-2.png&cdnurl=https%3A%2F%2Fth.bing.com%2Fth%2Fid%2FR.8d19a256a7b8f1a4656b2d0d51bfebd9%3Frik%3D%252f6F3uKWBGJ4ZQg%26pid%3DImgRaw%26r%3D0&exph=236&expw=400&q=javascript&simid=608043335525471524&form=IRPRST&ck=1C43CFEC16FEA252872A7A0CE9143257&selectedindex=0&itb=0&ajaxhist=0&ajaxserp=0&cit=ccid_rcbv%2BbKz*cp_2321E703672A4E069AAA604685C5A10A*mid_9162A91C3FB6C5B7FD0E8F0781947416A5850BEE*simid_608041003353062594*thid_OIP.rcbv-bKzGSyPbclJg6moBwEsB4&vt=2&sim=11",
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
            "date":date(2022,9,10),
            "isActive":  False,
            "isUpdated": False

        },
        {
             "title":"web geliştirme kursu",
            "description":"web geliştirme kurs açıklaması",
            "imageUrl":"https://th.bing.com/th/id/R.57e269d772efb557362226367e9e2a63?rik=4E4g719M7vqo1w&pid=ImgRaw&r=0",
            "slug":"web-gelistirme-kursu",
            "date":date(2022,8,10),
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

def create_course(request):
    if request.method == "POST":
        title=request.POST["title"]
        imageUrl=request.POST["imageUrl"]
        description = request.POST["description"]
        slug = request.POST["slug"]
        isActive = request.POST.get("isActive", False)
        isHome = request.POST.get("isHome", False)
        print(title, description, slug, isActive, isHome)

        if isActive == "on":
            isActive = True
        
        if isHome == "on":
            isHome = True

        kurs=Course(title=title, imageUrl=imageUrl, description=description, slug=slug, isActive=isActive, isHome=isHome)
        kurs.save()
        return redirect("/kurslar")
    return render(request, "courses/create_course.html")

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





