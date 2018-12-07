int led = 13;
int led1= 12;
int led2= 11;
int led3= 10;
int led4= 9;
int led5= 8;
int led6= 7;
char mydata=0;

//estados



void setup() {                
 
  pinMode(led, OUTPUT);
  pinMode(led1, OUTPUT);
  pinMode(led2, OUTPUT);
  pinMode(led3, OUTPUT);
  pinMode(led4, OUTPUT);
  pinMode(led5, OUTPUT);
  pinMode(led6, OUTPUT);    
    Serial.begin(9600);
}
 
 

void loop() {
 
 mydata= int(Serial.read());
 
if (mydata=='1')
  digitalWrite(led, HIGH);
if (mydata=='0') 
  digitalWrite(led, LOW);
   
  

if (mydata=='2')
  digitalWrite(led1, HIGH);  
 
  if(mydata=='3')
  digitalWrite(led1, LOW); 


if (mydata=='4')
  digitalWrite(led2, HIGH);   
 
  if(mydata=='5')
  digitalWrite(led2, LOW);   


if (mydata=='6')
  digitalWrite(led3, HIGH);   
 
  if(mydata=='7')
  digitalWrite(led3, LOW);   

if (mydata=='8')
  digitalWrite(led4, HIGH);  
 
  if(mydata=='9')
  digitalWrite(led4, LOW);

if (mydata=='a')
  digitalWrite(led5, HIGH);   
 
  if(mydata=='b')
  digitalWrite(led5, LOW);

if (mydata=='c')
  digitalWrite(led6, HIGH);   
 
  if(mydata=='d')
  digitalWrite(led6, LOW);


if (mydata=='e')
  digitalWrite(led,HIGH);  
        
 
  if(mydata=='f')
  digitalWrite(led,LOW);
  

  
  
  
   
}
