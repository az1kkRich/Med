from django.shortcuts import render
from .models import *
from django.views.generic import DetailView, ListView

# Create your views here.
def index(request):
    ser = ServicesImg.objects.all()
    last = LatestBlog.objects.all()
    mem = Member.objects.all().order_by('-date')[0:5]
    tes = Testimonial.objects.all()
    pag = Page.objects.all()

    context = {'ServicesImg':ser, 'LatestBlog':last, 'Member':mem, 'Testimonial':tes, 'Page':pag}
    return render(request, 'index.html', context)

def about(request):
    mem1 = Member.objects.all()
    tes1 = Testimonial.objects.all()
    pag = Page.objects.all()

    context = {'Member':mem1, 'Testimonial':tes1, 'Page':pag}
    return render(request, 'about.html', context)

def team(request):
    mem1 = Member.objects.all()
    pag = Page.objects.all()
    context = {'Member':mem1, 'Page':pag}
    return render(request, 'team.html', context)

def galery(request):
    pag = Page.objects.all()
    context = {'Page':pag}

    return render(request, 'grid-gallery.html', context)


def timatables(request):
    pag = Page.objects.all()
    context = {'Page':pag}
    return render(request, 'timetable.html', context)

def departaments(request):
    pag = Page.objects.all()

    context = {'Page':pag}

    return render(request, 'departments.html', context)

def contact(request):
    pag = Page.objects.all()
    context = {'Page':pag}

    return render(request, 'contacts.html', context)

def blog(request):
    last = LatestBlog.objects.all()
    pag = Page.objects.all()

    context = {'LatestBlog':last, 'Page':pag}
    return render(request, 'blog-masonry.html', context)

def services(request):
    pag = Page.objects.all()
    context = {'Page':pag}

    return render(request, 'services.html', context)

def make(request):
    pag = Page.objects.all()
    context = {'Page':pag}

    return render(request, 'make-an-appointment.html', context)

class member_detail(DetailView):
    model = Member
    template_name = 'team-member.html'
    context_object_name = 'more'

class page_detail(DetailView):
    model = Page
    template_name = 'page.html'
    context_object_name = 'more'