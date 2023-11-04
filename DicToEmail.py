import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.application import MIMEApplication

class DicToEmail:
    def __init__(self, username, password, smtp_server="smtp.gmail.com", smtp_port=587) -> None:
        # self
        # 连接到SMTP服务器
        self.sender_email = username
        self.server = smtplib.SMTP(smtp_server, smtp_port)
        self.server.starttls()
        self.server.login(username, password)
    
    def __del__(self):
        self.server.quit()

    def sendEmail(self, your_dictionary):
        # 定义接收方的邮箱地址
        receiver_email = your_dictionary['学号'] + "@fzu.com"
        receiver_name = your_dictionary['姓名']
        receiver_score = your_dictionary['成绩']
        # json格式
        # your_dictionary = {
        #     "学号": "102102***",
        #     "姓名": "张三",
        #     "成绩": {
        #         "语文": 90,
        #         "数学": 80,
        #         "英语": 70
        #     }
        # }

        # 创建邮件主题和正文
        subject = "{}-{}, 您的成绩单".format(your_dictionary['学号'], receiver_name)
        dict_str = "\n".join([f"{key}: {value}" for key, value in receiver_score.items()])
        message = """
        亲爱的{}同学:
        祝贺您顺利完成本学期的学习！教务处在此向您发送最新的成绩单。

        {}

        希望您能够对自己的成绩感到满意，并继续保持努力和积极的学习态度。如果您在某些科目上没有达到预期的成绩，不要灰心，这也是学习过程中的一部分。我们鼓励您与您的任课教师或辅导员进行交流，他们将很乐意为您解答任何疑问并提供帮助。请记住，学习是一个持续不断的过程，我们相信您有能力克服困难并取得更大的进步。
        再次恭喜您，祝您学习进步、事业成功！
        教务处
        """.format(receiver_name, dict_str)

        # 创建邮件
        msg = MIMEMultipart()
        msg['From'] = self.sender_email
        msg['To'] = receiver_email
        msg['Subject'] = subject
        msg.attach(MIMEText(message, 'plain'))  # 第二个参数 'plain' 指定消息文本的格式为纯文本

        # 将字典数据转换为字符串并附加到邮件正文中
        # your_dictionary = {
        #     "key1": "value1",
        #     "key2": "value2",
        #     "key3": "value3"
        # }

        # 发送邮件
        try:
            self.server.sendmail(self.sender_email, receiver_email, msg.as_string())
        except Exception as e:
            return "Email sent failed!" + str(e)

        # finally:
        # 退出SMTP服务器连接
        # server.quit()

        return "发送成功！"


