from django.urls import path
from PopularWeb import views
urlpatterns = [
    path('',views.indexpg,name='indexpg'),
    path('contactpg/',views.contactpg,name='contactpg'),
    path('productpg/',views.productpg,name='productpg'),
    path('aboutpg/',views.aboutpg,name='aboutpg'),
    path('staffpg/',views.staffpg,name='staffpg'),
    path('displaycategory/<ItemCatg>/',views.displaycategory,name='displaycategory'),
    path('prodetail/<int:dataid>/',views.prodetail,name='prodetail'),

    path('login/',views.login,name='login'),
    path('loginsave/',views.loginsave,name='loginsave'),
    path('customerlogin/',views.customerlogin,name='customerlogin'),
    path('logout/',views.logout,name='logout'),
    path('contactsave/',views.contactsave,name='contactsave'),

    path('cart/',views.cart,name='cart'),
    path('cartsave/',views.cartsave,name='cartsave'),
    path('estimate/',views.estimate,name='estimate')

]