#include <ESP32Servo.h>

#define TRIG 5
#define ECHO 18

Servo radarServo;

float getDistance() {

  digitalWrite(TRIG, LOW);
  delayMicroseconds(2);

  digitalWrite(TRIG, HIGH);
  delayMicroseconds(10);
  digitalWrite(TRIG, LOW);

  long duration = pulseIn(ECHO, HIGH);
  float distance = duration * 0.034 / 2;

  return distance;
}

void setup() {
  Serial.begin(115200);

  pinMode(TRIG, OUTPUT);
  pinMode(ECHO, INPUT);

  radarServo.attach(13);
}

void loop() {

  // Forward sweep
  for(int angle = 0; angle <= 180; angle += 5) {

    radarServo.write(angle);
    delay(200);

    float dist = getDistance();

    Serial.print(angle);
    Serial.print(",");
    Serial.println(dist);
  }

  // Backward sweep
  for(int angle = 180; angle >= 0; angle -= 5) {

    radarServo.write(angle);
    delay(200);

    float dist = getDistance();

    Serial.print(angle);
    Serial.print(",");
    Serial.println(dist);
  }
}
