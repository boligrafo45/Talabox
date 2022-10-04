const int stepX2 = 2;
const int dirX2  = 5;

const int stepY = 3;
const int dirY  = 6;

const int enPin = 8;

const int stepX = 4;
const int dirX  = 7;

const int stepY2 = 12; //SpnEn
const int dirY2  = 13; //Spn Dir


void setup() {
  pinMode(stepX,OUTPUT);
  pinMode(dirX,OUTPUT);

  pinMode(stepY,OUTPUT);
  pinMode(dirY,OUTPUT);
  
  pinMode(stepX2,OUTPUT);
  pinMode(dirX2,OUTPUT);

  pinMode(stepY2,OUTPUT);
  pinMode(dirY2,OUTPUT);

  pinMode(enPin,OUTPUT);
  Serial.begin(9600); 

digitalWrite(dirX,HIGH);
digitalWrite(dirY,LOW);
digitalWrite(dirX2,HIGH);
digitalWrite(dirY2,LOW);
    
}

void loop() {

  for(int x = 0; x<200; x++) { // loop for 200 steps
  digitalWrite(stepX2,HIGH);
  delayMicroseconds(500);
  digitalWrite(stepX2,LOW); 
  delayMicroseconds(500);
  
if (Serial.available()>0){
    String buttee= Serial.readStringUntil('\n');
    if (buttee== "D")
    {digitalWrite(dirX,LOW);
    Serial.print("Change direction to the left");}
    if (buttee== "G")
    {digitalWrite(dirX,HIGH);
    Serial.print("Change direction to the right");}
    if (buttee== "H")
    {digitalWrite(dirY,HIGH);
    Serial.print("Change direction down");}
    if (buttee== "B")
    {digitalWrite(dirY,LOW);
    Serial.print("Change direction up");}
   if (buttee== "D2")
    {digitalWrite(dirX2,LOW);
    Serial.print("Change direction to the left");}
    if (buttee== "G2")
    {digitalWrite(dirX2,HIGH);
    Serial.print("Change direction to the rigth");}
    if (buttee== "H2")
    {digitalWrite(dirY2,HIGH);
    Serial.print("Change direction down");}
    if (buttee== "B2")
    {digitalWrite(dirY2,LOW);
    Serial.print("Change direction up");}

  
 }
 //delay(1000); 
  
  }
  }
  
