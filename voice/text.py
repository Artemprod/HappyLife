TEXT: dict[str:str] = {
    'prepare_for_practice': 'Начнем нашу практику. Прими удобное положение, закрой глаза. '
                            'Мы готовимся исследовать и освещать наше подсознание, заглядывать в его самые потаенные уголки.',
    'instruction_relax':
        [
            """Позвольте себе начать процесс расслабления. Начнем с глубокого вдоха, затем медленного выдоха, позволяя вашему телу постепенно освобождаться от напряжения.""",
            """Почувствуйте, как ваше тело начинает расслабляться, начиная сверху и спускаясь вниз. Начнем с головы, позвольте вашей голове стать свободной от напряжения. Отпустите любые напряженные мышцы в лице и шее. Переместитесь к грудной клетке и спине. Позвольте этой области вашего тела медленно расслабиться. Ощутите, как напряжение уходит.""",
            """ Теперь перейдем к животу. Позвольте ему расслабиться и расшириться с каждым вдохом и выдохом. Продолжайте дыхание и перейдите к бедрам, ногам и стопам. Разрешите этим частям вашего тела полностью расслабиться. Почувствуйте, как напряжение уходит, и ваше тело становится более спокойным. """,
            """Теперь, когда ваше тело расслаблено, обратите внимание на ощущения. Почувствуйте тепло, которое окутывает ваше тело, как нежное прикосновение. Сфокусируйтесь на ощущениях внутри вашего тела, будто бы вы обнимаете себя теплом в каждой клеточке. Находясь в этом состоянии расслабления, вы готовы начать терапевтический сеанс. Помните, что вы всегда можете вернуться к этому состоянию расслабления в любой момент, если это необходимо."""],
    'remember_struggle': """ Сейчас тебе нужно вспомнить свой загон. Или чувства, которые тебя беспокоят или тревожат в данный момент. Вспоминай событие, которое причинило тебе неприятные эмоции.\nЭто может быть ситуация, которая причинила боль, обиду, может быть вызвала злость или ощущение растерянности, непонимания. Расскажи о нем! Ты можешь использовать голосовые сообщения, если тебе так удобнее. \nНажми \b"К следующему шагу"\b, когда закончишь """,
    'struggle_details': """Выбери это неприятное событие, вспомни его максимально ясно. Сфокусируйся на деталях этого события и на чувствах, которые ты испытывал в тот момент. Проговори или напиши их""",
    'struggle_details_continue': """Прокручиваем это событие и с максимальной силой проявляем все самые неприятные эмоции в этом событии. Даже если это самые стыдные и "плохие" эмоции. Используй конструкции по типу "Я чувствую (злость/обиду/вину). Если тебе сложно понять свои чувства, то можешь так и сказать : 'Я не понимаю, что чувствую / ощущаю' / 'Мне сложно разобарться в своих ощущениях'.Скажи это вслух""",
    'enhance_emotions': 'Продолжай усиливать эти ощущения, окунись полностью в эти эмоции, проживи их максимально',
    'body_response': """В какой части тела самые неприятные чувства проявляются? Прикоснись медленно рукой к этому месту представь как со всего тела в это место собираются все эмоции и события. Усиль свои ощущения, сконентрируй их в этой точке.Медленно начни доставать это чувство рукой. “Смотри” на эти чувства с закрытыми глазами, какой они формы? Какого объема? Это может быть сфера, квадрат, большая или маленькая масса. Какое это ощущение? Твердое/ жидкое/газообразное/вязкое или текучее? Какого оно цвета? Почувствуй, из чего оно состоит? Как оно ощущается в твоих руках? Быть может, оно липкое или вязкое, холодное или обжигающее ладони. Сконцентрируйся на этом и опиши максимально подробно""",
    'tactile_feelings': 'Что это ощущение хочет сделать с тобой? Тебе придет ответ, опиши эти действия/чувства',
    'root_struggle_question': 'Спроси, откуда это ощущение? Откуда оно пришло, кто тебе его дал? Твое подсознание дает тебе ответ, запиши его',
    'find_the_root_of_struggle': """Схватись за это ощущение руками, двигайся в прошлое и найди то место в ленте своей жизни и подсознания, когда ты это испытал впервые так сильно? Кто это был? Что это была за ситуация?' Ты еще сильнее чувствуешь это ощущение, оно разрастается, события разворачиваются. Расскажи об этом""",
    'get_rid_of_emotion': """Это чувство теперь ощущается в большой силой, оно наполняет тебя, ты чувствуешь напряжение. Ты можешь выбросить это ощущение в пропасть. Сделай глубокий вдох и выход и выброси его! Раз, два, три! Мы снова находимся в начале нашего события""",
    'find_reason': """Какой неприятный осадок и эмоции от этого события? Когда еще раньше ты испытывал(а) эти эмоции связанные с твоим убеждением/загоном? потаенных уголках находим еще  другие события, где эти убеждения вызывали эти эмоции.\nОписывай вслух, что там происходило. Какие неприятные чувства ты испытываешь? Это может быть что-то из раннего детства. Что-то, где ты уже испывал(а) подобные чувства как и в первых ситуациях""",
    'body_response_deeper': """Теперь молча проявляем все неприятные эмоции (мысленно). Но Наше тело на 100 процентов реагирует на эти эмоции, фокусируемся на этом.""",
    'body_enhance_1': """Еще раз проявляем все самые неприятные эмоции, связанные с этим событием, на уровне тела. 
                         Где собираются эти чувства? Позволь своему телу больше напрягаться / сдавливаться в этой зоне. Начинай максимально концентрироваться на этом  ( тут можно таймер который видно)""",
    'body_enhance_2': """Чувства такие неприятные, что парализуют твое тело, сдавливают грудную клетку, виски, живот. Заметь, как твое тело сдавливается и хочется закрыть лицо. Подумай, какое неудобное положение хочет принять твое тело и как часто в жизни тебе приходится принимать такую позу, например, закрыть лицо руками, скрыть свои эмоции и ощущения. Накрути это ощущение вновь и почувствую как оно тобой овладевает с головы до ног""",
    'deep_struggle_quetsion': """Выдели, какое чувство заставляет тебя казаться кем-то, прятать свои эмоции. Выдели эту эмоцию, обратись к подсознанию и оно даст тебе ответ. Проговори это""",
    'deep_struggle_root': """Ответ приходит с ощущением и событием, где ты усваиваешь негативную стратегию поведения, когда ты начинаешь накручвать, загоняться , а не получаешь удовольствие и являешься собой. Ты четко видишь эту страгтегию. Какая эмоция является фундаментом этой стратегии? Скажи это""",

    'deep_sttruggle_situation': """Иди за своим подсознанием в ту сторону, откуда пришел ответ. Оно ведет тебя к этому фундаменту, который повлиял на то, что ты зависишь от своих эмоций, чужого мнения, от чужого удобства. Найди корневое событие  или ответ, начни заново его перепруживать. С самого начала.  Мы находим ключевое событие, которые повлияло на твои установки (повторение погружения). Начни заново его перепруживать со всеми эмоциями и событиями """,
    'dialogue_to_adult': """Представь персонажа, которому ты хочешь высказать свои эмоции (скорее всего, это кто-то из родителей/взорослых, которые окружали в детстве) - начни говорить вслух то, что думаешь.Все, что приходит в голову. Скажи, что устал/а кем-то казаться, подстраиваться. Как тяжело быть все время неуверенным/ой в себе, например: “Я устал () / Я не могу больше ()/ Мне надоело () !”""",
    'dialogue_adult_enhance': """Высказывай ВСЕ что думаешь. Если тебя что-то сдерживает, скажи об этом вслух, “”Что-то скрывается
    Что-то смущает,". Обрати внимание на эти зоны. Что не дает тебе быть эмоциальным/ой  и настоящим/настоящей? Кто не дает тебе себя проявлять? Кто этот конкретный персонаж или какое это событие?""",
    'dialogue_adult_enhace_continue': """Мы снова погружаемся в эту ситуацию. Проявляй все самые неприятные эмоции, которые можно проявить! Усиливай эти чувства, говори их конкретному персонажу, который повлиял на эту установку. Во всех эмоциях скажи все, что думаешь этому человеку. Если это злость, можешь замахнуться рукой, начни кричать. Если это обида, можешь начать плакать, Не сдерживайся, выкрути на полную, даже если хочешь сказать с оскорблениями Продолжай, говори все, что думаешь, все, что накипело по типу "Я сильно злюсь! Я очень обижен/обижена! Со мной так нельзя поступать!" Скажи это вслух!""",
    'dialogue_to_kid': """ А теперь ты с позиции родителя видишь, как утомительно ребенку , как он находится в цепочки событий из-за твоей тревоги и твоих эмоций, которую ты передал ребенку. Ты хочешь помочь ей/ему? Поговори вслух со своим ребенком, что бы ты хотел ему сказать в этой позиции? На уровне ощущений, все что идет от сердца \n“Я не хочу чтобы ты переживал” ”мне жаль что ты злишься” / "я не хочу тебя расстраивать" """,
    'dialogue_to_adult_response': """А теперь, что ты чувствуешь на месте ребенка? Что ты хотел ответить взрослому? Продолжай общение с ним с детской позиции. Ты можешь продолжать высказывать недовольство""",
    'dialogue_to_kid_response': """Теперь ты снова во взрослой позиции. Почувствуй, что ты испытваешь, когда твой ребенок говорит тебе эти слова. Тебе хочется прийти к примирению, объясниться. """,
    'dialigue_to_kid_enhance': """Продолжай говорить вслух. Почувствуй, как сердце бьется чаще, может быть тебе хочется попросить прощения? Передать эти добрые чувства ребенку, дать ему понять, что он любим и ты его принимаешь. Вместе с этим, любви становится больше, становится меньше тревоги. Через твою любовь передается спокойствие и расслабление твоему ребенку. Те места где были тревоги, злость, беспокойства заменяются расслаблением""",
    'peace_dialogue': """Почувствуй эту любовь и спокойствие, которое передает тебе родитель. Ты снова на детском месте. Почувствуй, как спокойно тебе со своим взрослым, как расслабленно он выглядит и как хорошо тебе рядом с ним. Как расслабляется твое тело, а тепло медленно разливается по тебе. Сделай глубокий вдох, почувствуй, как спокойствие наполняет тебя полностью""",
    'kid_adult_response': """Теперь ты маленький, тебя держит мама, ты чувствуешь ее тепло и любовь.\nТы чувствуешь эту энергию и тепло.\nС каждым вдохом чувствуем расслабление.\nГлубокий вход - глубокий выдох. Чувствуешь, как любовь и спокойствие наполняет тебя, а обиды, злость\nи непонимание уходят, давая место новым приятным эмоциям. Давай пройдемся по этим событиям еще раз, но из точки расслабления.\nПогрузись в это чувство, подумай, так ли тебя беспокоит ситуация, с которой мы начали?\nКакую новую установку ты приобретаешь, когда чувствуешь себя спокойно? Чувствуешь ли ты себя увереннее в себе?""",
    'new_belief_upper_response_1': """Давай еще раз вернемся к этому событию. Испытваешь ли ты те же чувства и эмоции? Стало ли тебе спокойнее? Отпускает ли тебя тревога? Что еще осталось от последствий?""",
    'new_belief_upper_response_2': """Вспомни другие ситауции, о которых ты думал/а сегодня. Используя новую установку, подумай, как ты теперь воспринимаешь эти события?""",
    'conclusion_practise': """Что ты теперь ощущаешь, после нашей практики? Так ли пугают тебя некоторые последствия? Много ли негативных эмоций осталось? Как ты чувствуешь себя по отношению к ситуации? Изменилось ли у тебя отношение к себе в сторону своего принятия и понимания себя?"""

}