"""Web Routes."""

from masonite.routes import Get, Post, Put, Delete, RouteGroup


ROUTES = [
    Get("/", "WelcomeController@show").name("welcome"),

    RouteGroup([Get("/", "SqsController@index").name("index"),
                Get("/manhattan", "SqsController@show_mh").name("show_mh"),
                Get("/bronx", "SqsController@show_bx").name("show_bx"),
                Get("/queens", "SqsController@show_qn").name("show_qn"),
                Get("/brooklyn", "SqsController@show_bk").name("show_bk"),
                Get("/staten_island", "SqsController@show_si").name("show_si"),
                Get("/@id", "SqsController@show").name("show"),
                Post("/", "SqsController@create").name("create"),
                Put("/@id", "SqsController@update").name("update"),
                Delete("/@id", "SqsController@destroy").name("destroy")
    ], prefix="/sqs", name="sqs")
]
