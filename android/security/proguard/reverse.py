import os
import os.path

from android.security.proguard.commands import *

WORKSPACE = R'D:\wiseda\security\hbzy'
APK_PATH = WORKSPACE + R"\hbzy_v3.6000_release.apk"
OUTPUT_PATH = WORKSPACE + "\hbzy"


def main():
    #reverse_apk(APK_PATH, OUTPUT_PATH)
    check_apk_sign(APK_PATH)


if __name__ == '__main__':
    main()
