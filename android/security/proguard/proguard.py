import os, os.path

# ANDROID
ANDROID_SDK_ROOT = r'D:\\devenv\\android\\sdk\\'
PROGUARD_TOOL_ROOT = ANDROID_SDK_ROOT + 'tools\\proguard\\bin\\'
RETRACE = PROGUARD_TOOL_ROOT + "retrace.bat"

# PROJECT
PROJECT_ROOT = r'D:\\code\\wiseda\\hbzy\\'
PROJECT_RELEASE_ROOT = PROJECT_ROOT + r'hbzy\\build\\outputs\\mapping\\hbzy\\release\\'
PROJECT_MAPPING_TXT = PROJECT_RELEASE_ROOT + 'mapping.txt'

# LOG
WORKSPACE = r'D:\\data\\log\\wiseda\\hbzy\\'
EXCEPTION_FLAG = R'System.err:     at'


def get_real_path(trace_name):
    return WORKSPACE + trace_name


def restore(trace):
    cmd = RETRACE + " -verbose " + PROJECT_MAPPING_TXT + " " + get_real_path(trace)
    current_dir = os.curdir
    os.chdir(PROGUARD_TOOL_ROOT)
    os.system(cmd)
    os.chdir(current_dir)


def log2trace(log):
    log_file = open(get_real_path(log))
    for line in log_file:
        if line.find(EXCEPTION_FLAG) != -1:
            print(line)
    log_file.close()


def main():
    restore("trace.txt")
    # log2trace("log.txt")


if __name__ == '__main__':
    main()
