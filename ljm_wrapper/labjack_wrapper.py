from labjack import ljm

class ljmWrapper():
      def __init__(self):
            # init to start communicating with labjack
      
            self.handle = ljm.openS("T7", "ANY", "ANY")
            self.info = ljm.getHandleInfo(self.handle)            
            self.uint16 = ljm.constants.UINT16
            self.uint32 = ljm.constants.UINT32
            self.int32 = ljm.constants.INT32
            self.float32 = ljm.constants.FLOAT32
            self.byte = ljm.constants.BYTE
            self.string = ljm.constants.STRING
            self.ADCeNames = ["AIN0","AIN1","AIN2","AIN3","AIN4","AIN5","AIN6",
                              "AIN7","AIN8","AIN9","AIN10","AIN11","AIN12","AIN13"]
            self.DACeNames = ["DAC0", "DAC1"]

            # stream settings

            self.aScanListNames = ["AIN0"] 
            self.numAddresses = len(self.aScanListNames)
            self.aScanList = ljm.namesToAddresses(self.numAddresses, self.aScanListNames)[0]
            self.scanRate = 1000
            self.scansPerRead = int(self.scanRate / 2)

      # functions to communicate with ljm

      def analog_read(self, pinNo):
            return ljm.eReadName(self.handle, self.ADCeNames[pinNo])

      def analog_write(self, pinNo, analogValue):
            return ljm.eWriteName(self.handle, self.DACeNames[pinNo], analogValue)

      def analog_read_stream_setup(self, pinNoList, scan_rate):
            self.aScanListNames = [self.ADCeNames[i] for i in pinNoList]
            self.numAddresses = len(self.aScanListNames)
            self.aScanList = ljm.namesToAddresses(self.numAddresses, self.aScanListNames)[0]
            self.scanRate = scan_rate
            self.scansPerRead = int(self.scanRate / 2)

            # Ensure triggered stream is disabled.
            ljm.eWriteName(self.handle, "STREAM_TRIGGER_INDEX", 0)

            # Enabling internally-clocked stream.
            ljm.eWriteName(self.handle, "STREAM_CLOCK_SOURCE", 0)

            # All negative channels are single-ended, AIN0 and AIN1 ranges are
            # +/-10 V, stream settling is 0 (default) and stream resolution index
            # is 0 (default).
            aNames = ["AIN_ALL_NEGATIVE_CH", "AIN0_RANGE", "AIN1_RANGE",
                        "STREAM_SETTLING_US", "STREAM_RESOLUTION_INDEX"]
            aValues = [ljm.constants.GND, 10.0, 10.0, 0, 0]

            numFrames = len(aNames)
            ljm.eWriteNames(self.handle, numFrames, aNames, aValues)

      def analog_read_stream(self):
            scanRate = ljm.eStreamStart(self.handle, self.scansPerRead, self.numAddresses, self.aScanList, self.scanRate)
            print(f"scan rate: {scanRate}")
            
            result = ljm.eStreamRead(self.handle)
            return result

      def analog_read_stream_stop(self):
            return ljm.eStreamStop(self.handle)