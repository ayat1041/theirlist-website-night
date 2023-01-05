from platformdirs import user_state_path
from app.models import Feedback,List,MusicList,BookList,Review,MusicReview,BookReview,Profile,Starr,MusicStarr,BookStarr,Profile
from django.shortcuts import redirect, render, HttpResponse,HttpResponseRedirect
from django.urls import reverse_lazy,reverse
from django.views.generic import UpdateView,TemplateView,ListView,DetailView,CreateView,DeleteView
from django.core.paginator import Paginator
from datetime import timedelta
from django.utils import timezone
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from .forms import ProfileUpdateForm,FeedbackForm,ReviewForm,BookReviewForm,MusicReviewForm,StarrForm,MusicStarrForm,BookStarrForm

# Create your views here.
def profile(request):
    if request.method == 'POST':
        p_form = ProfileUpdateForm(request.POST,request.FILES,instance=request.user.profile)
        #u_form = UserUpdateForm(request.POST,instance=request.user)
        if p_form.is_valid(): #and u_form.is_valid():
            #u_form.save()
            p_form.save()
            #messages.success(request,'Your Profile has been updated!')
            return redirect('app:all')
    else:
        p_form = ProfileUpdateForm(instance=request.user)
        #u_form = UserUpdateForm(instance=request.user.profile)

    context={'p_form': p_form}
    return render(request, 'app/profile_form.html',context )


class HomeView(TemplateView):
    template_name = 'index.html'

class EditProfile(TemplateView):
    template_name = 'app/edit_profile.html'


def UserComments(request):
    movie = Review.objects.all()
    music = MusicReview.objects.all()
    book = BookReview.objects.all()
    movmu = movie.union(music)
    all = movmu.union(book)
    print(all)

    params = {'movie' : movie, 'music' : music, 'book' : book, 'all' : all}
    return render(request, 'app/user_comments.html', params)


def userpost(request):
    # movie = List.objects.all()
    # music = MusicList.objects.all()
    # book = BookList.objects.all()
    
    movie = List.objects.filter(posted__gte=timezone.now() - timedelta(days=5000)).all().order_by("-id")
    music = MusicList.objects.filter(posted__gte=timezone.now() - timedelta(days=5000)).all().order_by("-id")
    book = BookList.objects.filter(posted__gte=timezone.now() - timedelta(days=5000)).all().order_by("-id")
    

    # a = movie.union(music)
    # allPosts = a.union(book)
    allPosts = list(movie)
    allPostsmusic = list(music)
    allPostsbook = list(book)
    # p = Paginator(allPosts, 2)
    
    # allPosts = List.objects.filter(title__search=query)
    params = {'allPosts' : allPosts, 'allPostsmusic' : allPostsmusic, 'allPostsbook' : allPostsbook}
    return render(request, 'app/userposts.html', params)

class AboutUs(LoginRequiredMixin, TemplateView):
    template_name = 'app/about_us.html'
    login_url = "login"
    redirect_field_name = 'redirect_to'

class Chat(TemplateView):
    template_name = 'app/chat_room.html'

# class Feedback(TemplateView):
#     template_name = 'app/feedback.html'

class Guidelines(TemplateView):
    template_name = 'app/guidelines.html'

class TheirListBookView(ListView): #books
    model = BookList
    template_name ='app/Booklist_list.html'

    def get_queryset(self, *args, **kwargs):
        qs = super().get_queryset(*args, **kwargs)
        qs = qs.order_by("-id")
        return qs

class TheirListMusicView(ListView): #music
    model = MusicList
    template_name ='app/Musiclist_list.html'

    def get_queryset(self, *args, **kwargs):
        qs = super().get_queryset(*args, **kwargs)
        qs = qs.order_by("-id")
        return qs

class TheirListView(ListView): #movies
    model = List
    paginate_by = 8
    template_name ='app/List_list.html'

    def get_queryset(self, *args, **kwargs):
        qs = super().get_queryset(*args, **kwargs)
        qs = qs.order_by("-id")
        # qs = qs.filter(author__name="Ayat")
        # qs = qs.filter(genre__name="Drama")
        return qs
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        modell = Review.objects.all()
        # filmod = Review.objects.filter(Review.List.id == List.id).all()
        context["modam"] = modell
        return context

