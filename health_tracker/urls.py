from django.urls import path
from . import views

urlpatterns = [

    # Dashboard/About Page
    path("", views.index, name="index"),

    # Authentication
    path("register", views.register, name="register"),
    path("login", views.login_view, name="login"),
    path("logout", views.logout_view, name="logout"),
    
    # Patient Dashboard URLs
    path("user/<str:id>", views.other_profile, name="other_profile"),
    path("health/<str:wbid>", views.health_status_function, name="health"),

    # Notifications URLs
    path("auth_messages", views.notification_page, name="auth_messages"),
    path("notifications", views.notifications, name="notifications"),

    # Files Search URLs
    path("myfiles", views.myfiles, name="myfiles"),
    path("search",views.search,name="search"),
    path("mydoctors_vendors",views.mydoctors_vendors,name="mydoctors_vendors"),
    path("mypatients_customers",views.mypatients_customers,name="mypatients_customers"),
    
    #  Public Doctor Search URLs
    path("visit/<str:id>",views.visit_qrcode,name="visit"),
    path("gopublic",views.go_public,name="go_public"),
    path("goprivate",views.go_private,name="go_private"),
    path("search_public",views.search_public_vendors,name="search_public"),

    # Covid Related URLs
    path("covid", views.covid, name="covid"),
    path("covid/info", views.covid_info, name="covid_info"),
    path("covid/norms", views.covid_norms, name="covid_norms"),
    path("covid/vaccination", views.covid_vaccinations, name="covid_vaccinations"),
   
   # Utility URLs
    path("upload", views.upload_file, name="upload_file"),
    path("media/<str:wbid>/<str:name>", views.file_page, name="file_page"),
    path("delete_file/<str:wbid>/<str:name>",views.delete_file,name="delete_file"),
    path("remove/<str:id>",views.remove_patient_vendor,name="remove_patient_vendor"),
    path('get_file/<str:wbid>/<str:name>', views.get_file, name="get_file"),
    path("edit/<str:wbid>/<str:file_name>",views.edit_file,name="edit_file"),
]

urlpatterns += [path('states', views.StatesAPI, name="states")]
