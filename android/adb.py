import os
import os.path

ADB = "D:\\devenv\\android\\sdk\\platform-tools\\adb.exe "


def run(cmd):
    print(cmd)
    os.system(cmd)


def start_activity(params, activity=".visit.offline.ui.Base64ImageCategoryListActivity", package="com.wiseda.hbzy"):
    extras = ""
    for k in params.keys():
        extras += " -e " + k + " " + params[k] + " "

    run(ADB + "shell am start -W " + extras + " -n " + package + "/" + activity)


def main():
    start_activity({"BUSINESS_ID": "4f301e41b78340f38cfc970dcef7e7a9"})


if __name__ == '__main__':
    main()
