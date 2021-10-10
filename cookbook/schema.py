import graphene
from graphene_django import DjangoObjectType

from ingredients.models import Category, Ingredient



"""First we make ObjectTypes, much like Serializers in DRF"""


class CategoryType(DjangoObjectType):
    class Meta:
        model = Category
        fields = ("id", "name", "ingredients")


class IngredientType(DjangoObjectType):
    class Meta:
        model = Ingredient
        fields = ("id", "name", "notes", "category")




"""Now we introduce GraphQL Queries"""

class Query(graphene.ObjectType):
    """We drop the endpoints/objects into the Query Object"""
    all_ingredients = graphene.List(IngredientType)
    category_by_name = graphene.Field(CategoryType, name=graphene.String(required=True))


    def resolve_all_ingredients(root, info):
        #We can optimize query count in the resolve method
        return Ingredient.objects.select_related("category").all()


    def resolve_category_by_name(root, info, name):
        try:
            return Category.objects.get(name=name)
        except Category.DoesNotExist:
            return None



schema = graphene.Schema(query=Query)