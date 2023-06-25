
void printTemp() {
  adc0 = ads.readADC_SingleEnded(0);
  Serial.print(adc0);
  Serial.print(" ");
  adc23 = ads.readADC_Differential_2_3()*-1;
  Serial.print(adc23);
}
