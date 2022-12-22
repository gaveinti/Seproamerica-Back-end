from django.contrib import admin

# Register your models here.
class AbstractNotifyAdmin(admin.ModelAdmin):
    raw_id_fields=('destiny'),
    list_display=('destiny','actor','verbo','read','publico')
    list_filter=('level','read')

    def get_queryset(self,requests):
        qs=super(AbstractNotifyAdmin,self).get_queryset(requests)
        return qs.prefetch_related('actor')