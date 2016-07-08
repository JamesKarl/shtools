#!/bin/bash
CURRENT_DIR=`pwd`

PJSIP_ROOT=/home/jameskarl/mye/code/sip/pjsip
APP_SWIG_ROOT=$PJSIP_ROOT/pjsip-apps/src/swig
APP_SWIG_OUTPUT=$APP_SWIG_ROOT/java/output
APP_SWIG_ANDROID_SRC=$APP_SWIG_ROOT/java/android/src
APP_SWIG_ANDROID_SO=$APP_SWIG_ROOT/java/android/libs

DEST_ROOT=/home/jameskarl/mye/code/azhixue/voipclient
DEST_JAR_LIBS=$DEST_ROOT/libs
DEST_SO_LIBS=$DEST_ROOT/src/main/libs

SO_NAME=libpjsua2.so
JAR_NAME=pjsip.jar
JAR_SRC_NAME=pjsip-src.jar

function make_target(){
	cd $PJSIP_ROOT
	local target=$1
	TARGET_ABI=$target ./configure-android --use-ndk-cflags
	make dep && make clean && make

	cd $APP_SWIG_ROOT
	make

	cd $APP_SWIG_OUTPUT
	jar cf $JAR_NAME org
	echo cp $APP_SWIG_ANDROID_SRC/$JAR_NAME $DEST_JAR_LIBS
	cp $APP_SWIG_ANDROID_SRC/$JAR_NAME $DEST_JAR_LIBS

	cd $APP_SWIG_ANDROID_SRC
	jar cf $JAR_SRC_NAME org
	echo cp $APP_SWIG_ANDROID_SRC/$JAR_SRC_NAME $DEST_JAR_LIBS
	#cp $APP_SWIG_ANDROID_SRC/$JAR_SRC_NAME $DEST_JAR_LIBS

	echo cp $APP_SWIG_ANDROID_SO/armeabi/$SO_NAME $DEST_SO_LIBS/$target
	cp $APP_SWIG_ANDROID_SO/armeabi/$SO_NAME $DEST_SO_LIBS/$target
}

make_target armeabi
make_target armeabi-v7a

cd $CURRENT_DIR
echo '========THE END========'
