const int lastLength = 0;

const int bzr1 = 5;
const int bzr2 = 6;
const int bzr3 = 9;
const int bzr4 = 10;

int buzzerOptions[4] = { bzr1, bzr2, bzr3, bzr4 };

const int btn1 = 2;
const int btn2 = 3;
const int btn3 = 4;
const int btn4 = 7;

int buttonOptions[4] = { btn1, btn2, btn3, btn4 };

int freq[6] = {125 ,250, 500, 1000, 2000, 4000};

const long interval = 5000;

void setup() {
    Serial.begin(9600);
    Serial.println();

    pinMode(bzr1, OUTPUT);
    pinMode(bzr2, OUTPUT);
    pinMode(bzr3, OUTPUT);
    pinMode(bzr4, OUTPUT);
    pinMode(btn1, INPUT);
    pinMode(btn2, INPUT);
    pinMode(btn3, INPUT);
    pinMode(btn4, INPUT);

    unsigned long startTime = millis();
    String comdata = "";
    bool soundState = false;
}



void loop() {
    
    int freqbzrindex = (int)random(0,6);
    int numero = random(1,5);
    int selectedBuzzer = buzzerOptions[numero];

    Serial.println(btn1);
    Serial.println(btn2);
    Serial.println(btn3);
    Serial.println(btn4);

    startTime = millis();
    if (soundState == false && ####### ) {
        tone(selectedBuzzer, freq[freqbzrindex]);
        soundState = true;
    }
    if ( soundState == true && millis() - startTime >= interval )
    {
        noTone(selectedBuzzer);
        soundState = false;
        println("[ERROR]: No presionaste el boton");
        
    } 
    else if ( soundState == true && digitalRead(buttonOptions[numero]) == 1 )
    {
        noTone(selectedBuzzer);
        soundState = false;
        println("SUCESS!!");
    }
}
//}