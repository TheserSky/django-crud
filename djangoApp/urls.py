
from django.contrib import admin
from tasks import views
from django.urls import path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('signup/', views.signup, name='signup'),
    path('tasks/', views.tasks, name='tasks'),
    path('logout/',views.signout, name='logout'),
    path('signin/',views.signin, name='signin'),
    path('createTasks/',views.createTasks, name='createTasks'),
    path('tasks/<int:task_id>/',views.taskdetail, name='taskdetail'),
    path('taskCompleted/<int:task_id>/',views.taskCompleted, name='taskCompleted'),
    path('task_completed/',views.task_completed, name='task_completed'),
    path('taskDelete/<int:task_id>/',views.taskDelete, name='taskDelete')
]
