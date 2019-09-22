import os
import sys
import datetime
import subprocess
import time
from testdatabase import TestsDatabase
from datetime import datetime
TEST_DESCRIPTION = 'Dummy test description'

test = TestsDatabase()
def readTestCases(testcase):
    if "," not in testcase:
        update_precomplition(testcase)
        update_postcompilation(testcase)

    else:
        testcase = testcase.split(',')
        # print("List is : {}".format(li))
        for tc in testcase:
            update_precomplition(tc)


def update_precomplition(testcase):
    current_now = datetime.now()
    environment = os.environ['VIRTUAL_ENV']
    fmttime = current_now.strftime("%d/%m/%Y %H:%M:%S")
    print("'{}' is the TestCase TestRunner is going to run".format(testcase))
    started_at = fmttime
    created_at = time.ctime(os.path.getctime(testcase))

    print("Start time : {}".format(started_at))
    print("Creation time : {}".format(created_at))
    test.addTestResults(testcase, environment, TEST_DESCRIPTION, created_at, started_at,
                             finished_at='N/A', status='In Progress', logs='N/A')
    # process = subprocess.Popen([sys.executable, testcase], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    # if process.stdout:
    #     print(process.communicate())


def update_postcompilation(testcase):
    print("'{}' is the TestCase TestRunner is going to run".format(testcase))
    process = subprocess.Popen([sys.executable, testcase], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    if process.stdout:
        log = process.communicate()[0]
    # log  = 'Dummy12'
    print('log', type(str(log)))
    log = log.decode("utf-8")
    current_now = datetime.now()
    fmttime = current_now.strftime("%d/%m/%Y %H:%M:%S")
    finished_time = fmttime
    completed = "Completed"
    print('finished time is ', finished_time)
    test.updatetestresults(testcase, finished_time, completed, log)


def readTestSuite(args):
    print("I am in readCases")


def getStatusAll(status):
    status = str(status[0])
    print(status)
    if status == 'all':
        print("I am inside")
        res = test.display()
        print(res)