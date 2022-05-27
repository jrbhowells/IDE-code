const byte pinI = 13;
const byte pinR = 12;
const byte pinL = 11;

const byte pinC = 0;
const byte pinY = 1;
const byte pinX = 2;

void setup() {
  pinMode(pinI, OUTPUT);
  pinMode(pinR, OUTPUT);
  pinMode(pinL, OUTPUT);
  
  pinMode(pinC, INPUT);
  pinMode(pinY, INPUT);
  pinMode(pinX, INPUT);

  randomSeed(analogRead(3));
}

void flash(int n) {
  for (int i = 0; i <= n; i++) {
    digitalWrite(pinI, HIGH);
    delay(50);
    digitalWrite(pinI, LOW);
    delay(50);
  }
}

void loop() {

  if (analogRead(pinY) <= 500) {
    digitalWrite(pinI, HIGH);
    digitalWrite(pinR, HIGH);
    delay(100);
  };

  if (analogRead(pinY) >= 1000) {
    digitalWrite(pinI, HIGH);
    digitalWrite(pinL, HIGH);
    delay(100);
  };
  
  digitalWrite(pinI, LOW);
  digitalWrite(pinL, LOW);
  digitalWrite(pinR, LOW);

  if (analogRead(pinX) <= 100) {
    flash(5);
    
    while (true) {
      const int L = random(1,3);
      if (L == 1) {
        digitalWrite(pinR, HIGH);
      } else {
        digitalWrite(pinL, HIGH);
      };
      delay(1000);
      digitalWrite(pinL, LOW);
      digitalWrite(pinR, LOW);
      delay(random(1000, 4000));
      
      if (analogRead(pinX) >= 1000) {
        flash(7);
        break;
      };
    };
  };
}
