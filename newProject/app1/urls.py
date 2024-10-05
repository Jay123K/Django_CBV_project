from django.urls import path

from app1 import views

urlpatterns=[
    path('',views.PostListView.as_view(),name='post_list'),
    path('about',views.AboutView.as_view(),name='about'),
    path('/<pk>',views.PostDetailView.as_view(),name='post_detail'),
    path('post_new',views.CreatePostView.as_view(),name='post_new'),
    path('post/pk',views.PostUpdateView.as_view(),name='post_edit'),
    path('<pk>/delete/',views.PostDeleteView.as_view(),name='post_remove'),
    path('draft',views.DraftListView.as_view(),name='post_draft'),
    
]    