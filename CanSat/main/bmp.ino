

void printbmp () {
Serial.print(bmpObj.temperature);
Serial.println(" *C");
Serial.print(bmpObj.pressure / 100.0);
Serial.println(" hPa");
Serial.print(bmpObj.readAltitude(SEALEVELPRESSURE_HPA));
Serial.println(" m");
Serial.println();
}
