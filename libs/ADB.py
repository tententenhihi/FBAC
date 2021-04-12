import os
import subprocess
import time

import requests


class ADB:

    def devices(self):
        command = 'adb devices'
        p = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        stdout, stderr = p.communicate()
        print("Device List !!")

    def openLink(self, url):
        command = 'adb shell am start -n com.android.chrome/com.google.android.apps.chrome.Main -a android.intent.action.VIEW -d "' + url + '"'
        p = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        stdout, stderr = p.communicate()
        print("Link Opened !!")

    def aeroplane(self, action):

        if action == 1:
            command = 'adb shell su -c "settings put global airplane_mode_on 1"'
            p = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            stdout, stderr = p.communicate()

            command = 'adb shell am broadcast -a android.intent.action.AIRPLANE_MODE'
            p = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            stdout, stderr = p.communicate()
            print("Flight Mode Enabled !!")

        else:
            command = 'adb shell su -c "settings put global airplane_mode_on 0"'
            p = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            stdout, stderr = p.communicate()

            command = 'adb shell am broadcast -a android.intent.action.AIRPLANE_MODE'
            p = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            stdout, stderr = p.communicate()
            print("Flight Mode Disabled !!")

        return True

    def hotspot(self, action):

        if action == 1:
            command = 'adb shell su -c "am start -n com.android.settings/.TetherSettings"'
            p = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            stdout, stderr = p.communicate()

            time.sleep(2)

            self.tapButton(999, 294)
            print("Hotspot Mode Enabled !!")

        else:
            command = 'adb shell su -c "adb shell am start -n com.android.settings/.TetherSettings"'
            p = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            stdout, stderr = p.communicate()

            self.tapButton(981, 563)
            print("Flight Mode Disabled !!")

        return True

    def connectWifi(self, ssid, password):
        time.sleep(2)
        os.system('networksetup -setairportnetwork en0 ' + ssid + ' ' + password + '')
        print("Connecting Wifi !!")

    def internet(self, action):

        if action == 1:
            command = 'adb shell svc data enable'
            p = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            stdout, stderr = p.communicate()
            print("Internet Enabled !!")

        else:
            command = 'adb shell svc data disable'
            p = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            stdout, stderr = p.communicate()
            print("Internet Disabled !!")

        return True

    def link(self, link):

        response = requests.get(link)
        print(response.status_code)

    def wifi(self, action):

        if action == 1:
            command = 'adb shell su -c "svc wifi enable"'
            p = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            stdout, stderr = p.communicate()
            print("Wifi Enabled !!")

        else:
            command = 'adb shell su -c "svc wifi disable"'
            p = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            stdout, stderr = p.communicate()
            print("Wifi Disabled !!")

        return True

    def openApp(self, packageName, activityName):

        command = 'adb shell su -c "am start -n ' + packageName + '/' + activityName + '"'
        # command = 'adb shell && su && am start -n ' + packageName + '/' + activityName + ''
        p = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        stdout, stderr = p.communicate()
        print("App Open Successful !!")

    def installApp(self):

        command = 'adb install app.apk'
        p = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        stdout, stderr = p.communicate()
        print("APP Installed !!")

    def uninstallApp(self, packageName):

        command = 'adb uninstall ' + packageName + ''
        p = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        stdout, stderr = p.communicate()
        print("APP Uninstalled !!")

    def screenshot(self, fileName):
        command = 'adb shell screencap -p /storage/emulated/0/Download/' + fileName + ''
        p = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        stdout, stderr = p.communicate()

    def getScreenshot(self, fileName):
        command = 'adb pull /storage/emulated/0/Download/' + fileName + ' /Users/baidya/PycharmProjects/ADB/tmp'
        p = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        stdout, stderr = p.communicate()

    def clearData(self, packageName):
        command = 'adb shell pm clear ' + packageName + ''
        p = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        stdout, stderr = p.communicate()
        print("Clear Data Successful !!")

    def pasteText(self, text):
        command = 'adb shell input text "' + text + '"'
        p = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        stdout, stderr = p.communicate()
        print("Paste Successful !!")

    def tapButton(self, x, y):
        command = 'adb shell su -c "input tap ' + str(x) + ' ' + str(y) + '"'
        p = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        stdout, stderr = p.communicate()
        print("Tap Successful !!")

    def backPress(self):
        command = 'adb shell input keyevent 4'
        p = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        stdout, stderr = p.communicate()

    def homeButton(self):
        command = 'adb shell input keyevent KEYCODE_HOME'
        p = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        stdout, stderr = p.communicate()
        print("Home BUtton Tap Successfully !!")

    def clearButton(self):

        command = 'adb shell input keyevent KEYCODE_HOME'
        p = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        stdout, stderr = p.communicate()

        command = 'adb shell input keyevent 82'
        p = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        stdout, stderr = p.communicate()

        command = 'adb shell input tap 568 1724'
        p = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        stdout, stderr = p.communicate()
        print("Home Screen Clear Successful !!")
