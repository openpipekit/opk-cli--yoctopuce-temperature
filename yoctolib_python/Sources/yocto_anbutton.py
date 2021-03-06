#*********************************************************************
#*
#* $Id: yocto_anbutton.py 19610 2015-03-05 10:39:47Z seb $
#*
#* Implements yFindAnButton(), the high-level API for AnButton functions
#*
#* - - - - - - - - - License information: - - - - - - - - - 
#*
#*  Copyright (C) 2011 and beyond by Yoctopuce Sarl, Switzerland.
#*
#*  Yoctopuce Sarl (hereafter Licensor) grants to you a perpetual
#*  non-exclusive license to use, modify, copy and integrate this
#*  file into your software for the sole purpose of interfacing
#*  with Yoctopuce products.
#*
#*  You may reproduce and distribute copies of this file in
#*  source or object form, as long as the sole purpose of this
#*  code is to interface with Yoctopuce products. You must retain
#*  this notice in the distributed source file.
#*
#*  You should refer to Yoctopuce General Terms and Conditions
#*  for additional information regarding your rights and
#*  obligations.
#*
#*  THE SOFTWARE AND DOCUMENTATION ARE PROVIDED 'AS IS' WITHOUT
#*  WARRANTY OF ANY KIND, EITHER EXPRESS OR IMPLIED, INCLUDING 
#*  WITHOUT LIMITATION, ANY WARRANTY OF MERCHANTABILITY, FITNESS
#*  FOR A PARTICULAR PURPOSE, TITLE AND NON-INFRINGEMENT. IN NO
#*  EVENT SHALL LICENSOR BE LIABLE FOR ANY INCIDENTAL, SPECIAL,
#*  INDIRECT OR CONSEQUENTIAL DAMAGES, LOST PROFITS OR LOST DATA,
#*  COST OF PROCUREMENT OF SUBSTITUTE GOODS, TECHNOLOGY OR 
#*  SERVICES, ANY CLAIMS BY THIRD PARTIES (INCLUDING BUT NOT 
#*  LIMITED TO ANY DEFENSE THEREOF), ANY CLAIMS FOR INDEMNITY OR
#*  CONTRIBUTION, OR OTHER SIMILAR COSTS, WHETHER ASSERTED ON THE
#*  BASIS OF CONTRACT, TORT (INCLUDING NEGLIGENCE), BREACH OF
#*  WARRANTY, OR OTHERWISE.
#*
#*********************************************************************/


__docformat__ = 'restructuredtext en'
from yocto_api import *


#--- (YAnButton class start)
#noinspection PyProtectedMember
class YAnButton(YFunction):
    """
    Yoctopuce application programming interface allows you to measure the state
    of a simple button as well as to read an analog potentiometer (variable resistance).
    This can be use for instance with a continuous rotating knob, a throttle grip
    or a joystick. The module is capable to calibrate itself on min and max values,
    in order to compute a calibrated value that varies proportionally with the
    potentiometer position, regardless of its total resistance.

    """
