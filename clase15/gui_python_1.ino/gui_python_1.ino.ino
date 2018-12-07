char serialData
int pinled = 10

void setup()
{
  pinMode(pinled,OUTPUT);
  Serial.begin(9600)
  // put your setup code here, to run once:

}

void loop() 
{
  if(Serial.available()>0)  {
    serialData = Serie.read();
    Serial.print(serialData);

    if(serialData == '1') {
      digitalWrite(pinled, HIGH)
    }else {
      if(serialData == '0') {
        digitalWrite(pinled, LOW);
      }
    }
  }
  // put your main code here, to run repeatedly:

}
