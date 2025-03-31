from telebot import types
from sys import *

markup = types.ReplyKeyboardMarkup(resize_keyboard = True)
key = types.KeyboardButton('Социальные сети')
key_2 =types.KeyboardButton("Договоры")
key_3 = types.KeyboardButton("приёмная")
key_4 = types.KeyboardButton('учителя')
key_5 = types.KeyboardButton('документы')
key_6 = types.KeyboardButton('профессии')
key_7 = types.KeyboardButton("Электронный дневник")
key_8 = types.KeyboardButton("Создание групп")
key_9 = types.KeyboardButton("Расписание")
key_10 = types.KeyboardButton("Стипендия")


knopka = types.InlineKeyboardMarkup()
knopka.add(types.InlineKeyboardButton("вк", url='https://vk.com/public163555854'))
knopka.add(types.InlineKeyboardButton("Официальный сайт", url='http://goupu20.ru/index.htm'))
knopka.add(types.InlineKeyboardButton("Одноклассники", url="https://ok.ru/group/62027728617583"))
knopka.add(types.InlineKeyboardButton("Телеграмм", url="https://t.me/optomut"))


knopka_2 = types.InlineKeyboardMarkup()
knopka_2.add(types.InlineKeyboardButton("Двусторонние договоры"))
knopka_2.add(types.InlineKeyboardButton("Четырехсторонние договоры"))
knopka_2.add(types.InlineKeyboardButton("Назад"))


knopka_3 = types.InlineKeyboardMarkup()
knopka_3.add(types.InlineKeyboardButton("Web-сайт",url= "https://www.rustore.ru/catalog/app/ru.integrics.kirovschool"))
knopka_3.add(types.InlineKeyboardButton("Приложение электронного дневника",url="https://one.43edu.ru/auth/login"))

knopka_4 = types.InlineKeyboardMarkup()
knopka_4.add(types.InlineKeyboardButton("Время до стипендии"))
knopka_4.add(types.InlineKeyboardButton("Сколько осталось до стипендии"))

markup.add(key,key_2,key_3,key_4,key_5,key_6,key_7,key_8,key_9,key_10) 




text_2 =  '''
<b>Ренева Марина Николаевна</b> - <em>директор Опт</em>
<b>Докучаева Надежда Васильевна </b> - <em>Заместитель директора по УВР</em>
<b>Тутынина Анна Александровна</b> - <em>Заместитель директора по УВР</em>
<b>Жукова Оксана Ивановна</b> - <em>Социальный педагог</em>
<b>Иванина Татьяна Николаевна </b> - <em>Библеотекарь</em>
<b>Орлов Сергей Владимирович</b> - <em>Руководитель физического воспитания</em>
<b>Шлемова Светлана Александровна</b> - <em> Педагог-психолог,педагог-организатор</em>
<b>Кротова Надежда Алексеевна</b> - <em>Заведующий учебной частью</em>
<b>Бабицева Ольга Владимирована</b> - <em>Преподователь химии,биологии</em>
<b>Волоскова Наталья Викторовна </b> - <em>Учитель английского языка</em>
<b>Житникова Елена Юрьевна</b> - <em>Преподаватель спецдисциплин</em>
<b>Корзюкова Анастасия Валерьевна</b> - <em>Преподаватель физической культуры</em>
<b>Мелузова Наталья Валерьевна</b> - <em>Преподаватель математики</em>
<b>Пересторонин Владимир Александрович</b> - <em>Преподаватель спецдисциплин</em>
<b>Пермякова Елена Анатольевна</b> - <em>Преподаватель русского языка</em>
<b>Репина Екатерина Юрьевна</b> - <em>Учитель математики</em>
<b>Чирков Евгений Александрович</b> - <em>Учитель истории</em>
<b>Чурюкаев Алексей Николаевич</b> - <em>Преподаватель спецдисциплин</em>
<b>Шкляева Ирина Николаевна</b> - <em>Учитель физики</em>
<b>Бойко Елена Владимировна</b> - <em>Заведующий практикой</em>
<b>Вачевских Людмила Александровна</b> - <em>Мастер п/о (повар)</em>
<b>Курдюков Сергей Сергеевич</b> - <em>Мастер п/о (электромонтер)</em>
<b>Лекомцев Андрей Валерьевич</b> - <em>Мастер п/о (сварщик)</em>
<b>Перминов Владимир Сергеевич</b> - <em>Мастер п/о (электромонтер)</em>
<b>Угрюмова Наталья Анатольевна</b> - <em>Мастер п/о (продавец)</em>
<b>Чадаев Дмитрий Сергеевич</b> - <em>Мастер п/о (каменщик)</em>
<b>Басманова Мария Николаевна</b> - <em>Преподаватель спецдисциплин (0,7ст)</em>
<b>Ситчихин Алексей Михайлович</b> - <em>Преподаватель информатики</em>
<b>Анастасия Петровна Шихалеева</b>-<em>Преподаватель информатики</em>'''


