""" A SqsController Module """

from masonite.controllers import Controller
from masonite.request import Request
from app.Sqs import Sqs


class SqsController(Controller):
    """Class Docstring Description
    """

    def __init__(self, request: Request):
        self.request = request

    def show(self):
        """Show a single resource listing
        ex. Model.find('id')
            Get().route("/show", SqsController)
        """

        id = self.request.param("id")
        return Sqs.find(id)

    def index(self):
        """Show several resource listings
        ex. Model.all()
            Get().route("/index", SqsController)
        """
        return Sqs.all()

        

    def create(self):
        """Show form to create new resource listings
         ex. Get().route("/create", SqsController)
        """
        borough = self.request.input("borough")
        name = self.request.input("name")
        section = self.request.input("section")
        description = self.request.input("description")
        address = self.request.input("address")
        image = self.request.input("image")
        sqs = Sqs.create({"borough": borough, "name": name, "section": section, "description": description, "address": address, "image": image})
        return sqs

    def update(self):
        """Edit an existing resource listing
        ex. Post target to update new Model
            Post().route("/update", SqsController)
        """
        borough = self.request.input("borough")
        name = self.request.input("name")
        section = self.request.input("section")
        description = self.request.input("description")
        address = self.request.input("address")
        image = self.request.input("image")
        id = self.request.param("id")
        Sqs.where("id", id).update({"borough": borough, "name": name, "section": section, "description": description, "address": address, "image": image})
        return Sqs.where("id", id).get()

    def destroy(self):
        """Delete an existing resource listing
        ex. Delete().route("/destroy", SqsController)
        """
        id = self.request.param("id")
        sqs = Sqs.where("id", id).get()
        Sqs.where("id", id).delete()
        return sqs
        