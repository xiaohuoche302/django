from django.contrib import admin
from .models import Player,Humen

# Register your models here.

class HumenInfo(admin.TabularInline):
    model = Humen
    extra = 2

class PlayerAdmin(admin.ModelAdmin):

    def get_rate_level(self):
        if self.rate >=9:
            return "goodgames"
        else:
            return "badgames"
    get_rate_level.short_description = "评价"
    #显示的字段
    list_display = ['name','rate',get_rate_level]
    #过滤的条件
    list_filter = ['rate','desc']
    #搜索的字段
    search_fields = ['name','rate','desc']
    #分页
    list_per_page = 1
    #分组
    fieldsets = [
        ("基本信息",{'fields':("name","desc",)}),
        ("附加信息",{'fields':("rate",)})
    ]
    inlines = [HumenInfo]



admin.site.register(Player,PlayerAdmin)
admin.site.register(Humen)

# class MyAdmin(admin.AdminSite):
#     site_header = "大大学堂"
#     site_title = "免费教学"
#     site_url = "http://www.baidu.com"
