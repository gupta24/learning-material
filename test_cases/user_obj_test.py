import unittest
import psycopg2



class ConnectDB:
    """
    Use to connect the database to get some object for testing
    """
    def __init__(self):
        self.conn_url  = psycopg2.connect(database="user", user="postgres", password="pass", host="localhost", port=5432)
        
    def close_conn(self):
        self.conn_url.close()



class TestUserObjecTest(unittest.TestCase):
    """
    Use to test the user object with different objects keys

    Test :
        python3 -m unittest user_obj_test.py
    """
    def setUp(self):
        self.db = ConnectDB()
        self.cursor = self.db.conn_url.cursor(cursor_factory=psycopg2.extras.NamedTupleCursor)
        self.query = f"SELECT * FROM user_content_modify LIMIT 1;"
        self.cursor.execute(query=self.query)
        self.content_data = self.cursor.fetchall()


    def test_user_obj_actions(self):
        # use to test available action for the object
        expected = True
        for data_indices in self.content_data:
            for media_row in data_indices[1]["media_rows"]:
                #print(f"media row type: {media_row['type']}, media item title: {media_row['title']}")
                for item in media_row["media_items"]:
                    if (item["actions"] == None) or (item["actions"]== {}):
                        expected = False
                        break
                if expected == False:
                    break
            if expected == False:
                break

        self.assertTrue(expected)


    def test_user_obj_images(self):
        # use to test available images for the object
        expected = True
        for data_indices in self.content_data:
            for media_row in data_indices[1]["media_rows"]:
                #print(f"media row type: {media_row['type']}, media item title: {media_row['title']}")
                for item in media_row["media_items"]:
                    if (item["image"] == None) and (item["image_hd"] == None):
                        expected = False
                        break
                if expected == False:
                    break
            if expected == False:
                break

        self.assertTrue(expected)