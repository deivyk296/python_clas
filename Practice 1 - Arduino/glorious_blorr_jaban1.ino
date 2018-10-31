int pin = 0;

void setup()
{
  pinMode(12, OUTPUT);
  pinMode(7, OUTPUT);
  pinMode(4, OUTPUT);
  pinMode(13, OUTPUT);
  pinMode(2, OUTPUT);
  pinMode(8, OUTPUT);
}

void loop()
{
  digitalWrite(12, HIGH);
  digitalWrite(7, HIGH);
  delay(5000); // Wait for 5000 millisecond(s)
  digitalWrite(12, LOW);
  digitalWrite(7, LOW);
  digitalWrite(4, HIGH);
  digitalWrite(13, HIGH);
  delay(5000); // Wait for 5000 millisecond(s)
  digitalWrite(4, LOW);
  digitalWrite(13, LOW);
  digitalWrite(2, HIGH);
  digitalWrite(8, HIGH);
  delay(5000); // Wait for 5000 millisecond(s)
  digitalWrite(2, LOW);
  digitalWrite(8, LOW);
}