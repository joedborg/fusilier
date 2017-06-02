from django.contrib import admin
from .models import Member


class ProvisionalFilter(admin.SimpleListFilter):
    title = 'Membership Status'
    parameter_name = 'is_provisional'

    def lookups(self, request, model_admin):
        return [
            (True, 'Is Provisional'),
            (False, 'Is Full Member')
        ]

    def queryset(self, request, queryset):
        if self.value() or self.value() is False:
            return queryset.filter(is_provisional=self.value())
        return queryset


class MemberAdmin(admin.ModelAdmin):
    list_filter = (ProvisionalFilter,)


admin.site.register(Member, MemberAdmin)
