from django.shortcuts import render


def HomePageView(request):
    return render(request,"cat_base/home_page.html")