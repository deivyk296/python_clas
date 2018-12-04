#include <Servo.h>
Servo myservo;// crear el odjeto servo

int pos = 0; //posicion de servo


void setup() {
  myservo.attach(9);//vincular el servo al pin digital 9
 
  

}

void loop() {
    //varia la posicion de 0 180 con espera de 15 ms 
  for (pos = 0; pos <= 180; pos += 1)
  {
    myservo.write(pos);
    delay(15);
  }
  for (pos = 180; pos >= 0; pos -= 1)
  {
    myservo.write(pos);
    delay(15);
  }

}
