class Utils:
    def __init__(self):
        pass

    def send_email(self,sender_email, subject, body, receiver_email):
        import smtplib
        from email.mime.text import MIMEText
        
        mail_host = "smtp.qq.com"
        mail_user = sender_email
        mail_pass = "ekgalptiarmrdjei"
        
        sender = sender_email
        
        try:
            smtpobj = smtplib.SMTP_SSL(mail_host, 465)
            smtpobj.login(mail_user, mail_pass)
            
            receivers = [receiver_email]
            message = MIMEText(body, 'plain')
            message['From'] = sender_email
            message['To'] = receiver_email
            message['Subject'] = subject
            smtpobj.sendmail(sender, receivers, message.as_string())
            print(f"邮件发送成功至{receiver_email}")
            
            smtpobj.quit()
        except smtplib.SMTPException as e:
            print("Error: 无法发送邮件")
            print(e)
            
        # 发送邮件功能
    def send_emails(self):
        
        student_info_list = self.getData()

        for student_info in student_info_list:
            grade_notification = self.generate_grade_notification(student_info)
            receiver_email = "102102131@fzu.edu.cn"
            if receiver_email:
                self.send_email('2435141349@qq.com', '成绩单通知', grade_notification, receiver_email)
                
        # 生成成绩单通知
    def generate_grade_notification(self,student_info_list):
        template = """
        亲爱的{}同学:

        祝贺您顺利完成本学期的学习！教务处在此向您发送最新的成绩单。

        """.format(student_info_list['姓名'])

        for course_info in student_info_list['课程信息']:
            template += """
            课程名称: {} 学分: {} 百分成绩: {} 五分成绩: {}
            """.format(course_info[0], course_info[1], course_info[2], course_info[3])

        template += """
        希望您能够对自己的成绩感到满意，并继续保持努力和积极的学习态度。如果您在某些科目上没有达到预期的成绩，不要灰心，这也是学习过程中的一部分。我们鼓励您与您的任课教师或辅导员进行交流，他们将很乐意为您解答任何疑问并提供帮助。请记住，学习是一个持续不断的过程，我们相信您有能力克服困难并取得更大的进步。

        再次恭喜您，祝您学习进步、事业成功！

        教务处
        """.format(student_info_list['姓名'])

        return template

    def checkFile(self):
        import os
        if os.path.exists('成绩表.xlsx'):
            return True
        else:
            return False
        
    def deleteFile(self):
        import os
        if os.path.exists('成绩表.xlsx'):
            os.remove('成绩表.xlsx')
            return True
        else:
            return False
        
    def getData(self):
        if not self.checkFile():
            return []
        import openpyxl
        student_info_list = []
        student_info = {}
        sheet = openpyxl.load_workbook('成绩表.xlsx').active
        for row in sheet.iter_rows(min_row=3, values_only=True):
            if student_info.get('学号') != row[1]:
                if '学号' in student_info:
                    student_info_list.append(student_info)

                student_info = {
                    '学号': row[1],
                    '姓名': row[2],
                    '课程信息': []
                }

            course_info = (row[3], row[4], row[5], row[6])
            student_info['课程信息'].append(course_info)

        if '学号' in student_info:
            student_info_list.append(student_info)
            
        return student_info_list
            
    def getDataNumber(self):
        
        student_info_list = self.getData()
        data = []
        for i in student_info_list:
            data.append({
                'id': i['学号'],
                'name': i['姓名'],
                'num': len(i['课程信息'])
            })
        return data
    

    

if __name__ == '__main__':
    utils = Utils()
    print(utils.getDataNumber())