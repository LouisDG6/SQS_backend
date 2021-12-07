"""Web Routes."""

from masonite.routes import Get, Post, Put, Delete, RouteGroup


ROUTES = [
    Get("/", "WelcomeController@show").name("welcome"),

    RouteGroup([Get("/", "SqsController@index").name("index"),
                Get("/@id", "SqsController@show").name("show"),
                Post("/", "SqsController@create").name("create"),
                Put("/@id", "SqsController@update").name("update"),
                Delete("/@id", "SqsController@destroy").name("destroy")
    ], prefix="/sqss", name="sqss")
]
