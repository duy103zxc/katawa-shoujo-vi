label en_A25:

window hide None
scene black
with dissolve

play sound sfx_alarmclock

scene bg school_dormhisao
with openeye

window show

"My morning alarm goes off, and I flail about uselessly for a while until I remember that I'd decided to give morning runs another shot."
"Báo thức buổi sáng bắt đầu nổ chuông, tôi vùng vẫy một lúc trước khi bắt đầu ngồi dậy và chuẩn bị đi chạy vào buổi sáng."

"Tôi chẳng biết liệu đây có phải là lựa chọn tốt nhất, nhưng tôi vẫn sẽ cố gắng tiếp tục thôi"

"This is about my health, after all."
"Đây là vì sức khỏe mà"

"Sure, things haven't been great lately for me, but that hasn't made existence so intolerable that I'm not going to try everything I can to stay healthy."
"Tuy dạo gần đây mọi thứ không ổn, nhưng điều đó chưa tới mức .... tôi sẽ thử mọi thứ tôi có thể để giữ cho mình khỏe mạnh"

"Besides, it's all about asserting some kind of control over this thing, right?"
"Bên cạnh đó, đây là cách để khẳng định quyền kiểm soát trước căn bệnh này mà phải không?"

"If I can manage that, well, I can manage anything."
"Nếu tôi có thể xử lý được điều đó thì mọi thứ sẽ ổn thôi"

"At least that's what I keep telling myself."
"Ít nhất thì tôi đã tự nhủ là vậy"

scene bg school_track
with locationskip

play ambient sfx_emirunning fadein 0.3

"Once again, it would appear that I'm not alone in my run."
"Một lần nữa, có vẻ như không phải chỉ có mình tôi đi chạy."

"Emi has apparently been here for some time."
"Emi đã có mặt ở đường chạy rồi được một lúc rồi"

"It looks like she's already worked up a good sweat."
"Có vẻ như cô ấy đã chạy được kha khá rồi đấy"

"Just when the hell does she come down here, anyway?"
"Cô ấy đã bắt đầu xuống đây từ bao giờ vậy?"

stop ambient fadeout 0.3

show emi basic_grin_gym at center
with charaenter

play music music_emi fadein 0.5

emi "Oh, it's you!"
emi "À, là Hisao này!"

show emi basic_closedgrin_gym
with charachange

emi "I'm surprised to see you again!"

hi "Why's that?"
hi "Tại sao?"

show emi basic_grin_gym
with charachange

emi "Well, not many people actually manage to come back for a second try."
emi "Không phải ai cũng quay lại đây để tiếp tục chạy"

show emi basic_annoyed_gym
with charachange

"She frowns, seemingly annoyed by a passing thought."
"Cô ấy trông hơi cay mày, có vẻ đang cảm thấy khó chịu vì một suy nghĩ thoáng qua"

emi "Like the rest of the track team, for instance."
emi "Ví dụ như đội chạy bền chẳng hạn"

emi "Still, it was only supposed to be on a volunteer basis, so it's not that big of a shock."
emi "Mà đấy cũng chỉ là tình nguyện thôi nên cũng không quá bất ngờ"

emi "And I guess it's pretty early in the morning…"
emi "Và tớ nghĩ là bây giờ vẫn còn khá sớm"

"A shrug, and suddenly it appears that she's forgotten what she was talking about."
"Cô ấy nhún vai, trông có vẻ như đã quên mình định nói gì."
 
show emi basic_happy_gym
with charachange

"The frown disappears entirely, and she seems to snap back to her previous train of thought."

emi "So! Come on, then!"
emi "Vậy bắt đầu nào!"

hi "What?"
hi "Cái gì?"

show emi excited_proud_gym
with charachange

emi "You're here to run again, right?"
emi "Cậu ở đây để chạy phải không?"

hi "Well, yes."
hi "Ừm"

show emi basic_closedhappy_gym
with charachange

emi "So come on!"
emi "Chuẩn bị thôi!"

scene bg school_track_on
with locationchange

"I find myself suddenly grabbed and yanked onto the track."
"Tôi đột ngột bị kéo ra đường chạy"

play ambient sfx_emijogging fadein 0.3

scene bg school_track_running
with locationchange

"Things seem to be set on mirroring yesterday's run."
""

"That is, I seem to be struggling, while Emi moves with an effortlessness that I find enviable."
""

"It's incredibly bothersome, to be so easily worn out."
"Khá khó chịu khi mình bị tụt sức dễ dàng đến vậy"

"I know I should be patient, work toward things gradually, but…"
"Dù biết là cần kiên trì và thực hiện từng chút một, nhưng..."

"It's difficult to stay positive about this."
"Thật không dễ dàng gì để giữ thái độ lạc quan về điều này được."

"We round the track and start on our second lap."
""

play ambient sfx_emirunning

"Emi seems to have grown impatient keeping pace with me, and begins to pull away."

"This is where I gave out yesterday."



label en_choiceA25:
menu:
    with menueffect

    "Will I be able to do more?"
    "Liệu tôi còn có thể tiếp tục chạy không?"

    "Go for it.":
    "Tiếp tục nào."
        return m1

    "Take it easy.":
    "Không cần vội"
        return m2

label en_A25a:

# if C72

stop music fadeout 10.0

"I let Emi go with her own pace, and she doesn't show mercy, pulling half a lap ahead of me in an instant."
"Để Emi tiếp tục chạy vậy,.."

"I don't blame her."
"Không thể trách cô ấy được"

"I mean, it's not as if I'm really putting up any sort of real fight out here, is it?"
""

"Instead, I'm just running at a steady pace, which is what I should be doing, right?"
"Thay vào đó, tôi chỉ cần giữ tốc độ chạy ổn định là được mà phải không?"

"There's no need to go pushing my limits at this stage of the game."
"Không cần phải cố quá trong giai đoạn này làm gì."

"God, is this even worth it?"
"Lạy chúa, liệu nó có đáng không vậy?"

scene bg school_track_on
with locationchange

"As we finish the second lap, I break off again."
vn "Khi chúng tôi hoàn thành vòng thứ hai, tôi lại tách ra."

"Emi keeps going, and it almost seems to me that she's disappointed."
vn "Emi tiếp tục chạy, và tôi gần như cảm thấy cô ấy có vẻ thất vọng."

"Well, that's stupid."
vn "Chà, thật ngớ ngẩn."

"I don't have anything to prove to her - come to think of it, I've got nothing to prove to myself, either."
vn "Tôi không có gì phải chứng minh với cô ấy cả - nghĩ kỹ thì, tôi cũng chẳng có gì phải chứng minh với bản thân mình."

"I'm just fine the way I am."
vn "Tôi ổn với con người mình hiện tại."

"And what I'm not is a runner."
vn "Và điều tôi không phải là một vận động viên chạy bộ."

"This was probably a bad idea."
vn "Đây có lẽ là một ý tưởng tồi."

"Maybe there's something else I can do instead of this."
vn "Có lẽ có thứ gì khác tôi có thể làm thay vì việc này."

"Getting up this early sucks, anyway. There's got to be some other way to keep healthy."
vn "Dù sao thì dậy sớm thế này cũng thật tệ. Chắc chắn phải có cách nào khác để giữ gìn sức khỏe chứ."

"Walking, maybe. Nice afternoon walks."
vn "Đi bộ, có lẽ vậy. Những buổi chiều đi dạo thư thái."

"Yeah, that sounds good. Running isn't for me."
vn "Ừ, nghe hay đấy. Chạy bộ không dành cho tôi."

stop ambient fadeout 2.0

scene bg school_track
with locationchange

"I wave to Emi and head back to my room."
vn "Tôi vẫy tay với Emi và quay trở lại phòng của mình."

"I'll think of something else later."
vn "Tôi sẽ nghĩ về chuyện khác sau."



#if C71

label en_A25b:

"What am I doing here?"
vn "Tôi đang làm cái quái gì ở đây vậy?"

"Am I really just going to fold and let Emi pull ahead?"
vn "Lẽ nào tôi lại bỏ cuộc và để Emi vượt lên sao?"

scene bg school_track_running
with locationchange

"I speed up."
vn "Tôi tăng tốc."

"The second lap's done quickly, and without even considering it I keep going."
vn "Vòng thứ hai kết thúc nhanh chóng, và thậm chí không cần suy nghĩ, tôi tiếp tục chạy."

"Emi looks back over her shoulder at me and grins."
vn "Emi ngoái đầu nhìn lại tôi và cười toe toét."

show emi excited_proud_gym at twoleft
with charaenter

emi "Still going?"
vn emi "Vẫn tiếp tục à?"

hi "Wouldn't *pant* want you *pant* to think I'm outta shape *pant*"
vn hi "Không *thở dốc* muốn cậu *thở dốc* nghĩ là tớ không khỏe *thở dốc*."

show emi excited_laugh_gym
with charachange

hide emi
with charamoveoutleft

play ambient sfx_emipacing

"Emi laughs - without breaking her stride, no less - and speeds up even more."
vn "Emi cười - thậm chí không hề giảm nhịp bước chân - và tăng tốc hơn nữa."

"Well, if this is the way we're going to play things…"
vn "Chà, nếu đây là cách chúng ta sẽ chơi trò này thì…"

"I increase my own pace as well."
vn "Tôi cũng sẽ tăng tốc độ chạy của mình lên."

"I can feel my lungs burning, and my legs are starting to question just what the hell I think I'm doing."
vn "Tôi có thể cảm thấy phổi mình đang cháy rát, và đôi chân bắt đầu nghi ngờ rằng tôi đang nghĩ cái quái gì trong đầu."

"Lactic acid screams in my muscles, but I close my ears."
vn "Axit lactic đang gào thét trong các khối cơ nhưng tôi nhắm chặt tai lại."

"I can't let myself fall behind, because that would be a loss."
vn "Không thể để mình bị bỏ lại phía sau được vì như thế chẳng khác nào thua cuộc."

"The rational voice in my head inquires mildly just when we started playing a game."
vn "Tiếng nói lý trí trong đầu tôi nhẹ nhàng hỏi rằng chính xác thì khi nào chúng tôi bắt đầu chơi trò chơi vậy."

"I'd answer it, but I'm having a lot of trouble thinking at present."
vn "Tôi muốn trả lời nó lắm, nhưng hiện tại tôi đang gặp rất nhiều khó khăn trong việc suy nghĩ."

"She's so {b}fast{/b}."
vn "Cô ấy {b}nhanh{/b} thật."

"How the hell does she keep it—{w=.5}{nw}"
vn "Làm thế quái nào mà cô ấy có thể duy trì được—{w=.5}{nw}"

stop music fadeout 0.2

play sound sfx_heartfast
show heartattack alpha
with Dissolve (0.1)

hide heartattack alpha
with Dissolve (0.2)

"It's like a string pulling at my chest, a choking feeling of narrowness and pain."
vn "Cứ như có một sợi dây kéo căng lồng ngực tôi, cảm giác nghẹt thở, khó chịu và đau đớn."

"Before I can think of anything else than “Oh shit,” the track disappears from under my feet."
vn "Trước khi tôi kịp nghĩ đến điều gì khác ngoài “Chết tiệt,” đường chạy biến mất khỏi dưới chân tôi."

scene bg school_track_on:
    xalign 0.5 yalign 0.52 rotate 0 zoom 1.0
    linear 0.1 rotate -6 zoom 1.2
with vpunch

"I stumble, one hand shooting down to clutch at my chest, the other hitting the track to keep me from falling on my face."
vn "Tôi loạng choạng, một tay vội vã đặt lên ngực, tay kia chống xuống đường chạy để giữ cho tôi khỏi ngã sấp mặt."

stop ambient fadeout 0.2

"Emi whirls around and her eyes widen."
vn "Emi quay phắt lại và mắt cô ấy mở to."

emi "Hisao!"
vn emi "Hisao!"

play ambient sfx_emisprinting

"She yells at me, sprinting from the other side of the track."
vn "Cô ấy hét lên với tôi, chạy nước rút từ phía bên kia đường chạy."

show emi basic_shock_gym:
    xalign 0.5 yalign 0.7 rotate -6 zoom 1.2
with charamoveinright

stop ambient fadeout 0.1

emi "What's wrong?"
vn emi "Sao vậy?"
emi "Sao vậy?"

hi "Nngh—Nothing, just…"
vn hi "Ư—Không có gì, chỉ là…"
hi "K-không có gì, chỉ là..."

play sound sfx_heartfast
show heartattack alpha
with Dissolve (0.1)

hide heartattack alpha
with Dissolve (0.2)

"Keep your breathing steady."
vn "Giữ nhịp thở đều nào."

"Calm down. Don't panic."
vn "Bình tĩnh lại. Đừng hoảng sợ."

play sound sfx_heartfast
show heartattack alpha
with Dissolve (0.1)

hide heartattack alpha
with Dissolve (0.2)

"Don't panic."
vn "Đừng hoảng sợ."

show emi basic_shock_gym:
    parallel:
        linear 0.2 rotate -12 zoom 1.5
    parallel:
        "emi basic_hes_gym" with Dissolve(0.2, alpha=True)
with None

emi "Do you need me to get the nurse?"
vn emi "Cậu có cần tớ gọi y tá không?"
emi "Cậu có cần mìn gọi y tá không?"

show black
with shuteyefast

scene black
with None

"I close my eyes, shutting out the outside world."
vn "Tôi nhắm mắt lại, đóng sầm thế giới bên ngoài."
vn "Tôi nhắm mắt lại..."

play sound sfx_heartfast
show heartattack
with Dissolve (0.1)

hide heartattack
with Dissolve (0.3)

with Pause(1.0)

play sound sfx_heartslow
show heartattack
with Dissolve (0.1)

hide heartattack
with Dissolve (0.7)

"My heart struggles to regain its rhythm."
vn "Quả tim tôi đang vật lộn để có thể tiếp tục đập ổn định."
vn "Quả tim tôi đang vật lộn để có thể tiếp tục đập ổn định."

"Slowly, the pain in my chest begins to subside."
vn "Chậm lại, cơn đau ở ngực bắt đầu dịu đi."
vn "Chậm lại, cơn đau ở ngực đang dần biến mất."

"Soon it's gone like nothing happened."
vn "Sớm thôi nó sẽ biến mất như chưa từng có gì xảy ra."
vn "Và sẽ sớm thôi, như chẳng có điều gì đã xảy ra."
 
"It was… nothing? No, something happened there."
vn "Chuyện này… không có gì sao? Không, chuyện gì đó đã xảy ra ở đây."

play music music_rain fadein 2.0

scene bg school_track_on
show emi basic_hes_gym_close at center
with openeye

"I open my eyes again and glance at a very worried Emi."
vn "Tôi lại mở mắt ra và liếc nhìn Emi đang vô cùng lo lắng."

hi "I think I'm fine."
vn hi "Tớ nghĩ là tớ ổn."

"My voice sounds weird even to myself, oddly even and matter-of-fact. It makes Emi frown."
vn "Giọng nói của tôi nghe thật kỳ lạ ngay cả với chính tôi, kỳ lạ bình tĩnh và khách quan. Điều đó khiến Emi cau mày."

show emi sad_annoyed_gym_close
with charachange

emi "I don't think you are."
vn emi "Tớ không nghĩ là cậu ổn đâu."

"She seems to come to a decision, and nods to herself."
vn "Cô ấy dường như đã đưa ra quyết định và tự gật đầu."

show emi basic_annoyed_gym_close
with charachange

emi "Right. You're coming with me."
vn emi "Được rồi. Cậu đi với tớ."

emi "You've got to see the nurse."
vn emi "Cậu phải đến gặp y tá."

with vpunch

"Emi grabs my arm and drags me up. I feel a bit wobbly, but I refuse the shoulder Emi offers for support."
vn "Emi nắm lấy cánh tay tôi và kéo tôi đứng dậy. Tôi cảm thấy hơi loạng choạng, nhưng tôi từ chối bờ vai mà Emi đề nghị làm chỗ dựa."

"Honestly, I'm a little ashamed by my own weakness."
vn "Thành thật mà nói, tôi có chút xấu hổ vì sự yếu đuối của bản thân."

"I'd really rather not have Emi concerned about me, but it seems to be too late."
vn "Tôi thực sự không muốn Emi phải lo lắng về tôi, nhưng có vẻ như đã quá muộn rồi."

"Heck, I'd really rather not have anyone concerned about my condition, though at this point, it seems to be too late for that as well."
vn "Chết tiệt, tôi thực sự không muốn bất cứ ai phải lo lắng về tình trạng của mình, mặc dù vào thời điểm này, có vẻ như cũng đã quá muộn rồi."

"I'd like to be able to deal with the whole thing on my own, without being a bother to anyone else."
vn "Tôi muốn có thể tự mình giải quyết mọi chuyện, mà không làm phiền đến bất cứ ai khác."

"While I'm wishing for things, I'd rather not have this condition in the first place."
vn "Trong khi tôi đang ước ao những điều xa vời, thì điều tôi muốn nhất là không phải mang cái bệnh này ngay từ đầu."

stop music fadeout 1.0

scene bg school_nurseoffice at bgleft
with locationskip

show emi basic_shock_gym at tworight
with easeinright

emi "Nurse!"
vn emi "Y tá ơi!"

"Emi crashes into his office without knocking, but it doesn't alarm the nurse in the least."
vn "Emi xông thẳng vào phòng y tế mà không cần gõ cửa, nhưng điều đó không làm y tá giật mình chút nào."

play music music_nurse fadein 0.5

show nurse grin at twoleft
with charaenter

nk "Good morning, sunshine. What's up?"
vn nk "Chào buổi sáng, mặt trời nhỏ. Có chuyện gì vậy?"

"Sunshine? Anyway, he calmly sips from his coffee mug but lays it down after following Emi's gaze to me looming in the doorway."
vn "Mặt trời nhỏ ư? Dù sao thì, anh ấy vẫn bình tĩnh nhấp một ngụm cà phê từ chiếc cốc của mình nhưng đặt nó xuống sau khi theo ánh mắt của Emi nhìn về phía tôi đang lờ mờ ở ngưỡng cửa."

show nurse fabulous
with charachange

nk "Hisao? What brings you here?"
vn nk "Hisao? Sao em lại đến đây?"

show emi excited_sad_gym
with charachange

emi "We were running and he stumbled over and started grabbing at his chest and I thought I'd come get you and make him wait there but he said he was okay but then I thought you should see him anyway and—{w=1.5}{nw}"
vn emi "Bọn em đang chạy thì cậu ấy vấp ngã và bắt đầu ôm ngực và em nghĩ là em nên đến gọi thầy và bảo cậu ấy đợi ở đó nhưng cậu ấy bảo là cậu ấy ổn nhưng rồi em lại nghĩ là dù sao thì thầy cũng nên xem qua cho cậu ấy và—{w=1.5}{nw}"

show nurse concern
with charachange

nk "Easy there, Emi. Calm down."
vn nk "Bình tĩnh nào, Emi. Bình tĩnh."

show nurse neutral
with charachange

nk "Hisao, what happened?"
vn nk "Hisao, chuyện gì đã xảy ra vậy?"

hi "I don't know. We were running, and then my chest started hurting like that time before, but it went away after a few seconds."
vn hi "Em không biết. Bọn em đang chạy, và rồi ngực em bắt đầu đau như lần trước, nhưng nó biến mất sau vài giây."

