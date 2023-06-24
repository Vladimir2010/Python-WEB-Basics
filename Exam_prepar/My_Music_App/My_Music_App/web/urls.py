from django.urls import path, include
from . views import home_page, add_album, album_details, edit_album, delete_album, profile_details, delete_profile



# • http://localhost:8000/ - home page
# • http://localhost:8000/album/add/ - add album page
# • http://localhost:8000/album/details/<id>/ - album details page
# • http://localhost:8000/album/edit/<id>/ - edit album page
# • http://localhost:8000/album/delete/<id>/ - delete album page
# • http://localhost:8000/profile/details/ - profile details page
# • http://localhost:8000/profile/delete/ - delete profile page

urlpatterns = [
    path("", home_page, name="home page"),

    path("album/", include([
        path("add/", add_album, name="add album"),
        path("details/<int:id>/", album_details, name="album details"),
        path("edit/<int:id>/", edit_album, name="edit album"),
        path("delete/<int:id>/", delete_album, name="delete album"),
        ])),

    path("profile/details/", profile_details, name="profile details"),
    path("profile/delete/", delete_profile, name="delete profile")

]


# add/", add_album, name="add album"),
#     path("album/details/<int:id>/", album_details, name="album details"),
#     path("album/edit/<int:id>/", edit_album, name="edit album"),
#     path("album/delete/<int:id>/", delete_album, name="delete album"),
#     path("profile/details/", profile_details, name="profile details"),