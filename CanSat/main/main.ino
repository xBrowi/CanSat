#include <Wire.h>
#include <Adafruit_Sensor.h>
#include "Adafruit_BMP3XX.h"

#define SEALEVELPRESSURE_HPA (1005.67)


Adafruit_BMP3XX bmpObj;
float a0;

void setup() {
  Serial.begin(9600);
  bmpObj.begin_I2C();
  delay(1000);
}

void loop() {
  Serial.print("akat ");
  Serial.print(millis());
  Serial.print(" ");
  printTemp();
  Serial.print(" ");
  printbmp();
  Serial.println();
delay(100);
}
