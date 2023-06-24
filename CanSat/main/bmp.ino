

void printbmp () {
Serial.print(bme.temperature);
Serial.print(" T ");
Serial.print(bme.pressure / 100.0);
Serial.print(" P ");
Serial.print(bme.humidity);
Serial.print(" H ");
//Serial.print(bme.gas_resistance / 1000.0);
//Serial.print(" R ");
}
