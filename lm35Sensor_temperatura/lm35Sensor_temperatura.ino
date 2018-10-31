float tempC;//declara variable para guardar temp en celsius
int pinSensorT=0;//declarar variable para el pin A0
int ledrojo=13;
void setup() {
  Serial.begin(9600);pinMode(ledrojo,OUTPUT);
  // put your setup code here, to run once:

}

void loop() {
  tempC = analogRead(pinSensorT);
  tempC =(5.0*tempC*100)/1024;
  Serial.println(tempC);
  delay(2000);
  digitalWrite(ledrojo,HIGH);
  delay(10);
  digitalWrite(ledrojo,LOW);
  
  // put your main code here, to run repeatedly:

}
