#define IN1 8
#define IN2 9
#define ENA 10

void setup() {

  pinMode(IN1, OUTPUT);
  pinMode(IN2, OUTPUT);
  pinMode(ENA, OUTPUT);

  digitalWrite(ENA, HIGH);

  // Forward
  digitalWrite(IN1, HIGH);
  digitalWrite(IN2, LOW);
}

void loop() {

}
