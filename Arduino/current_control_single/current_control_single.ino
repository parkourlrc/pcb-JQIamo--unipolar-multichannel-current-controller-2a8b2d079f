// Ahreum Lee, 2022
#include <SPI.h>
#define CLOCK_SPEED 4000000

const int CS = 10;
const float MAX_CURRENT = 5;

SPISettings settings(CLOCK_SPEED, MSBFIRST, SPI_MODE0);

void setup() {
  // put your setup code here, to run once:
  pinMode (CS, OUTPUT);
  SPI.begin();
  Serial.begin(115200);
  digitalWrite (CS, HIGH);
}

uint8_t stat, val1, val2, result;

void loop() {
  float ampere; // in ampere, should be smaller than 5
  float voltage;
  int data;
  String commend;

  while(!Serial.available());

  if(Serial.available()){
    commend = Serial.readStringUntil('\n');
    ampere = commend.toFloat();
    //voltage = ampere/5; // in volts, should be smaller than 1
    //data = round(voltage/4.096*65535);

    // If the input is larger than the max current, force it to max current.
    if(ampere > MAX_CURRENT){
      ampere = MAX_CURRENT;
    };
    
    data = round(ampere*3205+11); // from calibration
    char temp[40];
    sprintf(temp,"%f",ampere);
    Serial.println(temp);
  };
  
  SPI.beginTransaction(settings);
  digitalWrite (CS, LOW);
  SPI.transfer(data>>8);
  SPI.transfer(data);
  digitalWrite (CS, HIGH);
  SPI.endTransaction();
  delay(1000);
}
