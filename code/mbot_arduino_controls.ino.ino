#include <MeMCore.h>
#include "MeLEDMatrix.h"

MeDCMotor leftMotor(M1);
MeDCMotor rightMotor(M2);
MeRGBLed led(0, 30);
volatile char inChar;
int commndDuration_millis = 500;
MeBuzzer buzzer;

void setup() {
  led.setpin(13);
  Serial.begin(115200);
}

/*  SerialEvent occurs whenever a new data comes in the
 hardware serial RX.*/
void serialEvent() {
  while (Serial.available()) {
    char inChar = (char)Serial.read();
    Serial.print("Received "); Serial.println(inChar);
    switch (inChar) {
     case 'f':
       led.setColor(0, 255, 0); 
       led.show();         
       rightMotor.run(200);
       leftMotor.run(-200); 
       break;
     case 'm':
       led.setColor(0, 0, 255); 
       led.show();                  
       rightMotor.run(150);
       leftMotor.run(-150);
       break;
     case 's':
       led.setColor(255, 255, 255);
       led.show();
       rightMotor.run(80);
       leftMotor.run(-80); 
       break;
     case 'h':
       led.setColor(0, 0, 0); //Blank
       led.show();
       rightMotor.stop();
       leftMotor.stop();
       break;
     }
  }
}


