from Blog import views
from django.urls import path


urlpatterns=[

    path('',views.PostListView.as_view(),name='blog_home'),
    path('post/<int:pk>/detail/', views.PostDetailView.as_view(),
         name='post_detail'),

    path('post/create/', views.PostCreateView.as_view(),
         name="post_create"),
    path('post/<int:pk>/update/', views.PostUpdateView.as_view(),
         name="post_update"),
    path('post/<int:pk>/delete/', views.PostDeleteView.as_view(),
         name='post_delete'),
    path('user/<str:username>/', views.UserPostListView.as_view(),
         name='user_posts'),
    path('responsive/', views.responsive_view, name='responsive'),

    # path('', views.home_view, name='blog_home'),
    path("about/", views.about, name='about'),
]
