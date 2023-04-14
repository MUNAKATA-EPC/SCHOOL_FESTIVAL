#include <Wiimote.h>

#define LED 22
#define SW 26

#define val 10

Wiimote wiimote;

int FrontG_offset = 0;
int BackG_offset = 0;
int LeftG_offset = 0;
int RightG_offset = 0;

void setup() {
  Serial.begin(115200);
  wiimote.init(wiimote_callback);

  pinMode(LED, OUTPUT);
  pinMode(SW, INPUT);

  pinMode(18, OUTPUT);
  pinMode(19, OUTPUT);
  pinMode(21, OUTPUT);//移動　or 停止

  pinMode(25, OUTPUT);//DAC

  digitalWrite(LED, LOW);
}

void loop() {
  wiimote.handle();

}

void wiimote_callback(wiimote_event_type_t event_type, uint16_t handle, uint8_t *data, size_t len) {
  static int connection_count = 0;
  //printf("wiimote handle=%04X len=%d ", handle, len);
  if (event_type == WIIMOTE_EVENT_DATA) {
    if (data[1] == 0x32) {
      for (int i = 0; i < 4; i++) {
        //printf("%02X ", data[i]);
      }
      // http://wiibrew.org/wiki/Wiimote/Extension_Controllers/Nunchuck
      uint8_t* ext = data + 4;
      /*printf(" ... Nunchuk: sx=%3d sy=%3d c=%d z=%d\n",
        ext[0],
        ext[1],
        0==(ext[5]&0x02),
        0==(ext[5]&0x01)
        );
      */
    } else if (data[1] == 0x34) {
      for (int i = 0; i < 4; i++) {
        //printf("%02X ", data[i]);
      }
      // https://wiibrew.org/wiki/Wii_Balance_Board#Data_Format
      uint8_t* ext = data + 4;
      /*printf(" ... Wii Balance Board: TopRight=%d BottomRight=%d TopLeft=%d BottomLeft=%d Temperature=%d BatteryLevel=0x%02x\n",
        ext[0] * 256 + ext[1],
        ext[2] * 256 + ext[3],
        ext[4] * 256 + ext[5],
        ext[6] * 256 + ext[7],
        ext[8],
        ext[10]
        );*/

      float weight[4];
      wiimote.get_balance_weight(data, weight);/*
      printf(" ... Wii Balance Board: TopRight=%f BottomRight=%f TopLeft=%f BottomLeft=%f\n",
        weight[BALANCE_POSITION_TOP_RIGHT],
        weight[BALANCE_POSITION_BOTTOM_RIGHT],
        weight[BALANCE_POSITION_TOP_LEFT],
        weight[BALANCE_POSITION_BOTTOM_LEFT]
      );*/

      int a = weight[BALANCE_POSITION_TOP_RIGHT];
      int b = weight[BALANCE_POSITION_BOTTOM_RIGHT];
      int c = weight[BALANCE_POSITION_TOP_LEFT];
      int d = weight[BALANCE_POSITION_BOTTOM_LEFT];

      //int SUM = weight[BALANCE_POSITION_TOP_RIGHT]+weight[BALANCE_POSITION_BOTTOM_RIGHT]+weight[BALANCE_POSITION_TOP_LEFT]+weight[BALANCE_POSITION_BOTTOM_LEFT];
      /*
            Serial.print(a);
            Serial.print("\t");
            Serial.print(b);
            Serial.print("\t");
            Serial.print(c);
            Serial.print("\t");
            Serial.print(d);
            Serial.println();
      */
      int FrontG = a + c;
      int BackG = b + d;
      int LeftG = c + d;
      int RightG = a + b;

      /*

        if (FrontG >= 35 && BackG < 35 && LeftG < 35 && RightG < 35) {
        Serial.println("前");
        } else if (FrontG < 35 && BackG >= 35 && LeftG < 35 && RightG < 35) {
        Serial.println("後");
        } else if (FrontG < 35 && BackG < 35 && LeftG >= 35 && RightG < 35) {
        Serial.println("左");
        } else if (FrontG < 35 && BackG < 35 && LeftG < 35 && RightG >= 35) {
        Serial.println("右");
        } else {
        Serial.println("止");
        }

      */
      /*
        if ((a + c) > (b + d)) {  //前>後、すなわち前進
        if ((a + c) - (b + d) > val) {
          Serial.println("前進");
        } else {
          Serial.println("停止");
        }
        } else if ((a + c) < (b + d)) { //前<後、すなわち後進
        if ((b + d) - (a + c) > val) {
          Serial.println("後進");
        } else {
          Serial.println("停止");
        }
        } else if ((c + d) > (a + b)) { //左>右、すなわち左
        if ((c + d) - (a + b) > val) {
          Serial.println("左");
        } else {
          Serial.println("停止");
        }
        } else if ((c + d) < (a + b)) { //左<右、すなわち右
        if ((a + b) - (c + d) > val) {
          Serial.println("右");
        } else {
          Serial.println("停止");
        }
        }
      */

      if (digitalRead(SW) == LOW) {
        FrontG_offset = FrontG;
        BackG_offset  = BackG;
        LeftG_offset  = LeftG;
        RightG_offset = RightG;
      }

      /*

      Serial.print (FrontG_offset);
      Serial.print(",");
      Serial.print (BackG_offset);
      Serial.print(",");
      Serial.print (LeftG_offset);
      Serial.print(",");
      Serial.println (RightG_offset);

      */

        if ((FrontG - FrontG_offset) > val) {
        Serial.println("前");
        digitalWrite(18, HIGH);
        digitalWrite(19, HIGH);
        digitalWrite(21, HIGH);

        } else if ((BackG - BackG_offset) > val) {
        Serial.println("後");
        digitalWrite(18, HIGH);
        digitalWrite(19, LOW);
        digitalWrite(21, HIGH);

        } else if ((LeftG - LeftG_offset) > val) {
        Serial.println("左");
        digitalWrite(18, LOW);
        digitalWrite(19, HIGH);
        digitalWrite(21, HIGH);

        } else if ((RightG - RightG_offset) > val) {
        Serial.println("右");
        digitalWrite(18, LOW);
        digitalWrite(19, LOW);
        digitalWrite(21, HIGH);

        } else {
        Serial.println("停止");
        digitalWrite(21, LOW);
        }


        /*
        //Serial.print("前後");
        Serial.print(FrontG - BackG);
        Serial.print(",");
        //Serial.print("左右");
        Serial.println(RightG - LeftG);
      */


      digitalWrite(LED, HIGH); //通信開始時にLED点灯
    } else {
      for (int i = 0; i < len; i++) {
        //printf("%02X ", data[i]);
      }
      //printf("\n");
    }

    bool wiimote_button_down  = (data[2] & 0x01) != 0;
    bool wiimote_button_up    = (data[2] & 0x02) != 0;
    bool wiimote_button_right = (data[2] & 0x04) != 0;
    bool wiimote_button_left  = (data[2] & 0x08) != 0;
    bool wiimote_button_plus  = (data[2] & 0x10) != 0;
    bool wiimote_button_2     = (data[3] & 0x01) != 0;
    bool wiimote_button_1     = (data[3] & 0x02) != 0;
    bool wiimote_button_B     = (data[3] & 0x04) != 0;
    bool wiimote_button_A     = (data[3] & 0x08) != 0;
    bool wiimote_button_minus = (data[3] & 0x10) != 0;
    bool wiimote_button_home  = (data[3] & 0x80) != 0;
    static bool rumble = false;
    if (wiimote_button_plus && !rumble) {
      wiimote.set_rumble(handle, true);
      rumble = true;
    }
    if (wiimote_button_minus && rumble) {
      wiimote.set_rumble(handle, false);
      rumble = false;
    }
  } else if (event_type == WIIMOTE_EVENT_INITIALIZE) {
    //printf("  event_type=WIIMOTE_EVENT_INITIALIZE\n");
    wiimote.scan(true);
  } else if (event_type == WIIMOTE_EVENT_SCAN_START) {
    //printf("  event_type=WIIMOTE_EVENT_SCAN_START\n");
  } else if (event_type == WIIMOTE_EVENT_SCAN_STOP) {
    //printf("  event_type=WIIMOTE_EVENT_SCAN_STOP\n");
    if (connection_count == 0) {
      wiimote.scan(true);
    }
  } else if (event_type == WIIMOTE_EVENT_CONNECT) {
    //printf("  event_type=WIIMOTE_EVENT_CONNECT\n");
    wiimote.set_led(handle, 1 << connection_count);
    connection_count++;
  } else if (event_type == WIIMOTE_EVENT_DISCONNECT) {
    //printf("  event_type=WIIMOTE_EVENT_DISCONNECT\n");
    connection_count--;
    wiimote.scan(true);
  } else {
    //printf("  event_type=%d\n", event_type);
  }
  //delay(10);
}
