import board

from kmk.hid import HIDModes
from kmk.kmk_keyboard import KMKKeyboard
from kmk.keys import KC
from kmk.scanners import DiodeOrientation
from kmk.extensions.media_keys import MediaKeys
from kmk.modules.holdtap import HoldTap
from kmk.modules.mouse_keys import MouseKeys
from kmk.modules.layers import Layers


keyboard = KMKKeyboard()

keyboard.col_pins = [
    board.SPI,
    board.RX,
    board.TX,
    board.D13,
    board.D12,
    board.D11,
    board.D10,
    board.D9,
    board.D6,
    board.D5,
    board.SCL,
    board.SDA,
]

keyboard.row_pins = [
    board.A0,
    board.A1,
    board.A2, # ent: p0_03
    board.A3,
    board.A4, # ent: p0_13
]

keyboard.diode_orientation = DiodeOrientation.COL2ROW

keyboard.modules.append(Layers())
keyboard.modules.append(MouseKeys())
keyboard.modules.append(HoldTap())
keyboard.extensions.append(MediaKeys())

LAYER1 = KC.MO(1)
LAYER2 = KC.MO(2)
LAYER3 = KC.MO(3)
MOUSE_1 = KC.MO(4)
MOUSE_2 = KC.MO(5)

ESC = KC.HT(KC.ESC, KC.LCTRL)
LANG1 = KC.LCTL(KC.SPC)
SCRN = KC.LGUI(KC.LSFT(KC.N4))