text_3 = '''
        <em><u>При себе иметь слудующие документы:</u></em> <b>собеседование 27 июня 2024 года</b>
    1.<b>Документ об образовании </b><em>(копию документа 2 штуки - для 2008 года рождения юноши)</em>
    2.<b>Копию паспорта</b> (<em>2 штуки</em>)
    3.<b>Копию свидетельства о рождении </b>(<em>2 штуки</em>)
    4. <em>4 фотографии (3х4)</em>
    5.<b>Медицинскую справку, прививочный сертификат, копию мед.полиса</b>
    6.<b>Характеристику со школы </b><em>(2 штуки)</em>
    7.<b>Копию СНИЛС</b>
    8.<b>Сертификат ПФДО (кружки)</b>
    9.<b>Юношам приписное свидетельство или военный билет</b>
    '''

text_4 =         '''<b>9 класс:</b>
<em>Программы подготовки специалистов среднего звена:</em>
        22.02.08 - металлургическое производство (по видам производства):<u> 3 года 10 месяцев</u>
        15.02.17 - Монтаж, техническое обслуживание, эксплутация и ремонт промышленного оборудования (по отраслям):<u> 3 года 10 месяцев</u>
<em>программы подготовки специалистов среднего звена:</em>
        38.02.08 - Торговое дело (квал. Специалист торгового дела):<u>2 года 10 месяцев</u>
<em>Срок обучения <u>1 год 10 месяцев</u> (программы подготовки клалифицированных рабочих):</em>
        13.01.10 - Электромонтер по ремонту и обслуживания электро - оборудования
        15.01.05 - Сварщик (ручной и частично механизированной сварки (наплавки)
        08.01.27 - Мастер общестроительных работ
<em>Адаптированные образовательные программы профессионального обучения:</em>
        12680 - Каменщик:<u>1 год 10 месяцев</u>
<b>ЗАОЧНОЕ ОТДЕЛЕНИЕ</b>
    <em>На базе основного общего образования (9 класс):</em>
        Программы подготовки специалистов среднего звена
                '22.02.08 - Металлургическое производство (по видам производства):<u>4 года 10 месяцев</u> 
            <em>На базе среднего общего образования (11 кл.):</em>
            Программы подготовки специалистов среднего звена : Отсуствуе'''

text_5 = "Вы можете скачать приложение или перейти на web-сайт"

