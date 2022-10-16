GENDERS = {
    ('', '----'),
    ('m', 'Мужской'),
    ('f', 'Женский'),
}
GROUPS = {
    ('a', 'Админ'),
    ('d', 'Доктор'),
    ('p', 'Пациент'),
}
SOCIAL_STATUS = {
    ('l', 'Низший'),
    ('m', 'Средний'),
    ('h', 'Высший'),
}
DISABILITY = {
    ('1', 'Первая'),
    ('2', 'Вторая'),
    ('3', 'Третья'),
}
BLOOD = {
    ('1', 'O(I)'),
    ('2', 'A(II)'),
    ('3', 'B(III)'),
    ('4', 'AB(IV)'),
}

RH = {
    ('+', '+'),
    ('-', '-'),
}

PREGNANCY_OUTCOME = {
    ('b', 'Роды'),      # birth
    ('a', 'Аборт'),     # abortion
    ('d', 'Смерть'),    # death
}

CHILDBIRTH = {
    ('swc', 'Самопроизвольным - без осложнений'),   # spanteniouslly without complications
    ('sc', 'Самопроизвольным - с осложнениями'),    # spanteniouslly (with) complications
    ('ocs', 'Оперативным - кесарево сечение'),      # operative C-section
}

ABORTION = {
    ('s', 'Самопроизвольный'),  # spanteniously
    ('a', 'Искусственный'),     # artiffical
}

VISIT = {
    ('1', 'Первая явка'),
    ('11-14', 'Явка на 11-14 неделе'),
    ('18-20', 'Явка на 18-20 неделе'),
    ('30-40', 'Явка на 30-40 неделе'),
}

FETUS_STIRRING = {
    ('+', 'Ощущается'),
    ('-', 'Не ощущается'),
}

FETAL_POSITION = {
    ('прод', 'Продольное'),
    ('кос', 'Косое'),
    ('попер', 'Попереченое'),
}

PELVIS_ENTRANCE = {
    ('гол', 'Головка'),
    ('тк', 'Тазовый конец'),
    ('др', 'Другое'),
}

ADJACENT_PART = {
    ('приж', 'Прижата'),
    ('под', 'Подвижна'),
}

RISK_LEVEL = {
    ('0', 'Низкий'),
    ('1', 'Высокий')
}

REGISTERED = {
    ('0', 'Не состояла'),
    ('1', 'Состояла')
}

IS_POSITIVE = {
    ('0', 'Отрицательный'),
    ('1', 'Положительный'),
}

SMOKING = {
    ('', '----'),
    ('<1/2', 'Меньше 1/2 пачки'),
    ('1/2-1', 'От 1/2 до 1 пачки'),
    ('1>', 'Больше 1 пачки'),
}

ALCOHOL = {
    ('', '----'),
    ('1', 'Каждый день'),
    ('1-2w', '1-2 раза в неделю'),
    ('1-2m', '1-2 раза в месяц'),
}

PROFUSION = {
    ('1', 'Скудные'),
    ('2', 'Умеренные'),
    ('3', 'Обильные'),
}

PAINFULNESS = {
    ('0', 'Безболезненные'),
    ('1', 'Болезненные'),
}

REGULARITY = {
    ('0', 'Нерегулярные'),
    ('1', 'Регулярные'),
}

BAD_HABITS = {
    ('', '----'),
    ('s', 'Курение'),
    ('a', 'Алкоголь'),
    ('d', 'Наркотики'),
}

PREGNANCY = {
    ('', ''),
    ('1', 'Первая'),
    ('2', 'Повторная'),
    ('3', 'Наступила спонтанно'),
    ('4', 'Индуцирована с помощью ВРТ'),
}

PREGNANCY_1 = {
    ('', ''),
    ('1', 'Одноплодность'),
    ('2', 'Многоплодность'),
}

EMBRYO = {
    ('', ''),
    ('1', 'Нативного'),
    ('2', 'Криоконсервированного'),
}

UPCOMING_BIRTH = {
    ('', ''),
    ('1', 'Первые'),
    ('2', 'Повторные'),
}

FAT_SEVERITY = {
    ('', ''),
    ('1', 'По женскому типу'),
    ('2', 'По мужскому типу'),
    ('3', 'Недостаточно выражена'),
    ('4', 'Нормально выражена'),
    ('5', 'Избыточно выражена'),
}

MAMMARY = {
    ('', ''),
    ('1', 'Патологических изменений нет'),
    ('2', 'Пальпируется узловое образование'),
    ('3', 'Безболезненны '),
    ('4', 'Масталгия'),
}

NIPPLES = {
    ('', ''),
    ('1', 'Сформированы правильно'),
    ('2', 'Втянуты'),
}

