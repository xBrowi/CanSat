#include <Wire.h>
#include <Adafruit_Sensor.h>
#include "Adafruit_BMP3XX.h"
#include <BH1750.h>
#include <TinyGPSPlus.h>
#include <SoftwareSerial.h>
BH1750 lightMeter;
TinyGPSPlus gps;

static const int gpsRXPin = 8, gpsTXPin = 9;
static const uint32_t GPSBaud = 9600;

SoftwareSerial gpsss(gpsRXPin, gpsTXPin);

#define SEALEVELPRESSURE_HPA (1025.36)

Adafruit_BMP3XX bmpObj;
float a0;

void setup() {
  Serial.begin(9600);
  gpsss.begin(GPSBaud);
  bmpObj.begin_I2C();
  Wire.begin();
  lightMeter.begin();
  delay(1000);
}

void loop() {
  Serial.print("amogus ");
  Serial.print(millis());
  Serial.print(" ");
  printTemp();
  Serial.print(" ");
  printbmp();
  Serial.print(" ");
  printLys();
  Serial.print(" ");
  printgps();
  
  Serial.println();
delay(100);
}
