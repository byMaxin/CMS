# import time
#
# from selenium import webdriver
#
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
# from selenium.common.exceptions import TimeoutException
# from selenium.webdriver.common.action_chains import ActionChains
# from base.base_page import BasePage
#
# dirver=webdriver.Edge()
# dirver.maximize_window()
# dirver.get("http://192.168.233.157:8080/cms")
# dirver.implicitly_wait(10)
#
# print(dirver.find_element(*(By.ID, 'loginBtn')))
#
# # dirver.find_element(By.ID,'userAccount').send_keys('admin')
# # dirver.find_element(By.ID,'loginPwd').send_keys(123456)
# # dirver.find_element(By.ID,'online').click()
# # dirver.find_element(By.ID,'loginBtn').click()
# # dirver.implicitly_wait(3)
# #
# # '''
# # 初始化变量：login_success 用于记录登录是否成功的状态。
# # try-except 块：
# # try 部分：使用 WebDriverWait 等待特定元素（链接文本为“爱软测教学后台”的元素）出现。如果在指定时间（10秒）内找到了该元素，会检查元素的文本，以确认登录是否成功，并更新 login_success 变量的值。
# # except 部分：如果在等待期间抛出 TimeoutException（即在指定时间内未找到元素），则认为登录失败，login_success 被设置为 False。
# # 结果处理：
# # 无论登录是否成功，login_success 变量都会被相应地设置，并可以用于后续的逻辑或断言。
# # 示例中的 print 语句用于输出登录状态，实际测试中可以替换为更复杂的逻辑或断言。
# # 后续代码：
# # 代码块的最后注释表示测试脚本的其他部分可以继续执行，不会因为登录步骤的失败而中断。
# # '''
# #
# #
# #
# # login_success = False
# # try:
# #     element = WebDriverWait(dirver, 10).until(
# #         EC.presence_of_element_located((By.LINK_TEXT, '爱软测教学后台'))
# #     )
# #     # 如果找到了元素，假设登录成功
# #     login_success = "爱软测教学后台" in element.text
# # except TimeoutException:
# #     # 如果超时未找到元素，则登录失败
# #     login_success = False
# # # 可以在这里进行一些断言或记录结果
# # print("Login success:", login_success)
# #
# # dirver.find_element(By.CLASS_NAME,'icon-user').click()
# # ActionChains(dirver).move_to_element(
# #     dirver.find_element(By.LINK_TEXT,'用户管理')).perform()#鼠标悬浮
# # dirver.find_element(By.LINK_TEXT,'用户管理').click()
# # dirver.switch_to.frame(dirver.find_element(
# #     By.NAME,'/cms/manage/user-list.html'))#进入iframe框架
#
#
# # dirver.find_element(By.XPATH,
# #                     '/html/body/div/div[2]/span[1]/a[2]').click()
# # dirver.switch_to.frame(
# #     dirver.find_element(By.ID,'xubox_iframe1'))
# # dirver.find_element(By.NAME,'userName').send_keys(12)
# # dirver.find_elements(By.NAME,'userSex')[0].click()
# # dirver.find_element(By.NAME,'userMobile').send_keys(12)
# # dirver.find_element(By.NAME,'userEmail').send_keys(123)
# # dirver.find_element(By.NAME,'userAccount').send_keys(12)
# # dirver.find_element(By.NAME,'loginPwd').send_keys(12)
# # dirver.find_element(By.NAME,'confirmPwd').send_keys(12)
# # dirver.switch_to.parent_frame()
# # dirver.find_element(By.XPATH,'/html/body/div[3]/div/span[1]/a').click()
#
# # dirver.find_element(By.XPATH,"/html/body/div/table/tbody/tr[2]/td[1]/input").click()
# # dirver.find_element(By.XPATH,"//a[@class='btn btn-danger radius']").click()
# # dirver.find_element(By.XPATH,'/html/body/div[3]/div[1]/span[2]/a[1]').click()
# #
# # dirver.find_element(By.ID,'datemin').send_keys(2000)
# # dirver.find_element(By.ID,'datemax').send_keys(2024)
# # dirver.find_element(By.ID,'searchValue').send_keys(18808555455)
# # dirver.find_element(By.ID,'searchBtn').click()
# # for i in range(1,10):
# #     ActionChains(dirver).move_to_element(dirver.find_element(By.XPATH,'//td[text()='+str(i)+']')).perform()
# #
# # # dirver.switch_to.parent_frame()
# # dirver.find_element(By.XPATH,'/html/body/nav/a/i').click()
#
# time.sleep(1.5)
# dirver.quit()










