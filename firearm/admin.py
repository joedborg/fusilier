from django.contrib import admin
from .models import Firearm, TYPES, CHARGES


class TypeFilter(admin.SimpleListFilter):
    title = 'Type'
    parameter_name = 'type'

    def lookups(self, request, model_admin):
        return enumerate(TYPES)

    def queryset(self, request, queryset):
        if self.value() or self.value() == 0:
            return queryset.filter(type=self.value())
        return queryset


class ChargeFilter(admin.SimpleListFilter):
    title = 'Charge'
    parameter_name = 'charge'

    def lookups(self, request, model_admin):
        return enumerate(CHARGES)

    def queryset(self, request, queryset):
        if self.value() or self.value() == 0:
            return queryset.filter(charge=self.value())
        return queryset


class FirearmAdmin(admin.ModelAdmin):
    list_filter = (TypeFilter, ChargeFilter)


admin.site.register(Firearm, FirearmAdmin)