hi "It was just a flutter or something."
vn hi "Chỉ là một cơn thoáng qua hay gì đó thôi."

show nurse concern
with charachange

"The nurse frowns, as if to say that “just a flutter” is some kind of oxymoron."
vn "Y tá cau mày, như thể muốn nói rằng “chỉ là một cơn thoáng qua” là một kiểu mâu thuẫn vậy."

nk "I didn't mean quite this when I suggested to get some exercise. You've got to be more careful, Hisao."
vn nk "Ý tôi không phải là thế này khi tôi gợi ý em nên tập thể dục. Em phải cẩn thận hơn, Hisao ạ."

hi "I was being careful, I just…"
vn hi "Em đã cẩn thận rồi mà, chỉ là…"

"Come to think of it, “I just got into a race with a member of the track team” doesn't seem as well reasoned as I thought it would."
vn "Nghĩ lại thì, “Em vừa mới tham gia một cuộc đua với một thành viên của đội điền kinh” có vẻ không hợp lý như tôi tưởng."

nk "You just what?"
vn nk "Em chỉ… gì cơ?"

hi "Er… that is…"
vn hi "Ờ… thì là…"

hi "I was racing Emi."
vn hi "Em đã đua với Emi ạ."

nk "Emi, is this true?"
vn nk "Emi, chuyện này có thật không?"

show emi basic_hes_gym
with charachange

"Emi fidgets, looking adorably contrite."
vn "Emi bồn chồn, trông hối lỗi đến đáng yêu."

emi "Um, well…"
vn emi "Ừm, thì…"

show emi basic_closedsweat_gym
with charachange

"Finally she can't seem to bring herself to say it aloud, and merely nods."
vn "Cuối cùng cô ấy dường như không thể tự mình nói ra, và chỉ đơn thuần gật đầu."

"The nurse sighs and rubs at his forehead with one hand tiredly."
vn "Y tá thở dài và xoa trán mệt mỏi bằng một tay."

nk "Emi, you've got to be more sensitive to the limits of others!"
vn nk "Emi, em phải nhạy cảm hơn với giới hạn của người khác chứ!"

nk "I don't know if he told you, but Hisao has a bad heart, and getting him to race you was incredibly irresponsible."
vn nk "Tôi không biết em đã biết chưa, nhưng Hisao có một trái tim không khỏe, và việc để em đua với cậu ấy là vô cùng vô trách nhiệm."

hi "Er, actually I started it."
vn hi "Ờ, thực ra là em bắt đầu đấy ạ."

"The nurse is stunned by my statement."
vn "Y tá sững sờ trước lời nói của tôi."

nk "You WHAT?"
vn nk "Em… CÁI GÌ?"

hi "We were just running, and Emi started to pull away, and so I uh, sped up to catch her."
vn hi "Bọn em chỉ đang chạy thôi, và Emi bắt đầu vượt lên, và thế là em, ờm, tăng tốc để đuổi theo cô ấy."

"The nurse stares at the ceiling, mutters a prayer for patience to some god or another, and looks back down at the both of us."
vn "Y tá nhìn chằm chằm lên trần nhà, lẩm bẩm cầu nguyện sự kiên nhẫn với một vị thần nào đó, rồi nhìn xuống cả hai chúng tôi."

nk "So you're {b}both{/b} stupid."
vn nk "Vậy là {b}cả hai{/b} đứa đều ngốc."

nk "That's a comfort, I guess."
vn nk "Thật là một niềm an ủi, tôi đoán vậy."

nk "Now come on, Hisao. I've got to make sure your heart's not going to explode or something."
vn nk "Nào đi thôi, Hisao. Tôi phải chắc chắn rằng tim em không nổ tung hay gì đó."

show bg school_nurseoffice at left
show nurse concern at center
show emi basic_closedsweat_gym at Alphaout(1.0), offscreenright
with charamove

hide emi
with None

"I dutifully obey and follow him to the adjacent room where we ascertain that I am, in fact, not going to keel over and die."
vn "Tôi ngoan ngoãn tuân theo và đi theo anh ấy đến căn phòng bên cạnh, nơi chúng tôi xác định rằng thực tế là tôi sẽ không gục xuống và chết."

nk "So how does it feel?"
vn nk "Vậy em cảm thấy thế nào?"

hi "I don't know. Nothing much. Tired, but it might be just from the exercise."
vn hi "Em không biết. Không có gì nhiều. Mệt mỏi, nhưng có lẽ chỉ là do tập thể dục thôi."

nk "You should stay here for a few hours and rest, and we'll see how you feel after that."
vn nk "Em nên ở đây vài tiếng và nghỉ ngơi, rồi chúng ta sẽ xem em cảm thấy thế nào sau đó."

"I am not going to object, so I lie down on the infirmary bed."
vn "Tôi không định phản đối, vì vậy tôi nằm xuống giường bệnh."

stop music fadeout 2.0

scene bg school_nurseoffice at left
with shorttimeskip

"A thoroughly miserable Emi comes in after getting an earful from the nurse in the other room."
vn "Một Emi hoàn toàn khổ sở bước vào sau khi bị y tá khiển trách một trận trong phòng bên."

"I couldn't hear what he said through the closed door, but I'm sure it wasn't pleasantries."
vn "Tôi không thể nghe thấy những gì anh ấy nói qua cánh cửa đóng kín, nhưng tôi chắc chắn đó không phải là những lời dễ nghe."

show emi sad_depressed_gym at center
with charaenter

play music music_dreamy fadein 0.5

emi "Look, I'm really, really sorry."
vn emi "Nghe này, tớ thực sự, thực sự xin lỗi."

emi "I should've been more careful."
vn emi "Tớ đáng lẽ nên cẩn thận hơn."

hi "Hey, you didn't know. It's not your fault."
vn hi "Này, cậu không biết mà. Không phải lỗi của cậu đâu."

"She looks awfully down and sorry, and my reassurances don't do anything much to cheer her up."
vn "Cô ấy trông vô cùng buồn bã và hối lỗi, và lời trấn an của tôi chẳng giúp cô ấy vui lên chút nào."

emi "I want to make it up to you."
vn emi "Tớ muốn bù đắp cho cậu."

"Again with that decisive nod."
vn "Lại là cái gật đầu quyết đoán đó."

show emi sad_shy_gym
with charachange

emi "So you have to come to lunch with me."
vn emi "Vậy nên cậu phải đi ăn trưa với tớ."

emi "I'll bring it for you, okay? Something really really good!"
vn emi "Tớ sẽ mang đồ ăn đến cho cậu, được chứ? Món gì đó thật sự, thật sự ngon!"

"I start with a “You don't have to…” but then shut up and just nod at her when I see her face."
vn "Tôi bắt đầu bằng một câu “Cậu không cần phải…” nhưng rồi im bặt và chỉ gật đầu với cô ấy khi nhìn thấy vẻ mặt của cô ấy."

show emi excited_proud_gym
with charachange

emi "Good!"
vn emi "Tốt!"

show emi basic_grin_gym
with charachange

emi "We meet on the roof."
vn emi "Bọn mình gặp nhau trên sân thượng nhé."

hi "We?"
vn hi "Bọn mình?"

show emi basic_closedgrin_gym
with charachange

emi "Yep! The weather's nice now, so the roof's a great spot for lunch, you know."
vn emi "Ừ! Thời tiết bây giờ đẹp mà, nên sân thượng là một chỗ tuyệt vời để ăn trưa, cậu biết đấy."

hi "I see."
vn hi "Tớ hiểu rồi."

show emi sad_shy_gym
with charachange

emi "You'll come, right?"
vn emi "Cậu sẽ đến chứ, đúng không?"

emi "You wouldn't deny me the chance to make it up to you?"
vn emi "Cậu sẽ không từ chối tớ cơ hội để bù đắp cho cậu chứ?"

hi "Of course not."
vn hi "Tất nhiên là không rồi."

show emi excited_joy_gym
with charachange

emi "Great! See you there!"
vn emi "Tuyệt vời! Gặp cậu ở đó nhé!"

hide emi
with charaexit

with shorttimeskip

"I stay afloat somewhere between asleep and awake, feeling completely drained."
vn "Tôi trôi nổi đâu đó giữa trạng thái ngủ và thức, cảm thấy hoàn toàn kiệt sức."

"Not only my body, but all of me is limp and paralyzed, apart from my senses."
vn "Không chỉ cơ thể tôi, mà toàn bộ con người tôi đều uể oải và tê liệt, ngoại trừ các giác quan."

"I swallow with difficulty and then try to lie as still as I can, which in this state is not a very hard thing to do."
vn "Tôi nuốt nước bọt một cách khó khăn rồi cố gắng nằm im bất động nhất có thể, điều mà trong trạng thái này không quá khó để thực hiện."

"The nurse is shuffling around on the other side of the curtains he drew to give me privacy. I can see his shadow shifting about in the sunlight."
vn "Y tá đang lụi cụi đâu đó phía bên kia tấm rèm mà anh ấy đã kéo lại để cho tôi sự riêng tư. Tôi có thể thấy bóng của anh ấy di chuyển lờ mờ trong ánh nắng."

"He has opened the window of his office. It's windy outside."
vn "Anh ấy đã mở cửa sổ phòng làm việc. Bên ngoài trời có gió."

"The clean white curtains flutter in the breeze in a heavy, lazy motion, like waves. Light sifts through them slowly, half absorbing into the fabric."
vn "Những tấm rèm trắng sạch sẽ phất phơ trong làn gió nhẹ một cách nặng nề, lười biếng, như những con sóng. Ánh sáng len lỏi qua chúng một cách chậm rãi, một nửa thấm vào chất liệu vải."

stop music fadeout 5.0

scene darkgrey
with shuteye

"I close my eyes. The breeze on my face feels like the soft fabric of the curtains."
vn "Tôi nhắm mắt lại. Làn gió nhẹ trên mặt tôi có cảm giác như chất liệu vải mềm mại của những tấm rèm."

"I listen to the sound of my heartbeat for a moment, trying to shut out the sound of the nurse tapping away on his computer, and my own heavy breathing."
vn "Tôi lắng nghe tiếng tim mình đập trong giây lát, cố gắng lờ đi tiếng y tá gõ lách cách trên máy tính và tiếng thở nặng nhọc của chính mình."

"It's steady."
vn "Nó đều đặn."

"Damn it, not even a week and I end up like this again. I really screwed up this time. Should've known better than to play the half-baked sports star in front of a real one."
vn "Chết tiệt, chưa đầy một tuần mà tôi lại ra nông nỗi này rồi. Lần này tôi thực sự đã làm hỏng mọi chuyện. Đáng lẽ tôi phải biết rõ hơn chứ, hơn là cố gắng đóng vai ngôi sao thể thao nửa mùa trước mặt một người chuyên nghiệp thực thụ."

"And why did I try to act brave, like that heart flutter was no big deal, even when it was obvious that it was?"
vn "Và tại sao tôi lại cố tỏ ra dũng cảm, như thể cơn tim đập loạn nhịp đó chẳng có gì to tát, ngay cả khi rõ ràng là có chuyện?"

"It was just a reflex, to push it away, to keep it inside."
vn "Đó chỉ là một phản xạ, để đẩy nó đi, để giữ nó bên trong."

"I didn't want it to happen."
vn "Tôi không muốn nó xảy ra."

"I didn't want Emi to see it."
vn "Tôi không muốn Emi nhìn thấy nó."

"Aaah…"
vn "Aaaah…"

"Stupidstupidstupid."
vn "Ngu ngốcngốcngốc."

"I have to be more careful, or I will end up in the hospital again, or worse."
vn "Tôi phải cẩn thận hơn, nếu không tôi sẽ lại phải nhập viện, hoặc tệ hơn."

"…"
vn "…"

"That's my final thought before I give in to the tiredness."
vn "Đó là suy nghĩ cuối cùng của tôi trước khi tôi buông mình cho cơn mệt mỏi."

scene black
with Dissolve(1.0)

window hide Dissolve(2.0)

with Pause(2.0)

scene bg school_nurseoffice at left
with openeye

window show

play music music_daily fadein 6.0

"I fell asleep. For how long? What time is it?"
vn "Tôi đã ngủ thiếp đi. Được bao lâu rồi? Mấy giờ rồi?"

"I'm feeling a little lightheaded and I keep blinking compulsively."
vn "Tôi cảm thấy hơi choáng váng và cứ chớp mắt liên tục."

show bg school_nurseoffice at center
with charamove

"Pushing the curtain aside, I squint my eyes against the unfiltered light pouring in from the window. The texture of the canvas feels nothing like the wind did before."
vn "Kéo tấm rèm sang một bên, tôi nheo mắt trước ánh sáng chói chang không lọc tràn vào từ cửa sổ. Chất liệu vải bạt chẳng có cảm giác gì giống như làn gió trước đó."

"The nurse looks up from his work, sitting exactly where he was before."
vn "Y tá ngẩng lên khỏi công việc của mình, vẫn ngồi đúng chỗ cũ."

show nurse fabulous at center
with charaenter

nk "How are you feeling?"
vn nk "Em cảm thấy thế nào rồi?"

"I can't really tell, so I don't answer anything. I'm feeling kinda groggy from falling asleep at such a weird time, hopefully I don't look too weird."
vn "Tôi không thực sự biết nữa, nên tôi không trả lời gì cả. Tôi cảm thấy hơi lờ đờ vì ngủ thiếp đi vào một thời điểm kỳ lạ như vậy, hy vọng là trông tôi không quá kỳ cục."

hi "What time is it?"
vn hi "Mấy giờ rồi ạ?"

"Me croaking the question to gain some orientation. The nurse looking at his wristwatch before answering."
vn "Tôi khàn giọng hỏi để định hướng thời gian. Y tá nhìn đồng hồ đeo tay trước khi trả lời."

"Things seem to happen in slow motion."
vn "Mọi thứ dường như diễn ra chậm lại."

show nurse neutral
with charachange

nk "Quarter past ten."
vn nk "Mười giờ mười lăm."

"I try to think for a moment what that means but I'm not really sure."
vn "Tôi cố gắng suy nghĩ một chút xem điều đó có nghĩa là gì nhưng tôi không thực sự chắc chắn."

show nurse concern
with charachange

nk "You didn't answer my question, Hisao."
vn nk "Em vẫn chưa trả lời câu hỏi của tôi đấy, Hisao."

hi "Oh. Fine."
vn hi "Ồ. Ổn ạ."

show nurse neutral
with charachange

nk "Climb down from that bed then, and let’s see how you are doing. Don’t…"
vn nk "Vậy thì xuống giường đi, và để tôi xem em thế nào rồi. Đừng…"

$ renpy.music.set_volume(0.5, 0.2, channel="music")

show bg school_nurseoffice as dizzy_bg behind nurse:
    xalign 0.5 yalign 0.5 rotate 0 zoom 1.0 alpha 0.0
    ease 0.4 rotate 6 zoom 1.05 alpha 0.5

show nurse neutral as dizzy_fg:
    xalign 0.5 yalign 0.5 rotate 0 zoom 1.0 alpha 0.0
    ease 0.4 rotate -4 zoom 1.05 alpha 0.5
with Pause(0.4)

show bg school_nurseoffice as dizzy_bg behind nurse:
    ease 1.0 rotate 0 zoom 1.0 alpha 0.0

show nurse neutral as dizzy_fg:
    ease 1.0 rotate 0 zoom 1.0 alpha 0.0

"I try to do exactly that, only to sway dizzily when I move too fast. The nurse moves to support me by an arm and sighs."
vn "Tôi cố gắng làm đúng như vậy, nhưng lại loạng choạng chóng mặt khi di chuyển quá nhanh. Y tá tiến đến đỡ tôi bằng một tay và thở dài."

show nurse concern
hide dizzy_bg
hide dizzy_fg
with charachange

nk "…stand up too quickly, is what I was going to say. Just sit there, I’ll check your pressure to make sure."
vn nk "…đứng dậy quá nhanh, đó là điều tôi định nói. Cứ ngồi đó đi, tôi sẽ kiểm tra huyết áp cho em để chắc chắn."

$ renpy.music.set_volume(1.0, 2.0, channel="music")

"My good intentions sure lasted for a long time. I shut up, embarrassed with myself, while the nurse gets busy with an old-fashioned contraption and my arm. After a couple of minutes, he puts it away, looking neither pleased nor unhappy."
vn "Ý định tốt đẹp của tôi quả thực kéo dài được rất lâu. Tôi im bặt, xấu hổ với chính mình, trong khi y tá bận rộn với một dụng cụ đo huyết áp kiểu cũ và cánh tay của tôi. Sau vài phút, anh ấy cất nó đi, trông không vui cũng chẳng buồn."

show nurse neutral
with charachange

nk "You’re all right. Head stopped spinning?"
vn nk "Em ổn rồi. Đầu hết quay cuồng chưa?"

hi "Yeah."
vn hi "Rồi ạ."

nk "Good. And how are the contents doing?"
vn nk "Tốt. Còn “nội dung bên trong” thì sao?"

show nurse concern
with charachange

nk "You didn’t show very good judgment out there, Hisao."
vn nk "Em đã không thể hiện sự sáng suốt cho lắm ngoài kia đâu, Hisao."

"I swallow the retort I was going to make. It’s what I was thinking myself, but hearing it stated by somebody else makes me want to protest."
vn "Tôi nuốt xuống lời phản bác mà tôi định nói. Đó là điều chính tôi cũng đang nghĩ, nhưng nghe người khác nói ra khiến tôi muốn phản đối."

"What he’s saying is not pleasant to hear. Doesn’t make him any less right."
vn "Những gì anh ấy nói không dễ nghe chút nào. Nhưng điều đó không làm cho anh ấy bớt đúng đi."

hi "No, sir."
vn hi "Dạ không ạ."

show nurse neutral
with charachange

"He nods, still looking as neutral as he was before."
vn "Anh ấy gật đầu, vẫn giữ vẻ mặt trung lập như trước."

"It would be easy to be angry at him if he said “Told you so” or something, but he doesn’t."
vn "Sẽ rất dễ nổi giận với anh ấy nếu anh ấy nói “Tôi đã bảo rồi mà” hay gì đó tương tự, nhưng anh ấy không làm vậy."

nk "I can try and help you to keep your health, but ultimately the last call lies with you. Hopefully this little episode will be something that’ll remind you of that."
vn nk "Tôi có thể cố gắng giúp em giữ gìn sức khỏe, nhưng cuối cùng thì quyết định vẫn là ở em. Hy vọng rằng sự việc nhỏ này sẽ là điều nhắc nhở em về điều đó."

show nurse fabulous
with charachange

nk "Here, a note for your teacher. To avoid an interrogation."
vn nk "Đây, giấy phép cho em đây. Để tránh bị thẩm vấn."

"I take the slip of paper he's offering and then make my leave as I can't think of anything else to say, nor even really want to."
vn "Tôi cầm lấy mảnh giấy mà anh ấy đưa và rồi rời đi vì tôi không thể nghĩ ra điều gì khác để nói, thậm chí cũng không thực sự muốn nói gì."

show nurse neutral
with charachange

