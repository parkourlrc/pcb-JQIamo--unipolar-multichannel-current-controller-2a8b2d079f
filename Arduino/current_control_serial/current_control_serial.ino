// Ahreum Lee, 2022
#include <SPI.h>
#define CLOCK_SPEED 4000000
#define NUM_BOARDS 5

const int CS = 10;
const float MAX_CURRENT = 5;

SPISettings settings(CLOCK_SPEED, MSBFIRST, SPI_MODE0);

void setup() {
  pinMode (CS, OUTPUT);
  SPI.begin();
  Serial.begin(115200);
  digitalWrite (CS, HIGH);
}

//uint8_t stat, val1, val2, result;
String delimiter =" ";
String commend;
String token[NUM_BOARDS];
float ampere[NUM_BOARDS];
int data[NUM_BOARDS];
int idx[NUM_BOARDS];


void loop() {

  while(!Serial.available());

  if(Serial.available()){
    commend = Serial.readStringUntil('\n');
    for(byte i=0; i<NUM_BOARDS; i=i+1){
      if(i==0){
        idx[i] = commend.indexOf(delimiter);
        token[i] = commend.substring(0,idx[i]);
        continue;
      }
      idx[i] = commend.indexOf(delimiter, idx[i-1]+1);
      token[i] = commend.substring(idx[i-1]+1);
    }

    char temp[40];
    for(byte i=0; i<NUM_BOARDS; i=i+1){
      ampere[i] = token[i].toFloat();
      if(ampere[i] > MAX_CURRENT){
        ampere[i] = MAX_CURRENT;
        //to-do: print error message
      }
      data[i] = round(ampere[i]*3205+11); // from calibration
      
      sprintf(temp,"%f",ampere[i]);
      Serial.println(temp);
    }
  };
  
  SPI.beginTransaction(settings);
  digitalWrite (CS, LOW);
  for(byte i=0; i<NUM_BOARDS; i=i+1){
    SPI.transfer(data[i]>>8);
    SPI.transfer(data[i]);
  }
  digitalWrite (CS, HIGH);
  SPI.endTransaction();
  delay(1000);
}
