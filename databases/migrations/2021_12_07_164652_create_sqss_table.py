"""CreateSqssTable Migration."""

from masoniteorm.migrations import Migration


class CreateSqssTable(Migration):
    def up(self):
        """
        Run the migrations.
        """
        with self.schema.create("sqss") as table:
            table.increments("id")
            table.string("borough")
            table.string("name")
            table.string("section")
            table.string("description")
            table.string("address")
            table.string("image")
            table.timestamps()

    def down(self):
        """
        Revert the migrations.
        """
        self.schema.drop("sqss")