keyboard.keymap = [
    ## ---- LAYER_0 -------------------------------------------------------------------------------------
    ## |  GRAV |  1   |  2   |  3   |  4    |  5     |   6     |  7     |  8   |  9    |   0   | BKDL   |
    ## |  TAB  |  Q   |  W   |  E   |  R    |  T     |   Y     |  U     |  I   |  O    |   P   |  \     |
    ## |  ESC  |  A   |  S   |  D   |  F    |  G     |   H     |  J     |  K   |  L    |   ;   |  '     |
    ## | SHIFT |  Z   |  X   |  C   |  V    |  B     |   N     |  M     |  ,   |  .    |   /   | RET    |
    ## |  LANG1| MOUSE_1| LALT | LGUI | L_1   | SPACE  |  SPACE  |  L_2   | LEFT |  DOWN |   UP  | RIGHT  |
    [
        KC.GRV,  KC.N1, KC.N2,   KC.N3,   KC.N4,  KC.N5,  KC.N6,   KC.N7,  KC.N8,   KC.N9,   KC.N0,   KC.BKDL,
        KC.TAB,  KC.Q,  KC.W,    KC.E,    KC.R,   KC.T,   KC.Y,    KC.U,   KC.I,    KC.O,    KC.P,    KC.BSLS,
        ESC,     KC.A,  KC.S,    KC.D,    KC.F,   KC.G,   KC.H,    KC.J,   KC.K,    KC.L,    KC.SCLN, KC.QUOT,
        KC.LSFT, KC.Z,  KC.X,    KC.C,    KC.V,   KC.B,   KC.N,    KC.M,   KC.COMM, KC.DOT,  KC.SLSH, KC.ENT,
        LANG1,   MOUSE_1, KC.LALT, KC.LGUI, LAYER1, KC.SPC, KC.BSPC, LAYER2, KC.LEFT, KC.DOWN, KC.UP,   KC.RGHT,
    ],

    ## ---- LAYER_1 ----------------------------------------------------------------------------
    ## |  F12  |  F1  |  F2  |  F3  |  F4  |  F5  |  F6   |  F7  |  F8  |   F9 |  F10  |  F11  |
    ## |       |      |      |      |      |      |       |  7   |   8  |  9   |       |       |
    ## |       |      |      |      |      |      |       |  4   |   5  |  6   |       |       |
    ## |       |      |      |      | 한/영 | SCRN |       |  1   |   2  |  3   |       |       |
    ## |       |      |      |      |      |      |       | L_3  |   0  | PREV | NEXT  | PLAY  |
    [
        KC.F12,  KC.F1,   KC.F2,   KC.F3,   KC.F4,    KC.F5,   KC.F6,   KC.F7,   KC.F8,   KC.F9,   KC.F10,  KC.F11,
        KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS,  KC.TRNS, KC.TRNS, KC.KP_7, KC.KP_8, KC.KP_9, KC.TRNS, KC.TRNS,
        KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS,  KC.TRNS, KC.TRNS, KC.KP_4, KC.KP_5, KC.KP_6, KC.TRNS, KC.TRNS,
        KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.LANG1, SCRN,    KC.TRNS, KC.KP_1, KC.KP_2, KC.KP_3, KC.TRNS, KC.TRNS,
        KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS,  KC.TRNS, KC.TRNS, LAYER3,  KC.KP_0, KC.MRWD, KC.MFFD, KC.MPLY,
    ],
    ## ---- LAYER_2 ----------------------------------------------------------------------------
    ## |  F12  |  F1  |  F2  |  F3  |  F4  |  F5   |  F6   |  F7   |  F8  |  F9       |   F10   |   DEL   |
    ## |       |      |      |  _   |  +   |   (   |   )   | HOME  |  UP  |  END      |         |         |
    ## |       |      |      |  =   |  -   |   [   |   ]   | LEFT  | DOWN | RIGHT     |         |         |
    ## |       |      |      |      |      |   {   |   }   |       |      |  BRGTDOWN |  BRGTUP |         |
    ## |       |      |      |      | L_3  |       |       |       | MUTE |   VOL-    |   VOL+  |  PLAY   |
    [
        KC.F12,  KC.F1,   KC.F2,   KC.F3,   KC.F4,   KC.F5,   KC.F6,   KC.F7,   KC.F8,   KC.F9,   KC.F10,  KC.DEL,
        KC.TRNS, KC.TRNS, KC.TRNS, KC.UNDS, KC.PLUS, KC.LPRN, KC.RPRN, KC.HOME, KC.UP,   KC.END,  KC.TRNS, KC.TRNS,
        KC.TRNS, KC.TRNS, KC.TRNS, KC.EQL,  KC.MINS, KC.LBRC, KC.RBRC, KC.LEFT, KC.DOWN, KC.RGHT, KC.TRNS, KC.TRNS,
        KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.LCBR, KC.RCBR, KC.TRNS, KC.TRNS, KC.BRID, KC.BRIU, KC.TRNS,
        KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, LAYER3,  KC.TRNS, KC.TRNS, KC.TRNS, KC.MUTE, KC.VOLD, KC.VOLU, KC.MPLY,
    ],
    ## ---- LAYER_3 ---------------------------------------------------------------------------------
    ## | RESET|      |      |      |      |      |      |      |      |        |        | BT_CLR |
    ## |      |      |      |      |      |      |      |      |      |        |        |        |
    ## |      |      |      |      |      |      |      |      |      |        |        |        |
    ## |      |      |      |      |      |      |      |      |      |        |        |        |
    ## |      |      |      |      |      |      |      |      |      | BT_PRV | BT_NXT |        |
    [
        KC.RESET, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS,   KC.TRNS,   KC.BT_CLR,
        KC.TRNS,  KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS,   KC.TRNS,   KC.TRNS,
        KC.TRNS,  KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS,   KC.TRNS,   KC.TRNS,
        KC.TRNS,  KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS,   KC.TRNS,   KC.TRNS,
        KC.TRNS,  KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.BT_PRV, KC.BT_NXT, KC.TRNS,
    ],
    ## ---- MOUSE_1 ------------------------------------------------------------------------------
    ## |       |      |      |      |      |      |       |       |       |       |       |       |
    ## |       |      |      |      |      |      |       | LT_CK | MS_UP | RT_CK |       |       |
    ## |       |      |      |      |      |      | MD_CK | MS_LT | MS_DN | MS_RT |       |       |
    ## |       |      |      |      |      |      |       |       |       |       |       |       |
    ## |MOUSE_2|      |      |      |      |      |       |       |       |       |       |       |
    [
        KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS,   KC.TRNS,   KC.TRNS,  KC.TRNS,   KC.TRNS, KC.TRNS,
        KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS,   KC.MB_LMB, KC.MS_UP, KC.MB_RMB, KC.TRNS, KC.TRNS,
        KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.MB_MMB, KC.MS_LT,  KC.MS_DN, KC.MS_RT,  KC.TRNS, KC.TRNS,
        KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS,   KC.TRNS,   KC.TRNS,  KC.TRNS,   KC.TRNS, KC.TRNS,
        MOUSE_2, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS,   KC.TRNS,   KC.TRNS,  KC.TRNS,   KC.TRNS, KC.TRNS,
    ],
    ## ---- MOUSE_2 ------------------------------------------------------------------------------
    ## |      |      |      |      |      |      |       |        |        |        |       |       |
    ## |      |      |      |      |      |      |       | LT_CK  | WHL_UP | RT_CK  |       |       |
    ## |      |      |      |      |      |      | MD_CK | WHL_LT | WHL_DN | WHL_RT |       |       |
    ## |      |      |      |      |      |      |       |        |        |        |       |       |
    ## |      |      |      |      |      |      |       |        |        |        |       |       |
    [
        KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS,   KC.TRNS,   KC.TRNS,  KC.TRNS,   KC.TRNS, KC.TRNS,
        KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS,   KC.MB_LMB, KC.MW_UP, KC.MB_RMB, KC.TRNS, KC.TRNS,
        KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.MB_MMB, KC.MW_LT,  KC.MW_DN, KC.MW_RT,  KC.TRNS, KC.TRNS,
        KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS,   KC.TRNS,   KC.TRNS,  KC.TRNS,   KC.TRNS, KC.TRNS,
        KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS,   KC.TRNS,   KC.TRNS,  KC.TRNS,   KC.TRNS, KC.TRNS,
    ],
]

if __name__ == '__main__':
    keyboard.go(hid_type=HIDModes.BLE, ble_name='5x12')
