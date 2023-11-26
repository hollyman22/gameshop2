from rest_framework import serializers
from .models import (
    Category,
    Subcategory,
    Game,
    GameDl,
    Review,
    SubReview,
    # SystemRequirement,
)

class GameSerializer(serializers.ModelSerializer):
    class Meta:
        model = Game
        fields = ('name', 'discription', 'price')

class FullGameSerializer(serializers.ModelSerializer):
    class Meta:
        model = Game
        fields = '__all__'

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ('name')

class SubCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Subcategory
        fields = ('name', 'category__name')

class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = '__all__'

class SubReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = SubReview
        fields = '__all__'

class GameDLSerializer(serializers.ModelSerializer):
    class Meta:
        model = GameDl
        fields = ('name', 'game__name')

class FullGameDLSerializer(serializers.ModelSerializer):
    class Meta:
        model = GameDl
        fields = '__all__'


# class SystemRequirementSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = SystemRequirement
#         fields = '__all__'