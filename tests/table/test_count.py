from ..base import DBTestCase
from ..example_project.tables import Band


class TestCount(DBTestCase):
    def test_exists(self):
        self.insert_rows()

        response = (
            Band.select().count().where(Band.name == "Pythonistas").run_sync()
        )

        self.assertTrue(response == 1)