nk "Stay out of trouble, you hear me? I don't think it was anything but a scare, but next time could be different."
vn nk "Tránh xa rắc rối ra đấy, em nghe rõ không? Tôi không nghĩ chuyện vừa rồi có gì nghiêm trọng hơn một phen hú vía, nhưng lần tới có thể sẽ khác đấy."

"I hear you."
vn "Em nghe rõ ạ."

scene bg school_nursehall
with locationchange

stop music fadeout 4.0

"There is some way to get to the school building straight from the auxiliary building, but I'm not keen to find out and possibly get lost, so I go out from the exit that I know works."
vn "Có một lối nào đó để đi thẳng đến tòa nhà trường học từ tòa nhà phụ trợ, nhưng tôi không muốn tìm hiểu và có thể bị lạc, nên tôi đi ra từ lối ra mà tôi biết chắc là đúng."

scene bg school_courtyard
with locationchange

"I stop at the stairs of the auxiliary building, deliberating for a moment between going to the dorms to get my books and stuff and going straight away to the class."
vn "Tôi dừng lại ở cầu thang của tòa nhà phụ trợ, do dự một lúc giữa việc về ký túc xá lấy sách vở và đồ đạc hay đi thẳng đến lớp."

"The sun stings my eyes, so I head towards the dorms."
vn "Ánh nắng mặt trời chói vào mắt tôi, vì vậy tôi đi về phía ký túc xá."


#******************************

label en_A26:

window hide None
scene black
with dissolve

scene bg school_dormhisao
with openeye

with Pause(0.2)

scene bg school_dormbathroom
with locationskip

window show

"I wake up and take a hot shower."
vn "Tôi thức dậy và đi tắm nước nóng."

label en_A26a:

scene bg school_dormhisao
with locationskip

"Back in my room, the first thing I see is the familiar row of medication bottles lined up on top of my dresser, and it makes me depressed, as usual."
vn "Trở lại phòng, điều đầu tiên tôi thấy là hàng lọ thuốc quen thuộc xếp hàng trên đầu tủ quần áo của mình, và nó khiến tôi chán nản, như thường lệ."

"It's annoying. I thought I was okay. I thought I had made my peace with this thing, gotten over it."
vn "Thật khó chịu. Tôi đã nghĩ là mình ổn rồi. Tôi đã nghĩ là mình đã chấp nhận chuyện này, vượt qua nó rồi."

"But what I really did… I allowed myself to forget that I have a problem. Being here really reminds me of the reality, and trying to fight against it just hurts."
vn "Nhưng điều tôi thực sự đã làm… là tôi đã cho phép bản thân quên đi rằng mình có một vấn đề. Ở đây thực sự nhắc nhở tôi về thực tế đó, và cố gắng chống lại nó chỉ khiến tôi đau khổ."

"Reflecting on it is only going to do so much. I've done this before, for months. It seems like it's time to get over it."
vn "Suy ngẫm về nó cũng chỉ đến thế thôi. Tôi đã làm điều này trước đây, trong nhiều tháng rồi. Có vẻ như đã đến lúc phải vượt qua nó."

"If I allow myself to forget that my life is definitely not going to be as long as those of others, I won't get anywhere."
vn "Nếu tôi cho phép bản thân quên đi rằng cuộc đời mình chắc chắn sẽ không dài bằng những người khác, tôi sẽ chẳng đi đến đâu cả."

"My life may be different from others. But it is a life in progress."
vn "Cuộc sống của tôi có thể khác với người khác. Nhưng nó vẫn là một cuộc sống đang tiếp diễn."

"That is how I'll rationalize it."
vn "Đó là cách tôi sẽ hợp lý hóa nó."

"I down the usual handful of pills, trying to push the sudden dreary feeling out of my head. Then I prepare to head out to class early, as usual."
vn "Tôi nuốt xuống nắm thuốc quen thuộc, cố gắng xua đi cảm giác ảm đạm đột ngột ra khỏi đầu. Sau đó, tôi chuẩn bị ra khỏi phòng để đến lớp sớm, như thường lệ."

scene bg school_dormhallway
with locationchange

"As I step into the hallway, I notice Kenji coming around the hallway corner, stealthily making his way over to his own room with a large bag. As he sneaks past me soundlessly like a ninja hiding in plain sight, I call out to him."
vn "Khi bước ra hành lang, tôi để ý thấy Kenji đang đi vòng qua góc hành lang, lén lút tiến về phía phòng riêng của mình với một chiếc túi lớn. Khi anh ấy lướt qua tôi một cách im lặng như một ninja ẩn mình giữa thanh thiên bạch nhật, tôi gọi với theo anh ấy."

hi "Hey."
vn hi "Này."

show kenji neutral at center
with charaenter

play music music_kenji fadein 0.5

"He jumps at the sound of my voice."
vn "Anh ấy giật mình khi nghe thấy giọng nói của tôi."

ke "Oh, hey, man. I didn't notice you there. I'm really tired."
vn ke "Ồ, chào cậu, người anh em. Tớ không để ý thấy cậu ở đó. Tớ mệt quá."

"I think it's more like he didn't see me, but that's not the issue."
vn "Tôi nghĩ đúng hơn là anh ấy không nhìn thấy tôi, nhưng đó không phải là vấn đề."

hi "Where have you been this early? Shopping?"
vn hi "Cậu đã đi đâu sớm thế này? Đi mua sắm à?"

show kenji tsun
with charachange

ke "Nah, I wasn't shopping. Sometimes I have to visit… the math teacher. Yeah, I figured it would be a good idea to find out when the next exam is, since he tells you in advance if you want."
vn ke "Không, tớ không đi mua sắm. Đôi khi tớ phải đến gặp… thầy giáo dạy toán. Ừ, tớ nghĩ là nên biết trước khi nào có bài kiểm tra tiếp theo, vì thầy ấy sẽ báo trước nếu cậu muốn."

hi "So then, what's in the bag?"
vn hi "Vậy thì, cái gì trong túi thế?"

show kenji neutral
with charachange

ke "I thought I'd go shopping while I was outside. I need supplies to continue the fight against the vast feminist conspiracy."
vn ke "Tớ nghĩ là sẽ đi mua sắm khi ra ngoài. Tớ cần đồ tiếp tế để tiếp tục cuộc chiến chống lại âm mưu nữ quyền rộng lớn."

hi "Uh, okay."
vn hi "Ờ, được rồi."

hi "I thought you didn't go outside."
vn hi "Tớ tưởng cậu không ra ngoài cơ mà."

show kenji happy
with charachange

ke "I wear a hat now."
vn ke "Bây giờ tớ đội mũ rồi."

"I decide to not point out that he is not wearing a hat."
vn "Tôi quyết định không chỉ ra rằng anh ấy không đội mũ."

"An awkward silence settles between us and then Kenji breaks it by pushing his door open slowly, releasing a creaking sound into the air that only makes the moment seem more awkward. He sets the bag down inside his room and then closes the door."
vn "Một sự im lặng gượng gạo bao trùm giữa chúng tôi và rồi Kenji phá vỡ nó bằng cách đẩy cửa phòng anh ấy từ từ, tạo ra một âm thanh скрип khi cánh cửa mở ra, càng khiến khoảnh khắc trở nên gượng gạo hơn. Anh ấy đặt chiếc túi xuống bên trong phòng rồi đóng cửa lại."

hi "I'm surprised you went out of your way to find out a test date. Trying to take advantage of an opportunity to study is pretty diligent."
vn hi "Tớ ngạc nhiên là cậu lại chịu khó ra ngoài để tìm hiểu ngày kiểm tra đấy. Cố gắng tận dụng cơ hội để học bài khá là siêng năng đấy chứ."

show kenji tsun
with charachange

ke "I never study."
vn ke "Tớ không bao giờ học."

hi "Oh…"
vn hi "Ồ…"

show kenji neutral
with charachange

ke "I just wanted to know when the next test day was. I'm still going to take it, duh. I need to know so I know what day I can't afford to skip class. He usually sends out updates on that crap by phone, so I had to step out and check up on it."
vn ke "Tớ chỉ muốn biết khi nào có bài kiểm tra tiếp theo thôi. Đương nhiên là tớ vẫn sẽ làm bài kiểm tra rồi. Tớ cần biết để tớ biết ngày nào tớ không thể bỏ học được. Thầy ấy thường gửi thông báo về mấy thứ vớ vẩn đó qua điện thoại, nên tớ phải ra ngoài để kiểm tra."

hi "And why do you have to go out, when you can get it on your phone?"
vn hi "Vậy tại sao cậu phải ra ngoài, trong khi cậu có thể biết được thông tin đó qua điện thoại?"

show kenji tsun
with charachange

ke "I don't carry a phone."
vn ke "Tớ không mang điện thoại."

hi "What do you mean you don't carry a phone? You mean you just leave it at home?"
vn hi "Ý cậu là cậu không mang điện thoại á? Ý cậu là cậu chỉ để nó ở nhà thôi à?"

show kenji neutral
with charachange

ke "Nah, I don't use phones. I don't have a phone. Phones. I have no phone."
vn ke "Không, tớ không dùng điện thoại. Tớ không có điện thoại. Điện thoại. Tớ không có điện thoại."

hi "Why don't you have a phone? How can you not have a phone? No phone at all? No phone?"
vn hi "Tại sao cậu lại không có điện thoại? Làm sao cậu có thể không có điện thoại được chứ? Không có điện thoạiเลย à? Không có điện thoại?"

show kenji tsun
with charachange

ke "I just don't like phones. Actually, I'm kind of scared of them. I don't know why. I think it's some kind of repressed trauma."
vn ke "Tớ chỉ là không thích điện thoại thôi. Thực ra, tớ có hơi sợ chúng nữa. Tớ không biết tại sao. Tớ nghĩ đó là một loại травма tâm lý bị kìm nén nào đó."

ke "I have two theories on it: either I have some fear of receiving some undefined, ominous, life-altering doom call, or I was beaten with a phone in the past. Beaten so badly I can't remember it."
vn ke "Tớ có hai giả thuyết về chuyện này: hoặc là tớ có nỗi sợ nhận được một cuộc gọi định mệnh, đáng ngại, thay đổi cuộc đời nào đó, hoặc là tớ đã từng bị đánh bằng điện thoại trong quá khứ. Bị đánh đến mức tớ không thể nhớ được."

hi "Beaten in the head."
vn hi "Bị đánh vào đầu."

show kenji tsun
with charachange

ke "Well, where else could I get beaten with a phone that would make me unable to remember it? The ass?"
vn ke "Vậy chứ còn chỗ nào khác có thể bị đánh bằng điện thoại mà khiến tớ không thể nhớ được nữa chứ? Mông à?"

"Unexpectedly logical. I feel very depressed now. Sensing this conversation is more or less over, Kenji opens his door again and prepares to head inside."
vn "Logic một cách bất ngờ. Tôi cảm thấy rất chán nản bây giờ. Cảm thấy cuộc trò chuyện này ít nhiều đã kết thúc, Kenji lại mở cửa phòng và chuẩn bị đi vào bên trong."

show kenji neutral
with charachange

ke "Yeah, I'm going to sleep, dude. Have a good one."
vn ke "Ừ, tớ đi ngủ đây, người anh em. Chúc cậu một ngày tốt lành."

hi "Class is going to start in like twenty minutes."
vn hi "Sắp đến giờ vào lớp rồi đấy, còn khoảng hai mươi phút nữa."

show kenji tsun
with charachange

ke "I already did something today. Too tired to go to school."
vn ke "Hôm nay tớ đã làm một việc rồi. Mệt quá không muốn đến trường."

show kenji happy_close
with characlose

ke "Hey, you need some lip balm? I accidentally bought two because I thought the store had started selling individual double A batteries."
vn ke "Này, cậu có cần son dưỡng môi không? Tớ vô tình mua hai cái vì tớ tưởng cửa hàng bắt đầu bán pin AA lẻ rồi."

hi "Thanks but no thanks."
vn hi "Cảm ơn nhưng thôi."



label en_A26b:

scene bg school_dormhallway
show kenji happy_close at center
with None

stop music fadeout 0.3

play sound sfx_doorslam

show kenji tsun_close
with vpunch

"The door down the hall opens with a crack as it swings forward from being pushed opened too strongly and crashing against the wall. The sound is followed by a peal of bubbly laughter, and I instantly know who it is."
vn "Cánh cửa ở cuối hành lang bật mở với một tiếng răng rắc khi nó bật ra phía trước do bị đẩy mở quá mạnh và đập mạnh vào tường. Âm thanh đó được tiếp nối bởi một tràng cười khúc khích vui vẻ, và tôi lập tức biết đó là ai."

play music music_comedy fadein 0.3

show misha perky_smile at center behind kenji
show shizu basic_normal2 at center behind kenji
with zoomin


show shizu basic_normal2:
    easein 1.0 tworight
show misha perky_smile:
    easein 1.0 twoleft
show kenji tsun_close:
    0.25
    easeout 0.5 offscreenleft alpha 0.0
with Pause(1.0)

hide kenji
with None

play sound sfx_impact2

"At the noise, Kenji disappears into his room like a ninja, slamming the door shut just as Shizune and Misha walk over, the former taking small, efficient steps towards me while the latter more or less bounces off the walls."
vn "Nghe thấy tiếng động, Kenji biến mất vào phòng như một ninja, đóng sầm cửa lại ngay khi Shizune và Misha bước tới, người trước bước những bước nhỏ, hiệu quả về phía tôi trong khi người sau gần như nảy tưng tưng vào tường."

show misha hips_smile_close at twoleft
with characlose

"I try to do the same as Kenji, but it's too late. Misha puts her foot between my door to prevent me closing it, so I have no other choice but to let them in."
vn "Tôi cố gắng làm giống như Kenji, nhưng đã quá muộn. Misha đặt chân vào giữa cánh cửa phòng tôi để ngăn tôi đóng nó lại, nên tôi không còn lựa chọn nào khác ngoài việc để họ vào."

scene bg school_dormhisao
with locationskip

show shizu behind_smile at center
with charaenter

shi "…"

show shizu behind_smile at tworight
with charamove

show misha hips_grin at twoleft
with charaenter

mi "Hi, Hicchan~! Hi~ hi~!"
vn mi "Chào Hicchan~! Hi~ hi~!"

hi "Hi."
vn hi "Chào."

hi "What are you two doing here?"
vn hi "Hai cậu làm gì ở đây vậy?"

"I wonder if the pause between those two sentences was politely long enough."
vn "Tôi tự hỏi liệu khoảng dừng giữa hai câu đó có đủ lịch sự không."

show shizu basic_normal
with charachange

shi "…"

show misha hips_frown
with charachange

mi "Hicchan, that's rude~! We came to pick you up!"
vn mi "Hicchan, cậu thật vô礼~! Bọn tớ đến đón cậu đó!"

show misha hips_smile
with charachange

mi "Did you think we thought you were going to escape and came to make sure you didn't? Surely not, Hicchan~!"
vn mi "Cậu có nghĩ là bọn tớ nghĩ cậu định trốn và đến để chắc chắn rằng cậu không trốn thoát không? Chắc chắn là không phải vậy đâu, Hicchan~!"

hi "Hey, I didn't say that that's what you were here for."
vn hi "Này, tớ không nói là đó là lý do hai cậu đến đây."

"But now I know it's exactly what they are here for."
vn "Nhưng bây giờ thì tôi biết chính xác đó là lý do họ đến đây."

show misha sign_smile
with charachange

mi "It's time for student council work, yes it is~!"
vn mi "Đến giờ làm việc hội học sinh rồi, đúng vậy đó~!"

show misha hips_grin
with charachange

mi "Aren't you happy, Hicchan, to be able to help the whole~ school~! You are like, a hero~! The future generations will tell stories of this day!"
vn mi "Cậu không vui à, Hicchan, khi có thể giúp đỡ toàn~ trường~! Cậu giống như một người hùng vậy~! Thế hệ tương lai sẽ kể những câu chuyện về ngày hôm nay!"

"Interesting. I didn't think joining the Student Council would be a heroic deed worthy of Hercules."
vn "Thú vị đấy. Tôi không nghĩ việc gia nhập Hội học sinh lại là một hành động anh hùng xứng đáng với Hercules."

hi "Well… I guess I did promise so…"
vn hi "Chà… tớ đoán là tớ đã hứa rồi mà…"

show shizu adjust_happy
with charachange

stop music fadeout 7.0

"I've neglected Shizune, and only now do I notice her in the corner of my vision, peering around my room over my shoulder, her analytical eyes darting from object to object…"
vn "Tôi đã bỏ quên Shizune, và giờ đây tôi mới để ý thấy cô ấy ở góc tầm nhìn của mình, đang nhìn quanh phòng tôi qua vai tôi, đôi mắt phân tích của cô ấy đảo từ vật này sang vật khác…"

"This is kinda intrusive, the feeling of being exposed crawls in my balls. Luckily I don't have dirty laundry on the floor or anything like that."
vn "Chuyện này hơi xâm phạm riêng tư, cảm giác bị phơi bày bò lan trong người tôi. May mắn là tôi không có quần áo bẩn vứt trên sàn hay thứ gì tương tự."

show shizu behind_smile
with charachange

shi "…"

show misha perky_confused
with charachange

mi "Hm~? What is it, Shicchan?"
vn mi "Hm~? Sao vậy, Shicchan?"

show misha hips_smile
with charachange

mi "Yeah, this is Hicchan's room~! We haven't seen it before, I didn't even realize!"
vn mi "Ừ, đây là phòng của Hicchan~! Bọn tớ chưa từng vào đây trước đây, tớ thậm chí còn không nhận ra!"

show misha hips_grin
with charachange

mi "It's kinda plain, but Hicchan hasn't had time to decorate it yet, isn't that so~?"
vn mi "Nó hơi đơn giản, nhưng Hicchan chưa có thời gian để trang trí nó, đúng không~?"

show misha sign_smile
with charachange

mi "What are those?"
vn mi "Kia là cái gì thế?"

"She points at my collection of medications on the night table."
vn "Cô ấy chỉ vào bộ sưu tập thuốc của tôi trên bàn cạnh giường ngủ."



label en_choiceA26:
menu:
    with menueffect

    "I don't really want to talk about it with these two."
vn "Tôi thực sự không muốn nói về chuyện đó với hai người này."

    "Try to dodge the subject.":
vn "Cố gắng né tránh chủ đề.":
        return m1

    "Kick them out of my room.":
vn "Đuổi họ ra khỏi phòng.":
        return m2


label en_A26c:

hi "It's nothing."
vn hi "Không có gì đâu."

show shizu basic_normal2
with charachange

"I quickly step in front of them, trying to hide the stuff behind my back. Shizune takes a step back, looking suspicious, but it's an expression not without concern."
vn "Tôi nhanh chóng bước lên phía trước họ, cố gắng giấu đồ đạc ra sau lưng. Shizune lùi lại một bước, trông có vẻ nghi ngờ, nhưng đó là một biểu cảm không thiếu sự lo lắng."

"I hope if I avoid it, she'll understand that I don't want her to keep prodding me about it."
vn "Tôi hy vọng nếu tôi né tránh, cô ấy sẽ hiểu rằng tôi không muốn cô ấy tiếp tục dò hỏi tôi về chuyện đó."

show shizu behind_blank
with charachange

shi "…"

show misha perky_confused
with charachange

mi "Really? What are you hiding, Hicchan~?"
vn mi "Thật á? Cậu đang giấu gì vậy, Hicchan~?"

