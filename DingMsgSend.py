import SQLExec
import DingTalkRobot
import Common.Const
CONST = Common.Const


def sub_function():
    # 通道库地址：
    s_server = "szbj1dat.sqlserver.rds.aliyuncs.com"
    s_port = "3433"
    s_database = "szbj02data"
    s_user = "szbj02data"
    s_password = "szbj02_8289986"

    # def int_exec(s_server, s_port, s_user, s_password, s_database, s_str_sql):

    row_count = 0
    row_count = row_count + SQLExec.int_exec(s_server, s_port, s_user, s_password, s_database,
                                             "select * from [dbo].[dtv5dtchdanz9csdxl20171127_ywdata-801huiz]")
    row_count = row_count + SQLExec.int_exec(s_server, s_port, s_user, s_password, s_database,
                                             "select * from [dbo].[dtv5dtchdanz9csdxl20171127_ywdata-801kuc]")
    row_count = row_count + SQLExec.int_exec(s_server, s_port, s_user, s_password, s_database,
                                             "select * from[dbo].[dtv5dtchdanz9csdxl20171127_ywdata-801caiw]")
    row_count = row_count + SQLExec.int_exec(s_server, s_port, s_user, s_password, s_database,
                                             "select * from[dbo].[dtv5dtchdanz9csdxl20171127_ywdata-801dd]")
    row_count = row_count + SQLExec.int_exec(s_server, s_port, s_user, s_password, s_database,
                                             "select * from[dbo].[dtv5dtchdanz9csdxl20171127_ywdata-801dhk]")
    row_count = row_count + SQLExec.int_exec(s_server, s_port, s_user, s_password, s_database,
                                             "select * from[dbo].[dtv5dtchdanz9csdxl20171127_ywdata-801hsq]")
    row_count = row_count + SQLExec.int_exec(s_server, s_port, s_user, s_password, s_database,
                                             "select * from[dbo].[dtv5dtchdanz9csdxl20171127_ywdata-801mdkd]")
    row_count = row_count + SQLExec.int_exec(s_server, s_port, s_user, s_password, s_database,
                                             "select * from[dbo].[dtv5dtchdanz9csdxl20171127_ywdata-801mdxs]")
    row_count = row_count + SQLExec.int_exec(s_server, s_port, s_user, s_password, s_database,
                                             "select * from[dbo].[dtv5dtchdanz9csdxl20171127_ywdata-801trfv3]")
    row_count = row_count + SQLExec.int_exec(s_server, s_port, s_user, s_password, s_database,
                                             "select * from[dbo].[dtv5dtchdanz9csdxl20171127_ywdata-801wul]")
    row_count = row_count + SQLExec.int_exec(s_server, s_port, s_user, s_password, s_database,
                                             "select * from[dbo].[dtv5dtchdanz9csdxl20171127_ywdata-801zaixzhh]")

    msg = ""
    msg = msg + "长沙多喜来 - " + str(row_count)
    DingTalkRobot.send_text(msg)