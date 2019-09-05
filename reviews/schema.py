import graphene
from graphene_django.types import DjangoObjectType
from reviews.models import Company, Product, Review


class CompanyType(DjangoObjectType):
    class Meta:
        model = Company


class ProductType(DjangoObjectType):
    class Meta:
        model = Product


class ReviewType(DjangoObjectType):
    class Meta:
        model = Review


class Query(graphene.ObjectType):
    all_companies = graphene.List(CompanyType)
    all_products = graphene.List(ProductType)
    all_reviews = graphene.List(ReviewType)

    company = graphene.Field(
        CompanyType, id=graphene.Int(), name=graphene.String()
    )
    product = graphene.Field(
        ProductType, id=graphene.Int(), name=graphene.String()
    )
    review = graphene.Field(
        ReviewType,
        id=graphene.Int(),
        comment=graphene.String(),
        stars=graphene.Int(),
    )

    def resolve_all_companies(self, info, **kwargs):
        return Company.objects.all()

    def resolve_all_products(self, info, **kwargs):
        return Product.objects.select_related("company").all()

    def resolve_all_reviews(self, info, **kwargs):
        return Review.objects.select_related("product").all()

    def resolve_company(self, info, **kwargs):
        id = kwargs.get("id")
        name = kwargs.get("name")

        if id is not None:
            return Company.objects.get(pk=id)

        if name is not None:
            return Company.objects.get(name=name)

        return None

    def resolve_product(self, info, **kwargs):
        id = kwargs.get("id")
        name = kwargs.get("name")

        if id is not None:
            return Product.objects.get(pk=id)

        if name is not None:
            return Product.objects.get(name=name)

        return None

    def resolve_review(self, info, **kwargs):
        id = kwargs.get("id")

        if id is not None:
            return Review.objects.get(pk=id)

        return None


schema = graphene.Schema(query=Query)