hi "Nothing."
vn hi "Không có gì cả."

show shizu basic_normal
with charachange

shi "…"

show misha sign_confused
with charachange

mi "Is that so~?"
vn mi "Thật vậy sao~?"

"I realize I can't really squirm my way out of this. They are nosy by nature and hiding it is just going to pique their curiosity more."
vn "Tôi nhận ra mình không thể thực sự lách qua khe cửa hẹp để thoát khỏi chuyện này. Họ vốn tò mò và việc che giấu nó chỉ càng khơi dậy sự tò mò của họ hơn thôi."

hi "Yeah okay, it is {b}something{/b}, but I don't really want to talk about it, okay? Not… yet."
vn hi "Ừ được rồi, đúng là {b}có gì đó{/b}, nhưng tớ thực sự không muốn nói về nó, được không? Chưa… phải lúc này."

hi "Can we just put this aside for now?"
vn hi "Bọn mình có thể bỏ qua chuyện này bây giờ được không?"

show misha perky_smile
with charachange

"As Misha translates, Shizune stares at me hard with her eyes focused and analytical as ever, peering at me curiously over the rims of her glasses."
vn "Trong khi Misha dịch lại, Shizune nhìn tôi chăm chú với đôi mắt tập trung và phân tích hơn bao giờ hết, tò mò nhìn tôi qua gọng kính."

"Her fingers press against each other thoughtfully, as if she's weighing the value of pursuing this further than necessary against the insult of disrespecting my wish."
vn "Các ngón tay cô ấy ấn vào nhau một cách trầm ngâm, như thể cô ấy đang cân nhắc giá trị của việc theo đuổi chuyện này hơn mức cần thiết so với sự xúc phạm khi không tôn trọng mong muốn của tôi."

"Her expression finally melts into a slight smile and she signs something to Misha."
vn "Biểu cảm của cô ấy cuối cùng cũng tan chảy thành một nụ cười nhẹ và cô ấy ký hiệu điều gì đó với Misha."

play music music_dreamy fadein 2.0

show shizu adjust_happy
with charachange

shi "…"

show misha hips_smile
with charachange

mi "Okay~! Then, we'll wait, and become better and better friends, and one day when you feel like it, you can tell us about it~!"
vn mi "Được thôi~! Vậy thì, bọn tớ sẽ đợi, và trở thành bạn tốt hơn và tốt hơn nữa, và đến một ngày nào đó khi cậu cảm thấy muốn kể, cậu có thể kể cho bọn tớ nghe về chuyện đó~!"

"Both of them smile widely at me, and I feel shocked and a little stupid about being like this."
vn "Cả hai người họ đều cười tươi với tôi, và tôi cảm thấy sốc và hơi ngớ ngẩn khi cư xử như vậy."

"They are not stupid, and probably can at least halfway guess what's going on with me. And…"
vn "Họ không hề ngốc nghếch, và có lẽ ít nhất cũng đoán được một nửa chuyện gì đang xảy ra với tôi. Và…"

"Such simple, kind words. I feel relieved that they don't think any worse of me even if I'm like this. Even if I'm not like the rest here. Even if I can't be at ease about it."
vn "Những lời nói thật đơn giản, tử tế. Tôi cảm thấy nhẹ nhõm khi họ không nghĩ xấu về tôi dù tôi có như thế này. Dù tôi không giống như những người khác ở đây. Dù tôi không thể thoải mái về chuyện đó."

"Seems that behind the obnoxious, mischievous acts, both of these girls are really kind and good people. That's what I think."
vn "Có vẻ như đằng sau những hành động tinh nghịch, khó chịu đó, cả hai cô gái này đều thực sự là những người tốt bụng và tử tế. Đó là những gì tôi nghĩ."

hi "Thanks."
vn hi "Cảm ơn."

hi "So, you want me to help you out today, right? Since I'm one of you now?"
vn hi "Vậy, hai cậu muốn tớ giúp một tay hôm nay, đúng không? Vì giờ tớ cũng là một thành viên rồi?"

show misha hips_grin
with charachange

mi "Yup~!"
vn mi "Đúng~!"

hi "After class?"
vn hi "Sau giờ học à?"

show misha sign_smile
with charachange

mi "No no no~! Now!"
vn mi "Không không không~! Bây giờ cơ!"

hi "Now? But what about class? You are going to skip again?"
vn hi "Bây giờ á? Nhưng còn lớp học thì sao? Hai cậu lại định trốn học nữa à?"

show shizu adjust_smug
with charachange

shi "…"

show misha cross_laugh
with charachange

mi "Hahaha~! It's for the common good, so we sacrifice our math lessons, and maybe the social studies too~!"
vn mi "Hahaha~! Vì lợi ích chung mà, nên bọn tớ hy sinh tiết toán, và có thể là cả tiết xã hội nữa~!"

hi "Well, I guess I'm fine with it."
vn hi "Chà, tớ đoán là tớ cũng ổn thôi."

show shizu behind_smile
with charachange

shi "…"

show misha sign_smile
with charachange

mi "Awesome, Hicchan~! You said it, okay? Remember: “I'm fine with helping out~,” that's what you said, right~?"
vn mi "Tuyệt vời, Hicchan~! Cậu nói rồi đó nha, được chứ? Nhớ nhé: “Tớ cũng ổn thôi khi giúp một tay~,” đó là những gì cậu đã nói đó, đúng không~?"

hi "Yeah."
vn hi "Ừ."

"That tone… I suddenly regret saying it."
vn "Cái giọng điệu đó… Tự nhiên tôi thấy hối hận khi đã nói vậy."

show shizu basic_normal2
with charachange

shi "…"

show misha hips_grin
with charachange

mi "Okay~! Are you ready to go then? We can go to the office together~!"
vn mi "Được rồi~! Vậy cậu đã sẵn sàng đi chưa? Bọn mình có thể cùng nhau đến văn phòng~!"

hi "No. You're probably going to make me carry all your stuff for you or something."
vn hi "Không. Chắc chắn hai cậu định bắt tớ vác hết đồ đạc cho hai cậu hay gì đó thôi."

show shizu adjust_happy
with charachange

shi "…"

show misha perky_smile
with charachange

mi "Don't be silly, Hicchan."
vn mi "Đừng ngốc thế, Hicchan."

show misha hips_smile
with charachange

mi "We've never walked to school together, Hicchan~."
vn mi "Bọn mình chưa bao giờ cùng nhau đi học mà, Hicchan~."

"I almost want to ask why we would, but then it dawns on me. The both of them consider me their friend, like Misha said before. And they want to become better friends with me, even."
vn "Tôi suýt chút nữa đã hỏi tại sao bọn tôi lại phải đi cùng nhau, nhưng rồi tôi chợt nhận ra. Cả hai người họ đều coi tôi là bạn, như Misha đã nói trước đó. Và họ còn muốn trở thành bạn tốt hơn với tôi nữa."

"It's weird, I've never really thought about them that way. Or any of the people I've met so far this week. Is it really so easy?"
vn "Thật kỳ lạ, tôi chưa bao giờ thực sự nghĩ về họ theo cách đó. Hay bất kỳ ai mà tôi đã gặp cho đến tuần này. Chuyện này thực sự dễ dàng đến vậy sao?"

"Just like that…"
vn "Chỉ đơn giản vậy thôi sao…"

hi "Okay, let's go, then."
vn hi "Được rồi, đi thôi."

show shizu behind_smile
with charachange

"Shizune grins craftily and puts her hands behind her back."
vn "Shizune cười ranh mãnh và khoanh tay sau lưng."

show misha hips_grin
with charachange

mi "Hahaha~! That's great, Hicchan~! Okay, okay, but first~! You had a really great idea, Shicchan liked it a lot… So~! it's time for a game!"
vn mi "Hahaha~! Tuyệt vời, Hicchan~! Được rồi, được rồi, nhưng trước hết~! Cậu đã có một ý tưởng thực sự tuyệt vời, Shicchan rất thích nó… Vậy nên~! Đến giờ chơi trò chơi rồi!"

hi "Oh no."
vn hi "Ôi không."

show misha hips_smile
with charachange

mi "Shicchan is holding a 1000-yen note in one hand, Hicchan~! If you guess which one, you can have it! If you don't…"
vn mi "Shicchan đang cầm một tờ 1000 yên trong một tay, Hicchan~! Nếu cậu đoán đúng tay nào, cậu sẽ có được nó! Nếu không thì…"

show misha hips_grin
with charachange

mi "You're carrying all our books to school~! Right, Shicchan~? Right~!"
vn mi "Cậu sẽ vác hết sách vở của bọn tớ đến trường~! Đúng không, Shicchan~? Đúng không~!"

"She and Shizune exchange nods."
vn "Cô ấy và Shizune trao nhau cái gật đầu."

show misha sign_smile
with charachange

mi "Okay, Hicchan~! Get ready~!"
vn mi "Được rồi, Hicchan~! Chuẩn bị nhé~!"

stop music fadeout 7.0

scene bg school_courtyard
with shorttimeskip

"Carrying three bags instead of one, I think about the day that's ahead of me. Of us."
vn "Vác ba chiếc túi thay vì một, tôi nghĩ về ngày sắp tới của mình. Của bọn tôi."

"I can see students walking back and forth through the courtyard, probably in preparation of their own projects."
vn "Tôi có thể thấy các học sinh đi đi lại lại trong sân trường, có lẽ là để chuẩn bị cho các dự án của riêng họ."

"The festival is practically here. That means there are only two possible reasons that my help is required."
vn "Lễ hội sắp đến rồi. Điều đó có nghĩa là chỉ có hai lý do có thể khiến họ cần sự giúp đỡ của tôi."

"Either there is only a small amount of work left, and they just want a helping hand to wrap up the mundane final checks they are obligated to do."
vn "Hoặc là chỉ còn một chút việc vặt, và họ chỉ muốn có thêm một bàn tay giúp họ hoàn thành những công đoạn kiểm tra cuối cùng nhàm chán mà họ buộc phải làm."

"Or there is a ton of work left, and Shizune is putting on a calm face as a torrent of built-up procrastinated work threatens to kill us all."
vn "Hoặc là còn rất nhiều việc phải làm, và Shizune đang cố tỏ ra bình tĩnh trong khi một loạt công việc bị trì hoãn dồn lại đang đe dọa sẽ giết chết tất cả bọn tôi."



label en_A26d:

play music music_rain fadein 4.0

"Even so, they have really crossed the line this time. Nosy annoyances."
vn "Dù vậy, lần này họ thực sự đã đi quá giới hạn rồi. Đúng là lũ phiền phức tọc mạch."

hi "It's nothing."
vn hi "Không có gì đâu."

show misha perky_smile
with charachange

mi "Really~, Hicchan? It doesn't look like it's nothing to me."
vn mi "Thật á~, Hicchan? Với tớ thì trông không giống như không có gì cả."

show shizu adjust_smug
with charachange

shi "…"

show misha hips_smile
with charachange

mi "What a long line of bottles, right~? Right~! What are all of those, Hicchan?"
vn mi "Một hàng dài các lọ thuốc kìa, đúng không~? Đúng không~! Tất cả những thứ đó là gì vậy, Hicchan?"

hi "Just a few things."
vn hi "Chỉ là một vài thứ thôi."

show shizu basic_normal2
with charachange

shi "…"

show misha perky_confused
with charachange

mi "That looks like a lot more than “just a few things”…"
vn mi "Trông có vẻ nhiều hơn “một vài thứ” đó…"

"I can't fault either of them for being this way. Misha's just talking for Shizune, and Shizune is just curious by nature. Still, I wish the two of them would stop digging and take the hint. But Misha wouldn't pick up on it, and Shizune can't."
vn "Tôi không thể trách cả hai người họ vì đã cư xử như vậy. Misha chỉ là đang nói hộ Shizune, và Shizune thì vốn dĩ tò mò. Dù vậy, tôi vẫn ước gì cả hai người họ sẽ ngừng đào sâu và hiểu ý tôi. Nhưng Misha thì sẽ không nhận ra, còn Shizune thì không thể."

"Because of that, they keep pressing on."
vn "Vì lẽ đó, họ cứ tiếp tục truy hỏi."

hi "It's really none of your business."
vn hi "Thực sự thì chuyện này không liên quan gì đến hai cậu cả."

hi "Shouldn't you be leaving? A man's room is private, you know."
vn hi "Hai cậu không nên đi sao? Phòng của đàn ông là chốn riêng tư đấy, hai cậu biết chứ."

"Shizune seems to take that as a challenge."
vn "Shizune dường như coi đó là một lời thách thức."

show shizu behind_frown
with charachange

shi "…"

show misha hips_frown
with charachange

mi "What does that mean, Hicchan? When someone sees something interesting, their first instinct is to ask what it is, that's obvious. What's wrong with that?"
vn mi "Ý cậu là sao, Hicchan? Khi ai đó thấy một thứ gì đó thú vị, bản năng đầu tiên của họ là hỏi xem nó là cái gì, đó là điều hiển nhiên mà. Có gì sai với chuyện đó chứ?"

hi "Because, like I said, there's nothing to see."
vn hi "Bởi vì, như tớ đã nói, chẳng có gì đáng xem cả."

show misha perky_confused
with charachange

mi "Hicchan, I think Shicchan is just concerned."
vn mi "Hicchan, tớ nghĩ Shicchan chỉ là đang lo lắng thôi."

hi "What I have in my room isn't any of your business, that's all."
vn hi "Những gì tớ có trong phòng mình không phải là chuyện của hai cậu, chỉ vậy thôi."

show misha sign_confused
with charachange

mi "But…"
vn mi "Nhưng…"

hi "Damn it! Sometimes, I wish you two would just stop playing around so much. It's not funny all the time. You know that, right?"
vn hi "Chết tiệt! Đôi khi, tớ ước gì hai cậu sẽ ngừng đùa giỡn nhiều như vậy đi. Không phải lúc nào cũng vui vẻ đâu. Hai cậu biết điều đó chứ, đúng không?"

"I say it way more strongly than I meant to, almost yelling straight at Misha's face. She flinches and freezes in mid-sign, and even Shizune reacts to it even though she didn't hear me."
vn "Tôi nói điều đó mạnh mẽ hơn nhiều so với ý định ban đầu, gần như hét thẳng vào mặt Misha. Cô ấy giật mình và khựng lại giữa chừng khi đang ra hiệu, và ngay cả Shizune cũng phản ứng lại mặc dù cô ấy không nghe thấy tôi."

stop music fadeout 6.0

"I guess my angry face said all that needs to be said to her."
vn "Tôi đoán là vẻ mặt giận dữ của tôi đã nói lên tất cả những gì cần phải nói với cô ấy rồi."

show misha perky_sad
show shizu behind_blank
with charachange

"After Misha slowly finishes the translation, the girls look at each other regretfully."
vn "Sau khi Misha chậm rãi dịch xong, hai cô gái nhìn nhau đầy hối lỗi."

show shizu behind_sad
with charachange

shi "…"

mi "Okay, Hicchan, we'll leave you alone."
vn mi "Được rồi, Hicchan, bọn tớ sẽ để cậu yên."

"It's the first time I've heard Misha speak without that familiar lilting up-and-down quality in her voice. It feels so strange to hear, and I want to apologize, but they have already turned to leave."
vn "Đây là lần đầu tiên tôi nghe thấy Misha nói mà không có cái chất giọng lên xuống quen thuộc đó. Nghe thật lạ lẫm, và tôi muốn xin lỗi, nhưng họ đã quay người rời đi rồi."

"As the silence settles in, I regret what I said more and more."
vn "Khi sự im lặng bao trùm, tôi càng ngày càng hối hận về những gì mình đã nói."

hide shizu
hide misha
with charaexit

"The girls leave quietly, and after a while of standing in my room I dress up and follow after them."
vn "Hai cô gái lặng lẽ rời đi, và sau một hồi đứng trong phòng, tôi mặc quần áo và đi theo họ."



label en_A26e:

show kenji tsun_close
with charachange

ke "Whatever, man."
vn ke "Sao cũng được, cha nội."

stop music fadeout 2.0

hide kenji
with charaexit

"He swiftly enters his lair, finally letting me go to the class."
vn "Anh ấy nhanh chóng chui vào hang ổ của mình, cuối cùng cũng để tôi đi đến lớp."

#*************************

label en_A27:

scene bg school_hallway3
with shorttimeskip

"The halls are quiet as the courtyard was, naturally so since everyone is in class. I knock lightly at the door of 3-3 and push open the door when Mutou calls from the other side."
vn "Hành lang yên tĩnh như sân trường, đương nhiên rồi vì mọi người đều đang ở trong lớp. Tôi gõ nhẹ cửa phòng 3-3 và đẩy cửa bước vào khi Mutou gọi từ phía bên kia."

scene bg school_scienceroom
with locationchange

hi "Sorry I'm late."
vn hi "Em xin lỗi vì đã đến muộn."

"Fifteen pairs of eyes turn to me."
vn "Mười lăm cặp mắt đổ dồn về phía tôi."

show muto irritated at center
with charaenter

mu "Good morning, Nakai."
vn mu "Chào buổi sáng, Nakai."

"Mutou seems to be somewhat confounded by my coming in late, as if I interrupted his flow or something."
vn "Mutou dường như hơi bối rối khi thấy tôi đến muộn, như thể tôi đã làm gián đoạn mạch giảng của ông ấy hay gì đó."

"Judging from the rambling lectures his classes tend to be, that might be the case."
vn "Đánh giá từ những bài giảng lan man thường thấy trong các tiết học của ông ấy, có lẽ đúng là vậy."

"I pass him the note the nurse gave me. Mutou takes it with a nod and reads it quickly."
vn "Tôi đưa cho ông ấy tờ giấy phép mà y tá đã đưa cho tôi. Mutou nhận lấy với một cái gật đầu và đọc nhanh nó."

show muto normal
with charachange

"He lifts his eyebrows and gives me a kind of a stern look but doesn't say anything, just nods solemnly again."
vn "Ông ấy nhướn mày và nhìn tôi với vẻ nghiêm nghị nhưng không nói gì, chỉ lại trang trọng gật đầu."

"I shrug and he gestures at me to run along so I naturally do."
vn "Tôi nhún vai và ông ấy ra hiệu cho tôi đi nhanh vào chỗ nên tôi tự nhiên làm theo."


label en_A27a:

scene bg school_scienceroom
show muto normal at center
with None

#so if you have joined SC, you see this
hide muto
with charaexit

"Only two pairs of eyes remain keenly following me as I walk to my seat."
vn "Chỉ còn hai cặp mắt chăm chú dõi theo tôi khi tôi đi về chỗ ngồi."

"I'm not surprised in the least when I feel Misha's fingernail prickle through my shirt about fifteen seconds after seating myself."
vn "Tôi không hề ngạc nhiên chút nào khi cảm thấy móng tay của Misha chọc qua áo tôi khoảng mười lăm giây sau khi tôi ngồi xuống."

show misha perky_smile_close at offscreenleft
with None

show bg school_scienceroom at bgright
show misha perky_smile_close  at Transform(xalign=-0.3)
with charamove

play music music_another fadein 2.0

mi "Psst! Where were you?"
vn mi "Psst! Cậu đã ở đâu vậy?"

hi "None of your business."
vn hi "Không phải việc của cậu."

