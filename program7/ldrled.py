 # To write a program for LDR to vary the light intensity of LED using Arduino.
 const int ldr_pin = 3; const int
 led_pin = 2; void setup() {
 pinMode(ldr_pin, INPUT);
 pinMode(led_pin, OUTPUT);
 Serial.begin(9600);
 }
 void loop() {
 if ( digitalRead( ldr_pin ) == 1) {
 digitalWrite(led_pin, HIGH);
 }
 else {
 digitalWrite(led_pin , LOW);
 }
 Serial.println(digitalRead( ldr_pin ));
 delay(100);
 }