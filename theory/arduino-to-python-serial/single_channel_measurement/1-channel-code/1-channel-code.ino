#define ADC_VREF_mV    5000.0 // in millivolt
#define ADC_RESOLUTION 1024.0

int senzor_adc;  
int senzor_mv;  
 
void setup(){
//   Serial.begin(9600);
  Serial.begin(115200);
}

void loop(){

  // vrednost 10 bitnega registra ADC
  senzor_adc = analogRead(A0);
  
  // coversion: ADC -> mV
  senzor_mv = (senzor_adc/ADC_RESOLUTION)*ADC_VREF_mV;
 
  Serial.println(senzor_mv);

  delay(100);
}
