#!/usr/bin/env python3
# importing the required modules
import os,time
__path__=[os.path.dirname(os.path.abspath(__file__))]
from .TestsDataBase import TestsDatabase as database
import threading
import os,sys
import argparse
import subprocess
from datetime import datetime
TEST_DESCRIPTION= 'This Test is to validate somethinng'
class Driver:
    def __init__(self):
        self.test = database()



    def main(self):
        # create parser object
        parser = argparse.ArgumentParser(description="A Test Runner!")

        # defining arguments for parser object
        parser.add_argument("-tc", "--testcase", type=str,
                            metavar="Test Case Names", default=None,
                            help="Specify the Testcase which needs to be executed.")

        parser.add_argument("-ts", "--testsuite", type=str, nargs=1,
                            metavar="path of the TestSuite", default=None,
                            help="Accepts the folder which has all the testcases")

        parser.add_argument("-s", "--getstatusall", type=str, nargs=1,
                            metavar="Status of the TestCases", default=None,
                            help="Status of all TestCases.")


        # parse the arguments from standard input
        args = parser.parse_args()

        #print("Check here : {}".format(args))

        # calling functions depending on type of argument
        if args.testcase != None:
            self.readTestCases(args.testcase)
        elif args.testsuite != None:
            self.readTestSuite(args.testsuite)
        elif args.getstatusall != None:
            self.getStatusAll(args.getstatusall)


    def readTestCases(self,testcase):
        if "," not in testcase:
            obj.update_precomplition(testcase)
            obj.update_postcompilation(testcase)

        else:
            testcase = testcase.split(',')
            #print("List is : {}".format(li))
            for tc in testcase:
                obj.update_precomplition(tc)

    def update_precomplition(self,testcase):
        current_now = datetime.now()
        environment = os.environ['VIRTUAL_ENV']
        fmttime = current_now.strftime("%d/%m/%Y %H:%M:%S")
        print("'{}' is the TestCase TestRunner is going to run".format(testcase))
        started_at = fmttime
        created_at= time.ctime(os.path.getctime(testcase))

        print("Start time : {}".format(started_at))
        print("Creation time : {}".format(created_at))
        self.test.addTestResults(testcase, environment, TEST_DESCRIPTION, created_at, started_at,
                                 finished_at = 'N/A', status='In Progress', logs='N/A')
        # process = subprocess.Popen([sys.executable, testcase], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        # if process.stdout:
        #     print(process.communicate())

    def update_postcompilation(self,testcase):
        print("'{}' is the TestCase TestRunner is going to run".format(testcase))
        process = subprocess.Popen([sys.executable, testcase], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        if process.stdout:
            log = process.communicate()[0]
        # log  = 'Dummy12'
        print('log', type(str(log)))
        log = log.decode("utf-8")
        current_now = datetime.now()
        fmttime = current_now.strftime("%d/%m/%Y %H:%M:%S")
        finished_time =fmttime
        completed = "Completed"
        print('finished time is ', finished_time)
        self.test.updatetestresults(testcase, finished_time, completed, log)


    def readTestSuite(self,args):
        print("I am in readCases")

    def getStatusAll(self,status):
        status = str(status[0])
        print(status)
        if status == 'all':
            print("I am inside")
            res= self.test.display()
            print(res)



if __name__ == '__main__':
    obj = Driver()
    obj.main()