/*
  Arduino Starter Kit example
  Project 12 - Knock Lock

  This sketch is written to accompany Project 12 in the Arduino Starter Kit

  Parts required:
  - 1 megohm resistor
  - 10 kilohm resistor
  - three 220 ohm resistors
  - piezo
  - servo motor
  - push button
  - one red LED
  - one yellow LED
  - one green LED
  - 100 uF capacitor

  created 18 Sep 2012
  by Scott Fitzgerald
  Thanks to Federico Vanzati for improvements

  http://www.arduino.cc/starterKit

  This example code is part of the public domain.
*/

// import the library
#include <Servo.h>
// create an instance of the Servo library
Servo myServo;

const int piezo = A0;      // pin the piezo is attached to
const int switchPin = 2;    // pin the switch is attached to
const int yellowLed = 3;    // pin the yellow LED is attached to
const int greenLed = 4;    // pin the green LED is attached to
const int redLed = 5;   // pin the red LED is attached to

// variable for the piezo value
int knockVal;
// variable for the switch value
int switchVal;



// variable to indicate if locked or not
bool locked = false;
// how many valid knocks you've received
int numberOfKnocks = 0;
String command;

void setup() {
  // attach the servo to pin 9
  myServo.attach(9);

  // make the LED pins outputs
  pinMode(yellowLed, OUTPUT);
  pinMode(redLed, OUTPUT);
  pinMode(greenLed, OUTPUT);

  // set the switch pin as an input
  pinMode(switchPin, INPUT);

  // start serial communication for debugging
  Serial.begin(9600);

  // turn the green LED on
  digitalWrite(greenLed, HIGH);

  // move the servo to the unlocked position
  myServo.write(0);

  // print status to the Serial Monitor
  Serial.println("the box is unlocked!");
}

void loop() {

  if(Serial.available()>0){
    command = Serial.readStringUntil("!");
    Serial.print("A command was recieved via Serial: ");
    Serial.println(command);
    if(command == "redon!"){
      digitalWrite(redLed,HIGH);
      digitalWrite(yellowLed,LOW);
      digitalWrite(greenLed,LOW);
      Serial.println("red is on!");
    }
    if(command == "yellowon!"){
      digitalWrite(redLed,LOW);
      digitalWrite(yellowLed,HIGH);
      digitalWrite(greenLed,LOW);
      Serial.println("yellow is on!");
    }
    if(command == "greenon!"){
      digitalWrite(redLed,LOW);
      digitalWrite(yellowLed,LOW);
      digitalWrite(greenLed,HIGH);
      Serial.println("green is on!");
    }
    if(command == "allon!"){
      digitalWrite(redLed,HIGH);
      digitalWrite(yellowLed,HIGH);
      digitalWrite(greenLed,HIGH);
      Serial.println("all are on!");
    }
    if(command == "lock!"){
      myServo.write(90);
      Serial.println("the box is locked!");
      delay(1000);
    }
    if(command == "unlock!"){

      myServo.write(0);
      Serial.println("the box is unlocked!");
      delay(1000);
    }
  }

  }