# import boto3
# import os
#
# import botocore
#
#
# def upload_directory_to_s3(bucket_name, directory_path, region_name, aws_access_key_id, aws_secret_access_key):
#     # 创建 S3 客户端
#     s3 = boto3.client(
#         's3',
#         region_name=region_name,
#         aws_access_key_id=aws_access_key_id,
#         aws_secret_access_key=aws_secret_access_key,
#         config=botocore.config.Config(proxies={'https': 'https://127.0.0.1:7890'}),
#         verify=False  # 禁用 SSL 验证
#     )
#
#     # 遍历目录并上传文件
#     for root, dirs, files in os.walk(directory_path):
#         for file in files:
#             local_path = os.path.join(root, file)
#             s3_path = os.path.relpath(local_path, start=directory_path)
#
#             print(f"Uploading {local_path} to {bucket_name}/{s3_path}")
#             s3.upload_file(local_path, bucket_name, s3_path)
#
# # 替换为你的参数
# bucket_name = 'by_Ma.Aaa76'
# directory_path = r'D:\TestAutomationFrameworks\allure_temp'
# region_name = 'cn-north-1'
# aws_access_key_id = 'by_Ma'
# aws_secret_access_key = 'Aaa258258'
#
# # 调用函数
# upload_directory_to_s3(bucket_name, directory_path, region_name, aws_access_key_id, aws_secret_access_key)



# import boto3
# from botocore.client import Config
# session = boto3.session.Session()
#
# file_path = r'D:\TestAutomationFrameworks\utils\tool_configuration\DYSV9849.MP4'
# key_name = 'demo.mp4'
# bucket_name = 'demo'
# access_key = 'by_Ma'
# secret_key = 'Aaa258258'
# endporint = 'http://s3.ceph.vip'
#
# s3 = session.client('s3',use_ssl=False,endpoint_url=endporint,
# aws_access_key_id=access_key,
# aws_secret_access_key=secret_key,
# config=Config(siganture_version='s3v4',s3={'addressing_style':'path'}))
#
# #创建bucket
# response = s3.create_bucket(Bucket=bucket_name)
# print(response)
#
# s3.upload_file(file_path,bucket_name,key_name,ExterArgs={'contenType':'vieo/mp4'})
#
# params = {'Bucket':bucket_name,'Key':key_name}
# url = s3.generate_presigned_url('get_object',Params=params,ExpiresIn=3600)
# print(url)



# import boto3
# from botocore.client import Config
# session = boto3.session.Session()
#
# file_path = r'D:\TestAutomationFrameworks\utils\tool_configuration\DYSV9849.MP4'
# key_name = 'demo.mp4'
# bucket_name = 'demo'
# access_key = 'by_Ma'
# secret_key = 'Aaa258258'
# endpoint_url = 'http://s3.ceph.vip'
#
# s3 = session.client('s3', use_ssl=False, endpoint_url=endpoint_url,
#                     aws_access_key_id=access_key,
#                     aws_secret_access_key=secret_key,
#                     config=Config(signature_version='s3v4', s3={'addressing_style':'path'}))
#
# # 创建bucket
# response = s3.create_bucket(Bucket=bucket_name)
# print(response)
#
# # 上传文件
# s3.upload_file(file_path, bucket_name, key_name, ExtraArgs={'ContentType':'video/mp4'})
#
# # 生成预签名URL
# params = {'Bucket': bucket_name, 'Key': key_name}
# url = s3.generate_presigned_url('get_object', Params=params, ExpiresIn=3600)
# print(url)


