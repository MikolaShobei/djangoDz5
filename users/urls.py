from django.urls import path


from users.views import CreateUserView, AddProfileView, MakeStaffView, FullOwnInfoView, DeleteUserView, \
    UpdateUserByUserView, ListUsersView, UpdateByStaffView

urlpatterns = [
    path('/create', CreateUserView.as_view()),
    path('/list', ListUsersView.as_view()),
    path('/<int:pk>/profile', AddProfileView.as_view()),
    path('/info', FullOwnInfoView.as_view()),
    path('/<int:pk>/make_staff', MakeStaffView.as_view()),
    path('/<int:pk>/delete', DeleteUserView.as_view()),
    path('/update_myself', UpdateUserByUserView.as_view()),
    path('/<int:pk>/update_by_staff', UpdateByStaffView.as_view())
]
