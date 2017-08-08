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


def main():
    #店铺陈列
    #start_activity({"-e BUSINESS_ID": "4f301e41b78340f38cfc970dcef7e7a9"})

    #喜庆活动
    start_activity(["-e BUSINESS_ID ace8a08a8feb4df5af1a07ada9a4113a",
                    "-e BUSINESS_TYPE CELEBRATION",
                    "--ez EDITABLE true"
                    ], ".visit.offline.ui.Base64ImageListActivity")


if __name__ == '__main__':
    main()
