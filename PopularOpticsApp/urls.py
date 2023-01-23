from django.urls import path
from PopularOpticsApp import views
urlpatterns = [
    path('index/',views.index,name='index'),
    path('cat/',views.cat,name='cat'),
    path('catsave/',views.catsave,name='catsave'),
    path('catdetails/',views.catdetails,name='catdetails'),
    path('catedit/<int:dataid>/',views.catedit,name='catedit'),
    path('catupdate/<int:dataid>/',views.catupdate,name='catupdate'),
    path('catdelete/<int:dataid>/',views.catdelete,name='catdelete'),

    path('addstaff/',views.addstaff,name='addstaff'),
    path('staffsave/',views.staffsave,name='staffsave'),
    path('staffdetails/',views.staffdetails,name='staffdetails'),
    path('staffedit/<int:dataid>/',views.staffedit,name='staffedit'),
    path('staffupdate/<int:dataid>/',views.staffupdate,name='staffupdate'),
    path('staffdelete/<int:dataid>/',views.staffdelete,name='staffdelete'),

    path('addpro/',views.addpro,name='addpro'),
    path('prosave/',views.prosave,name='prosave'),
    path('prodetails/',views.prodetails,name='prodetails'),
    path('proedit/<int:dataid>/',views.proedit,name='proedit'),
    path('proupdate/<int:dataid>/',views.proupdate,name='proupdate'),
    path('prodelete/<int:dataid>/',views.prodelete,name='prodelete'),

    path('',views.adminlogin,name='adminlogin'),
    path('adminlog/',views.adminlog,name='adminlog'),
    path('contactdetails/',views.contactdetails,name='contactdetails'),
    path('adminlogout/',views.adminlogout,name='adminlogout')

]