# from flask import Flask, request, send_file
#
# app = Flask(__name__)
#
# @app.route('/upload', methods=['POST'])
# def upload_file():
#     file = request.files['file']
#     file.save(f'videos/{file.filename}')
#     return f'File uploaded successfully: {file.filename}'
#
# @app.route('/video/<filename>')
# def video_file(filename):
#     return send_file(f'videos/{filename}', as_attachment=True)
#
# if __name__ == '__main__':
#     app.run(debug=True)

# import os
# import zipfile
#
# def zip_directory(folder_path, zip_path):
#     with zipfile.ZipFile(zip_path, 'w', zipfile.ZIP_DEFLATED) as zipf:
#         for root, dirs, files in os.walk(folder_path):
#             for file in files:
#                 zipf.write(os.path.join(root, file),
#                            os.path.relpath(os.path.join(root, file),
#                                            folder_path))
#
# # 使用方法
# directory_path = r'D:\TestAutomationFrameworks\allure_temp'  # 要压缩的目录路径
# zip_file_path = r'D:\TestAutomationFrameworks\my_archive.zip'  # 压缩文件保存路径
# zip_directory(directory_path, zip_file_path)



import logging
import time

# 创建一个日志记录器
# logger = logging.getLogger('my_logger')
# logger.setLevel(logging.DEBUG)

# # 创建一个用于写入日志文件的处理器
# file_handler = logging.FileHandler('file.log')
# file_handler.setLevel(logging.DEBUG)

# 创建一个用于控制台输出的处理器
# stream_handler = logging.StreamHandler()
# stream_handler.setLevel(logging.DEBUG)
#
# # 定义日志格式
# formatter = logging.Formatter(
#     '%(asctime)s--%(name)s--%(levelname)s--%(levelno)s--%(message)s')
# # file_handler.setFormatter(formatter)
# stream_handler.setFormatter(formatter)
#
# # 添加处理器到日志
# # logger.addHandler(file_handler)
# logger.addHandler(stream_handler)
# class Test_log:
#     def stream_log(self):
#         #创建一个用于控制台输出的处理器， 并设置级别
#         logger = logging.getLogger('my_logger')
#         logger.setLevel(logging.DEBUG)
#         if not logger.handlers:
#             str=logging.StreamHandler()
#             str.setLevel(logging.INFO)
#             str.setFormatter(logging.Formatter('%(asctime)s--%(name)s--%(levelname)s--%(levelno)s-->> %(message)s'))
#             logger.addHandler(str)
#         return logger
#
#         #使用日志记录器
#         # logger.debug('这是个 调试 级别日志')
#         # logger.info('这是个 提示 级别日志')
#         # logger.warning('这是个 警告 级别日志')
#         # logger.error('这是个 错误 级别日志')
#         # logger.critical('这是个 严重 级别的日志')
#
#     def text_log(self,file_path=r'D:\TestAutomationFrameworks\log\{}-{}H-{}M-{}S_log'.format(
#                 time.strftime('%Y-%m-%d', time.localtime()), time.strftime('%H'), time.strftime('%M'), time.strftime('%S'))):
#         logger = logging.getLogger('my logger')
#         logger.setLevel(logging.DEBUG)
#         if not logger.handlers:
#             file_handler=logging.FileHandler(file_path,'a',encoding='utf-8')
#             file_handler.setLevel(logging.INFO)
#             file_handler.setFormatter(logging.Formatter('%(asctime)s--%(name)s--%(levelname)s--%(levelno)s-->> %(message)s'))
#             logger.addHandler(file_handler)
#
#         return logger
#
# def sun(a,b):
#     try:
#         sun = a+b
#         Test_log().text_log().info('{}+{}计算和是正确的:{}'.format(a,b,sun))
#         Test_log().stream_log().info('{}+{}计算和是正确的:{}'.format(a,b,sun))
#     except Exception as e:
#         Test_log().text_log().error('{}+{}计算和是错误的 {}'.format(a,b,e))
#         Test_log().stream_log().error('{}+{}计算和是错误的 {}'.format(a,b,e))
#
# def diaoyong():
#     sun(3,8)
#     sun(22,999)
#     sun(3,'l')
# diaoyong()

