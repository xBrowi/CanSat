

void printbme () {
Serial.print(bme.temperature);
Serial.print(" ");
Serial.print(bme.pressure / 100.0);
Serial.print(" ");
Serial.print(bme.humidity);
//Serial.print(bme.gas_resistance / 1000.0);
//Serial.print(" R ");
}
