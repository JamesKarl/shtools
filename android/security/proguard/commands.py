import os
import os.path

WINDOWS_REVERSE_TOOLS_ROOT = r'D:\devenv\android\security\reverse\apk_reverse'

WINDOWS_APK_TOOL_ROOT = WINDOWS_REVERSE_TOOLS_ROOT + r"\apk-tool"
WINDOWS_DEX2JAR_ROOT = WINDOWS_REVERSE_TOOLS_ROOT + r"\dex2jar"
WINDOWS_JD_GUI_ROOT = WINDOWS_REVERSE_TOOLS_ROOT + r"\jd-gui"

COMMAND_APK_TOOL = WINDOWS_APK_TOOL_ROOT + r"\apktool.bat"
COMMAND_APK_TOOL_JAR = WINDOWS_APK_TOOL_ROOT + r"\apktool.jar"
COMMAND_AAPT = WINDOWS_APK_TOOL_ROOT + r"\aapt.exe"


def run(cmd):
    print(cmd)
    os.system(cmd)


def reverse_apk(apk_file_path, output_directory):
    if not os.path.exists(apk_file_path):
        print(apk_file_path + " not exist")
        return

    if not os.path.exists(output_directory):
        os.mkdir(output_directory)

    cmd = COMMAND_APK_TOOL + " d -f " + apk_file_path + " " + output_directory
    run(cmd)


def check_apk_sign(apk_file_path):
    if not os.path.exists(apk_file_path):
        print(apk_file_path + " not exist")
        return

    cmd = r"jarsigner -verify -certs -verbose " + apk_file_path
    run(cmd)