"I know this is probably the worst answer I can give as it only serves to pique their curiosity, but I have no energy to come up with elaborate cover stories right now."
vn "Tôi biết đây có lẽ là câu trả lời tệ nhất mà tôi có thể đưa ra vì nó chỉ càng khơi dậy sự tò mò của họ, nhưng tôi không còn năng lượng để nghĩ ra những câu chuyện bao biện phức tạp lúc này nữa."

show misha perky_confused_close
with charachange

show bg school_scienceroom at center
show misha perky_confused_close at offscreenleft
with charamove

"However, Misha backs off. She's unexpectedly fast to give up today."
vn "Tuy nhiên, Misha lại lùi bước. Hôm nay cô ấy bỏ cuộc nhanh đến bất ngờ."

"…"
vn "…"

"In a minute, she's back at poking me with her finger."
vn "Một lát sau, cô ấy lại tiếp tục chọc ngón tay vào lưng tôi."

show misha hips_grin_close
with None

show bg school_scienceroom at bgright
show misha hips_grin_close  at Transform(xalign=-0.3)
with charamove

mi "Come on, tell us! Shicchan is very interested too!"
vn mi "Thôi mà, kể cho bọn tớ nghe đi! Shicchan cũng rất muốn biết đó!"

"It was just my wishful thinking. She just talked about it with Shizune, probably devising ways to get me to spill the beans."
vn "Đó chỉ là mong muốn nhất thời của tôi thôi. Cô ấy vừa mới nói chuyện với Shizune, có lẽ là đang nghĩ ra cách để khiến tôi phải khai thật."

hi "No."
vn hi "Không."

show misha perky_sad_close
with charachange

show bg school_scienceroom at center
show misha perky_sad_close at offscreenleft
with charamove

"She retreats to negotiate again."
vn "Cô ấy lại rút lui để thương lượng lần nữa."

show misha sign_smile_close
with None

show bg school_scienceroom at bgright
show misha sign_smile_close  at Transform(xalign=-0.3)
with charamove

label en_choiceA27:
menu:
    with menueffect

    mi "As a member of the Student Council, it's your duty to tell us why you are skipping class! Especially if it's something fun fun fun~!"
vn mi "Với tư cách là một thành viên của Hội học sinh, cậu có nghĩa vụ phải nói cho bọn tớ biết tại sao cậu lại trốn học! Đặc biệt là nếu đó là chuyện gì đó vui vui vui~!"

    "Yeah, I sure was having fun fun fun at the nurse's office…":
vn "Ừ, tớ chắc chắn là đã có khoảng thời gian vui vui vui ở phòng y tế rồi…":
    #to A27b
        return m1

    "I don't want to talk about it, okay?":
vn "Tớ không muốn nói về chuyện đó, được không?":
    #to A27c
        return m2

label en_A27b:

stop music fadeout 4.0

"God damn it. She just doesn't know when to stop."
vn "Khỉ thật. Cô ấy đúng là không biết khi nào nên dừng lại."

hi "Yeah fine. Whatever. I'll tell you. I was having a great time."
vn hi "Ừ thôi được rồi. Sao cũng được. Tớ sẽ kể cho cậu nghe. Tớ đã có một khoảng thời gian tuyệt vời."

hi "I had a heart attack first thing in the morning and then hung out with the head nurse for a few hours for kicks."
vn hi "Tớ bị đau tim ngay sáng sớm và sau đó đã đi chơi với y tá trưởng vài tiếng cho vui."

hi "Best morning of my life, I gotta tell you."
vn hi "Sáng nay là buổi sáng tuyệt vời nhất trong cuộc đời tớ, tớ phải nói với cậu như vậy."

"I'm trying to imitate her ridiculous lilting speech while keeping my voice so low that nobody else hears me. The words come spitting out of my mouth."
vn "Tôi cố gắng bắt chước cái giọng điệu lên xuống ngớ ngẩn của cô ấy trong khi vẫn giữ giọng đủ nhỏ để không ai khác nghe thấy. Những lời nói tuôn ra khỏi miệng tôi."

show misha perky_confused_close
with charachange

mi "Hicchan, you had a what? Seriously?"
vn mi "Hicchan, cậu bị cái gì cơ? Nghiêm túc đấy à?"

hi "Just drop it. You heard me."
vn hi "Thôi bỏ đi. Cậu nghe tớ nói rồi đấy."

show misha perky_sad_close
with charachange

mi "But Hicchan, this is important!"
vn mi "Nhưng Hicchan, chuyện này quan trọng mà!"

hi "No, really. Leave me alone. We're in the middle of the class, too."
vn hi "Không, thật đấy. Để tớ yên đi. Bọn mình đang trong giờ học đấy."

show misha sign_sad_close
with charachange

mi "But Hicchan!"
vn mi "Nhưng Hicchan!"

"Misha sounds concerned, or maybe panicky. I wonder if she realizes herself that it wasn't the best of ideas to be so damn intrusive."
vn "Giọng Misha nghe có vẻ lo lắng, hoặc có lẽ là hoảng sợ. Tôi tự hỏi liệu cô ấy có tự nhận ra rằng việc quá tò mò đó không phải là một ý hay hay không."

"…"
vn "…"

"I let her simmer in her own juices for a while before replying. It won't translate to Shizune but I don't care."
vn "Tôi để cô ấy tự nghiền ngẫm một lúc trước khi trả lời. Chuyện đó sẽ không dịch được cho Shizune nhưng tôi không quan tâm."

hi "Piss off, Misha."
vn hi "Biến đi, Misha."

hi "And tell Shizune to do so too."
vn hi "Và bảo Shizune cũng biến luôn đi."

"As the words leave my mouth, I immediately regret saying them, but it's not like I can take them back any more."
vn "Khi những lời đó vừa rời khỏi miệng tôi, tôi lập tức hối hận vì đã nói ra, nhưng cũng chẳng thể rút lại được nữa rồi."

show misha perky_sad_close
with charachange

show bg school_scienceroom at center
show misha perky_sad_close at offscreenleft
with charamove

hide misha
with None

"To my partial surprise, Misha actually shuts up though I don't bother checking if she passes the message to Shizune. Doesn't matter either way."
vn "Có phần ngạc nhiên là Misha thực sự im lặng mặc dù tôi không buồn kiểm tra xem liệu cô ấy có chuyển lời nhắn đó cho Shizune hay không. Dù sao thì cũng chẳng quan trọng."

"Mutou ends his class in some generic talk about the festival two days from now."
vn "Mutou kết thúc tiết học bằng một vài lời nói chung chung về lễ hội sẽ diễn ra sau hai ngày nữa."

#to A29, needs a conditional about Emi making Hisao feel better



label en_A27c:

hi "Give up. I'm not going to tell."
vn hi "Từ bỏ đi. Tớ sẽ không kể đâu."

show misha hips_grin_close
with charachange

mi "Is that so~?"
vn mi "Vậy à~?"

hi "Yeah."
vn hi "Ừ."

show misha perky_confused_close
with charachange

"She thinks about this for a moment."
vn "Cô ấy suy nghĩ về điều này trong giây lát."

show misha hips_frown_close
with charachange

mi "That's stingy, Hicchan~!"
vn mi "Cậu keo kiệt thật đó, Hicchan~!"

"I can hear the pout in her voice, disappointed and downcast."
vn "Tôi có thể nghe thấy sự hờn dỗi trong giọng nói của cô ấy, thất vọng và chán nản."

show bg school_scienceroom at center
show misha hips_frown_close at offscreenleft
with charamove

"She retreats again for a moment to negotiate with the brainy half of the dynamic duo, before returning."
vn "Cô ấy lại rút lui một lát để thương lượng với nửa kia thông minh của bộ đôi năng động, trước khi quay trở lại."

show misha hips_smile_close
with None

show bg school_scienceroom at bgright
show misha hips_smile_close  at Transform(xalign=-0.3)
with charamove

mi "I think we should have lunch together and discuss more about this… Shicchan says."
vn mi "Tớ nghĩ bọn mình nên ăn trưa cùng nhau và thảo luận thêm về chuyện này… Shicchan nói vậy."

show misha hips_grin_close
with charachange

mi "It's our treat."
vn mi "Bọn tớ sẽ đãi cậu."

show misha sign_smile_close
with charachange

mi "Besides, you need to make up for not being there in the morning and we need help with the work~!"
vn mi "Ngoài ra, cậu cần phải bù đắp vì đã không có mặt ở đây vào buổi sáng và bọn tớ cần cậu giúp làm việc nữa~!"

"The other students around us are starting to give us looks, probably because Misha is leaning so much over her desk that she's almost bumping heads with me. Her curly hair brushes my neck."
vn "Những học sinh khác xung quanh bọn tôi bắt đầu nhìn bọn tôi, có lẽ là vì Misha đang nghiêng người quá nhiều qua bàn đến mức gần như va đầu vào tôi. Mái tóc xoăn của cô ấy chạm vào cổ tôi."

"It smells like shampoo and very much like whatever she puts in there to make it go like that."
vn "Nó có mùi dầu gội và rất giống với thứ gì đó mà cô ấy dùng để khiến nó xoăn như vậy."

"I think the girl in front of me is trying to eavesdrop. Hope nobody is getting the wrong idea about this, though I'm not really sure how it would be possible to get any other kind of idea."
vn "Tôi nghĩ cô gái ngồi trước mặt tôi đang cố gắng nghe lỏm. Hy vọng là không ai hiểu sai về chuyện này, mặc dù tôi không thực sự chắc chắn làm thế nào mà người ta có thể có bất kỳ ý nghĩ nào khác được nữa."

"Luckily Mutou stays oblivious, or deliberately ignores Misha. So far."
vn "May mắn là Mutou vẫn không hay biết gì, hoặc cố tình phớt lờ Misha. Cho đến giờ là vậy."

"I can't really win this one, can I?"
vn "Tôi thực sự không thể thắng vụ này được, phải không?"



label en_choice2A27:
menu:
    with menueffect

    "I promised to eat with Emi too, but I can't be in two places at the same time."
vn "Tôi đã hứa ăn trưa với Emi rồi, nhưng tôi không thể ở hai nơi cùng một lúc được."

    "I'll go to the lunch with Emi and her friend.":
vn "Tôi sẽ đi ăn trưa với Emi và bạn của cô ấy.":
        return m1

    "I'll go with Shizune, after all I'm in the Student Council now.":
vn "Tôi sẽ đi với Shizune, dù sao thì giờ tôi cũng là thành viên Hội học sinh rồi.":
        return m2


label en_A27h:
#lol label order

hi "Sorry, I can't. I promised to have lunch with someone else already."
vn hi "Xin lỗi, tớ không đi được. Tớ đã hứa ăn trưa với người khác rồi."

show misha perky_confused_close
with charachange

mi "Eeeh? Who? Is it a girl~?"
vn mi "Eeeh? Ai cơ? Có phải là con gái không~?"

hi "Yeah…"
vn hi "Ừ…"

show misha hips_grin_close
with charachange

"Her giggle compels me to quickly follow with something so she doesn't get the wrong idea."
vn "Tiếng cười khúc khích của cô ấy thúc đẩy tôi nhanh chóng nói thêm điều gì đó để cô ấy không hiểu lầm."

hi "It's nothing like that! It's… a bit complicated."
vn hi "Không phải kiểu đó đâu! Chuyện này… hơi phức tạp."

show misha perky_smile_close
with charachange

"Complicated… yeah, that's what my life is, despite already setting into a daily routine of school life."
vn "Phức tạp… ừ, cuộc sống của tôi là như vậy đó, mặc dù đã đi vào nề nếp sinh hoạt hàng ngày ở trường rồi."

"All things must be put into a new kind of perspective in this second life, reconsidered from the point of view of this new me."
vn "Mọi thứ đều phải được đặt vào một góc nhìn mới trong cuộc sống thứ hai này, xem xét lại từ quan điểm của con người mới này của tôi."

"The me with a broken heart."
vn "Con người tôi với trái tim tan vỡ."

hi "Also, I don't know if I can come to the council after all."
vn hi "À mà, tớ không biết liệu tớ có thể đến hội đồng học sinh được hay không nữa."

hi "Or at least for now. I have something else I need to focus on first."
vn hi "Hoặc ít nhất là bây giờ thì không. Tớ có việc khác cần tập trung vào trước đã."

"That's right. I have to rethink my priorities. This is something that has swirled around in my head since the nurse gave me that speech. I really can't afford to pretend I don't have this condition."
vn "Đúng vậy. Tôi phải suy nghĩ lại về những ưu tiên của mình. Đây là điều mà tôi đã nghĩ quẩn quanh trong đầu kể từ khi y tá có bài nói chuyện đó với tôi. Tôi thực sự không thể tiếp tục giả vờ như mình không có bệnh này được nữa."

"I'm surprised that I can think so analytically, but I'll go with the flow for now."
vn "Tôi ngạc nhiên là mình có thể suy nghĩ phân tích đến vậy, nhưng thôi thì cứ thuận theo dòng chảy đã."

hi "I promise I'll explain properly later, but not now, okay? Please tell Shizune I'm sorry for letting her down."
vn hi "Tớ hứa sẽ giải thích rõ ràng sau, nhưng không phải bây giờ, được không? Làm ơn nói với Shizune rằng tớ xin lỗi vì đã làm cô ấy thất vọng nhé."

show misha perky_confused_close
with charachange

mi "If you say so, Hicchan."
vn mi "Nếu cậu nói vậy thì thôi vậy, Hicchan."

"She sounds surprised, and serious, which I don't think I've ever heard Misha to be before."
vn "Giọng cô ấy nghe có vẻ ngạc nhiên, và nghiêm túc, điều mà tôi không nghĩ là mình từng nghe thấy ở Misha trước đây."

show bg school_scienceroom at center
show misha perky_confused_close at offscreenleft
with charamove

hide misha
with None

stop music fadeout 3.0

"Misha luckily understands that I'm serious, a stroke of luck that I could tell what I mean so clearly even she got it. She retreats to translate our discussion to Shizune."
vn "May mắn thay, Misha hiểu rằng tôi đang nghiêm túc, một điều may mắn là tôi có thể diễn đạt ý mình rõ ràng đến mức ngay cả cô ấy cũng hiểu được. Cô ấy lùi lại để dịch cuộc thảo luận của bọn tôi cho Shizune."

"Neither of them talk to me after that."
vn "Sau đó, cả hai người họ đều không nói chuyện với tôi nữa."



label en_A27i:

hi "Fine, I'll come with you, but get off my back for the rest of the class, okay?"
vn hi "Được rồi, tớ sẽ đi cùng hai cậu, nhưng để tớ yên cho đến hết giờ học, được chứ?"

show misha hips_grin_close
with charachange

mi "It's a deal, Hicchan~!"
vn mi "Thỏa thuận nhé, Hicchan~!"

stop music fadeout 2.0

show bg school_scienceroom at center
show misha hips_grin_close at offscreenleft
with charamove

scene bg school_scienceroom
with shorttimeskip

play sound sfx_normalbell

with Pause(7.0)

play ambient sfx_crowd_indoors fadein 0.3

scene bg school_hallway3
show crowd
with locationchange

"On the way to the student council room, I can see students walking back and forth through the halls, probably in preparation of their own projects."
vn "Trên đường đến phòng hội học sinh, tôi có thể thấy các học sinh đi đi lại lại trong hành lang, có lẽ là để chuẩn bị cho các dự án của riêng họ."

"The festival is practically here. That means there are only two possible reasons that my help is required."
vn "Lễ hội sắp đến rồi. Điều đó có nghĩa là chỉ có hai lý do có thể khiến họ cần sự giúp đỡ của tôi."

"Either there is only a small amount of work left, and they just want a helping hand to wrap up the mundane final checks they are obligated to do."
vn "Hoặc là chỉ còn một chút việc vặt, và họ chỉ muốn có thêm một bàn tay giúp họ hoàn thành những công đoạn kiểm tra cuối cùng nhàm chán mà họ buộc phải làm."

"Or there is a ton of work left, and Shizune is putting on a calm face as a torrent of built-up procrastinated work threatens to kill us all."
vn "Hoặc là còn rất nhiều việc phải làm, và Shizune đang cố tỏ ra bình tĩnh trong khi một loạt công việc bị trì hoãn dồn lại đang đe dọa sẽ giết chết tất cả bọn tôi."

stop ambient fadeout 1.0


label en_A27d:

#if you are not SC member and did not get a heartattack OR if you blew Shizune and Misha off in A26, you come straight to this, the day begins with it in some cases.

scene bg school_scienceroom
with locationskip

"For a change, I'm not among the first ones to come to morning class."
vn "Thay đổi một chút, hôm nay tôi không phải là một trong những người đầu tiên đến lớp buổi sáng."

"Instead, almost everyone else seems to be here already. I recognize most of my class by their faces by now, though the names escape me still."
vn "Thay vào đó, hầu như tất cả mọi người khác dường như đã ở đây rồi. Đến giờ tôi đã nhận ra hầu hết các bạn trong lớp qua khuôn mặt, mặc dù vẫn chưa nhớ được tên."



label en_A27e:

#If you have not joined SC, you see this instead of A27a, this is also a followup on A27e

scene bg school_scienceroom
with shorttimeskip

play music music_normal fadein 3.0

"The class goes on lazily. I think I'm starting to get into the rhythm of the school."
vn "Tiết học trôi qua một cách uể oải. Tôi nghĩ là mình đang bắt đầu làm quen với nhịp điệu của trường học."

"I have even stopped worrying about taking notes and being overtly attentive. The first days, I was pretty high-strung in class."
vn "Tôi thậm chí đã ngừng lo lắng về việc ghi chép và tỏ ra quá chăm chú. Những ngày đầu, tôi đã khá căng thẳng trong lớp."

"Mutou finishes his lecture about electricity early, but continues without a pause about the festival."
vn "Mutou kết thúc bài giảng về điện sớm hơn dự kiến, nhưng tiếp tục không ngắt quãng về lễ hội."

show muto normal at center
with charaenter

mu "So, as you know, the festival is on the day after tomorrow. I hope everyone's projects are going to be successful this year."
vn mu "Vậy, như các em đã biết, lễ hội sẽ diễn ra vào ngày kia. Tôi hy vọng các dự án của mọi người sẽ thành công trong năm nay."

show muto smile
with charachange

mu "Have a good time, but also come Sunday, please keep the meaning of this festival in your minds…"
vn mu "Hãy vui vẻ, nhưng cũng hãy nhớ đến ý nghĩa của lễ hội này vào Chủ Nhật nhé…"

mi "Games and fried food!"
vn mi "Trò chơi và đồ chiên rán!"

"Everyone bursts out in laughter, and so do I."
vn "Mọi người phá lên cười, và tôi cũng vậy."

show muto irritated
with charachange

mu "Yes, thank you Mikado."
vn mu "Vâng, cảm ơn Mikado."

show muto normal
with charachange

mu "But what I meant was more the—{w=.5}{nw}"
vn mu "Nhưng ý tôi muốn nói là về—{w=.5}{nw}"

play sound sfx_normalbell

"The remainder of his sentence is buried beneath the ring of the lunch bells, and everyone starts packing their things."
vn "Phần còn lại trong câu nói của ông ấy bị chìm xuống dưới tiếng chuông báo giờ ăn trưa, và mọi người bắt đầu thu dọn đồ đạc."

