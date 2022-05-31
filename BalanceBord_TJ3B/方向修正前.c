#include "D_Main.h"
#include "D_I2C.h"
#include "D_SIO.h"
//--------------------------------------------------------------------------------
// Program Name : ï˚å¸èCê≥ëO.C
//--------------------------------------------------------------------------------
void user_main(void)
{
    while (TRUE) {
        if (gAD[CN1] < 255) {
            gPwm[0] = 0x28 | 0x80;
            gPwm[1] = 0x3C | 0x80;
            gPwm[2] = 0x3C | 0x80;
            gPwm[3] = 0x28;
            pwm_out();
        } else if (gAD[CN1] < 358) {
            gPwm[0] = 0x28 | 0x80;
            gPwm[1] = 0x28 | 0x80;
            gPwm[2] = 0x28 | 0x80;
            gPwm[3] = 0x28;
            pwm_out();
        } else if (gAD[CN1] < 409) {
            gPwm[0] = 0x28 | 0x80;
            gPwm[1] = 0x00 | 0x80;
            gPwm[2] = 0x00 | 0x80;
            gPwm[3] = 0x28;
            pwm_out();
        } else if (gAD[CN1] < 511) {
            gPwm[0] = 0x28 | 0x80;
            gPwm[1] = 0x28;
            gPwm[2] = 0x28;
            gPwm[3] = 0x28;
            pwm_out();
        } else {
            gPwm[0] = 0x28 | 0x80;
            gPwm[1] = 0x3C;
            gPwm[2] = 0x3C;
            gPwm[3] = 0x28;
            pwm_out();
        }
    }
}
//--------------------------------------------------------------------------------
