import subprocess


def get_udid() -> str:
    """
        Finds udid of connected device

        :return: device's udid
    """
    command = "adb devices"
    command_result = (
        subprocess.run(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
        .stdout.decode()
        .strip()
    )
    if "device" in command_result:
        return command_result.split("\n")[1].split("\t")[0]
    return "device not found"


def android_get_desired_capabilities():
    return {
        "autoGrantPermissions": True,
        "automationName": "uiautomator2",
        "newCommandTimeout": 500,
        "noSign": True,
        "platformName": "Android",
        "platformVersion": "10",
        "resetKeyboard": True,
        "systemPort": 8301,
        "takesScreenshot": True,
        "udid": get_udid(),
        "appPackage": "com.ajaxsystems",
        "appActivity": "com.ajaxsystems.ui.activity.LauncherActivity",
    }