#--- (end of YAnButton class start)
    #--- (YAnButton return codes)
    #--- (end of YAnButton return codes)
    #--- (YAnButton dlldef)
    #--- (end of YAnButton dlldef)
    #--- (YAnButton definitions)
    CALIBRATEDVALUE_INVALID = YAPI.INVALID_UINT
    RAWVALUE_INVALID = YAPI.INVALID_UINT
    CALIBRATIONMAX_INVALID = YAPI.INVALID_UINT
    CALIBRATIONMIN_INVALID = YAPI.INVALID_UINT
    SENSITIVITY_INVALID = YAPI.INVALID_UINT
    LASTTIMEPRESSED_INVALID = YAPI.INVALID_LONG
    LASTTIMERELEASED_INVALID = YAPI.INVALID_LONG
    PULSECOUNTER_INVALID = YAPI.INVALID_LONG
    PULSETIMER_INVALID = YAPI.INVALID_LONG
    ANALOGCALIBRATION_OFF = 0
    ANALOGCALIBRATION_ON = 1
    ANALOGCALIBRATION_INVALID = -1
    ISPRESSED_FALSE = 0
    ISPRESSED_TRUE = 1
    ISPRESSED_INVALID = -1
    #--- (end of YAnButton definitions)

    def __init__(self, func):
        super(YAnButton, self).__init__(func)
        self._className = 'AnButton'
        #--- (YAnButton attributes)
        self._callback = None
        self._calibratedValue = YAnButton.CALIBRATEDVALUE_INVALID
        self._rawValue = YAnButton.RAWVALUE_INVALID
        self._analogCalibration = YAnButton.ANALOGCALIBRATION_INVALID
        self._calibrationMax = YAnButton.CALIBRATIONMAX_INVALID
        self._calibrationMin = YAnButton.CALIBRATIONMIN_INVALID
        self._sensitivity = YAnButton.SENSITIVITY_INVALID
        self._isPressed = YAnButton.ISPRESSED_INVALID
        self._lastTimePressed = YAnButton.LASTTIMEPRESSED_INVALID
        self._lastTimeReleased = YAnButton.LASTTIMERELEASED_INVALID
        self._pulseCounter = YAnButton.PULSECOUNTER_INVALID
        self._pulseTimer = YAnButton.PULSETIMER_INVALID
        #--- (end of YAnButton attributes)

    #--- (YAnButton implementation)
    def _parseAttr(self, member):
        if member.name == "calibratedValue":
            self._calibratedValue = member.ivalue
            return 1
        if member.name == "rawValue":
            self._rawValue = member.ivalue
            return 1
        if member.name == "analogCalibration":
            self._analogCalibration = member.ivalue
            return 1
        if member.name == "calibrationMax":
            self._calibrationMax = member.ivalue
            return 1
        if member.name == "calibrationMin":
            self._calibrationMin = member.ivalue
            return 1
        if member.name == "sensitivity":
            self._sensitivity = member.ivalue
            return 1
        if member.name == "isPressed":
            self._isPressed = member.ivalue
            return 1
        if member.name == "lastTimePressed":
            self._lastTimePressed = member.ivalue
            return 1
        if member.name == "lastTimeReleased":
            self._lastTimeReleased = member.ivalue
            return 1
        if member.name == "pulseCounter":
            self._pulseCounter = member.ivalue
            return 1
        if member.name == "pulseTimer":
            self._pulseTimer = member.ivalue
            return 1
        super(YAnButton, self)._parseAttr(member)

    def get_calibratedValue(self):
        """
        Returns the current calibrated input value (between 0 and 1000, included).

        @return an integer corresponding to the current calibrated input value (between 0 and 1000, included)

        On failure, throws an exception or returns YAnButton.CALIBRATEDVALUE_INVALID.
        """
        if self._cacheExpiration <= YAPI.GetTickCount():
            if self.load(YAPI.DefaultCacheValidity) != YAPI.SUCCESS:
                return YAnButton.CALIBRATEDVALUE_INVALID
        return self._calibratedValue

    def get_rawValue(self):
        """
        Returns the current measured input value as-is (between 0 and 4095, included).

        @return an integer corresponding to the current measured input value as-is (between 0 and 4095, included)

        On failure, throws an exception or returns YAnButton.RAWVALUE_INVALID.
        """
        if self._cacheExpiration <= YAPI.GetTickCount():
            if self.load(YAPI.DefaultCacheValidity) != YAPI.SUCCESS:
                return YAnButton.RAWVALUE_INVALID
        return self._rawValue

    def get_analogCalibration(self):
        """
        Tells if a calibration process is currently ongoing.

        @return either YAnButton.ANALOGCALIBRATION_OFF or YAnButton.ANALOGCALIBRATION_ON

        On failure, throws an exception or returns YAnButton.ANALOGCALIBRATION_INVALID.
        """
        if self._cacheExpiration <= YAPI.GetTickCount():
            if self.load(YAPI.DefaultCacheValidity) != YAPI.SUCCESS:
                return YAnButton.ANALOGCALIBRATION_INVALID
        return self._analogCalibration

    def set_analogCalibration(self, newval):
        """
        Starts or stops the calibration process. Remember to call the saveToFlash()
        method of the module at the end of the calibration if the modification must be kept.

        @param newval : either YAnButton.ANALOGCALIBRATION_OFF or YAnButton.ANALOGCALIBRATION_ON

        @return YAPI.SUCCESS if the call succeeds.

        On failure, throws an exception or returns a negative error code.
        """
        rest_val = "1" if newval > 0 else "0"
        return self._setAttr("analogCalibration", rest_val)

    def get_calibrationMax(self):
        """
        Returns the maximal value measured during the calibration (between 0 and 4095, included).

        @return an integer corresponding to the maximal value measured during the calibration (between 0
        and 4095, included)

        On failure, throws an exception or returns YAnButton.CALIBRATIONMAX_INVALID.
        """
        if self._cacheExpiration <= YAPI.GetTickCount():
            if self.load(YAPI.DefaultCacheValidity) != YAPI.SUCCESS:
                return YAnButton.CALIBRATIONMAX_INVALID
        return self._calibrationMax

    def set_calibrationMax(self, newval):
        """
        Changes the maximal calibration value for the input (between 0 and 4095, included), without actually
        starting the automated calibration.  Remember to call the saveToFlash()
        method of the module if the modification must be kept.

        @param newval : an integer corresponding to the maximal calibration value for the input (between 0
        and 4095, included), without actually
                starting the automated calibration

        @return YAPI.SUCCESS if the call succeeds.

        On failure, throws an exception or returns a negative error code.
        """
        rest_val = str(newval)
        return self._setAttr("calibrationMax", rest_val)

    def get_calibrationMin(self):
        """
        Returns the minimal value measured during the calibration (between 0 and 4095, included).

        @return an integer corresponding to the minimal value measured during the calibration (between 0
        and 4095, included)

        On failure, throws an exception or returns YAnButton.CALIBRATIONMIN_INVALID.
        """
        if self._cacheExpiration <= YAPI.GetTickCount():
            if self.load(YAPI.DefaultCacheValidity) != YAPI.SUCCESS:
                return YAnButton.CALIBRATIONMIN_INVALID
        return self._calibrationMin

    def set_calibrationMin(self, newval):
        """
        Changes the minimal calibration value for the input (between 0 and 4095, included), without actually
        starting the automated calibration.  Remember to call the saveToFlash()
        method of the module if the modification must be kept.

        @param newval : an integer corresponding to the minimal calibration value for the input (between 0
        and 4095, included), without actually
                starting the automated calibration

        @return YAPI.SUCCESS if the call succeeds.

        On failure, throws an exception or returns a negative error code.
        """
        rest_val = str(newval)
        return self._setAttr("calibrationMin", rest_val)

    def get_sensitivity(self):
        """
        Returns the sensibility for the input (between 1 and 1000) for triggering user callbacks.

        @return an integer corresponding to the sensibility for the input (between 1 and 1000) for
        triggering user callbacks

        On failure, throws an exception or returns YAnButton.SENSITIVITY_INVALID.
        """
        if self._cacheExpiration <= YAPI.GetTickCount():
            if self.load(YAPI.DefaultCacheValidity) != YAPI.SUCCESS:
                return YAnButton.SENSITIVITY_INVALID
        return self._sensitivity

    def set_sensitivity(self, newval):
        """
        Changes the sensibility for the input (between 1 and 1000) for triggering user callbacks.
        The sensibility is used to filter variations around a fixed value, but does not preclude the
        transmission of events when the input value evolves constantly in the same direction.
        Special case: when the value 1000 is used, the callback will only be thrown when the logical state
        of the input switches from pressed to released and back.
        Remember to call the saveToFlash() method of the module if the modification must be kept.

        @param newval : an integer corresponding to the sensibility for the input (between 1 and 1000) for
        triggering user callbacks

        @return YAPI.SUCCESS if the call succeeds.

        On failure, throws an exception or returns a negative error code.
        """
        rest_val = str(newval)
        return self._setAttr("sensitivity", rest_val)

    def get_isPressed(self):
        """
        Returns true if the input (considered as binary) is active (closed contact), and false otherwise.

        @return either YAnButton.ISPRESSED_FALSE or YAnButton.ISPRESSED_TRUE, according to true if the
        input (considered as binary) is active (closed contact), and false otherwise

        On failure, throws an exception or returns YAnButton.ISPRESSED_INVALID.
        """
        if self._cacheExpiration <= YAPI.GetTickCount():
            if self.load(YAPI.DefaultCacheValidity) != YAPI.SUCCESS:
                return YAnButton.ISPRESSED_INVALID
        return self._isPressed

    def get_lastTimePressed(self):
        """
        Returns the number of elapsed milliseconds between the module power on and the last time
        the input button was pressed (the input contact transitioned from open to closed).

        @return an integer corresponding to the number of elapsed milliseconds between the module power on
        and the last time
                the input button was pressed (the input contact transitioned from open to closed)

        On failure, throws an exception or returns YAnButton.LASTTIMEPRESSED_INVALID.
        """
        if self._cacheExpiration <= YAPI.GetTickCount():
            if self.load(YAPI.DefaultCacheValidity) != YAPI.SUCCESS:
                return YAnButton.LASTTIMEPRESSED_INVALID
        return self._lastTimePressed

    def get_lastTimeReleased(self):
        """
        Returns the number of elapsed milliseconds between the module power on and the last time
        the input button was released (the input contact transitioned from closed to open).

        @return an integer corresponding to the number of elapsed milliseconds between the module power on
        and the last time
                the input button was released (the input contact transitioned from closed to open)

        On failure, throws an exception or returns YAnButton.LASTTIMERELEASED_INVALID.
        """
        if self._cacheExpiration <= YAPI.GetTickCount():
            if self.load(YAPI.DefaultCacheValidity) != YAPI.SUCCESS:
                return YAnButton.LASTTIMERELEASED_INVALID
        return self._lastTimeReleased

    def get_pulseCounter(self):
        """
        Returns the pulse counter value

        @return an integer corresponding to the pulse counter value

        On failure, throws an exception or returns YAnButton.PULSECOUNTER_INVALID.
        """
        if self._cacheExpiration <= YAPI.GetTickCount():
            if self.load(YAPI.DefaultCacheValidity) != YAPI.SUCCESS:
                return YAnButton.PULSECOUNTER_INVALID
        return self._pulseCounter

    def set_pulseCounter(self, newval):
        rest_val = str(newval)
        return self._setAttr("pulseCounter", rest_val)

    def get_pulseTimer(self):
        """
        Returns the timer of the pulses counter (ms)

        @return an integer corresponding to the timer of the pulses counter (ms)

        On failure, throws an exception or returns YAnButton.PULSETIMER_INVALID.
        """
        if self._cacheExpiration <= YAPI.GetTickCount():
            if self.load(YAPI.DefaultCacheValidity) != YAPI.SUCCESS:
                return YAnButton.PULSETIMER_INVALID
        return self._pulseTimer

    @staticmethod
    def FindAnButton(func):
        """
        Retrieves an analog input for a given identifier.
        The identifier can be specified using several formats:
        <ul>
        <li>FunctionLogicalName</li>
        <li>ModuleSerialNumber.FunctionIdentifier</li>
        <li>ModuleSerialNumber.FunctionLogicalName</li>
        <li>ModuleLogicalName.FunctionIdentifier</li>
        <li>ModuleLogicalName.FunctionLogicalName</li>
        </ul>

        This function does not require that the analog input is online at the time
        it is invoked. The returned object is nevertheless valid.
        Use the method YAnButton.isOnline() to test if the analog input is
        indeed online at a given time. In case of ambiguity when looking for
        an analog input by logical name, no error is notified: the first instance
        found is returned. The search is performed first by hardware name,
        then by logical name.

        @param func : a string that uniquely characterizes the analog input

        @return a YAnButton object allowing you to drive the analog input.
        """
        # obj
        obj = YFunction._FindFromCache("AnButton", func)
        if obj is None:
            obj = YAnButton(func)
            YFunction._AddToCache("AnButton", func, obj)
        return obj

    def resetCounter(self):
        """
        Returns the pulse counter value as well as its timer.

        @return YAPI.SUCCESS if the call succeeds.

        On failure, throws an exception or returns a negative error code.
        """
        return self.set_pulseCounter(0)

    def nextAnButton(self):
        """
        Continues the enumeration of analog inputs started using yFirstAnButton().

        @return a pointer to a YAnButton object, corresponding to
                an analog input currently online, or a None pointer
                if there are no more analog inputs to enumerate.
        """
        hwidRef = YRefParam()
        if YAPI.YISERR(self._nextFunction(hwidRef)):
            return None
        if hwidRef.value == "":
            return None
        return YAnButton.FindAnButton(hwidRef.value)

