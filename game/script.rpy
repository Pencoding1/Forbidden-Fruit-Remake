call splashscreen from _call_splashscreen
label start:
    call opening from _call_opening
    call FirstMeet from _call_FirstMeet
    call wakeup from _call_wakeup
    call hospital from _call_hospital
    if end == 1:
        call end from _call_end
    if chap2 == 1:
        stop music
        call transformchap2 from _call_transformchap2
        call chap2 from _call_chap2
return
label gameover:
    "Game Over"
return
