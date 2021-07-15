from . import views
from django.urls import path
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
# vijay003.pythonanywhere.com
urlpatterns = [
    path('', views.home, name="home"),

    path('register/', views.register, name='register'),
    path('viewdata/', views.viewdata, name='viewdata'),
    path('delete/<str:email>', views.delete, name='delete'),
    path('supdate/<str:email>', views.supdate, name='supdate'),
    path('update/', views.update, name='update'),

    path('userReg/', views.userReg, name='userReg'),
    path('ulogin/', views.ulogin, name='ulogin'),
    path('dlogin/', views.dlogin, name='dlogin'),
    path('uregister/', views.uregister, name='uregister'),
    path('userLog/', views.userLog, name='userLog'),
    path('docLog/', views.dogLog, name='docLog'),
    path('dregister/', views.dregister, name='dregister'),
    path('docReg/', views.docReg, name='docReg'),
    # path('userprofile/',views.userprofile,name='userprofile'),
    path('logout/', views.logout, name='logout'),
    path('userProfile/', views.userProfile, name='userProfile'),
    path('docProfile/', views.docProfile, name='docProfile'),
    path('edituserprofile/', views.edituserprofile, name='editUserProfile'),
    path('userupdate/', views.userupdate, name='userupdate'),
    path('docupdate/', views.docupdate, name='docupdate'),
    path('editdocprofile/', views.editdocprofile, name='editdocprofile'),
    path('submitmessage/', views.submitmessage, name='submitmessage'),
    path('uploaddocument/', views.uploaddocument, name='uploaddocument'),
    path('upload/', views.upload, name='upload'),
    path('viewdoc/', views.viewdoc, name='viewdoc'),
    path('download/<str:filename>', views.download, name='download')
]
