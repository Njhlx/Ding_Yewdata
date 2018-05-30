import SQLExec
import DingTalkRobot
import ConstSettings
import Common.Const
CONST = Common.Const


def sub_function():
    # 通道库地址：
    s_server = "szbj1dat.sqlserver.rds.aliyuncs.com"
    s_port = "3433"
    s_database = "szbj02data"
    s_user = "szbj02data"
    s_password = "szbj02_8289986"

    #将字段客户通道转为两个列表，分别为客户名称、客户CODE
    names = list(ConstSettings.CONST.TONGDAO_CODE.keys())
    codes = list(ConstSettings.CONST.TONGDAO_CODE.values())
    chans = CONST.TONGDAO_CHAINS

    for name in names:
        # print(name)
        code = ConstSettings.CONST.TONGDAO_CODE[name]
        # print(code)
        row_count = 0

        for chan in chans:
            # print(chan)
            sSQL = 'select * from [dtv5dtchdan' + code + '_' + chan + ']'
            # print(sSQL)
            row_count = row_count + SQLExec.int_exec(s_server, s_port, s_user, s_password, s_database,
                                         sSQL)
            # print(row_count)
        msg = ''
        msg = msg + name + ": 业务数据仓库待接收数据包：" + str(row_count)
        DingTalkRobot.send_text(msg)
