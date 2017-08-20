//more info https://learn.adafruit.com/adafruit-neopixel-uberguide/arduino-library
#include <Adafruit_NeoPixel.h>
int switchPin = 7;

Adafruit_NeoPixel strip = Adafruit_NeoPixel(4, 8);

void setup() {
  strip.begin();
  strip.show(); // Initialize all pixels to 'off'
  strip.setBrightness(100); //sets diferente values for brigtness (255=max)
}

void loop() {
    if (digitalRead(switchPin) == HIGH)
  {
    strip.setPixelColor(0, 255, 0, 255); //set color of led 1 to magenta
    strip.show();
    delay(100); //delay on next action (value in miliseconds)
    strip.setPixelColor(1, 0, 0, 255); //set color of led 2 to blue
    strip.show();
    delay(100);
    strip.setPixelColor(2, 13, 150, 71); //set color of led 3 to green
    strip.show();
    delay(100);
    strip.setPixelColor(3, 255, 255, 0); //set color of led 4 to yellow
    strip.show();
  }
  else
  {
    strip.setPixelColor(0, 0, 0, 0); //turn off led 1
    strip.setPixelColor(1, 0, 0, 0); //turn off led 2
    strip.setPixelColor(2, 0, 0, 0); //turn off led 3
    strip.setPixelColor(3, 0, 0, 0); //turn off led 4
    strip.show();
  }
}
