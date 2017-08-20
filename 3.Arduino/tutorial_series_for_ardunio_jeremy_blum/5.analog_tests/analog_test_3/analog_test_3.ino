//Program to test analog inputs
int sensePin =0;
int ledPin = 9;

void setup(){
  analogReference(DEFAULT); //isn´ necessary
  Serial.begin(9600);  //gauge definition
  pinMode(ledPin, OUTPUT);

}

void loop() {
  Serial.println(analogRead(sensePin));  //serial values printing
  delay (500);  //delay for the printing
  int val = analogRead(sensePin);

  val = constrain(val, 750, 900);
  int ledLevel = map(val, 750, 900, 255, 0);
  analogWrite(ledPin, ledLevel);
}

