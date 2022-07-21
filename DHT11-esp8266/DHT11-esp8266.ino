//#include <WiFi.h>
//#include <HTTPClient.h>
#include <ESP8266WiFi.h>
#include <ESP8266HTTPClient.h>
#include <WiFiClient.h>

#include "DHT.h"
#define DHTPIN D2     // Digital pin connected to the DHT sensor

const char* ssid     = "TP-LINK_726B0E";
const char* password = "15370792";
const char* serverName = "http://192.168.43.126:8000/appiot/api/post";
// Uncomment whatever type you're using!
#define DHTTYPE DHT11   // DHT 11
DHT dht(DHTPIN, DHTTYPE);
//------------------------setup(Wifi, Bps ...)-------------------------
void setup() {
  Serial.begin(9600);
  Serial.println(F("DHTxx test!"));

  dht.begin();
//------------------------Wifi-------------------------
  WiFi.begin(ssid, password);
  Serial.println("Connecting");
  while(WiFi.status() != WL_CONNECTED) {
    delay(500);
    Serial.print(".");
  }
  Serial.println("");
  Serial.print("Connected to WiFi network with IP Address: ");
  Serial.println(WiFi.localIP());
}
//------------------------programme à éxecuter-----------------------
void loop() {
//if ((millis() - lastTime) > timerDelay) {
    // Reading temperature or humidity takes about 250 milliseconds!
            // Sensor readings may also be up to 2 seconds 'old' (its a very slow sensor)
            float h = dht.readHumidity();
            // Read temperature as Celsius (the default)
            float t = dht.readTemperature();
            // Read temperature as Fahrenheit (isFahrenheit = true)
            float f = dht.readTemperature(true);

            // Check if any reads failed and exit early (to try again).
            if (isnan(h) || isnan(t) || isnan(f)) {
              Serial.println(F("Failed to read from DHT sensor!"));
              delay(500);
              return;
            }

            // Compute heat index in Fahrenheit (the default)
            float hif = dht.computeHeatIndex(f, h);
            // Compute heat index in Celsius (isFahreheit = false)
            float hic = dht.computeHeatIndex(t, h, false);

            Serial.print(F("Humidity: "));
            Serial.print(h);
            Serial.print(F("%  Temperature: "));
            Serial.print(t);
            Serial.print(F("°C "));



    //Check WiFi connection status
    if(WiFi.status()== WL_CONNECTED){
      WiFiClient client;
      HTTPClient http;
      http.begin(client, serverName);
      http.addHeader("Content-Type", "application/json");
      int httpResponseCode = http.POST("{\"temp\":"+String(t)+",\"hum\":"+String(h)+"}");
      if (httpResponseCode>0) {
                 Serial.print("HTTP Response code: ");
                 Serial.println(httpResponseCode);
                }
                else {
                  Serial.print("Error code: ");
                  Serial.println(httpResponseCode);
                }
                // Free resources
                http.end();
              }
              else {
                Serial.println("WiFi Disconnected");
              }
              //Send an HTTP POST request every 30 seconds
              delay(90000);
//}
//}
}