CERVIX = {
    ('', ''),
    ('1', 'Плотная'),
    ('2', 'Размягченная'),
    ('3', 'Мягкая'),
}

CERVIX_DEVIATIONS = {
    ('', ''),
    ('1', 'Кзади'),
    ('2', 'Кпереди'),
    ('3', 'Расположена по центру'),
}

PHARYNX = {
    ('', ''),
    ('1', 'Сомкнут'),
    ('1', 'Пропускает кончик пальца'),
    ('1', 'Пропускает палец'),
}

UTERUS = {
    ('', ''),
    ('1', 'Подвижное'),
    ('2', 'Безболезненное'),
    ('3', 'Болезненное'),
}

APPENDAGES = {
    ('', ''),
    ('1', 'Без особенностей'),
    ('2', 'Есть особенности'),
}

UTERINE_PULSE = {
    ('', ''),
    ('1', 'Правая'),
    ('2', 'Левая'),
}

HIGH_LOW = {
    ('', ''),
    ('0', 'Низкий'),
    ('1', 'Высокий'),
}

AMNIOTIC_FLUID = {
    ('', ''),
    ('0', 'Норма'),
    ('1', 'Маловодие'),
    ('2', 'Многоводие'),
}

PRESENTATION = {
    ('', ''),
    ('0', 'Головное'),
    ('1', 'Тазовое'),
}

INSURANCE = {
    ('1', 'АО «Медицинская акционерная страховая компания» (АО «МАКС-М»)'),
    ('2', 'ООО «МСК «МЕДСТРАХ»»'),
    ('3', 'ООО «Страховая медицинская компания РЕСО-МЕД» (Московский филиал)'),
    ('4', 'АО «Страховая компания «СОГАЗ-Мед»»'),
    ('5', 'ООО «Страховая компания «Ингосстрах-М»'),
    ('6', 'ООО «КАПИТАЛ МС» ')
}
CITYVILLAGE = {
    ('', '----'),
    ('1', 'Город'),
    ('2', 'Село')
}
TERRITORY = {
    ('', '----'),
    ('Инзенский', 'Инзенский район'),
    ('Майнский', 'Майнский район'),
    ('Старокулаткинский', 'Старокулаткинский район'),
    ('Сурский', 'Сурский район'),
    ('Барышский', 'Барышский район'),
    ('Кузоватовский', 'Кузоватовский район'),
    ('Николаевский', 'Николаевский район'),
    ('Тереньгульский', 'Тереньгульский район'),
    ('Вешкаймский', 'Вешкаймский район'),
    ('Карсунский', 'Карсунский район'),
    ('Новомалыклинский', 'Новомалыклинский район'),
    ('Новоспасский', 'Новоспасский район'),
    ('Радищевский', 'Радищевский район'),
    ('Сенгилеевский', 'Сенгилеевский район'),
    ('Базарносызганский', 'Базарносызганский район'),
    ('Павловский', 'Павловский район'),
    ('Цильнинский', 'Цильнинский район'),
    ('Мелекесский', 'Мелекесский район'),
    ('Старомайнский', 'Старомайнский район'),
    ('Ульяновский', 'Ульяновский район'),
    ('Чердаклинский', 'Чердаклинский район ')
}
class CHANGETYPE:
    Добавлена_история_болезни: str = 'Добавлена история болезни'
    Изменена_личная_информация: str = 'Изменена личная информация'
    Был_отвязан_от_доктора: str = 'Был отвязан от доктора'
    Был_привязан_к_доктору: str = 'Был привязан к доктору'
    Добавлена_запись_в_журнал_самонаблюдения: str = 'Добавлена запись в журнал самонаблюдения'
    Пользователь_был_удален: str = 'Пользователь был удален'
    Пользователь_был_создан: str = 'Пользователь был создан'

MEDICAL_ORGANIZATION = (
    ('', '----'),
    ('1', 'Болька 1'),
    ('2', 'Болька 2'),
    ('3', 'Болька 3'),
)

ROLES = {
    ('акушер-гинеколог', 'акушер-гинеколог'),
    ('терапевт ', 'терапевт'),
    ('стоматолог', 'стоматолог'),
    ('офтальмолог', 'офтальмолог'),
    ('специалист', 'специалист'),
    ('педиатор', 'педиатор')
}

MARITAL_STATUS = {
    ('', '----'),
    ('1', 'Никогда не состояла в браке'),
    ('2', 'Состоит в зарегистрированном браке'),
    ('3', 'Состоит в незарегистрированном браке'),
    ('4', 'Вдова' ),
    ('5', 'Разведена' ),
    ('6', 'Разошлась' ),
}