class TheirDetailBookView(DetailView): #books
    model = BookList
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        modell = BookReview.objects.all()
        bookstarr = BookStarr.objects.all()
        context["bookstarr"] = bookstarr
        context["modam"] = modell
        # context["form"] = BookReviewForm()
        return context

class TheirDetailMusicView(DetailView): #music
    model = MusicList
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        modell = MusicReview.objects.all()
        musicstarr = MusicStarr.objects.all()
        context["musicstarr"] = musicstarr
        context["modam"] = modell
        # context["form"] = MusicReviewForm()
        return context

class TheirDetailView(DetailView):
    model = List
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        modell = Review.objects.all()
        starr = Starr.objects.all()
        context["starr"] = starr
        context["modam"] = modell
        return context

class ListCreateBookView(CreateView): #book
    model = BookList
    # fields = "__all__"
    fields = ['title','genre','spoiler','content']
    success_url = reverse_lazy("app:booklist") 

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.creator = self.request.user
        self.object.save()
        form.save_m2m()
        return HttpResponseRedirect(self.get_success_url())

class ListCreateMusicView(CreateView): #music
    model = MusicList
    # fields = "__all__"
    fields = ['title','genre','content']
    success_url = reverse_lazy("app:musiclist") 

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.creator = self.request.user
        self.object.save()
        form.save_m2m()
        return HttpResponseRedirect(self.get_success_url())

class ListCreateView(CreateView):
    model = List
    fields = ['title','genre','spoiler','content']
    success_url = reverse_lazy("app:list") 

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.creator = self.request.user
        self.object.save()
        form.save_m2m()
        return HttpResponseRedirect(self.get_success_url())

class ListDeleteView(DeleteView):
    model = List
    success_url ="/home/all"
    template_name = "app/list_confirm_delete.html"
class MusicListDeleteView(DeleteView):
    model = MusicList
    success_url ="/home/all"
    template_name = "app/musiclist_confirm_delete.html"
class BookListDeleteView(DeleteView):
    model = BookList
    success_url ="/home/all"
    template_name = "app/booklist_confirm_delete.html"

class ListUpdateView(UpdateView):
    model = List
    fields = ['title','genre','spoiler','content']
    # template_name = "app/booklist_confirm_delete.html"
    success_url ="/home/all"
class MusicListUpdateView(UpdateView):
    model = MusicList
    fields = ['title','genre','content']
    # template_name = "app/booklist_confirm_delete.html"
    success_url ="/home/all"
class BookListUpdateView(UpdateView):
    model = BookList
    fields = ['title','genre','spoiler','content']
    # template_name = "app/booklist_confirm_delete.html"
    success_url ="/home/all"

def search(request):
    query = request.GET['query']
    allPoststit = List.objects.filter(title__icontains=query)
    allPostscont = List.objects.filter(content__icontains=query)
    genremovie = List.objects.all()
    allPostsl = allPoststit.union(allPostscont)
    allPoststitm = MusicList.objects.filter(title__icontains=query)
    allPostscontm = MusicList.objects.filter(content__icontains=query)
    genremusic = MusicList.objects.all()
    allPostsm = allPoststitm.union(allPostscontm)
    allPoststitb = BookList.objects.filter(title__icontains=query)
    allPostscontb = BookList.objects.filter(content__icontains=query)
    genrebook = BookList.objects.all()
    allPostsb = allPoststitb.union(allPostscontb)
    allPosts2 = allPostsl.union(allPostsm)
    allPosts = allPosts2.union(allPostsb)
    params = {'allPosts' : allPosts, 'query':query, 'genremovie': genremovie, 'genremusic': genremusic, 'genrebook': genrebook}
    return render(request, 'app/search.html', params)



def film(request,query=None):
    if not query:
        qs = List.objects.all()
    else:
        qs = List.objects.filter(genre__name__icontains=query)
    return render(request, 'app/film.html', {'query': qs, 'result' : query} )

