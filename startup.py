import os
cmd = "robot --listener allure_robotframework;./allure_xml -d ./report ./testsuite"
os.system(cmd)

