from django.views.generic import TemplateView
from apps.recipes.models import Recipe, Category
from django.contrib.auth import get_user_model

User = get_user_model()

class HomeView(TemplateView):
    template_name = 'home.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        # Statistics
        context['recipe_count'] = Recipe.objects.filter(is_published=True).count()
        context['user_count'] = User.objects.count()
        context['category_count'] = Category.objects.count()
        context['total_likes'] = 0  # You can calculate this if you have a Like model

        # Featured recipes (latest 6)
        context['featured_recipes'] = Recipe.objects.filter(is_published=True).order_by('-created_at')[:6]

        # Categories
        context['categories'] = Category.objects.all()

        return context