"Mutou deliberates for a moment, but since almost nobody seems to pay attention any more, he gives up and sits down."
vn "Mutou do dự một lúc, nhưng vì hầu như không ai còn chú ý nữa, ông ấy bỏ cuộc và ngồi xuống."

stop music fadeout 2.0

scene bg school_hallway3
show crowd
with locationchange

play ambient sfx_crowd_indoors fadein 0.3

"It's crowded in the hallway… or as crowded as hallways in this school probably get. Most of the students seem to be heading down for the cafeteria."
vn "Hành lang đông đúc… hoặc đông đúc như hành lang ở trường này có thể trở nên như vậy. Hầu hết các học sinh dường như đang đi xuống столовая."


#to A29



label en_A27f:

scene bg school_scienceroom
with shorttimeskip

stop music fadeout 2.0

"Misha, and by proxy, Shizune, doesn't bother me for the entire morning."
vn "Misha, và gián tiếp là Shizune, không làm phiền tôi suốt cả buổi sáng."

play sound sfx_normalbell

"When the bell rings, I don't even look at the two of them as I walk out of the class."
vn "Khi chuông reo, tôi thậm chí còn không nhìn hai người họ khi bước ra khỏi lớp."

scene bg school_hallway3
show crowd
with locationchange

play ambient sfx_crowd_indoors fadein 0.3

"It's crowded in the hallway… or as crowded as hallways in this school probably get. Most of the students seem to be heading down for the cafeteria."
vn "Hành lang đông đúc… hoặc đông đúc như hành lang ở trường này có thể trở nên như vậy. Hầu hết các học sinh dường như đang đi xuống столовая."



#***************

label en_A28:

scene bg school_council
with locationchange

show misha perky_smile at twoleft
show shizu behind_smile at tworight
with charaenter

"Once inside the office, I look around and see that it's deserted."
vn "Khi vào trong văn phòng, tôi nhìn quanh và thấy nó vắng tanh."

hi "I guess this means there isn't a lot of work left, huh? Since there's no one here, and all."
vn hi "Tớ đoán là điều này có nghĩa là không còn nhiều việc phải làm nữa, hả? Vì không có ai ở đây cả, và mọi thứ."

show misha sign_smile
with charachange

mi "It's always like this, Hicchan~!"
vn mi "Lúc nào cũng thế này mà, Hicchan~!"

"This confirms what I have thought before but have never actually been able to confirm definitively: Shizune and Misha are the Student Council. The whole Student Council."
vn "Điều này xác nhận những gì tôi đã nghĩ trước đây nhưng chưa bao giờ thực sự có thể xác nhận chắc chắn: Shizune và Misha là Hội học sinh. Toàn bộ Hội học sinh."

hi "Damn. So it's true. The Student Council is really only you two."
vn hi "Chết tiệt. Vậy là thật à. Hội học sinh thực sự chỉ có hai cậu thôi sao."

play music music_ease fadein 4.0

show misha hips_grin
show shizu cross_wut
with charachange

"Shizune looks as if she's stuck wondering whether to be ashamed or explode with anger, and Misha is equally divided between laughing and trying to stop her."
vn "Shizune trông như thể cô ấy đang mắc kẹt giữa việc tự xấu hổ hay bùng nổ cơn giận, và Misha cũng chia rẽ giữa việc cười phá lên và cố gắng ngăn cô ấy lại."

show shizu behind_frustrated
with charachange

shi "…"

show misha sign_smile
with charachange

mi "Well, then, Hicchan, you'll be happy to know that since it's just us three, we have a lot to do! A lot~! A lot~ lot~ lot~…"
vn mi "Chà, vậy thì, Hicchan, cậu sẽ rất vui khi biết rằng vì chỉ có ba bọn mình thôi, nên bọn mình có rất nhiều việc phải làm đó! Rất nhiều~! Rất rất rất rất nhiều~…"

hi "That does not make me happy."
vn hi "Chuyện đó không làm tớ vui chút nào."

show shizu adjust_happy
with charachange

"But it seems to make Shizune very happy."
vn "Nhưng có vẻ như nó lại khiến Shizune rất vui."

show misha cross_laugh
with charachange

mi "Wahaha~!"
vn mi "Wahaha~!"

show misha hips_grin
with charachange

mi "Just kidding!"
vn mi "Đùa thôi!"

label en_A28a:
#you see this if you have been spending the morning in the infirmary

scene bg school_council
with shorttimeskip

"The work turns out to be sorting and double-checking the considerable amount of paperwork necessary for an event such as the school festival to get done."
vn "Công việc hóa ra là sắp xếp và kiểm tra kỹ lưỡng một lượng lớn giấy tờ cần thiết cho một sự kiện như lễ hội trường học được hoàn thành."

"Bureaucracy is a mindboggling thing."
vn "Quan liêu đúng là một thứ khó hiểu."

play sound sfx_normalbell

"But we manage to finish it just when the lunch bells ring."
vn "Nhưng bọn tôi đã xoay sở để hoàn thành nó vừa kịp lúc chuông báo giờ ăn trưa reo."

show misha hips_grin at twoleft
show shizu adjust_happy at tworight
with charaenter

mi "Okay~, now that we are done, we can relax a little! But not too much, we have lots more to do in the afternoon~!"
vn mi "Được rồi~, giờ thì bọn mình xong việc rồi, bọn mình có thể thư giãn một chút! Nhưng không được thư giãn quá nhiều đâu nha, bọn mình còn rất nhiều việc phải làm vào buổi chiều nữa đó~!"

label en_A28b:

$ renpy.music.play(music_ease, fadein=4.0, if_changed=True)

show shizu behind_smile
with charachange

shi "…"

show misha sign_smile
with charachange

mi "It's actually not that much work, Hicchan~. So~, we can afford to enjoy a little lunch first."
vn mi "Thực ra không có nhiều việc đến thế đâu, Hicchan~. Vậy nên~, bọn mình có thể dành thời gian để thưởng thức bữa trưa trước đã."

show misha cross_laugh
with charachange

mi "Hahaha~!"
vn mi "Hahaha~!"

"The two of them produce a small array of plastic containers seemingly out of thin air."
vn "Cả hai người họ lôi ra một loạt hộp nhựa nhỏ như thể từ trong không khí loãng."

show misha hips_grin
with charachange

mi "Hm~ hm~… It's chicken cutlet with tomatoes and soybean sprouts~! Doesn't it sound delicious, Hicchan?"
vn mi "Hm~ hm~… Là котлета gà với cà chua và giá đỗ~! Nghe có ngon không Hicchan?"

mi "It was just made this morning, and it's still warm, so eat eat eat~!"
vn mi "Món này vừa mới được làm sáng nay thôi, và nó vẫn còn ấm, nên ăn ăn ăn thôi nào~!"

"I take one of the containers and open it. It looks nice, and certainly smells good. The fact that I'm really hungry adds to that even more."
vn "Tôi cầm lấy một trong những chiếc hộp và mở nó ra. Trông đẹp mắt đấy chứ, và chắc chắn là thơm ngon nữa. Việc tôi thực sự đói bụng càng làm tăng thêm điều đó."

hi "Wow, this looks great. Where did you get this?"
vn hi "Wow, trông tuyệt vời thật. Hai cậu lấy cái này ở đâu ra vậy?"

show shizu basic_normal
with charachange

shi "…"

show misha hips_smile
with charachange

mi "That isn't important, Hicchan!"
vn mi "Chuyện đó không quan trọng, Hicchan!"

show misha sign_smile
with charachange

mi "There was supposed to be a stall selling lunchboxes, but the girl who was to run it suddenly said she couldn't do it. Shicchan said, “What a waste, it was a lot of work to trick Hicchan into making this~”—"
vn mi "Lẽ ra sẽ có một gian hàng bán hộp cơm trưa, nhưng cô gái định điều hành nó đột nhiên nói là cô ấy không thể làm được nữa. Shicchan đã nói, “Thật là lãng phí, tốn bao công lừa Hicchan làm món này~”—"

hi "Hey, what the hell…"
vn hi "Này, cái quái gì vậy…"

show misha hips_grin
with charachange

mi "…So~! Shicchan wanted to see if she could do it, but then decided not to, right, Shicchan~?"
vn mi "…Vậy nên~! Shicchan đã muốn xem liệu cô ấy có thể làm được không, nhưng rồi lại quyết định không làm, đúng không, Shicchan~?"

show shizu basic_angry
with charachange

"Shizune sulks angrily, shooting Misha a displeased look. I don't think I was supposed to hear that story."
vn "Shizune hờn dỗi giận dữ, liếc nhìn Misha một cái không hài lòng. Tôi không nghĩ là mình được phép nghe câu chuyện đó."

hi "This is your test food?"
vn hi "Đây là đồ ăn thử nghiệm của hai cậu à?"

show shizu behind_frown
with charachange

shi "…"

show misha sign_smile
with charachange

mi "I'm eating it too, Hicchan~!"
vn mi "Tớ cũng ăn mà, Hicchan~!"

show misha hips_grin
with charachange

mi "And Shicchan is, too~!"
vn mi "Và Shicchan cũng vậy~!"

"That doesn't answer the question!"
vn "Như thế không trả lời được câu hỏi của tớ!"

"Nevertheless, I split a pair of chopsticks Shizune offers me, pick up a piece of cutlet, and pop it into my mouth."
vn "Tuy nhiên, tôi vẫn tách đôi đũa mà Shizune đưa cho, gắp một miếng котлета và bỏ vào miệng."

hi "It's surprisingly good. I didn't expect Shizune to be such a good cook."
vn hi "Ngon hơn tôi tưởng đấy. Tớ không ngờ Shizune lại nấu ăn ngon đến vậy."

show shizu basic_frown
with charachange

"Shizune puts her chopsticks down to sign curtly towards Misha, who gulps down her cutlet with noticeable difficulty in order to speak for her."

show misha sign_smile
with charachange

mi "Hicchan~! Don't talk with food in your mouth~!"

hi "It's not like I enjoy doing it. Anyway, how motherly to show that kind of concern…"

show shizu behind_frown
with charachange

shi "…"

show misha hips_frown
with charachange

mi "You can't even eat right, Hicchan~! That's all it is~!"

show misha perky_sad
with charachange

"It's a stalemate. I can't eat in order to talk to Shizune, who can't eat in order to chastise me for eating the wrong way. Misha, caught in between, is in the same situation, and looks the most disheartened by how this is going."

show shizu behind_blank
show misha perky_smile
with charachange

"Either way, our food is getting colder by the second, and it wasn't piping hot to start with. Wherever this was going, it dies down pretty fast once we all realize that, and we eat."

play sound sfx_warningbell

"After a while the bell rings, but Misha makes no attempt to tell Shizune, so I'm sure they're planning to skip classes and spend the rest of the day in here again."

show shizu adjust_smug
with charachange

shi "…"

show misha sign_smile
with charachange

mi "Hicchan, do you have any plans for the festival?"

hi "No, not really. After all, I've only been here a week, what could I set up in that time?"

show misha cross_laugh
with charachange

mi "Wahaha~! Hicchan, you helped us out so much, don't sell yourself short!"

hi "Okay."

show shizu basic_angry
with charachange

shi "…"

show misha hips_frown
with charachange

mi "We're serious~!"

hi "Okay!"

"The two of them seem to get indignant over the strangest things."

show shizu adjust_happy
with charachange

shi "…"

show misha hips_smile
with charachange

mi "You're going though, right, Hicchan? You should at least see what we've ac—complished…? Everyone should be able to look at what they have done so they can fully understand their work, that's my belief~! You're no exception!"

show misha perky_smile
with charachange

mi "Hicchan, you should definitely go~! If you don't have anything planned, then maybe we can even go together~!"

show shizu adjust_blush
with charachange

hi "Do you need a hand? If there's anything you need help with, I'm fine with sticking around."

"I feel much more at ease than I did earlier; my previous concerns and fears long gone. I'd forgotten about this morning's trouble entirely until now, having fun with Shizune like this."

"Having fun with Shizune… It seems like an unfamiliar concept to think of, but, looking back on it, I've really enjoyed the moments I've spent with Shizune and Misha these past few days, in spite of everything else."

"If we might be going together, then maybe I can afford to stick around a little longer. And I guess it beats class."

show shizu behind_blank
with charachange

shi "…"

show misha hips_smile
with charachange

mi "Really, Hicchan? Okay~! We can consider this you repaying us for the free lunch~!"

show misha cross_laugh
with charachange

mi "Great, this is great, really~ really~ great~! Shicchan was hoping to bring this up again later anyway! Ahahaha~! Wahahahahaha~!"

"That's not a free lunch at all. Normally I would be angry, or at least slightly unsettled, but my mood has improved from earlier on, so I'll let it slide."

"Helping them out turns out to consist mostly of stamping forms and making what seems like ten thousand copies apiece of fifty different budget reports."

"It's not hard, but very boring, and according to Misha, the simplest of the tasks they deal with."

"I feel myself getting more and more tired, and with that, less eager to return to class. This is especially bad because the more time I spend out of class, the harder it seems to just get up and go back."

"These two, they're a terrible influence. Terrible role models. Not that it bothers me all that much, and I'm sure no one looks up to them, but it's the principle of the thing…"

show shizu adjust_happy
with charachange

shi "…"

show misha hips_grin
with charachange

mi "Done~!"

hi "Ah, that was fast. I'll be finished before this period's over, I think."

show misha sign_smile
with charachange

mi "No, no, Hicchan, everything is done. So, you're done, too~!"

hi "That doesn't make any sense, are you telling me this is all arbitrary and you've been keeping me here for the hell of it?"

show misha hips_grin
with charachange

mi "No~…"

show shizu basic_normal
with charachange

shi "…"

show misha perky_smile
with charachange

mi "But we have kept you long enough~! You should go back to class, Hicchan~! You can still make it for most of this period!"

hi "What about you?"

show shizu behind_blank
with charachange

shi "…"

show misha hips_smile
with charachange

mi "Of course we're coming too, of course; we'll be right behind you!"

stop music fadeout 6.0

scene bg school_hallway3
with locationchange

"Reassured, I start heading back to class, but the period is almost halfway over, so I start thinking it would be pointless halfway there and pass the difference between this class and the next drinking juice in the hallway."

"I keep an eye on the door to the student council room, but it doesn't open. What's taking them so long? Are they busy wrapping up my share of the work? Well, it shouldn't take so long, unless there's more, and they just wanted me to leave."

"The more I think about it, the likelier it seems."

"Shizune is… well, not an idiot, but clearly, she's unable to just come out with things."

"Maybe it's because she can't talk, so it's harder for her. She has Misha, but all in all, as easy as they make it look, there's still a difference between casual speech and sign language."

play sound sfx_normalbell

"I contemplate going back there to check on them, but the bell rings, and I have to go to class."

scene bg school_scienceroom
with locationchange

"They join me a few minutes later, and the thoughts I had in my mind before slip away in the routine of school life."

with shorttimeskip

"By the time I remember, school is over for the day and I'm too tired to do anything but go home, do my homework, and then go to sleep."

$ suppress_window_after_timeskip = True

scene black
with Dissolve(3.0)


#***************

label en_A29:

scene bg school_hallway3
show crowd
with None

play ambient sfx_crowd_indoors fadein 0.3
play music music_emi fadein 0.3

show emi basic_happy at center
with charaenter

emi "Hisao!"

show emi excited_proud
with charachange

emi "I'm going to make you a one-time-only, super extra special lunch offer!"

show emi excited_laugh
with charachange

emi "Emi's home made lunch boxes, and the privilege of enjoying them in private with two bombshell beauties!"

"Her overly flirtatious sales pitch echoes in the hallway, a remarkable feat since it's full of people."

show emi basic_closedgrin
with charachange

"Emi strikes a very confident-looking pose as though as an attempt to one-up her own ridiculousness, puffing her very modest chest and making the V for victory sign with her hand."

hi "Sounds delicious. To what do I owe this honor of being invited?"

show emi excited_proud
with charachange

emi "You stood there looking really lost and sad so I thought you could use some company."

"That is probably the most depressing reason imaginable."

show emi basic_closedgrin
with charachange

emi "So how about it? You're probably really lonely and would eat that awful cafeteria food all alone, otherwise."

hi "Eeeh…"

show emi excited_proud
with charachange

emi "I'm kidding, I'm kidding!"

hi "Sure, I'll have your lunch offer. With pleasure."

show emi basic_happy
with charachange

emi "Let's go to the roof!"

hi "The roof?"

hi "Why the roof?"

show emi basic_closedgrin
with charachange

emi "Because that's where we eat lunch!"

emi "And if I don't get up there, then she'll probably wander off and then I just know she'll go hungry because she never packs a lunch for herself!"

hi "Who will?"

show emi basic_closedhappy
with charachange

emi "Come with me!"

"Without answering my question or waiting for a response, she grabs me by the arm and drags me through the hallways."

"I attempt to make conversation on the way."

hi "Why do you have an extra lunch?"

show emi sad_grin
with charachange

"Emi smiles guiltily."

emi "Actually, it's yesterday's lunch."

emi "I slipped in a run at lunch and forgot to eat it."

"Huh."

# The line above will go wherever the scene changes from out of the hallway, I guess.


label en_A29x:

"Her expression is so funny that I almost laugh out loud."

"Emi giggles, to herself or to something or other, or maybe for no reason at all. I like the sound of it."

"Emi's sunny, energetic disposition alleviates the constricting feeling in the back of my head from the fight with Shizune and Misha."

"I let that issue slide out of my mind, and smile for the first time today."



label en_A29a:

#and this is what happens if you had a heart flutter:
scene bg school_hallway3
show crowd
with None

play ambient sfx_crowd_indoors fadein 0.3

"Normally, I'd join the flow and grab a lunch myself, but today is different."

"Today, I've been invited to lunch on the roof."

"An odd location, but that's where I was told to go."

"Fortunately, I manage to find shelter from the storm in the lee of the classroom door."

stop ambient fadeout 1.0

hide crowd
with Dissolve(2.0)

"Eventually the torrent subsides and I step tentatively out into the hallway."

"Only to be met by Emi, who comes flouncing down the hallway like a cannonball."

play music music_emi fadein 0.3

show emi basic_happy at center
with charaenter

emi "Hey! Hi Hisao! Great timing!"

show emi excited_proud
with charachange

emi "I have super extra lunch today, as promised! Let's go upstairs!"



label en_A29b:

#Finally, this is where the two join up again

stop music fadeout 2.0
stop ambient fadeout 1.0

scene bg school_staircase1
with locationchange

"The stairway to the roof is a little dilapidated, but it's clearly been used recently."

"At the top of the stairs is a door, complete with missing padlock."

"I wonder who the intrepid individual was that removed the lock?"

$ renpy.music.set_volume(0.5, 0.0, channel="ambient")
play ambient sfx_rooftop fadein 2.0

scene bg school_roof at bgright
show emi basic_closedgrin at center
with Fade(0.5,0.3,1.0,color="#FFF")

"Emi shoves the door open and steps beaming into the sunlight."

show rin silhouette at offscreenright
with None

show bg school_roof at center
show emi basic_closedgrin at left
show rin silhouette at tworight
with ease

show emi basic_shock
with vpunch

