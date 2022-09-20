void setup() {
  Serial.begin(9600);
  pinMode(A0, INPUT); //Data pin for ambient light sensor
  pinMode(8, INPUT); //Pin for PIR 
  pinMode(9, OUTPUT); //Led for PIR
  pinMode(12,OUTPUT); //Pin for Buzzer
  pinMode(13, OUTPUT); //Led for ambient light sensor
}

void loop() {
  int light_value = analogRead(A0);
  float light = light_value * 0.0976; // Percentage calculation 
  Serial.println(light);
  delay(100);
  if (light_value < 1000) //If the surrounding is dark the LED will glow
  {
    digitalWrite(13, HIGH);
  }
  else 
  {
    digitalWrite(13,LOW);
  }
  
  int a=digitalRead(8); //Motion detection
  
  digitalWrite(9,LOW);  
  if(a)
  {
    Serial.println("Motion detected!");
    digitalWrite(9,HIGH);
  }
  
  double t=analogRead(A1);
  double tm=(((t/1024)*5)-0.5)*100; // Temperature conversion to Celcius
  Serial.print("Temperature value: ");
  Serial.println(tm);
  if (tm>58) //If temperature is more than 58°C, fire is detected; led will glow and buzzer will go off 
    tone(12,15000);
  else
    noTone(12);

}  