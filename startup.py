import os
current_path=os.path.abspath(__file__)
project_root_path=os.path.abspath(os.path.dirname(current_path)+os.path.sep+'.')
cmd = "robot -P %s --listener allure_robotframework;./allure_xml -d ./report ./testsuite" %project_root_path
os.system(cmd)

