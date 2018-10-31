int led = 2;
void setup() 
{
  Serial.begin(9600);
  pinMode(led,OUTPUT);
  
  
  // zona de abilitacion

}

void loop()
{
  while (Serial.available))==0
  char val=Serial.read();
  if (val=="1")   {
    Serial.println("led esta ON");
    digitalWrite(led,HIGH);
  }
  
 else if(val== "0") {
  Serial.println("led esta OFF");
  digitalWrite(led,LOW);
 }
  else          {
    Serial.println("tecla invalida")
  }
  // zona de instruccion 

}