def music(request,query=None):
    if not query:
        qs = MusicList.objects.all()
    else:
        qs = MusicList.objects.filter(genre__name__icontains=query)
    return render(request, 'app/music.html', {'query': qs, 'result' : query} )

def book(request,query=None):
    if not query:
        qs = BookList.objects.all()
    else:
        qs = BookList.objects.filter(genre__name__icontains=query)
    return render(request, 'app/book.html', {'query': qs, 'result' : query} )


def all(request):   
    movie = List.objects.filter(posted__gte=timezone.now() - timedelta(days=5000)).all().order_by("-id")
    music = MusicList.objects.filter(posted__gte=timezone.now() - timedelta(days=5000)).all().order_by("-id")
    book = BookList.objects.filter(posted__gte=timezone.now() - timedelta(days=5000)).all().order_by("-id")
    
    allPosts = list(movie)
    p = Paginator(allPosts, 2)
    allPostsmusic = list(music)
    allPostsbook = list(book)

    if request.user.is_authenticated:
        madefmovies = List.objects.filter(genre__id__in= request.user.profile.fav_movie_genre.all().values_list("id", flat=True))
        madefmusic = MusicList.objects.filter(genre__id__in= request.user.profile.fav_music_genre.all().values_list("id", flat=True))
        madefbooks = BookList.objects.filter(genre__id__in= request.user.profile.fav_Book_genre.all().values_list("id", flat=True))
        params = {'allPosts' : allPosts, 'allPostsmusic' : allPostsmusic, 'allPostsbook' : allPostsbook, 'madefmovies' : madefmovies, 'madefmusic' : madefmusic, 'madefbooks' : madefbooks}
    else:
        madefmovies = "nono"
        madefmusic = "nono"
        madefbooks = "nono"
        params = {'allPosts' : allPosts, 'allPostsmusic' : allPostsmusic, 'allPostsbook' : allPostsbook}

    return render(request, 'app/all.html', params)



def create_comment(request):
    context = {}
    form = ReviewForm(request.POST or None)
    if form.is_valid():
        form.save()
        print(form)
        # redirect_url = reverse("app:list_detail", kwargs={"slug": slug})
        # return redirect(redirect_url)
        return HttpResponseRedirect(request.META.get('HTTP_REFERER', '/'))
    else:
        context['form'] = form
        return render(request, "app/create_comment.html", context)
def create_musiccomment(request):
    context = {}
    form = MusicReviewForm(request.POST or None)
    if form.is_valid():
        form.save()
        return HttpResponseRedirect(request.META.get('HTTP_REFERER', '/'))
    else:
        context['form'] = form
        return render(request, "app/create_comment.html", context)

def create_bookcomment(request):
    context = {}
    form = BookReviewForm(request.POST or None)
    if form.is_valid():
        form.save()
        return HttpResponseRedirect(request.META.get('HTTP_REFERER', '/'))
    else:
        context['form'] = form
        return render(request, "app/create_bookcomment.html", context)


def create_starr(request):
    context = {}
    form = StarrForm(request.POST or None)
    if form.is_valid():
        form.save()
        return HttpResponseRedirect(request.META.get('HTTP_REFERER', '/'))
    else:
        context['form'] = form
        return render(request, "app/already_rated.html", context)
        

def create_musicstarr(request):
    context = {}
    form = MusicStarrForm(request.POST or None)
    if form.is_valid():
        form.save()
        return HttpResponseRedirect(request.META.get('HTTP_REFERER', '/'))
    else:
        context['form'] = form
        return render(request, "app/already_rated.html", context)

def create_bookstarr(request):
    context = {}
    form = BookStarrForm(request.POST or None)
    if form.is_valid():
        form.save()
        return HttpResponseRedirect(request.META.get('HTTP_REFERER', '/'))
    else:
        context['form'] = form
        return render(request, "app/already_rated.html", context)

def create_feedback(request):
    context = {}
    form = FeedbackForm(request.POST or None)
    if form.is_valid():
        form.save()
    context['form'] = form
    return render(request, "app/feedback.html", context)
