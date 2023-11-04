import tkinter as tk
from tkinter import filedialog, simpledialog
import openpyxl
import smtplib
from email.mime.text import MIMEText

def import_grades(file_path):
    workbook = openpyxl.load_workbook(file_path)
    sheet = workbook.active
    return sheet

def generate_grade_notification(student_info):
    template = """
    亲爱的{}同学:

    祝贺您顺利完成本学期的学习！教务处在此向您发送最新的成绩单。

    """.format(student_info['姓名'])

    for course_info in student_info['课程信息']:
        template += """
        课程名称: {} 学分: {} 百分成绩: {} 五分成绩: {}
        """.format(course_info[0], course_info[1], course_info[2], course_info[3])

    template += """
    希望您能够对自己的成绩感到满意，并继续保持努力和积极的学习态度。如果您在某些科目上没有达到预期的成绩，不要灰心，这也是学习过程中的一部分。我们鼓励您与您的任课教师或辅导员进行交流，他们将很乐意为您解答任何疑问并提供帮助。请记住，学习是一个持续不断的过程，我们相信您有能力克服困难并取得更大的进步。

    再次恭喜您，祝您学习进步、事业成功！

    教务处
    """.format(student_info['姓名'])

    return template

def process_student_info(sheet):
    student_info_list = []
    student_info = {}

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

def send_email(sender_email, subject, body, receiver_email):
    mail_host = "smtp.qq.com"
    mail_user = sender_email
    mail_pass = "ekgalptiarmrdjei"
    
    sender = sender_email
    receivers = [receiver_email]
    
    message = MIMEText(body, 'plain')
    message['From'] = sender_email
    message['To'] = receiver_email
    message['Subject'] = subject
    
    try:
        smtpobj = smtplib.SMTP_SSL(mail_host, 465)
        smtpobj.login(mail_user, mail_pass)
        smtpobj.sendmail(sender, receivers, message.as_string())
        print("邮件发送成功")
        smtpobj.quit()
    except smtplib.SMTPException as e:
        print("Error: 无法发送邮件")
        print(e)

def upload_file():
    global file_path
    file_path = filedialog.askopenfilename(filetypes=[("Excel Files", "*.xlsx")])
    label.configure(text=file_path)

def get_receiver_email():
    receiver_email = simpledialog.askstring("输入邮箱", "请输入要发送到的邮箱地址:")
    return receiver_email

def send_emails():
    receiver_email = get_receiver_email()
    if receiver_email:
        sheet = import_grades(file_path)
        student_info_list = process_student_info(sheet)

        for student_info in student_info_list:
            grade_notification = generate_grade_notification(student_info)
            send_email('2435141349@qq.com', '成绩单通知', grade_notification, receiver_email)

root = tk.Tk()
root.title("成绩单通知")

label = tk.Label(root, text="请上传成绩表")
label.pack(pady=10)

upload_button = tk.Button(root, text="上传文件", command=upload_file)
upload_button.pack(pady=10)

email_button = tk.Button(root, text="输入邮箱并发送邮件", command=send_emails)
email_button.pack(pady=10)

root.mainloop()
