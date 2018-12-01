int dioda = 13;
int czas =(230);
int czas2 = (600);
int czasbreak = (2000);
void setup(){
pinMode (dioda, OUTPUT);
}
void loop(){
    for (int i = 0; i < 3; i = i + 1){
        digitalWrite(dioda, HIGH);
        delay(czas);
        digitalWrite(dioda, LOW);
        delay(czas);
    }
    for (int i = 0; i < 3; i = i + 1){
        digitalWrite(dioda, HIGH);
        delay(czas2);
        digitalWrite(dioda, LOW);
        delay(czas);
    }
    for (int i = 0; i < 3; i = i + 1){
        digitalWrite(dioda, HIGH);
        delay(czas);
        digitalWrite(dioda, LOW);
        delay(czas);
    }
delay(czasbreak);
}
