import xadmin
from xadmin import views
from xadmin.plugins.auth import UserAdmin
from .models import EmailVerifyRecord, UserProfile, Banner


class UserProfileAdmin(UserAdmin):
    pass


class BaseSetting(object):
    enable_themes = True
    use_bootswatch = True


class GlobalSettings(object):
    site_title = 'DSH Admin'
    site_footer = 'DSH Admin'
    menu_style = 'accordion'


class EmailVerifyRecordAdmin(object):
    list_display = ['code', 'email', 'send_type', 'send_time']
    search_fields = ['code', 'email', 'send_type']
    list_filter = ['code', 'email', 'send_type', 'send_time']


class UserProfileAdmin(object):
    list_display = ['username', 'birthday', 'gender', 'address', 'mobile', 'image']
    search_fields = ['username', 'nick_name', 'birthday', 'gender', 'address', 'mobile', 'image']
    list_filter = ['username', 'nick_name', 'birthday', 'gender', 'address', 'mobile', 'image']


class BannerAdmin(object):
    list_display = ['title', 'image', 'url', 'index', 'add_time']
    search_fields = ['title', 'image', 'url', 'index', 'add_time']
    list_filter = ['title', 'image', 'url', 'index', 'add_time']


xadmin.site.register(EmailVerifyRecord, EmailVerifyRecordAdmin)
# xadmin.site.register(UserProfile, UserProfileAdmin)
xadmin.site.register(Banner, BannerAdmin)
xadmin.site.register(views.BaseAdminView, BaseSetting)
xadmin.site.register(views.CommAdminView, GlobalSettings)



