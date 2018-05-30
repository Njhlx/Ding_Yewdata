import time
import datetime

import DingMsgSend
import ConstSettings
import Common.Const
CONST = Common.Const


def main():
    print("Begin")
    ConstSettings.define()
    counter = 0
    while counter < 10000:
        DingMsgSend.sub_function()
        counter = counter + 1
        i = datetime.datetime.now()
        print(str(i) + " " + str(counter))
        time.sleep(60)
    print("End")


if __name__ == "__main__":
    main()
