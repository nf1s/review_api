from django.contrib import admin

from reviews.models import Company, Product, Review


class ReviewAdmin(admin.ModelAdmin):
    list_display = ('comment', 'product')
    list_filter = ('product__company__name', 'product__name')
    ordering = ('-date',)

    fieldsets = (
        (None, {'fields': ['product', 'comment', 'stars']}),
    )

    def get_readonly_fields(self, request, obj=None):
        if obj is None:
            return ()

        return 'product',


admin.site.register(Company)
admin.site.register(Product)
admin.site.register(Review, ReviewAdmin)
