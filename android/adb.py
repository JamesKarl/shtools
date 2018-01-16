import os
import os.path

ADB = "D:\\devenv\\android\\sdk\\platform-tools\\adb.exe "


def run(cmd):
    print(cmd)
    os.system(cmd)


def start_activity(params, activity=".visit.offline.ui.Base64ImageCategoryListActivity", package="com.wiseda.hbzy"):
    extras = ""
    for it in params:
        extras += " " + it + " "

    run(ADB + "shell am start -W " + extras + " -n " + package + "/" + activity)


def show_store(business_id):
    start_activity(["-e BUSINESS_ID " + business_id])


def show_celebration(celebration_id, editable):
    start_activity(["-e BUSINESS_ID " + celebration_id,
                    "-e BUSINESS_TYPE CELEBRATION",
                    "-e SUBTYPE_NAME 图片",
                    "--ez EDITABLE " + editable
                    ], ".visit.offline.ui.Base64ImageListActivity")


def show_feedback():
    start_activity([
        "--ei FRAGMENT_ID 1",
        "-e TITLE 意见反馈",
        "-e DOC_ID xx"
    ], "com.wiseda.hbzy.HubActivity", "com.wiseda.hbzy.mini")


def show_chat_activity():
    start_activity([
        #"-e oppositeUid CS1",
        #"-e oppositeName 测试员1",
        "-e oppositeUid kejun",
        "-e oppositeName 柯军",
        "--ei chatType 0"
    ], ".chat.activity.ChatActivity")


def main():
    # 店铺陈列
    #show_store("b67c8b04c461499ebd549a15f23b5261")
    #show_feedback()
    show_chat_activity()

    # 喜庆活动
    #show_celebration("ace8a08a8feb4df5af1a07ada9a4113a", "true")


if __name__ == '__main__':
    main()
