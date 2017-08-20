//Program to test analog inputs
int sensePin =0;

void setup(){
  analogReference(DEFAULT); //isn´ necessary

  Serial.begin(9600);
}

void loop() {
  Serial.println(analogRead(sensePin));
  delay (500);
}

