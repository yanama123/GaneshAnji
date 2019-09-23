import sqlite3


class TestsDatabase:
    def __init__(self):
        print("Came to init")
        self.conn = sqlite3.connect('results.db')
        print('connecyed')
        # self.conn = sqlite3.connect(':memory:')
        self.c = self.conn.cursor()

        try:
            self.c.execute("""CREATE TABLE IF NOT EXISTS testresults(
                id text PRIMARY KEY,
                environment text,
                test text,
                created_at text,
                started_at text,
                finished_at text,
                status text,
                logs text
                )""")

        except sqlite3.OperationalError as e:
            pass

    def add_test_results(self, id, environment, test, crated_at, started_at, finished_at, status, logs):
        """

        :param id:
        :param environment:
        :param test:
        :param crated_at:
        :param started_at:
        :param finished_at:
        :param status:
        :param logs:
        :return:
        """
        self.id = id
        self.environment = environment
        self.test = test
        self.created_at = crated_at
        self.started_at = started_at
        self.finished_at = finished_at
        self.status = status
        self.logs = logs

        try:
            self.c.execute("INSERT INTO testresults VALUES ('{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}' )"
                           .format(self.id, self.environment, self.test, self.created_at,
                                   self.started_at, self.finished_at, self.status, self.logs))
        except sqlite3.IntegrityError as e:
            print("Failed to Insert the element due to - {}".format(e))
        self.conn.commit()

    def update_test_results(self, id, finished_at, status, logs):
        """

        :param id:
        :param finished_at:
        :param status:
        :param logs:
        :return:
        """
        try:
            self.c.execute(
                "UPDATE testresults SET finished_at='{}',status='{}',logs='{}' WHERE id='{}'".format(finished_at,
                                                                                                     status, logs, id))
            self.conn.commit()
        except Exception as e:
            print(e.message)

    def get_status(self, id):
        """

        :param id:
        :return:
        """
        status = self.c.execute("SELECT status FROM testresults WHERE id= '{}'".format(id)).fetchall()
        return status

    def display(self):
        """

        :return:
        """
        result = self.c.execute("""SELECT * FROM testresults""").fetchall()
        return result

    def __del__(self):
        self.conn.commit()
        self.conn.close()

