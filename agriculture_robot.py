#include <SoftwareSerial.h>
#include <Servo.h>

#define BT_TX 10
#define BT_RX 11
#define MOISTURE_SENSOR A0
#define RELAY_PIN 8
#define MOTOR_IN1 2
#define MOTOR_IN2 3
#define MOTOR_IN3 4
#define MOTOR_IN4 5
#define MOTOR_ENA 6
#define MOTOR_ENB 7
#define SERVO_PIN1 9
#define SERVO_PIN2 12

Servo servoMotor1, servoMotor2;
SoftwareSerial bluetooth(BT_RX, BT_TX);

void setup() {
  pinMode(RELAY_PIN, OUTPUT);
  pinMode(MOTOR_IN1, OUTPUT);
  pinMode(MOTOR_IN2, OUTPUT);
  pinMode(MOTOR_IN3, OUTPUT);
  pinMode(MOTOR_IN4, OUTPUT);
  pinMode(MOTOR_ENA, OUTPUT);
  pinMode(MOTOR_ENB, OUTPUT);

  servoMotor1.attach(SERVO_PIN1);
  servoMotor2.attach(SERVO_PIN2);
Serial.begin(9600);
  bluetooth.begin(9600);
}

void loop() {
  int moistureLevel = analogRead(MOISTURE_SENSOR);
  int mappedMoisture = map(moistureLevel, 0, 1023, 0, 100);




  if (bluetooth.available() > 0) {
    char command = bluetooth.read();

    switch (command) {
      case '1':  // Turn on water pump
        digitalWrite(RELAY_PIN, HIGH);
        break;
        case '2':  // Turn off water pump
        digitalWrite(RELAY_PIN, LOW);
        break;

      case '3':  // Move left
        motorControl(150, 150, LOW, HIGH);
        break;

      case '4':  // Move right
        motorControl(150, 150, HIGH, LOW);
        break;

      case '5':  // Move forward
        motorControl(170, 170, HIGH, HIGH);
        break;

      case '6':  // Move backward
        motorControl(135, 135, LOW, LOW);
        break;

      case '7':  // Stop
        motorControl(0, 0, LOW, LOW);
        break;

      case '8':  // Rotate servo clockwise
        servoMotor1.write(140);
        break;
case '9':  // Rotate servo counterclockwise
        servoMotor1.write(175);
        break;

    
    }
  }

  bluetooth.print("Moisture Level: ");
  bluetooth.print(mappedMoisture);
  bluetooth.println("%");

  delay(1000);

  servoMotor2.write(55);
  delay (1000);
  servoMotor2.write(85);
  

  

}

void motorControl(int speedA, int speedB, int directionA, int directionB) {
  analogWrite(MOTOR_ENA, speedA);
  analogWrite(MOTOR_ENB, speedB);
  digitalWrite(MOTOR_IN1, directionA);
   digitalWrite(MOTOR_IN2, !directionA);
  digitalWrite(MOTOR_IN3, directionB);
  digitalWrite(MOTOR_IN4, !directionB);
}

