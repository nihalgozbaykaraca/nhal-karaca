from django.contrib import admin

# Register your models here.
from mptt.admin import MPTTModelAdmin, DraggableMPTTAdmin

from emlak.models import Category, Rentalad, Images, Location, Comment


class CategoryAdmin(admin.ModelAdmin):
    list_display = ['title', 'status', 'parent']
    list_filter = ['status', 'parent']

# admin.site.register



class CategoryAdmin2(DraggableMPTTAdmin):
    mptt_indent_field = "title"
    list_display = ('tree_actions', 'indented_title',
                    'related_rentalads_count', 'related_rentalads_cumulative_count')
    list_display_links = ('indented_title',)
    prepopulated_fields = {'slug': ('title',)}
    # inlines = [Category]
    def get_queryset(self, request):
        qs = super().get_queryset(request)

        # Add cumulative product count
        qs = Category.objects.add_related_count(
                qs,
                Rentalad,
                'category',
                'rentalads_cumulative_count',
                cumulative=True)

        # Add non cumulative product count
        qs = Category.objects.add_related_count(qs,
                 Rentalad,
                 'category',
                 'rentalads_count',
                 cumulative=False)
        return qs

    def related_rentalads_count(self, instance):
        return instance.rentalads_count
    related_rentalads_count.short_description = 'Related rentalads (for this specific category)'

    def related_rentalads_cumulative_count(self, instance):
        return instance.rentalads_cumulative_count
    related_rentalads_cumulative_count.short_description = 'Related rentalads (in tree)'

admin.site.register(Category, CategoryAdmin2)

class LocationAdmin2(DraggableMPTTAdmin):
    mptt_indent_field = "title"
    list_display = ('tree_actions', 'indented_title',
                    'related_rentalads_count', 'related_rentalads_cumulative_count')
    list_display_links = ('indented_title',)
    prepopulated_fields = {'slug': ('title',)}
    # inlines = [Category]
    def get_queryset(self, request):
        qs = super().get_queryset(request)

        # Add cumulative product count
        qs = Location.objects.add_related_count(
                qs,
                Rentalad,
                'location',
                'rentalads_cumulative_count',
                cumulative=True)

        # Add non cumulative product count
        qs = Location.objects.add_related_count(qs,
                 Rentalad,
                 'location',
                 'rentalads_count',
                 cumulative=False)
        return qs

    def related_rentalads_count(self, instance):
        return instance.rentalads_count
    related_rentalads_count.short_description = 'Related rentalads (for this specific location)'

    def related_rentalads_cumulative_count(self, instance):
        return instance.rentalads_cumulative_count
    related_rentalads_cumulative_count.short_description = 'Related rentalads (in tree)'

admin.site.register(Location, LocationAdmin2)

class RentaladImageInline(admin.TabularInline):
    model = Images
    readonly_fields = ('image_tag',)
    extra = 5


class RentaladAdmin(admin.ModelAdmin):
    list_display = ['title', 'image_tag', 'status', 'category']
    list_filter = ['status', 'category']
    prepopulated_fields = {'slug': ('title',)}
    inlines = [RentaladImageInline]

admin.site.register(Rentalad, RentaladAdmin)

class ImagesAdmin(admin.ModelAdmin):
    list_display = ['title','rentalad','image_tag']

admin.site.register(Images,ImagesAdmin)

class CommentAdmin(admin.ModelAdmin):
    list_display = ['subject','comment', 'status','create_at']
    list_filter = ['status']
    readonly_fields = ('subject','comment','ip','user','rentalad','rate','id')

admin.site.register(Comment,CommentAdmin)