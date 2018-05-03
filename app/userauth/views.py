from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse
from django.views.generic import DetailView, ListView, RedirectView, UpdateView

from .models import CustomUser


class UserDetailView(LoginRequiredMixin, DetailView):
    model = CustomUser
    # These next two lines tell the view to index lookups by username (empid)
    slug_field = "empid"
    slug_url_kwarg = "empid"


class UserRedirectView(LoginRequiredMixin, RedirectView):
    permanent = False

    def get_redirect_url(self):
        return reverse("users:detail", kwargs={"empid": self.request.user.empid})


class UserUpdateView(LoginRequiredMixin, UpdateView):

    fields = ["name", "empid", "emp_type", "street", "postcode", "city", "phone"]

    # we already imported User in the view code above, remember?
    model = CustomUser

    # send the user back to their own page after a successful update

    def get_success_url(self):
        return reverse("users:detail", kwargs={"empid": self.request.user.empid})

    def get_object(self):
        # Only get the User record for the user making the request
        return CustomUser.objects.get(empid=self.request.user.empid)


class UserListView(LoginRequiredMixin, ListView):
    model = CustomUser
    # These next two lines tell the view to index lookups by username
    slug_field = "empid"
    slug_url_kwarg = "empid"
