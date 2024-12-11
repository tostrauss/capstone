from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from . import views

app_name = 'djangoapp'

urlpatterns = [
    # Path for login
    path(route='login', view=views.login_user, name='login'),
    path(route='logout', view=views.logout_user, name='logout'),
    path(route='register', view=views.register_user, name='register'),

    # Placeholder: Path for dealer reviews view
    # path(route='dealer/<int:dealer_id>/reviews', view=views.get_dealer_reviews, name='dealer_reviews'),

    # Placeholder: Path for add a review view
    # path(route='dealer/<int:dealer_id>/add_review', view=views.add_review, name='add_review'),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

