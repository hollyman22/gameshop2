from django.contrib import admin
from .models import (
    Category,
    Subcategory,
    Game,
    GameDl,
    Review,
    SubReview,
    # SystemRequirement,
)
admin.site.register(Category)
admin.site.register(Subcategory)
admin.site.register(Game)
admin.site.register(GameDl)
admin.site.register(Review)
admin.site.register(SubReview)
# admin.site.register(SystemRequirement)

