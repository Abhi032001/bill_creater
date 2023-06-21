from django.contrib import admin

# Register your models here.

from .models import Wedding

from .models import Girls

from .models import Kids

from .models import Album

from .models import Boy

from .models import Team

from .models import Admin_rk, Admin_ak


admin.site.register(Wedding)

admin.site.register(Girls)

admin.site.register(Kids)

admin.site.register(Album)

admin.site.register(Boy)

admin.site.register(Team)

admin.site.register(Admin_rk)

admin.site.register(Admin_ak)



# ============================bill========================

from .models import Invoice, LineItem

admin.site.register(Invoice)
admin.site.register(LineItem)
