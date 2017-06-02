from django.contrib import admin
from .models import Visit, RANGES


class RangeFilter(admin.SimpleListFilter):
    title = 'Range'
    parameter_name = 'range'

    def lookups(self, request, model_admin):
        return enumerate(RANGES)

    def queryset(self, request, queryset):
        if self.value() or self.value() == 0:
            return queryset.filter(range=self.value())
        return queryset


class VisitAdmin(admin.ModelAdmin):
    list_filter = (RangeFilter,)


admin.site.register(Visit, VisitAdmin)
