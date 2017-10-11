__author__ = 'astha'

from consider import Consider #importing library for thinkgear
import threading #class for thread of control --> to arduino
import arduino_controls as arduino
import time
import sys
import os
import serial

out = sys.stdout

def stream():
        try:

            con = Consider()  #consider object
            attention_threshold_slow = 25
            attention_threshold_mod = 50
            attention_threshold_fast = 75
            print "waiting for BCI headset signal ..."

            for p in con.packet_generator():

                if p.poor_signal == 0:  #if signal is good,
                    print "meditation: %s / 100 | attention : %s / 100" % (p.meditation, p.attention)

                    if p.attention <= attention_threshold_slow:
                        print "Boost attention"
                        t4 = threading.Thread(target=arduino.stop_moving())
                        t4.daemon = True
                        t4.start()

                    if p.attention > attention_threshold_slow and p.attention < attention_threshold_mod:
                        print 'Attention greater than slow threshold'
                        t1 = threading.Thread(target=arduino.send_go_forward_slow())
                        t1.daemon = True
                        t1.start()
                        print 'Signal sent to arduino'

                    if p.attention >= attention_threshold_mod and p.attention < attention_threshold_fast:
                        print 'Attention greater than moderate threshold'
                        t2 = threading.Thread(target=arduino.send_go_forward_mod())
                        t2.daemon = True
                        t2.start()
                        print 'Signal sent to arduino'

                    if p.attention >= attention_threshold_fast:
                        print 'Attention greater than fast threshold'
                        t3 = threading.Thread(target=arduino.send_go_forward_fast())
                        t3.daemon = True
                        t3.start()
                        print 'Signal sent to arduino'

            else:
                print "no signal yet"

        except serial.serialutil.SerialException:
            print('lost connection to port...retrying')
            stream()


        except KeyboardInterrupt:

            if hasattr(out,'close'):
                t5 = threading.Thread(target=arduino.halt())
                t5.daemon = True
                t5.start()
                print "program will exit now"
                out.close()

if __name__ == "__main__":
    stream()
