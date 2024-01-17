import os
from datetime import datetime

import pytest

from utils.tool_kit.AllFileEditingTool import File_Tool

if __name__ == '__main__':
    time=datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    pytest.main(['-vs',r'D:\TestAutomationFrameworks\tests\test_login.py',
                 '--alluredir',f'./allure_temp','--clean-alluredir'])
    os.system(f'allure generate ./allure_temp -o ./allure_temp/report{time} --clean')

    File_Tool().generate_text_file(r'D:\TestAutomationFrameworks\allure_temp\generate_html.bat',f'allure open report{time}')
