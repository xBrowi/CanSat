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



double q1=0;
double q2=0;
double q3=0;
float acc_x=0;
float acc_y=0;
float acc_z=0;
double q1a=0;
double q2a=0;
double q3a=0;
float acc_xa=0;
float acc_ya=0;
float acc_za=0;


void setup() {
  Serial.begin(115200);
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
  
  q1a=q1;
  q2a=q2;
  q3a=q3;
  acc_xa=acc_x;
  acc_ya=acc_y;
  acc_za=acc_z;

  
  bme.performReading();
  Serial.print("amogus ");
  Serial.print(millis());
  Serial.print(" ");
  printTemp();
  Serial.print(" ");
  printbmp();
  Serial.print(" ");
  //printLys();
  //Serial.print(" L ");
  printIMU();

  if (q1!=q1a or q2!=q2a or q3!=q3a) {
  
  Serial.print(q1,3);
  Serial.print(" ");
  Serial.print(q2,3);
  Serial.print(" ");
  Serial.print(q3,3);
  Serial.print(" ");
  } else {
    Serial.print("a a a ");
  }


  if (acc_x!=acc_xa or acc_y!=acc_ya or acc_z!=acc_za) {
  
  Serial.print(acc_x,1);
  Serial.print(" ");
  Serial.print(acc_y,1);
  Serial.print(" ");
  Serial.print(acc_z,1);
  Serial.print(" ");
  } else {
    Serial.print("a a a ");
  }
  
  //printgps();
  Serial.println();
}
