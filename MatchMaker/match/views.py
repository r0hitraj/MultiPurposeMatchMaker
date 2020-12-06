from django.shortcuts import render, get_object_or_404
from .models import Detail    # this import statement is used for database data to show on home
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
# LoginRequireMixin import will allow to create view only when logged in as user
# UserPassesTestMixin import will limit such that only the creator of Post could update it
from django.contrib.auth.models import User
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView
)


# Create your views here.
def home(request):
    context = {
        "details": Detail.objects.all()
    }
    return render(request, 'match/home.html', context)


class DetailListView(ListView):
    model = Detail
    template_name = 'match/home.html'    # <app>/<model>_<viewtype>.html
    context_object_name = 'details'
    ordering = ['-date_posted']         # ordering of posts by date
    paginate_by = 5                     # 5 posts per page


class UserDetailListView(ListView):
    model = Detail
    template_name = 'match/user_detail.html'
    context_object_name = 'details'
    paginate_by = 5

    def get_queryset(self):
        user = get_object_or_404(User, username=self.kwargs.get('username'))
        return Detail.objects.filter(author=user).order_by('-date_posted')


class DetailDetailView(DetailView):
    model = Detail


class DetailCreateView(LoginRequiredMixin, CreateView):
    model = Detail
    fields = ['Branch', 'Semester', 'Interests', 'cgpa']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class DetailUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Detail
    fields = ['Branch', 'Semester', 'Interests', 'cgpa']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        detail = self.get_object()
        if self.request.user == detail.author:
            return True
        return False


class DetailDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Detail
    success_url = '/'

    def test_func(self):
        detail = self.get_object()
        if self.request.user == detail.author:
            return True
        return False


def about(request):
    return render(request, 'match/about.html', {'title': "About"})

