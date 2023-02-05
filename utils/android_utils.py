import subprocess


def get_udid() -> str:
    """
    Finds udid of connected device from console.

    example:
    'List of devices attached
    2dcd6117        device' --> '2dcd6117'

    :return: device's udid
    """
    command = "adb devices"
    command_result = (
        subprocess.run(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
        .stdout.decode().strip()
    )
    if "device" in command_result:
        row_with_udid = command_result.split("\n")[1]
        udid = row_with_udid.split("\t")[0]
        return udid
    return "device not found"


def android_get_desired_capabilities() -> dict:
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
