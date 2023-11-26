from rest_framework.generics import ListAPIView, RetrieveAPIView
from .models import (
    Category,
    Subcategory,
    Game,
    GameDl,
    Review,
    SubReview,
    # SystemRequirement,
)
from .serializers import(
    GameSerializer,
    CategorySerializer,
    SubCategorySerializer,
    ReviewSerializer,
    SubReviewSerializer,
    GameDLSerializer,
    # SystemRequirementSerializer,
)

class GameView(ListAPIView):
    queryset = Game.objects.all()
    serializer_class = GameSerializer
class GameView(ListAPIView):
    queryset = Game.objects.all()
    serializer_class = GameSerializer
