

void printbmp () {
Serial.print(bmpObj.temperature);
Serial.print(" ");
Serial.print(bmpObj.pressure / 100.0);
Serial.print(" ");
Serial.print(bmpObj.readAltitude(SEALEVELPRESSURE_HPA));
Serial.print(" ");
}
