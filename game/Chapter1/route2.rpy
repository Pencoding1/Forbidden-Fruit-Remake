label route2:
    show char_x1 at Shake((0.5, 1.0, 0.5, 1.0), 1.0, dist=5)
    x1 "{b}HẢ?"
    "Dù là người hỏi, thế nhưng vị bác sĩ kia lại nhảy dựng lên vì bất ngờ. "
    x1 "Cô gái đó là ai? Cháu gặp cô ta ở đâu? Có phải ở đoạn đường đó không? Ngoài cháu ra thì có ai khác thấy cô gái đó không?"
    "Bác sĩ hỏi dồn dập đến mức chẳng cho tôi một chút kẻ hở để trả lời. Điều đó bỗng khiến tôi nhận ra mình đã sai khi khai ra rằng có một cô gái ở đây."
    x1 "Thôi được rồi, đổi câu hỏi đi..."
    x1 "Lý do gì khiến cho cậu nghĩ đó là một cô gái?"
    main "Tôi... cũng không biết nữa. Nhưng chắc là tóc mái cô ấy dài và cơ thể có vẻ thon gọn hơn. Hoặc là một vài chổ khác."
    x1 "Một vài chổ khác?"
    main "À chả gì cả."
    x1 "Làm sao mà tôi có thể nói rằng ngực của cô ấy làm tôi liên tưởng đến con gái chứ."
    x1 "Hừm, tôi hiểu rồi, tôi sẽ báo cáo lại về phía chính quyền sau, giờ cậu cứ nghỉ ngơi đi. Mà tốt nhất là cậu nên về nhà sớm đi, dù sao thì cậu cũng đã mắc nó."
    x1 "Chắc cậu cũng tự hiểu “nó” ở đây là gì nên tôi sẽ không giải thích thêm." 
    x1 "Lát nữa sẽ có người mang thuốc đến cho cậu, tuy rằng không thể chữa khỏi nhưng ít nhất thì nó sẽ kiềm chế cảm giác đó. Nhớ rằng mỗi ngày chỉ uống một viên thôi đấy."
    x1 "Cậu chỉ còn sống được một tháng nữa thôi, thế nên hãy cân nhắc hành động của mình đi."
    main "Tôi biết rồi."
    x1 "..."
    main "Sao thế bác sĩ? Anh còn gì muốn nói à?"
    x1 "Không chỉ là tôi hơi tò mò thôi. Tại sao cậu lại bình tĩnh như thế khi biết mình chỉ còn sống được một tháng nữa thôi chứ."
    main "À...chắc là vì tôi không quan tâm. Chắc là vậy."
    x1 "Thôi sao cũng được. Tôi có việc rồi."
    play sound footstep
    hide char_x1 with dissolve
    scene blace with dissolve
    pause(1)
    scene wall with dissolve
    "Ở hành tinh này, việc yêu đương là tối kỵ."
    "Toàn bộ nam nữ đều được chia ra thành hai thế giới riêng biệt, không xâm phạm lẫn nhau."
    "Tất cả những đứa trẻ sinh ra đều nhờ phương pháp nuôi cấy nhân tạo và được bảo vệ dưới quyền của chính phủ cho đến khi kiếm được việc làm."
    "Tuy vậy thì họ cũng quản lý người dân của mình bằng một thiết bị theo dõi được cấy dưới cánh tay phải."
    "Thứ đó sẽ cho người quản lý biết địa điểm, tình trạng thể chất cũng như sinh hoạt hằng ngày của những “đứa con” của họ."
    "Hẳn thứ này đã cung cấp thông tin của tôi cho bệnh viện."
    "Dù nói như tôi biết hết nhưng những điều này cũng chỉ được nên ra trong sách vở, còn thực tế như thế nào thì tôi chưa bao giờ biết được."
    "Điều tôi biết được chính là bên kia của “Bức tường thế giới” chính là địa phận của phụ nữ."
    "Còn tất cả đàn ông chúng tôi đều sống bên này bức tường."
    "Bức tường cao đến mức dù cho nhìn ra từ phía cửa sổ phòng bệnh (một nơi cách khá xa) đi chăng nữa thì vẫn chỉ thấy được một phần bức tường xuyên lên những tầng mây."
    "Theo như trong sách vở đề cập thì bức tường cũng nằm khá sâu dưới mặt đất, hơn nữa còn được bảo trì rất thường xuyên nên chưa bao giờ thấy nứt mẻ hay trầy xước."
    stop music fadeout 1.0
    x1 "Cậu có chắc không?"
    scene bedhop2 at Shake((0.5, 1.0, 0.5, 1.0), 1.0, dist=5)
    show char_x1 with dissolve:
        xalign 0.5
    "Tôi giật mình quay mặt lại vị bác sĩ đang ngồi cạnh, vì quá mải mê chìm đắm trong mộng tưởng mà tôi lại quên đi hiện thực trước mắt."
    play music bg4 fadein 1.0
    main "À xin lỗi anh vừa nói gì vậy?"
    x1 "Tôi hỏi cậu chắc là mình chưa từng gặp cô gái nào chứ?"
    main "Tôi không nghĩ là mình lại may mắn gặp được sinh vật hiếm đó ở đây đâu."
    x1 "Vậy... à?"
    "Vị bác sĩ thở dài nhìn vào xấp giấy mà vị y tá nam kia đưa rồi làm vẻ chán nản."
    x1 'Không biết bằng cách, thế nhưng cậu đã mắc nó. Chắc cậu cũng tự hiểu “nó” ở đây là gì nên tôi sẽ không giải thích thêm.'
    x1 "Lát nữa sẽ có người mang thuốc đến cho cậu, tuy rằng không thể chữa khỏi nhưng ít nhất thì nó sẽ kiềm chế cảm giác đó."
    x1 "À đúng rồi. Vì 'nó' nên cậu chỉ còn sống có một tháng thôi đấy. Tôi khuyên cậu nên cân nhắc việc làm vào cuối đời đi."
    main "Vâng. Tôi hiểu rồi."
    scene wall with dissolve
    "Tại thế giới này, thứ mang tên “Tình Yêu” chẳng khác nào một đại dịch, là một căn bệnh chết người."
    "Một căn bệnh vốn đang chìm vào quên lãng theo dòng lịch sử, ấy vậy mà giờ đây tôi lại được chứng kiến nó bằng chính cơ thể của mình."
    "Hơi thở của tôi như bị ngưng đọng bởi thời gian. Tôi thở ra nặng nề như vừa hít phải một thứ không khí bẩn thỉu nào đó."
    "Đầu óc dần choáng váng, những hình ảnh hiện lên bắt đầu quay cuồng. Tôi nằm bệt xuống giường như thể bị đè xuống và cứ như thế chìm vào giấc ngủ tưởng chừng vĩnh hằng."
    "Tôi có lẽ sẽ chết."
    "Bởi một căn bệnh quái lạ đáng ra chỉ tồn tại trong sách vở."
    "Tất cả chỉ vì tôi đem lòng yêu một cô gái mà tôi lần đầu gặp mặt."
    stop music
    scene black with dissolve
    pause (3)
    scene bg_house with dissolve
    "Sau một thời gian nằm liệt ở bệnh viện thì tôi cuối cùng cũng được thả về, nghĩ rằng dù có ở lại lâu cũng chẳng thể chữa khỏi, nhưng tôi cũng chẳng muốn chết lây lất ở con hẻm nào đó."
    "Điều đó bỗng dưng làm tôi muốn trở lại cái nơi sặc mùi thuốc khử trùng và một bầu không khí đầy đau khổ."
    play sound opendoor
    "Tôi tra chìa khóa vào ổ khóa và mở cánh cửa gỗ có phần hơi cũ kỹ ra. Bên trong vẫn bừa bộn như ngày nào. Nhưng bỗng có một thứ gì đó làm tôi có cảm giác không thoải mái."
    "Đưa móng tay lên cào vào miếng băng gạc đang băng bó trước ngực, tôi rên lên trong đau đớn. Cổ họng như bị thiêu đốt bởi một mùi hương lạ kỳ phảng phất bên trong."
    "Lý trí tôi như bị bào mòn, tất cả cảm giác không còn hoạt động. Không còn có thể kiểm soát, tôi đưa lưỡi ra phía răng cửa và cắn thật mạnh nhằm lấy lại chút tỉnh táo."
    "Thứ cảm giác hiện giờ là thứ mà tôi không bao giờ muốn nghĩ đến, bởi lẽ rất có thể trong căn phòng này, ngay trong căn phòng tôi đang đứng tồn tại một sinh vật không thuộc về nơi này."
    "Tôi nuốt lấy nước bọt cùng máu trên đầu lưỡi vào bên trong cái cổ họng đau rát, từ từ bước vào bên trong phòng khách. Và điều có thể đoán trước đã xảy ra."
    scene black with fade
    scene bg_house with fade
    "Mùi hương dịu nhẹ phảng phất khắp căn phòng bừa bộn, một dòng suối màu đen mượt mà chảy ra khỏi mũ áo và trải đều ra xung quanh."
    "Ngay giữa phòng bỗng nhiên tỏa sáng lạ kỳ, ánh sáng như chiếu thẳng từ trên xuống tỏa ra rực rỡ khắp căn phòng."
    "Từ dưới mặt đất tắm mình trong ánh sáng, những bông hoa màu hổ phách mọc lên cùng những nhúm cỏ xanh tươi."
    "Cô gái đó, cô gái mà tôi từng bắt gặp trên đường, giờ đây hệt như nàng công chúa ngủ trong rừng."
    "Cô công chúa không còn diện váy đầm rực rỡ, chỉ còn chiếc hoodie đen quá cỡ."
    main "{b}CHUYỆN GÌ VẬY CHỨ!?"
    "Tôi khụy xuống vì cơn đau trong cơ thể. Có lẽ việc cắn lưỡi đã không còn tác dụng nữa rồi."
    "Tôi không muốn chấp nhận thứ cảm xúc mơ hồ và đầy đau đớn này nữa."
    "Vực mình ngồi dậy, tôi căng tròn đôi mắt nhìn vào cô gái đó một lần nữa. Sau hai lần đảo mắt trong đau đớn, tôi vẫn không thể tìm thấy điểm gì giống đàn ông."
    "Hẳn đây chắc chắn là phụ nữ trong truyền thuyết với bộ ngực đẫy đà cùng vòng eo quyến rũ... không thể nhầm được."
    "Dù không còn cây cỏ mọc xung quanh hay ánh sáng từ bầu trời rọi xuống thì cô gái này vẫn tỏa sáng lạ thường."
    "Nhưng vì sao..."
    pause (1)
    "Cơn đau đang lấn áp tâm trí tôi, đôi mắt một lần nữa mờ lại, đầu tôi nhức lên như búa bổ."
    "Tôi muốn thử lại phương thức cắn lưỡi khi nãy nhưng một phần trong tôi không còn nghe theo bản thân."
    "Tôi ngã khuỵu ra một lần nữa trong khi bàn tay vẫn nắm chặt lồng ngực."
    "Tôi hít một hơi thật sâu và chống cánh tay trái xuống đất, vực mình dậy."
    "Vì sao cô gái này lại ở đây, vì sao cô ta nằm ngay giữa phòng tôi, tôi không biết. Mà vốn dĩ ngay từ đầu làm sao cô ta vào nhà được cũng là một bí ẩn rồi."
    "Tôi biết rằng đây hẳn chẳng phải điều gì tốt lành gì khi giữ một người con gái trong nhà. Nhưng ít nhất cũng phải nằm trong giường của tôi đi chứ."
    "Chẳng muốn cắn lưỡi lần nữa, tôi đưa tay ra và tát bản thân một cái thật mạnh, nhưng với cái sự yếu ớt của tôi bây giờ thì cái tất vừa rồi chỉ đủ để đuổi muỗi."
    "Biết rằng chẳng thể để cô gái này ở đây, tôi quỳ một gối xuống và bế cô ta lên trong khi bản thân đang bị công kích một cách nặng nề."
    "Mùi hương ngọt ngào, làn da mền mịn, đàn hồi, cũng mái tóc mượt thoang thoảng lại chạm nhẹ vào tay tôi làm tôi sợ rằng tôi không thể giữ vững ý chí cho đến khi vào phòng được."
    "Đôi bàn chân run rẩy từng bước nặng trĩu như mang trên mình thứ gông cùm bằng kim loại, tôi lết cơ thể đang rỉ máu của mình vào tận phòng ngủ."
    play sound bone volume 2.0
    "Cánh cửa phòng đã ở ngay phía trước. Thế nhưng, ngay khi bước qua cánh cửa, tôi vô tình dập ngón chân vào cạnh cửa."
    "Sự đau đớn bắt đầu lan tuyền từ ngón chân chạy qua chặng đường dài của dây thần kinh và lên đến não tôi, cộng thêm sự đau đớn của những vết thương rỉ máu cũng trái tim loạn nhịp."
    "Tôi chẳng còn cách nào ngoài đầu hàng trước cơn đau và ngã khuỵu xuống."
    "Nhưng cũng nhờ vậy, sự tỉnh táo của tôi đã được lấy lại."
    play sound opendoor
    "Tôi với tay mở cửa."
    "Gì vậy chứ? Tại sao tôi lại là người rơi vô cái tình cảnh éo le mà tưởng chừng mình sẽ chẳng bao giờ gặp này chứ? Đây chẳng phải điều mà tôi mong đợi."
    "Thứ cảm xúc kỳ lạ khi trước giờ đây lại ào ạt trở lại như một cơn sóng thần đổ ập vào đất liền, chính bản thân nó là động lực duy nhất khiến tôi làm việc này, một công việc làm rút ngắn tuổi thọ của tôi đi hàng chục năm."
    "Tất cả là tại cô gái này, thứ cảm xúc không đáng xuất hiện kia, sự đau đớn không đáng có của tôi đều xuất phát từ cô ta mà ra."
    "Ấy vậy mà thay về chịu trách nhiệm về việc mình đã làm thì cô ta lại nằm gọn trong tôi và ngủ một cách ngon lành."
    "Đôi lúc tôi chỉ muốn mắt mình bị mù khi thấy được những thứ kinh tởm đằng sau con hẻm, nhưng bây giờ tôi cũng ước, điều ước làm phế bỏ tất cả các giác quan trước sự hiện diện tuyệt trần này."
    "Trong căn phòng không chút ánh đèn chỉ có độc một cái giường rất đỗi bình thường cùng vài cái kệ sách nằm xung quanh."
    "Còn phần diện tích còn lại chỉ có rác là rác. Mặc kệ đống rác dưới chân, tôi dẫm lên chúng và tiến đến gần chiếc giường đơn sơ của mình."
    "Khỏi phải nói cũng biết khi đặt cô ta xuống giường thì còn khó hơn cả việc bế cô ta lên bởi giờ đây cánh tay đang kẹt cứng giữa mặt giường và cái cơ thể nặng trịch kia."
    "Nếu chẳng may tôi động trúng một thứ gì đó thì nó chẳng phải lỗi của tôi."
    "Đúng vậy, tôi không có lỗi."
    "Mải mê lảm nhảm, tôi quên mất việc lồng ngực mình đau đến mức nào."
    "Chẳng còn sức mà đùa cợt, tôi nhẹ nhàng rút cánh tay của mình ra và bước ra ngoài."
    play sound closedoor fadein 2.0
    "Đóng chặt cánh cửa để chắc chắn mình sẽ không mở ra trong một khoảng thời gian đủ để làm nguội lại tinh thần."
    "Chẳng còn cần bất cứ liều thuốc giảm đau nào, tôi bỗng hoàn toàn trở lại trạng thái bình thường ngay khi bước ra ngoài."
    "Không ngờ giờ đây tôi lại sợ phải đi vào chính căn nhà của bản thân."
    $ end += 1
    return