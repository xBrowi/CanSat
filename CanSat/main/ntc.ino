void printTemp() {
  adc0 = ads.readADC_SingleEnded(0);
  Serial.print(adc0);
}
