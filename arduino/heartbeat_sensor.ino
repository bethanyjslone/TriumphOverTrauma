#include <Wire.h>
#include "MAX30100_PulseOximeter.h"
#include <LiquidCrystal.h>

#define UPDATE_TIME   1000

// variables and pin defination
const int rs = 8, en = 9, d4 = 10, d5 = 11, d6 = 12, d7 = 13;
byte heart [8] = {0b00000, 0b01010, 0b11111, 0b11111, 0b11111, 0b01110, 0b00100, 0b00000};
uint32_t previous_update_time = 0;

LiquidCrystal lcd(rs, en, d4, d5, d6, d7);
PulseOximeter pulse;

void on_pulse_detected()
{
  Serial.println("Pulse Detected!");
}

void setup() {
  Serial.begin(9600);
  Serial.print("Initializing Pulse Oximeter..");

  lcd.createChar(2, heart);
  lcd.begin(16, 2);
  lcd.clear();
  lcd.setCursor(2, 0);
  lcd.print("Initializing");
  lcd.setCursor(1, 1);
  lcd.print("Pulse Oximeter");

  delay(3000);

  if (!pulse.begin()) {
    Serial.println("Sensor begin Failed");
  } else {
    Serial.println("Sensor begin Success");
  }
  //set current
  pulse.setIRLedCurrent(MAX30100_LED_CURR_7_6MA);

  // for the pulse detection
  //pulse.setOnBeatDetectedCallback(on_pulse_detected);
}

void loop() {
  pulse.update();

  if (millis() - previous_update_time > UPDATE_TIME) {

    // Display Result on LCD
    lcd.clear();
    lcd.setCursor(0, 0);
    lcd.write((uint8_t)2);
    lcd.print(" Rate:");
    lcd.print(pulse.getHeartRate());
    lcd.print("bpm");
    lcd.setCursor(0, 1);
    lcd.print(" SpO2 :");
    lcd.print(pulse.getSpO2());
    lcd.print("%");
    previous_update_time = millis();

    // Display Result on Serial Monitor
    // Serial.print("Heart ❤ Rate:");
    // Serial.print(pulse.getHeartRate());
    // Serial.println("bpm");
    // Serial.print(" SpO2 Level  :");
    // Serial.print(pulse.getSpO2());
    // Serial.println("%");

    //Serial.print("Heart ❤ Rate:");
    Serial.print(pulse.getHeartRate());
    //Serial.println("bpm");
    Serial.print(",");
    //Serial.print(" SpO2 Level  :");
    Serial.print(pulse.getSpO2());
    //Serial.println("%");
    Serial.print("\n");

    previous_update_time = millis();
  }
}