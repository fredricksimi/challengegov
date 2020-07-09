from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.template.defaultfilters import slugify
from .forms import CreatePreapprovedChallengeForm
# from taggit.models import Tag
from django.db.models import Q, F
from django.utils import timezone
from datetime import datetime
from .models import Challenges, ChallengeTag
from django.core.paginator import Paginator, EmptyPage, InvalidPage
# from django.views.generic import ListView


"""This is a filter for Challenges with tags e.g Education, Science, Energy e.t.c"""
def tagged(request, id):
    tag = get_object_or_404(ChallengeTag, id=id)
    the_challenges = Challenges.objects.all().filter(Q(status='Open') | Q(status='Rolling'))
    challenges = the_challenges.filter(tags=tag).order_by('-date_posted')
    the_tags = ChallengeTag.objects.all()[:12]

    paginator = Paginator(challenges, 6)
    try:
        page = int(request.GET.get('page', '1'))
    except:
        page = 1
    try:
        posts = paginator.page(page)
    except(EmptyPage, InvalidPage):
        posts = paginator.page(paginator.num_pages)


    context = {
        'tag':tag,
        'the_tags':the_tags,
        'challenges':posts
    }
    return render(request, 'mainapp/tagged-detail.html', context)



"""This displays *some* of the challenges in the system"""

def home(request):

    latest_challenges = Challenges.objects.all().filter(status='Open').order_by('-date_posted').reverse()[:6]
    the_tags = ChallengeTag.objects.all()[:12]

    context = {
    'latest_challenges':latest_challenges,
    'the_tags':the_tags,
    "home_page": "active",

    'obcolor':'#5db97c',
    'ocolor':'#fff',

    'rbcolor':'#eb0678',
    'rcolor':'#fff'

    }
    return render(request, 'mainapp/index.html', context)

def all_categories(request):
    allcategories = ChallengeTag.objects.all()
    return render(request, 'mainapp/allcategories.html', {'allcategories':allcategories })

"""This displays all the latest challenges in the system"""
def challenges(request):
    posts_list = Challenges.objects.all().filter(Q(status='Open') | Q(status='Rolling')).order_by('-id')
    the_tags = ChallengeTag.objects.all()[:12]
    paginator = Paginator(posts_list, 6)

    try:
        page = int(request.GET.get('page', '1'))
    except:
        page = 1
    try:
        posts = paginator.page(page)
    except(EmptyPage, InvalidPage):
        posts = paginator.page(paginator.num_pages)

    context = {
    'the_tags':the_tags,
    'posts':posts,
    "challenge_page": "active",

    'obcolor':'#5db97c',
    'ocolor':'#fff',

    'abcolor':'#d61111',
    'acolor':'#fff',

    'pbcolor':'#f5cc04',
    'pcolor':'#000',

    'rbcolor':'#eb0678',
    'rcolor':'#fff'

    }
    return render(request, 'mainapp/challenges.html', context)

def open_challenges(request):
    challenges = Challenges.objects.all().filter(status='Open')
    the_tags = ChallengeTag.objects.all()[:12]
    paginator = Paginator(challenges, 6)

    try:
        page = int(request.GET.get('page', '1'))
    except:
        page = 1
    try:
        posts = paginator.page(page)
    except(EmptyPage, InvalidPage):
        posts = paginator.page(paginator.num_pages)

    context = {
        'challenges':posts,
        'bcolor':'#5db97c',
        'the_tags':the_tags,
        'color':'#fff'
        }
    return render(request, 'mainapp/open-challenges.html', context)

def coming_soon_challenges(request):
    challenges = Challenges.objects.all().filter(status='Coming Soon')
    the_tags = ChallengeTag.objects.all()[:12]
    paginator = Paginator(challenges, 6)

    try:
        page = int(request.GET.get('page', '1'))
    except:
        page = 1
    try:
        posts = paginator.page(page)
    except(EmptyPage, InvalidPage):
        posts = paginator.page(paginator.num_pages)

    context = {
        'challenges':posts,
        'bcolor':'#f5cc04',
        'the_tags':the_tags,
        'color':'#000'
    }
    return render(request, 'mainapp/coming-soon-challenges.html', context)

def archived_challenges(request):
    challenges = Challenges.objects.all().filter(status='Archived')
    the_tags = ChallengeTag.objects.all()[:12]
    paginator = Paginator(challenges, 6)

    try:
        page = int(request.GET.get('page', '1'))
    except:
        page = 1
    try:
        posts = paginator.page(page)
    except(EmptyPage, InvalidPage):
        posts = paginator.page(paginator.num_pages)

    context = {
        'challenges':posts,
        'bcolor':'#d61111',
        'the_tags':the_tags,
        'color':'#fff'
        }
    return render(request, 'mainapp/archived-challenges.html', context)

def rolling_challenges(request):
    challenges = Challenges.objects.all().filter(status='Rolling')
    the_tags = ChallengeTag.objects.all()[:12]
    context = {
        'challenges':challenges,
        'bbcolor':'#eb0678',
        'the_tags':the_tags,
        'ccolor':'#fff'
    }
    return render(request, 'mainapp/rolling-challenges.html', context)


def about(request):
    return render(request, 'mainapp/about.html')

def privacy_policy(request):
    return render(request, 'mainapp/privacy_policy.html')


"""This displays the details of a selected Challenge"""
@login_required
def challenge_detail(request, id, slug):
    the_tags = ChallengeTag.objects.all()
    allchallenges = Challenges.objects.all().order_by('-date_posted')[:3]
    the_post = get_object_or_404(Challenges, id=id, slug=slug)
    # related_challenges = Challenges.objects.all().filter(tags=rtags).order_by('-date_posted')[:3]
    context = {'the_post':the_post, 'allchallenges':allchallenges}
    return render(request, 'mainapp/detail.html', context)


def search_results(request):
    query = request.GET.get('q')
    challenges = Challenges.objects.filter(
    Q(title__icontains=query) | Q(description__icontains=query) |
    Q(challenge_summary__icontains=query) | Q(offered_by__icontains=query) |
    Q(status__icontains=query) | Q(targeted_audience__name__icontains=query) |
    Q(tags__name__icontains=query))

    paginator = Paginator(challenges, 4)

    try:
        page = int(request.GET.get('page', '1'))
    except:
        page = 1
    try:
        posts = paginator.page(page)
    except(EmptyPage, InvalidPage):
        posts = paginator.page(paginator.num_pages)

    context = {'posts':posts, 'query':query}

    return render(request, 'mainapp/search_results.html', context)


@login_required
def submit_a_challenge(request):
    if request.method == 'POST':
        form = CreatePreapprovedChallengeForm(request.POST or None)
        if form.is_valid():
            form.save()
            return redirect('mainapp:homepage')
    else:
        form = CreatePreapprovedChallengeForm()
    context = {'form':form}
    return render(request, 'mainapp/submit-a-challenge.html', context)
