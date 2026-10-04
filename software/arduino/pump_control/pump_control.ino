int pumpPin = 7;

void setup() {

  Serial.begin(9600);

  pinMode(pumpPin, OUTPUT);
  digitalWrite(pumpPin, LOW);

  delay(1000);

  Serial.println("Sprayer Ready!");
  Serial.println("Press 1 -> Spray 3.5 seconds");
  Serial.println("Press 2 -> Spray 5 seconds");
}

void loop() {

  if (Serial.available() > 0) {

    char cmd = Serial.read();

    if (cmd == '1') {

      Serial.println("Spraying 3.5 sec...");

      digitalWrite(pumpPin, HIGH);
      delay(3500);
      digitalWrite(pumpPin, LOW);

      Serial.println("Done!");
    }

    else if (cmd == '2') {

      Serial.println("Spraying 5 sec...");

      digitalWrite(pumpPin, HIGH);
      delay(5000);
      digitalWrite(pumpPin, LOW);

      Serial.println("Done!");
    }

    else {

      Serial.println("Invalid! Press 1 or 2 only.");
    }
  }
}
