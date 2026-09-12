from django.urls import path

from . import views


urlpatterns = [

    # Home
    path(
        "",
        views.home,
        name="home"
    ),

    # About Me
    path(
        "about/",
        views.about,
        name="about"
    ),

    # Skills
    path(
        "skills/",
        views.skills,
        name="skills"
    ),

    # Projects
    path(
        "projects/",
        views.projects,
        name="projects"
    ),

    # Education
    path(
        "education/",
        views.education,
        name="education"
    ),

    # Contact
    path(
        "contact/",
        views.contact,
        name="contact"
    ),

]