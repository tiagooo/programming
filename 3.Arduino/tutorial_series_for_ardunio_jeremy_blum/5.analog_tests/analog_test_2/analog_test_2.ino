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

 if(val <800) digitalWrite(ledPin, HIGH);  //condition to output power on pin 9
 else digitalWrite(ledPin, LOW);
}

