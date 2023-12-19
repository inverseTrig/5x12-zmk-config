import board

from kmk.bootcfg import bootcfg

bootcfg(
    sense=board.D13,  # column
    source=board.A0, # row
    usb_id=('5x12', 'Ortholinear Keyboard'),
    midi=False,
    mouse=True,
    pan=True,
    nkro=True,
    storage=False,
)
