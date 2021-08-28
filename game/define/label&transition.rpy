label splashscreen:

    scene black with dissolve

    scene logo with dissolve

    pause (3)

    show black with dissolve

    hide logo with dissolve

    return

label opening:
    stop music
    scene black with dissolve
    pause(2)
    play music "audio/ost1.ogg" volume 0.65 fadein (1)
    "{cps=20}Một căn bệnh không thể miêu tả bằng lời.{w} Tất cả chỉ như một khái niệm không thể xác định{/cps}"
    "{cps=20}Không nguyên nhân.{/cps}"
    "{cps=20}Không triệu chứng.{/cps}"
    "{cps=20}Chỉ thầm lặng đến...{w} rồi mang theo sinh mệnh của nạn nhân{/cps}"
    "{cps=20}Căn bệnh mang tên {color=#990000}TÌNH YÊU{/color}.{/cps}"
    "{cps=20}Nghe thật ngọt ngào. {w} Nhưng cũng thật tàn nhẫn.{/cps}"
    "{cps=20}Không có thuốc chữa.{/cps}"
    "{cps=20}Không thể kiểm soát.{/cps}"
    "{cps=20}Tuy vậy vẫn có duy nhất một cách để phòng tránh hoàn toàn{/cps}."
    "{cps=20}Thế giới này sẽ không tồn tại tình yêu.{/cps}"
    "{cps=20}Đại khủng hoảng đã được dập tắt sau hàng ngàn năm.{/cps}"
    "{cps=20}Khi thế giới đang dần hồi phục.{/cps}"
    "{cps=20}Mọi thứ giờ chỉ còn là lịch sử{/cps}"
    "{cps=20}Vậy nhưng một thế giới như vậy có đáng để tồn tại?{/cps}"
    "{cps=20}Thế giới không có tình yêu?{/cps}"
    stop music fadeout 1.0
    scene black with dissolve
    pause (2)
    return

label callgirl:
    main "Này. Tỉnh lại đi. Làm sao mà cô vào nhà tôi được thế?"
    "Cô gái" "..."
    main "Này, tỉnh lại đi nào."
    "Mặc dù tôi liên tục to tiếng gọi cô dậy nhưng cô nàng vẫn nằm bất động như không có gì xảy ra."
    main "Mình không thể chạm vào con gái được. Nhưng có vẻ là không có cách nào để làm cô ta tỉnh dậy nhỉ?"
    menu:
        "Đi ra ngoài tìm hiểu.":
            jump end
return

label transformchap2:
    scene black with fade
    pause(3)
    show txta with dissolve
    pause(1)
    hide txta
    show txtb with dissolve
    pause(2)
return

init python:

    def wakeup():
        return fade(old_widget = black, new_widget = bedhop2)
        return pixellate(old_widget = bedhop2, new_widget = bedhop2)