"Suddenly, a tall dark stranger appears out of nowhere, standing imposingly in front of us. Emi flinches back, almost falling back down the stairs."

$ doublespeak (emi, rin_, "Eeek!", "Hello.")

show emi basic_hes
with charachange

show emi basic_hes at twoleft
with charamove

emi "Yipes! You scared me, Rin!"

"Wait, isn't she…"

show rin relaxed_surprised
with charachange

play music music_rin fadein 2.0

rin "Hello."

"Noticing that Rin is speaking to me, Emi looks curiously at me."

show emi basic_confused
with charachange

emi "You two know each other?"

"I look confusedly at Emi."

hi "She's that friend of yours?"

show rin relaxed_nonchalant
with charachange

"Rin has turned her gaze towards the clouds drifting above the school."

rin "I didn't know you knew this person, Emi."

stop music fadeout 2.0

"…"

"The awkward silence lasts only for a few seconds until Emi lets out a tiny giggle, shrugging the coincidence off."

show emi basic_closedgrin
with charachange

emi "I invited Hisao for lunch. If you know him, that's just better."

show rin basic_deadpan
with charachange

rin "Oh. Does this mean I don't get food? Or did you invite him for lunch without the lunch?"

show emi basic_grin
with charachange

emi "Erm, neither, I have food for three."

show rin basic_deadpanamused
with charachange

rin "Nice thinking."

hide rin
hide emi
with charaexit

"They walk to the other end of the roof while I stay at the clock tower for a while, taking in the atmosphere."

play music music_soothing fadein 0.5

"There is nobody else but us here. I guess the roof is not as popular as it is in other schools."

"A few rundown benches and tables are scattered around the edges, perhaps in an attempt to make the rooftop look less desolate."

"The small pebbles covering the roof rattle beneath our feet."

"I peek through the chain link fence to take a look at the school grounds and beyond."

"Students are strolling in pairs and groups around the quadrangle and at the cafeteria."

"A few delivery trucks are driving past the school towards the convenience store nearby."

"Somewhere a watchdog barks at a passer-by."

"Somehow, when I look towards the town center the small town feel strikes me very strongly, almost palpably."

"The hectic lifestyle of big metropolises seems so far away and foreign here; nobody has to run to catch a bus like their life depended on it or get their senses overloaded by the neon lights and traffic jams."

"I feel surprisingly optimistic about this new life of mine, looking at my new hometown, even if it's going to be mine for only one short year."

"Finding out about my illness and having to move away from home all came so suddenly I haven't had time to think how I feel about it."

"When I step out of the shadow of the clock tower to the open I feel warmth touching my back."

"The sun shines from a perfectly clear cerulean sky."

"A cool breeze sweeping over the rooftop makes me shiver, but only briefly."

"The wind carries the scent of trees and flowers, not smog and car exhaust like it used to, just a few weeks ago."

"Emi settles on a bench with Rin in tow and produces one big and two small lunch boxes from her bag."

show rin basic_deadpannormal at tworight
show emi basic_happy at twoleft
with charaenter

emi "Come on, Hisao! What are you waiting for?"

"She is beckoning me to join them, making room on the already small bench."

hide emi
hide rin
show bg school_roof at bgleft
with charamoveoutleft

show emi basic_happy_close at closeleft
show rin basic_deadpannormal_close at closeright
show bg school_roof at center
with charamoveinleft


"I seat myself on the corner of the bench to take as little space as possible. It's pretty cramped, but somehow all three of us fit on it."

hi "Impressive view."

show emi basic_closedhappy_close
with charachange

"Emi suppresses a giggle and places a lunchbox in front of Rin, and hands another lunchbox to me."

show emi excited_proud_close
with charachange

emi "Here you go! Lunch, as promised!"

"Homemade, no less. I'm impressed."

hi "Wow. This looks really good."

show emi excited_amused_close
with charachange

emi "Thanks! I make 'em myself when I can."

"Conversation dies off as I set about the business of feeding myself."

show rin basic_awayabsent_close
with charachange

"Taking a few bites, I glance up and notice Rin deftly opening the lunch box and popping a forkful of food into her mouth using only her feet."

"Even though I've seen it before, I can't help but be impressed at her dexterity."

"It's also a reminder of the sort of place I am in right now."

"Will I ever get used to sights such as this?"

"I can't decide if getting used to such a thing would be a good thing or a bad thing either."

"Does getting used to this place mean that I'm giving up on being a normal person?"

"Or does it just mean that I'm becoming more understanding about those around me?"

"I'm distracted from my thoughts by the sight of Emi tearing into her lunch as if it had insulted her ancestors."

show rin basic_absent_close
with charachange

hi "You seem pretty hungry."

show emi basic_grin_close
with charachange

"Emi looks up, mouth half full, and swallows before nodding."

emi "My morning run always works up an appetite."

show emi basic_closedhappy_close
with charachange

emi "Which is great, because then I burn through lunch pretty quickly."

show emi excited_proud_close
with charachange

emi "Helps me keep my girlish figure."

show rin basic_deadpan_close
with charachange

rin "What would happen if you'd lose it? Would you become a man?"

"I very nearly choke on my lunch trying not to laugh."

show emi basic_annoyed_close
with charachange

emi "It's a figure of speech."

show rin basic_deadpandelight_close
with charachange

rin "Does your figure have to run in the mornings too?"

hi "Do you always talk like this?"

show rin relaxed_surprised_close
show emi basic_confused_close
with charachange

$ doublespeak(emi, rin, "Talk like what?", "Like what?")

"I think that answers my question."

hi "Er, never mind."

hi "So, uh…"

"I struggle to think of small talk and settle on the obvious question."

hi "How'd you two meet?"

show rin basic_awayabsent_close
with charachange

"Rin seems content to let Emi answer this question."

show emi basic_grin_close
with charachange

emi "Someone in the housing department thought that we'd complement each other well, so we were assigned rooms next to one another."

hi "Complement each other?"

show rin basic_deadpannormal_close
with charachange

rin "Like shoes and a suit."

hi "Huh?"

show emi basic_closedgrin_close
with charachange

"Emi giggles at my confusion."

emi "Put us together and we've got all our limbs, get it?"

hi "Ah."

show emi basic_happy_close
with charachange

emi "So I started helping Rin get ready in the mornings, and that was that!"

show emi basic_grin_close
with charachange

emi "I mean, you can't help someone get dressed every morning and not get along."

hi "I see."

"Rin chooses this moment to interject."

show rin basic_deadpan_close
with charachange

rin "I have trouble with shirts."

hi "Right, that seems… fairly obvious."

show rin basic_surprised_close
with charachange

rin "Really?"

hi "Kind of…?"

"This isn't helping, but at least Emi seems to find the whole thing funny."

"That, combined with the fact that Rin is genuinely curious, makes me feel slightly better and yet, confused."

hi "I mean, you've got no arms."

hi "So uh, putting on a shirt seems like one of those things that would be… difficult."

"You know what? I'm going to just stop talking now."

"It'll save me a lot of trouble in the long run."

"Rin nods in what I suspect is meant to be a sage manner."

show rin basic_lucid_close
with charachange

rin "I see."

show rin basic_absent_close
with charachange

"The conversation dies as I turn my attention back to my lunch."

"It's really quite good."

"Emi finishes her lunch first and makes a contented noise."

show emi excited_laugh_close
with charachange

emi "Ah, that was good."

"As she busies herself with cleaning up her lunch, Rin speaks up."

show rin basic_deadpan_close
with charachange

rin "I'm thirsty."

show emi basic_shock_close
with charachange

emi "Oh! I almost forgot about that! Sorry!"

show emi basic_closedgrin_close
with charachange

"With a flourish, she reaches into her bag and removes a trio of juiceboxes."

"She tosses me one that appears to be cranberry juice, one to Rin that appears to be some kind of strawberry milk (complete with pink color scheme), and keeps an (equally pink) box of some kind of fruit punch for herself."

show rin basic_awayabsent_close
with charachange

"Rin dexterously stabs her straw through the top of her box and begins to drink."

"I'm once again impressed by how flexible she is, but this time I keep my comment to myself."

"Somehow I don't think either Emi or Rin are the sorts of people to think twice about the way they work around their particular disabilities."

"Rin especially so."

"Indeed, she gives off the impression of being entirely unaware that she's missing any limbs at all."

"Whether or not that's a conscious decision is another matter."

"I'm honestly not sure."

show emi basic_grin_close
with charachange

emi "So Hisao, how do you like it up here?"

show rin basic_absent_close
with charachange

hi "Hmm?"

hi "It's quite nice, actually. I like high places, for the view."

hi "Thanks for inviting me up here."

hi "And for the lunch, too."

show emi excited_amused_close
with charachange

"Emi grins a thousand-watt grin, pleased by my response I suppose."

emi "No problem!"

show emi excited_proud_close
with charachange

emi "Feel free to eat with us next time too, okay?"

emi "I won't make you a lunch, but you can bring your own up here."

hi "No lunch service? I don't know…"

show emi basic_annoyed_close
with charachange

"Emi looks mock offended."

emi "Trying to take advantage of my good nature?"

emi "The nerve!"

show emi basic_closedgrin_close
with charachange

"She giggles."

show emi sad_depressed_close
with charachange

emi "Well, if that's your answer, I guess Rin and I will just keep eating lunch all alone…"

"I am suddenly assaulted by the most heart-rending puppy-dog eyes I've ever seen as Emi pouts."

hi "Kidding! I was kidding!"

hi "I'd love to eat lunch up here again."

hi "Good location, and the company's okay too."

show emi basic_grin_close
with charachange

"Emi frowns a bit at my declaration of “okay” but seems happy enough that I've accepted her invitation."

"I guess this makes us friends now."

"Or at least acquaintances."

play sound sfx_warningbell

"The lunch bell rings, signaling a return downstairs."

show emi basic_hes_close
with charachange

emi "Rin, you didn't finish your lunch again!"

show rin basic_deadpan_close
with charachange

rin "I wasn't that hungry."

show emi basic_annoyed_close
with charachange

emi "If you don't eat more, you're going to fade away!"

show rin relaxed_boredom_close
with charachange

"Rin shrugs, as if this is an acceptable risk."

stop music fadeout 4.0

hi "Come on, we'd better get going."

stop ambient fadeout 2.0

scene bg school_staircase1
with locationchange

"The three of us head down the stairs together."

scene bg school_scienceroom
with shorttimeskip

"The afternoon class passes. Once again, I find myself without a plan for something to do after school, so I head to the library to return a couple of the books I finished reading."

$ renpy.music.set_volume(1.0, 0.0, channel="ambient")

scene bg school_library
with locationskip

"Walking inside, I see that there are about as many students here as there were on Tuesday, all the more evident from the almost total silence enveloping the room."

play sound sfx_impact2
with vpunch

show yuuko panic_up at center
with easeinbottom

play music music_happiness fadein 2.0

"As I drop the books I'd borrowed into the returns slot in the counter, Yuuko suddenly pops up from behind it, quite startled from the banging they make as they hit the trolley next to her."

hi "Ah, sorry Yuuko. Didn't mean to startle you."

show yuuko worried_up
with charachange

yu "No, no. That's fine. It happens… a lot. I'm used to it by now."

show yuuko neurotic_up
with charachange

yu "Um, can I help you?"

hi "It's okay, I think I know where everything is. Thanks anyway."

hide yuuko
with charaexit

"I suppose I'll grab another book or two while I'm here. There's not much else to do, and after reading so much during my stay in the hospital, it's become a hard habit to break."

stop music fadeout 5.0

"I wander down to the fiction section towards the back of the library, scanning the bookshelves for anything that catches my eye."

"As I do, I look over to the corner where Hanako had been the last time I was here, not really expecting anything to come of it."

scene ev hana_library_read_std
with locationskip

"…surprisingly, though, she's there, absorbed completely in a fairly thick book. I decide against intruding on her like last time and get back to finding reading material."

scene bg school_library_ss
with shorttimeskip

play music music_tranquil fadein 6.0

"After an indiscernible amount of time spent perusing the aisles, I finally decide on a couple of books to get and slide them off the shelf."

"With a minimum of fuss, I quickly walk over to the counter, check out my books and pop them into my bag as I walk out."

scene bg school_courtyard_ss
with locationskip

"By the time I leave the main building, sunset isn't too far away. A small trickle of students remain, but the majority have left; presumably to their homes and dorms."



label en_A29c:

scene bg school_dormhisao_ss
with locationskip

"Feeling utterly drained, I head to my room to read the books I borrowed. There's been enough action and excitement for one day already."

"The first is “Alice's Adventures in Wonderland”. I know the story, of course, but I've never actually read the original book."

"It's just as trippy as I remember the story to be, with the wacky characters and nonsense plot."

"I start thinking of myself as some kind of an Alice too, haplessly tumbling down the rabbit hole into this Cripple Wonderland."

"…Okay, that's a rather strong expression. Still, the isolated location and the overt way the school accommodates to absolutely everything is unsettling. It is like another world."

"I wonder why I can't shake the feeling of being an outsider like Alice, despite most everyone being so hospitable and friendly with me."

"Turning another page, my mind starts drifting further away from the book. It's quiet, I can hear my heartbeat thumping against the fabric of my shirt."

"For some reason, it makes me feel really bad like it has since that time in the forest with Iwanako. Like I was locked in a cage with something nasty and scary."

stop music fadeout 5.0

scene bg school_dormhisao_ni
with Dissolve(3.0)

"I put the book down for a while and stare at the ceiling, taking my time to shake off the feeling."

"200 pages later, I fall asleep."

scene black
with shuteye


#*********************

label en_A30:

scene bg school_courtyard_ss
with None

$ renpy.music.play(music_tranquil, fadein=3.0, if_changed=True)

"I guess I need to buy some supplies. I can't live off cafeteria food and eating out for my entire stay here."

scene bg school_gate_ss
with locationchange

"As I leave for the gate, I make a few loud stretches to try and stave off the tiredness that's accumulated over the week."

scene bg school_road_ss
show lilly back_smileclosed_ss at center
show lillyprop back_cane_ss at center
with locationchange

#stop music fadeout 4.0

"After passing through and rounding the corner, though, I see a solitary figure walking downhill towards the small town below. The color of her hair and tapping of her cane are unmistakable."

show lilly cane_surprised_ss
hide lillyprop
with charachange

"I quickly walk up to her, which seems to catch her attention without a word needing to be said."

hi "Hi, Lilly."

show lilly cane_weaksmile_ss
with charachange

"She takes a moment to place the voice, slightly adjusting her head to face a bit more towards the source of my voice as she does."

#play music music_lilly fadein 3.0

show lilly cane_smile_ss
with charachange

li "…Hisao?"

hi "Yep, that's me."

"She seems to have a good memory for voices. The fact that she actually remembered is a pleasant surprise."

li "Good evening. What brings you here?"

show lilly cane_weaksmile_ss
with charachange

"Once again, she gives a small polite bow. And, once again, I reply in kind before realizing that I needn't do so."

hi "Just going into town. You?"

show lilly cane_ara_ss
with charachange

li "My my, what a coincidence."

hi "Doing the same thing, eh?"

show lilly cane_smile_ss
with charachange

li "Mm. I usually go shopping on Fridays."

show lilly cane_surprised_ss
with charachange

"She pauses for a moment, suddenly looking a little lost."

li "That said, Hanako usually comes into town with me…"

"Ah. Not lost, but worried. The two do seem to keep pretty close tabs on one another. It's kind of surprising that Hanako would just forget Lilly like that."

hi "I noticed her reading in the library. She probably just got caught up in a book."

show lilly cane_weaksmile_ss
with charachange

"She lets out a small sigh of relief."

li "Thank you. She has a habit of doing that."

hi "Avid reader?"

show lilly cane_smile_ss
with charachange

li "Right. She doesn't like being around crowds of people, so reading away from everyone lets her relax a bit."

"Although she probably didn't intend it, I can't help but grimace as I recall my first meeting with her."

show lilly cane_smileclosed_ss
with charachange

"Hardly wanting to bring it up, I remain silent as we quietly continue to walk down the quiet road."

"Tack, tack. Tack, tack."

"With the road bereft of cars and the students of Yamaku increasingly far behind us, the quiet rustling of the leaves and the measured tapping of Lilly's cane against the sidewalk are all that can be heard."

"It's kind of nice, especially compared to the hustle and bustle of where I used to live."

"Before I know it, I've relaxed so much that a loud yawn escapes before I can control it."

show lilly cane_giggle_ss
with charachange

li "Tired?"

hi "Yeah, been running ragged these past few days."

"That's an understatement, to be sure. Transferring into a different school would be bad enough, but nothing like this…"

show lilly cane_smile_ss
with charachange

li "Well, hopefully everything should settle down for you. The festival's got everyone in a spin right now, and you've been plopped right in the middle of things."

"For a moment I hesitate, but given her apparent tolerance for frankness I decide to give my full thoughts."

hi "I guess. Yamaku's kind of different though. I mean, the formality surrounding everything, the isolation around it… not to mention the most obvious difference."

hi "It's kind of a whole different mindset. I suppose I'll get used to it though, in time."

show lilly cane_smileclosed_ss
with charachange

"She gives a matter-of-fact nod, apparently pleased with my answer. It feels almost as if she's included me in the flock of students she's shepherding, along with class 3-2 and Hanako."

"Well, not that I mind. It's nice to get the thoughts off my chest in any case."

show lilly cane_smile_ss
with charachange

li "Looking on the bright side, one could see it as a chance for a new beginning. You should cherish the ability to make new friends."

"That's optimistic. Nonetheless, it's good to have a positive attitude about such things, I suppose."

hi "I guess that's a good take on it."

scene bg suburb_roadcenter_ss
show lilly cane_reminisce_ss at center
with shorttimeskip

stop music fadeout 6.0

"Walking on down the road, she seems to become somewhat unsettled. Before I can ask what's on her mind, she seems to collect herself and speaks up about something else."

show lilly cane_weaksmile_ss
with charachange

li "So, where in town were you going?"

"That's actually a pretty good question. I'd come in to buy food, but the layout of the place is still totally foreign to me."

"I had intended to just wander around and see what I could find, but with sunset already approaching and nightfall not too far away, that doesn't seem very wise."

"I'm going to have to ask her for directions. Again."

hi "I was just going to get some food… but now that you mention it, I don't really know the way."

show lilly cane_planned_ss
with charachange

li "Well now, this is quite lucky. I was just about to go to the convenience store myself."

hi "Looks like I'll be in your care again, then. Thanks."

"Together we walk to the store, my paces carefully slowed to remain beside her. Compared to my usual walking pace, hers is quite a bit slower. Not that it's without reason."

scene bg suburb_konbiniext_ss
with shorttimeskip

play music music_daily fadein 2.0

"After what couldn't be more than several minutes, I catch sight of our objective. This town really is pretty small."

scene bg suburb_konbiniint
with locationchange

"Without further ado, we make our way inside with a greeting from the counter."

show lilly cane_weaksmile at center
with charaenter

li "Mind if I tag along with you? Usually Hanako would help me, but seeing as she's not here…"

"It takes a moment before I realize what she means."

"Considering she wouldn't be able to read any of the labels, shopping without any help would be a big pain for her."

"That said, I can't shake the feeling that she'd had this idea since I said I was coming here."

hi "Sure. It'd be my pleasure."

