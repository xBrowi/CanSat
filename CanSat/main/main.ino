#include <Adafruit_BME680.h>
#include <Wire.h>
#include <Adafruit_Sensor.h>
#include "Adafruit_BMP3XX.h"
#include <BH1750.h>
#include <TinyGPSPlus.h>
#include <SoftwareSerial.h>
#include <Adafruit_ADS1X15.h>
#include "ICM_20948.h" // Click here to get the library: http://librarymanager/All#SparkFun_ICM_20948_IMU


BH1750 lightMeter;
TinyGPSPlus gps;
Adafruit_ADS1115 ads;

//static const int gpsRXPin = 8, gpsTXPin = 9;
static const uint32_t GPSBaud = 9600;

//SoftwareSerial gpsss(gpsRXPin, gpsTXPin);

#define SEALEVELPRESSURE_HPA (1025.36)
#define AD0_VAL 1

Adafruit_BME680 bme;
float a0;
int16_t adc0;
int UVOUT = A13; //Output from the sensor
int REF_3V3 = A10; //3.3V power on the Arduino board



#include "ICM_20948.h" // Click here to get the library: http://librarymanager/All#SparkFun_ICM_20948_IMU

//#define USE_SPI       // Uncomment this to use SPI

#define SERIAL_PORT Serial

#define SPI_PORT SPI // Your desired SPI port.       Used only when "USE_SPI" is defined
#define CS_PIN 2     // Which pin you connect CS to. Used only when "USE_SPI" is defined

#define WIRE_PORT Wire // Your desired Wire port.      Used when "USE_SPI" is not defined
// The value of the last bit of the I2C address.
// On the SparkFun 9DoF IMU breakout the default is 1, and when the ADR jumper is closed the value becomes 0
#define AD0_VAL 1

#ifdef USE_SPI
ICM_20948_SPI myICM; // If using SPI create an ICM_20948_SPI object
#else
ICM_20948_I2C myICM; // Otherwise create an ICM_20948_I2C object
#endif






void setup() {
  Serial.begin(9600);
  Serial1.begin(GPSBaud);
  Wire.begin();
  lightMeter.begin();
  delay(1000);
  bme.begin();
  bme.setGasHeater(320, 1); // 320*C for 150 ms
  bme.setIIRFilterSize(BME680_FILTER_SIZE_1);
  ads.begin();
  ads.setGain(GAIN_TWOTHIRDS); //gain 2/3 -> range = +-6.144V, 1bit=0.1875........gain 1 -> range +-4.096V, 1bit=0.125V
  
  pinMode(UVOUT, INPUT);
  pinMode(REF_3V3, INPUT);

  IMUsetup();
  

}

void loop() {
  
  bme.performReading();
  Serial.print("amogus ");
  Serial.print(millis());
  Serial.print(" ");
  printTemp();
  Serial.print(" ");
  printbmp();
  Serial.print(" ");
  printLys();
  Serial.print(" L ");
  printIMU();
  Serial.print(" ");
  //printgps();
  Serial.println();

}
