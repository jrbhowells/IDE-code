// Import sample GPS roude data generated from Google Maps API
// Analyse data and use for guidance

// J Howells 25.05.2021
// IDE Group 1
// Dyson School of Design Engineering

#include "FS.h"
#include "SPIFFS.h"


void setup(){
  Serial.begin(115200);

  if(!SPIFFS.begin()){
        Serial.println("SPIFFS Mount Failed");
        return;
   }

  String directions;
  
  Serial.println("Reading...");
  
  File file = SPIFFS.open("/directions.txt");
  while(file.available()){
    directions += file.readString();
  }

  file.close();

  directions.replace(" ", "");
  directions.replace("\n", "");
  directions.replace("[", "{");
  directions.replace("]", "}");
//  directions.replace("]],[[", "*");
//  directions.replace("],[", "^");
//  directions.replace("[", "");
//  directions.replace("]", "");
//
//  String steps = directions.substring(0, directions.indexOf("*", 0));
//  String overview = directions.substring(directions.indexOf("*", 0)+1, directions.length() - 1);
//
//  String stepL[]
//  
//  Serial.println(steps);
//  Serial.println(overview);
  Serial.println(directions);
}

void loop(){
  
}