#--- (end of YAnButton implementation)

#--- (AnButton functions)

    @staticmethod
    def FirstAnButton():
        """
        Starts the enumeration of analog inputs currently accessible.
        Use the method YAnButton.nextAnButton() to iterate on
        next analog inputs.

        @return a pointer to a YAnButton object, corresponding to
                the first analog input currently online, or a None pointer
                if there are none.
        """
        devRef = YRefParam()
        neededsizeRef = YRefParam()
        serialRef = YRefParam()
        funcIdRef = YRefParam()
        funcNameRef = YRefParam()
        funcValRef = YRefParam()
        errmsgRef = YRefParam()
        size = YAPI.C_INTSIZE
        #noinspection PyTypeChecker,PyCallingNonCallable
        p = (ctypes.c_int * 1)()
        err = YAPI.apiGetFunctionsByClass("AnButton", 0, p, size, neededsizeRef, errmsgRef)

        if YAPI.YISERR(err) or not neededsizeRef.value:
            return None

        if YAPI.YISERR(
                YAPI.yapiGetFunctionInfo(p[0], devRef, serialRef, funcIdRef, funcNameRef, funcValRef, errmsgRef)):
            return None

        return YAnButton.FindAnButton(serialRef.value + "." + funcIdRef.value)

#--- (end of AnButton functions)
