#��������
FROM base_mydemo:v1.0
 
#���Ա�������
RUN localedef -c -f UTF-8 -i zh_CN zh_CN.utf8
ENV LC_ALL zh_CN.UTF-8
 
 
#����ĿĿ¼�ļ����Ƶ�������,CODE_DIR���ڻ��������ж����
COPY ./hrms $CODE_DIR/hrms/
 
 
#��װ��Ŀ������
RUN pip3 install -r $CODE_DIR/hrms/requirements.txt
 
#��¶�˿�
EXPOSE 8080
 
 
#������Ŀ
CMD ["python3.5", "/opt/mydemo/mydemo/login.py", "runserver", "0.0.0.0:8080"]