text_6 = '''ПОЛОЖЕНИЕ О РАСХОДОВАНИИ СРЕДСТВ СТИПЕНДИАЛЬНОГО ФОНДА НА МАТЕРИАЛЬНУЮ ПОДДЕРЖКУ И ОРГАНИЗАЦИЮ КУЛЬТУРНО-МАССОВОЙ, СПОРТИВНОЙ, ФИЗКУЛЬТУРНООЗДОРОВИТЕЛЬНОЙ РАБОТЫ В КОГПОАУ «ОМУТНИНСКИЙ ПОЛИТЕХНИЧЕСКИЙ ТЕХНИКУМ»
1. Кировское областное государственное профессиональное образовательное
автономное учреждение «Омутнинский политехнический техникум» (далее -
Техникум) с учётом мнения обучающихся в пределах стипендиального фонда
вправе самостоятельно назначать материальные выплаты обучающимся в виде
единовременной материальной поддержки при соответствии деятельности
обучающегося одному или нескольким критериям:
- ставшим победителем и (или) призёром внутритехникумовских, городских,
областных, региональных, всероссийских и международных олимпиад; творческих
конкурсов; конкурсов профессионального мастерства и иных аналогичных
мероприятий - до 1 000 рублей за каждое мероприятие;
- ставшим победителем и (или) призёром внутритехникумовских, городских,
областных, региональных, всероссийских и международных спортивных
соревнований - до 1 000 рублей за каждое мероприятие;
- получившему награды (призы, дипломы, грамоты, сертификаты) за
результаты научно-исследовательской работы - до 1 000 рублей за каждое
мероприятие;
- участвовавшему в конкурсах, мастер-классах, олимпиадах, смотрах,
спортивных мероприятиях, концертах и других мероприятиях - до 500 рублей за
каждое мероприятие;
- участвовавшему в культурно-массовых, спортивных, физкультурнооздоровительных, военно-патриотических и профессиональноориентационных
мероприятиях - до 1 000 рублей за каждое мероприятие.
2. Стипендиальная комиссия с учётом мнения обучающихся, вправе оказать
единовременную материальную помощь обучающимся, находящимся в трудной
жизненной ситуации, а также:
- в связи с рождением ребёнка;
- семейным обучающимся;
- обучающимся из многодетных семей;
- обучающимся, имеющим родителей-инвалидов;
- обучающимся - донорам;
- обучающимся - старостам;
- обучающимся из малообеспеченных семей;
- в связи с операцией, несчастным случаем;
- обучающимся из неполных семей;
- обучающимся - инвалидам;
- беженцам из зоны военных конфликтов;
- обучающимся, относящимся к категории детей-сирот и детей, оставшихся без
попечения родителей, лиц из числа детей-сирот и детей, оставшихся без попечения
родителей.
Основанием для получения единовременной материальной поддержки и
единовременной материальной помощи является наличие документов,
подтверждающих наличие призовых мест, личное заявление с ходатайством
мастера производственного обучения или классного руководителя, справка из
соответствующих органов (больниц, полиции, администрации города, органов
социальной защиты населения и другое).
3. Техникум вправе финансировать культурно-массовые, спортивные,
физкультурно-оздоровительные мероприятия за счёт средств стипендиального
фонда.
К культурно-массовым, спортивным, физкультурно-оздоровительным
мероприятиям для обучающихся, финансирование которых осуществляется за счёт
3
стипендиального фонда, относятся:
- экскурсионные поездки;
- посещение музеев, выставок, кинотеатров, театров и другое;
- участие обучающихся в конкурсах, олимпиадах, соревнованиях, ярмарках,
форумах, конференциях, КВНе и другое;
Расходование средств для культурно-массовых, спортивных, физкультурнооздоровительных, военно-патриотических и профессионально-ориентационных
мероприятий предполагает оплату на:
- приобретение (изготовление) кубков, призов, грамот, дипломов,
сертификатов, медалей, ценных подарков, сувенирной продукции;
- аренда автобуса, проездные документы, суточные обучающимся,
направляемым на участие в конкурсах, чемпионатах, соревнованиях за пределы
города, области;
- питание и проживание во время проведения региональных и всероссийских
мероприятий;
- приобретение оборудования и материалов:
- проведение культурно-массовых мероприятий (конференций, круглых столов
с работодателями, концертов – приобретение экрана, проектора, ноутбука,
видеокамеры, фотоаппарата, усилителя звука, колонок акустических, микрофонов,
пультов, комплектов звукового оборудования, комплектов светового оборудования,
принтера, МФУ и другое);
- обеспечение культурно-массовых мероприятий необходимым реквизитом
(ткань для пошива костюмов и эмблем, танцевальная обувь, оформление зала);
- приобретение спортивного инвентаря и оборудования (платформа для
отжимания, перекладина навесная, маты гимнастические, мячи футбольные и
волейбольные, мячи баскетбольные, сетки для волейбола, ракетки теннисные,
теннисные столы, сетка для настольного тенниса, теннисные мячики, тренажёры,
футбольные ворота, настольные игры, лыжи, лыжные палки, лыжные ботинки и
другое);
- обеспечение физкультурно-оздоровительных мероприятий необходимым
реквизитом (форма спортивная, гетры футбольные, наколенники волейбольные,
футболки, бейсболки, табло и другое);
- приобретение билетов на посещение обучающимися экскурсий, театров,
музеев, киносеансов, концертов, КВНа и другое;
услуги по предоставлению инвентаря и оборудования для стрельб
- награждение участников соревнований денежными призами; аренда катка,
бассейна, стадиона или других спортивных сооружений;
- организационные взносы для участия обучающихся в конкурсах, чемпионатах,
соревнованиях различного уровня; другие расходы.
Решение о финансировании культурно-массовых, спортивных, физкультурнооздоровительных мероприятий для обучающихся принимает стипендиальная
комиссия на основании ходатайства, сметы расходов, нормативно-методических
документов, представляемых ответственным за проведение мероприятия в
соответствующие сроки.
Расходование средств стипендиального фонда осуществляется приказом
директора Техникума по представлению стипендиальной комиссии.'''

photo = ('indev_project/боты/bot_photo/5377475324801053223.jpg',)