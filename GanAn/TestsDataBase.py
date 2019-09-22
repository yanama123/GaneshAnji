import sqlite3


class TestsDatabase:
    def __init__(self):
        print("Came to init")
        self.conn = sqlite3.connect('tests.db')
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
            # print("Couldn't create Employee table due to '{}'".format(e))

    def addTestResults(self, id, environment, test, crated_at, started_at, finished_at, status, logs):
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

    def updatetestresults(self, id, finished_at, status, logs):
        try:
            self.c.execute(
                "UPDATE testresults SET finished_at='{}',status='{}',logs='{}' WHERE id='{}'".format(finished_at,
                                                                                                     status, logs, id))
            self.conn.commit()
        except Exception as e:
            print(e.message)

    def getstatus(self, id):
        status = self.c.execute("SELECT status FROM testresults WHERE id= '{}'".format(id)).fetchone()
        print(status)
        return status

    def display(self):
        # print("{}".format(self.c.execute("""SELECT * FROM employees""")))
        result = self.c.execute("""SELECT * FROM testresults""").fetchall()
        # print(result)
        return result
        # print(self.c.fetchall())

    def __del__(self):
        self.conn.commit()
        self.conn.close()

# if __name__ == '__main__':
# test = TestsDatabase()
# test.addTestResults('testcase1','venv','test','1pm','2pm','3pm', 'Inprogress', 'Dumylog')
##test.display()
# test.updateSalaryDetails('testcase1','3pm', 'completed', 'Dummy success' )
# test.display()
# test.addTestResults('testcase1', 'venv', 'test2', '1pm22', '2pm22', '3pm', 'Inprogress', 'Dumy2222log')
# test.updateSalaryDetails('testcase1', '3pm', 'completed', 'Dummy success')
# test.getstatus('testcase1')
# test.display()
