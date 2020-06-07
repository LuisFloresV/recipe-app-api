from rest_framework import serializers

from core.models import Tag, Ingredient,Recipe


class TagSerializer(serializers.ModelSerializer):
    """Serializer for Tag Model"""


    class Meta:
        model = Tag
        fields = ('id','name')
        read_only_fields = ('id',)

class IngredientSerializer(serializers.ModelSerializer):
    """Serializer for Ing Model"""


    class Meta:
        model = Ingredient
        fields = ('id','name')
        read_only_fields = ('id',)


class RecipeSerializer(serializers.ModelSerializer):
    """Serializer for Recipe Model"""

    ingredients = serializers.PrimaryKeyRelatedField(
        many= True,
        queryset = Ingredient.objects.all()
    )

    tags = serializers.PrimaryKeyRelatedField(
        many= True,
        queryset = Tag.objects.all()
    )

    class Meta:
        model = Recipe
        fields = ('id','title','ingredients','tags','time_minutes','price','link')
        read_only_fields = ('id',)

class RecipeDetailSerializer(RecipeSerializer):
    """Serializer for Recipe Detail"""

    ingredients = IngredientSerializer(many=True, read_only=True)
    tags = serializers.PrimaryKeyRelatedField(
        many= True,
        read_only=True
    )

class RecipeImageSerializer(serializers.ModelSerializer):
    """ser for image upload"""
    class Meta:
        model = Recipe
        fields = ('id','image')
        read_only_fields = ('id',)






