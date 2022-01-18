## Title
ToDo app with authentication in django



##
Installation

pip install django

pip install mysql

##
Usage

Import django.urls

import Views

import models




##
Example

urlpatterns = [
    path('login/', CustomLoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(next_page='login'), name='logout'),
    path('register/', RegisterPage.as_view(), name='register'),
    ]
    
    
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('base.urls')),
]   

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'djangoecom',
        'HOST': 'localhost',
        'USER': 'root',
        'PASSWORD': '',
        'PORT':'3306',
    }
}



![image](https://user-images.githubusercontent.com/79367834/149776401-0634b0fc-131c-4239-8bc6-9b2c8cd36d97.png)
![image](https://user-images.githubusercontent.com/79367834/149776591-54e9a36a-e689-49b4-b29a-2282ae77acc0.png)

