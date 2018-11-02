class MobileCommand(object):
    CONTEXTS = 'getContexts',
    GET_CURRENT_CONTEXT = 'getCurrentContext',
    SWITCH_TO_CONTEXT = 'switchToContext'
    TOUCH_ACTION = 'touchAction'
    MULTI_ACTION = 'multiAction'
    OPEN_NOTIFICATIONS = 'openNotifications'
    GET_NETWORK_CONNECTION = 'getNetworkConnection'
    SET_NETWORK_CONNECTION = 'setNetworkConnection'
    GET_AVAILABLE_IME_ENGINES = 'getAvailableIMEEngines'
    IS_IME_ACTIVE = 'isIMEActive'
    ACTIVATE_IME_ENGINE = 'activateIMEEngine'
    DEACTIVATE_IME_ENGINE = 'deactivateIMEEngine'
    GET_ACTIVE_IME_ENGINE = 'getActiveEngine'
    TOGGLE_LOCATION_SERVICES = 'toggleLocationServices'
    LOCATION_IN_VIEW = 'locationInView'

    # Appium Commands
    GET_APP_STRINGS = 'getAppStrings'
    PRESS_KEYCODE = 'pressKeyCode'
    KEY_EVENT = 'keyEvent' # Needed for Selendroid
    LONG_PRESS_KEYCODE = 'longPressKeyCode'
    GET_CURRENT_ACTIVITY = 'getCurrentActivity'
    GET_CURRENT_PACKAGE = 'getCurrentPackage'
    SET_IMMEDIATE_VALUE = 'setImmediateValue'
    PULL_FILE = 'pullFile'
    PULL_FOLDER = 'pullFolder'
    PUSH_FILE = 'pushFile'
    BACKGROUND = 'background'
    IS_APP_INSTALLED = 'isAppInstalled'
    INSTALL_APP = 'installApp'
    REMOVE_APP = 'removeApp'
    TERMINATE_APP = 'terminateApp'
    ACTIVATE_APP = 'activateApp'
    QUERY_APP_STATE = 'queryAppState'
    LAUNCH_APP = 'launchApp'
    CLOSE_APP = 'closeApp'
    END_TEST_COVERAGE = 'endTestCoverage'
    LOCK = 'lock'
    UNLOCK = 'unlock'
    IS_LOCKED = 'isLocked'
    SHAKE = 'shake'
    TOUCH_ID = 'touchId'
    TOGGLE_TOUCH_ID_ENROLLMENT = 'toggleTouchIdEnrollment'
    RESET = 'reset'
    HIDE_KEYBOARD = 'hideKeyboard'
    IS_KEYBOARD_SHOWN = 'isKeyboardShown'
    REPLACE_KEYS = 'replaceKeys'
    START_ACTIVITY = 'startActivity'
    GET_SETTINGS = 'getSettings'
    UPDATE_SETTINGS = 'updateSettings'
    SET_LOCATION = 'setLocation'
    GET_DEVICE_TIME = 'getDeviceTime'
    CLEAR = 'clear'
    START_RECORDING_SCREEN = 'startRecordingScreen'
    STOP_RECORDING_SCREEN = 'stopRecordingScreen'
    SET_CLIPBOARD = 'setClipboard'
    GET_CLIPBOARD = 'getClipboard'
    COMPARE_IMAGES = 'compareImages'