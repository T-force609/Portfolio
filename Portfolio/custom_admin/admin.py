from django.contrib import admin
from django.contrib.admin import AdminSite

# Register your models here.
class CustomAdminSite(AdminSite):
    site_header = 'Custom Admin'
    site_title = 'Custom Admin Portal'
    index_title = 'Welcome to Custom Admin'
    name = 'customadmin'

    def __ini__(self, name='customadmin'):
        super().__init__(name)

        self._template_overrides = {
            'admin/base.html': 'admin/custom_admin/base.html',
            'admin/base_site.html': 'admin/custom_admin/base_site.html',
            'admin/index.html': 'admin/custom_admin/index.html'
        }

    def get_template(self, template_name):
        if template_name in self._template_overrides:
            return self._template_overrides[template_name]
        return super().get_template(template_name)



custom_admin = CustomAdminSite(name='customadmin')