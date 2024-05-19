#include <Servo.h>

Servo myservo; 

void setup() {
  Serial.begin(9600);
  myservo.attach(9);  
}

void loop() {
  if (Serial.available() > 0) {
    char comando = Serial.read();  
    if (comando == 'D') {
      moverDerecha();
    } else if (comando == 'I') {
      moverIzquierda();
    } else if (comando == 'S') {
      pararMotor();
    }
  }
}

void moverDerecha() {
  myservo.write(180); 
}

void moverIzquierda() {
  myservo.write(0);
}

void pararMotor() {
  myservo.write(90); 
}