"I grab two well-used red baskets from the small stack beside the entrance, handing one to Lilly."

show lilly cane_weaksmile at Transform(ypos=800)
with charamove

show lilly basic_smileclosed at Transform(ypos=800)
with charachange

show lilly basic_smileclosed at center
with charamove

"She lays it on the ground, putting her schoolbag in, retracting her cane and sliding it through the basket's handles before picking it back up in her right hand."

"Wait, if she doesn't use her cane…"

show lilly basic_smileclosed at Slide(0.5,0.5,0.3,0.5,1.0, time_warp=_ease_time_warp)
with None

show lilly basic_smileclosed_close at Slide(0.5,0.5,0.3,0.5,1.0, time_warp=_ease_time_warp)
with Dissolve(1.0)

"Before I can complete the thought, she comes beside me and pinches the cuff of my uniform in her slender fingers."

show lilly basic_concerned_close at twoleft
with characlose

li "Is this all right?"

hi "Ah, sure."

show lilly basic_smileclosed_close
with characlose

"I have no reason not to accept. I can think of worse things than shopping with a pretty girl holding onto me, even if it is out of necessity."

"We navigate our way through the store, with not one of the occasional passing customers seeming to bat an eyelid."

"Considering how close Yamaku is, I guess seeing students from there must be entirely normal for the local residents."

"As we reach each aisle, I quickly check with Lilly and find out what she needs. I grab it along with what I'm looking for, and put our items into their respective baskets."

"I guess this is the same routine she and Hanako follow every Friday."

hi "Right, all that's left is the bread and that should be my shopping done. Do you need anything else, Lilly?"

show lilly basic_smile_close
with characlose

li "No, this should be everything."

hi "Off we go, then."

show lilly basic_smileclosed_close
with characlose

"With a quick side trip to the bakery section, we make our way to the registers."

"The line, thankfully, is almost nonexistent. It's not long before we've both paid for our food and are out the door."

scene bg misc_sky_ni at Fullpan(15.0)
with locationchange

"As Lilly retrieves her cane and extends it to full length, I waste a minute looking upwards at the night sky while holding both our bags."

"For a moment I try to make clouds with my breath, but the summer's heat doesn't seem to cooperate."

"Eventually she rights herself, taking a quick stretch before taking her bag and leaving me to my two."

scene bg suburb_konbiniext_ni
show lilly cane_listen_ni at center
with locationchange

hi "You tired as well?"

show lilly cane_sleepy_ni
with charachange

li "The festival preparations have been complete chaos. Shizune breathing down my neck doesn't exactly help things, either."

hi "Hey, she's only trying to get everything organized. Better now than later, right?"

show lilly cane_weaksmile_ni
with charachange

li "I suppose. I'm going to enjoy relaxing in town tomorrow, that's for certain."

"I guess the festival preparations must be taking their toll on both of them."

scene bg suburb_roadcenter_ni at bgright
with locationchange

"We walk out into the quiet street, talking between ourselves as we carry our bags of food and supplies from the store."

"…Wait, what's that?"

"I notice a very distinctive figure making its way towards us, silhouetted by the streetlamps."

"For a second I think it's another male student from my class, but as he, or should I say she, gets closer I recognize her quickly."

show bg suburb_roadcenter_ni at center
show rin relaxed_nonchalant_ni at right
with charamoveinright

stop music fadeout 8.0

hi "Rin? What're you doing out here so late?"

show lilly cane_surprised_ni at center
with charaenter

li "Rin?"

"Lilly perks her head, looking like she's trying to focus on listening more keenly. It suddenly comes to me that I should probably interpret the scene for her."

hi "It's Rin… Tezuka, I think was her last name, from our school."

show lilly cane_weaksmile_ni
with charachange

"She stiffens at the name and gives a complicated-looking expression, something like a forced fusion of a composed smile and a painful cringe."

li "Ah. I understand."

"I guess Lilly knows Rin too."

show rin basic_awayabsent_ni
with charachange

show bg suburb_roadcenter_ni at bgleft
show rin basic_awayabsent_ni at tworight
show lilly cane_weaksmile_ni at twoleft
with charamove

"Rin turns to look at us, looking terribly out of it. I'm not entirely sure if she recognizes either of us or at least she doesn't acknowledge it if she does."

"She looks like a zombie. Or a statue. A statue of a zombie."

"But slowly, some symptoms of understanding seem to light in her dark eyes: this is something she must react to."

show rin basic_lucid_ni
with charachange

show rin basic_awayabsent_ni
with charachange

"Rin blinks once. Very thoroughly."

show rin basic_absent_ni
with charachange

rin "Hello."

"…"

"There is an awkward pause, everyone waiting for someone else to say something."

hi "What are you doing here this late?"

"…"

rin "I…"

show rin basic_deadpan_ni
with charachange

rin "I was wondering about that myself too. Just now."

play music music_rin fadein 0.5

show rin basic_deadpannormal_ni
with charachange

rin "Some people asked that just before. I assume they were wondering the same."

rin "I didn't know. They didn't know either. I asked. That's why I'm wondering."

rin "So that was pretty much it. It's a murder mystery without a murder."

"…"

show rin negative_spaciness_ni
with charachange

rin "They were going that way."

show rin basic_absent_ni
with charachange

"She turns facing to her right in order to demonstrate the direction the other people went to as if that was important, then rotates back like a mechanical puppet in one of those overly complicated clockworks."

"For a person who gives an impression of being the quiet type, Rin really does use a lot of words to say things that don't need a lot to be said."

"Unsure if she's finished, I say nothing. Neither does Lilly, who seems equally robbed of words for the time being."

"I think that both of us are in fact just scared that any response might provoke her to continue."

"Our stupefied lack of reaction doesn't faze Rin at all. She keeps looking at us expectantly, a calm hint of expression on her blank face."

"She seems to be that kind of person. Always so relaxed."

"As if bull elephant-grade sedatives were flowing in her veins in the place of blood."

show lilly cane_concerned_ni
with charachange

li "Do you have amnesia? I don't recall you having anything of the sort, though…"

hi "No, I don't think it's that."

hi "The other passersby were probably just worried, though. You do look really lost, the way you're standing in the middle of the street."

show rin basic_deadpan_ni
with charachange

rin "Oh, I see."

show rin relaxed_nonchalant_ni
with charachange

rin "Maybe I should've taken some other kind of pose in that case."

"I ponder for a while whether I should chase this angle further, or give up for the sake of my own sanity."

"I decide on the latter."

"It seems that most of the time, it's better to not read too deeply into what Rin is babbling about."

"Talking with Rin is like playing chess with a supercomputer who does seemingly completely random moves as if to mock everything you know about chess. It's like that, except with human interaction."

"And even if I win, it feels like losing."

"Damn, it's just like Kenji said. Even when I win, I lose. Is this the power of the girls of Yamaku?"

"…"

"I push the thought aside as too dangerous to consider further. It's probably just Kenji's anti-female propaganda getting to me during a moment of weakness."

hi "Yeah, maybe taking another pose might have worked."

hi "So anyway, you have no idea what you're doing here?"

show rin negative_annoyed_ni
with charachange

"She frowns, looking extremely displeased at either my question, its consequences, or the answer she's about to give."

rin "I do have. Some idea. I can't really tell what kind of an idea."

show lilly cane_smile_ni
with charachange

li "That sounds like progress, at least."

"Lilly sounds as if she's spotted an opening for some kind of discernibly normal conversation. I can't say I share her optimism."

rin "Yes, there is some. Definitely. The rest will come later."

show rin basic_deadpanupset_ni
show lilly cane_weaksmile_ni
with charachange

rin "I'm sure of it. I always have… reasons."

"The ensuing silence kills Lilly's hopes all too visibly. That didn't last long."

"Rin's, as far as I can tell unbased, assurances aside… what should be done?"

"We could just leave her to her own devices, whatever those are… but it's late and I don't think we'll be getting any thanks if Rin is found standing here in the middle of the night."

"Which she probably will, unless she manages to remember what she was doing here in the first place."

"As for me trying to guess what might've been going on in her mind when she decided to embark on this adventure, the chances seem to be on par with winning the lottery."

"Several times in a row."

"Lilly is oddly quiet too. I'd appreciate some support from the sidelines here, especially if she's more familiar with Rin than I am."

"But it can't be helped. It seems her familiarity with Rin is exactly why she's staying subdued."

hi "So, I assume you were going somewhere, not coming back to the school… any idea where?"

show rin relaxed_surprised_ni
show lilly cane_surprised_ni
with charachange

"Her eyes widen in shock and she jolts back in a somewhat artificial way, making it seem like an act rehearsed for situations like this."

rin "Are you a mind reader? Is that your disability? How unique!"

hi "No… What? Why would you think that?"

show rin relaxed_disgust_ni
show lilly cane_listen_ni
with charachange

rin "You knew what I was doing."

show lilly cane_displeased_ni
with charachange

hi "Eh, it was just an educated guess. We walked this same street in the other direction just before, to get to the store."

hi "If you were going to school, we would've met you on the way."

show rin basic_deadpanupset_ni
with charachange

rin "Oh."

"She looks a little disappointed."

"Like Kenji, Rin appears quick to jump to completely irrational conclusions."

"Maybe it's something in the water here. I make a mental note to stock up on soft drinks."

hi "You know, that is the second time this week that someone asked if I was a mind reader."

hi "Do I really give off that impression?"

show rin basic_deadpannormal_ni
with charachange

"Rin shrugs her shoulders, which is all the answer I get."

hi "You know—{w=0.3}{nw}"

show lilly cane_smile_ni
with charachange

li "Maybe you should come with us back to the school?"

"Lilly interjects just as I am about to further debunk my alleged mind-reading capabilities. She sounds rather concerned, the paper-thin smile on her face badly disguising that fact."

"Maybe she came to the same conclusion as I did. For everyone's sake, I decide to let the mind-reading topic drop, as it's entirely inane anyway."

hi "Yeah, Lilly's right. If you can't remember, there's no point staying here."

show rin basic_awayabsent_ni
with charachange

"Rin considers this rather simple deduction for a moment, then nods."

show rin basic_absent_ni
with charachange

stop music fadeout 2.0

rin "Okay."

scene bg school_road_ni
with shorttimeskip

$ renpy.music.set_volume(0.1, 0.0, channel="ambient")
play ambient sfx_cicadas
play music music_dreamy fadein 2.0

"We start towards the school again, having wasted way more time than necessary with this episode."

show rin basic_awayabsent_ni at tworight
show lilly cane_smileclosed_ni at twoleft
with charaenter

"Rin walks along the edge of the sidewalk in her arrhythmic way, looking like a mix of sleepwalker and rope dancer, while Lilly keeps one hand on my shoulder, tapping at the ground with her cane."

"Tap step step tap tap step step step."

"Apart from that and a few fragmented beginnings of conversation, it's quiet. A quiet quite apart from the relaxing one into town, at that."

hi "So how's the mural going?"

show rin basic_deadpan_ni
with charachange

rin "We are going to get bad luck. Never talk about works in progress."

show lilly cane_weaksmile_ni
with charachange

li "I'm sure it'll be wonderful."

show rin basic_deadpannormal_ni
with charachange

rin "Bad luck."

"Tap step tap step. She doesn't care to talk about it. Lilly's politeness feels out of place, for the first time. Step step step."

"The hill Yamaku rests on top of is surprisingly steep, going uphill. We slow the pace, but I still feel my pulse rising and breathing getting heavier."

"Almost there, I can see the gates already."

"More than that, though, I notice that Lilly's hand slightly tightens on my shoulder. Interpreting it as a gesture that she wants to ask something, I speak up."

hi "Anything wrong, Lilly?"

"I resist the urge to say “Aside from our traveling companion?” But only just."

"For a moment she seems to debate whether she should even bring it up, but goes for it anyway."

show lilly cane_concerned_ni
with charachange

li "Is everything… all right?"

hi "All right? How do you mean?"

"The fact I can't interpret her incredibly vague question puts her off, for a second."

li "It's just… you seem unusually tired, I guess."

"Now that she brings it up, I notice that my breathing is strangely heavy. The uphill walk has really done a job on me."


label en_choiceA30:
menu:
    with menueffect

    "Lilly noticed it all too quickly…"

    "Sorry, I'm not in very good condition.":
        return m1

    "I don't really want to talk about it.":
        return m2

label en_A30a:

$ renpy.music.set_volume(0.1, 1.0, channel="ambient")
stop music fadeout 5.0

hi "I… I'm fine."

hi "There's nothing to worry about, the hill is just surprisingly steep, don't you think?"

hi "I wonder what they have the school so high up here for anyway, don't we have students in wheelchairs and everything?"

show lilly cane_sad_ni
with charachange

li "Indeed."

show lilly cane_concerned_ni
with charachange

"Lilly's forehead wrinkles in concern, and I don't really want her to have that kind of an expression over me. We barely know each other."

hi "Yeah, my thoughts exactly. Not that you can find a place like this wherever, I guess, but it makes me wonder what they were thinking."

"My voice is overly calm, it sounds weird to my own ear and I speak way too fast. I briefly wonder how much Lilly can sense from someone's voice alone."

li "Mmm…"

hi "Let's continue. We're almost there anyway."

hide lilly
hide rin
with charaexit

"For the rest of the way back to the school, we all remain silent."

stop ambient fadeout 3.0

scene black
with Dissolve(3.0)


label en_A30b:

$ renpy.music.set_volume(0.1, 1.0, channel="ambient")

hi "It's all right, I just need to catch my breath. My condition isn't the best, these days."

show lilly cane_oops_ni
with charachange

li "Oh."

li "Is it something that… is related to you being transferred here? I mean…"

show lilly cane_concerned_ni
with charachange

"She cuts herself off rather abruptly, maybe realizing she was being a bit intrusive. Her instincts are sharp though, and while I don't like the subject it's not like I should lie about it."

"If it's Lilly, I don't think I mind."

hi "I'm just a little weak for the time being."

show lilly cane_oops_ni
with charachange

li "Hanako said you look fairly… healthy, so I naturally thought…"

show lilly cane_sad_ni
with charachange

"Lilly doesn't finish her sentence again, letting it trail off with a measure of concern."

"As she furrows her brow, Lilly's uncomfortable expression spurs me to say at least something to ease her feelings."

"It's surprising she's this flustered, considering her straightforward attitude with her own blindness. She must know that not all share her own comfort about such things."

hi "No, it's okay."

hi "I have a pretty… I guess the best way to put it would be messed-up… heart. Arrhythmia."

hi "I had a bad heart attack a while ago because of it, and spent most of the spring in a hospital. Ended in Yamaku on doctor's orders."

"She silently nods her head in acknowledgment."

"My answer, though, only seems to make Lilly furrow her brow even further. She doesn't seem to quite know how to react, given we don't really know each other that well."

"I can't really fault her for it, given I have the exact same reaction."


label en_A30c:

"To my surprise, in a moment's time her face shows that she comes to some sort of realization."

show lilly cane_oops_ni
with charachange

li "Wait… so the time when Emi and you collided in the hallway…?"

"I grimace slightly. Her ability to connect the dots quite so fast is unexpected."

hi "Yeah. I guess I'm a textbook example of why those rules about running in the corridors exist."

show lilly cane_sad_ni
with charachange

"That was a lot more dry than I'd intended. Lilly visibly shies away from continuing the topic."


label en_A30d:

"While I do want to assuage her concern, I really don't want to dwell on this either."

hi "Don't worry about it."

show lilly cane_weaksmile_ni
with charachange

"I try to offer a reassuring smile but then I realize the futility. Without knowing this, Lilly smiles at me reassuringly but doesn't say anything further."

$ renpy.music.set_volume(0.5, 5.0, channel="ambient")
stop music fadeout 2.0

scene bg school_dormext_half_ni
show rin relaxed_surprised_ni at tworight
show lilly cane_weaksmile_ni at twoleft
with shorttimeskip

"Arriving at the dorms, Rin stops in front of her mural as if lightning struck her. She had been so quiet for almost all of the walk back that I had all but forgotten she was here."

show rin relaxed_disgust_ni
with charachange

rin "It's Friday, isn't it?"

show lilly cane_smile_ni
with charachange

li "Yes… Friday, the eighth of June."

show rin basic_upset_ni
with charachange

play music music_rin fadein 0.5

rin "This is bad."

show lilly cane_surprised_ni
with charachange

li "Bad? Why?"

show rin negative_annoyed_ni
with charachange

rin "I think I am going to go in a fetal position and throw up. Possibly in reverse order."

show lilly cane_concerned_ni
with charachange

li "Is something wrong?"

show rin negative_confused_ni
with charachange

rin "No. Nothing is wrong. It's Friday and nothing is wrong yet. This mural, it's going to need to be finished by Sunday. So everything's all right."

show rin negative_worried_ni
with charachange

rin "Do you have any drugs? Or a time machine?"

show rin negative_confused_ni
with charachange

rin "This is not good. Not good."

"So she's behind her schedule. Recalling Shizune's exasperation at Rin's carefree attitude several days ago, I don't know what to think."

"She has left herself open for a “told you so” unless she can pull off whatever she needs to pull off by Sunday morning."

"Rin keeps staring at her mural looking as mortified as she can."

show rin negative_annoyed_ni
with charachange

rin "Leave me. I'm going to need to work for a while."

"I glance at Lilly, expecting her to share an incredulous look with me as I roll my eyes, but then I realize she's not one to do that kind of thing."

show rin negative_angry_ni
with charachange

rin "Leave me."

stop music fadeout 2.0

hide rin
with charaexit

show lilly cane_concerned_ni at center
show bg school_dormext_half_ni at bgright
with charamove

"We do, of course, not wanting to aggravate her any more than she already is."

"There is a churning bad feeling in my gut. Rin sure has a knack of making people feel worried about her."

"She seems like a person who should never be left alone."

hi "Maybe we should call someone? She sounded like she was going into shock or something."

show lilly cane_oops_ni
with charachange

li "I'm sure she will be just fine. She's just a… eeeh… how to say…"

"Lilly cocks her head a little, trying to find a polite way of calling Rin crazy without calling her crazy."

hi "Unique?"

show lilly cane_weaksmile_ni
with charachange

li "Yes, a very unique person."

hi "I guess you could say that."

show lilly cane_giggle_ni
with charachange

"She giggles at the notion melodiously, nodding in agreement."

show lilly cane_weaksmile_ni
with charachange

li "Sorry about leaving you stranded as you talked to her. I… don't really understand her, so I keep my distance."

"So my guess was right. Lilly offers a slight, apologetic smile as if she was sorry that her own shortcomings have prevented her from becoming closer to Rin."

"I'm not one to blame her. At all."

"Lilly lets slip a long breath, probably a disguised yawn. I imagine she's as exhausted by all this as I am."

show lilly cane_cheerful_ni
with charachange

li "I'd better leave now and give these to Hanako. Thank you for the company, Hisao."

"She smiles very sweetly at me. It feels different than normal, despite the fact that she seems to be smiling so often."

"I can't put my finger on what the difference is. It's just different."

"Relaxed, I'd say, but that's probably just relief over getting rid of Rin. Maybe."

hi "Yeah… good night. Say hi to Hanako for me."

show lilly cane_smile_ni
with charachange

li "I will. Good night."

hide lilly

stop ambient fadeout 2.7

scene black
with Dissolve(3.0)

return

