-- Добавить столбец username, если он не существует
DO $$
BEGIN
    IF NOT EXISTS (SELECT 1 FROM information_schema.columns WHERE table_name='app_quiz_customuser' AND column_name='username') THEN
        ALTER TABLE app_quiz_customuser ADD COLUMN username VARCHAR(150);
    END IF;
END $$;

-- Добавить столбец first_name, если он не существует
DO $$
BEGIN
    IF NOT EXISTS (SELECT 1 FROM information_schema.columns WHERE table_name='app_quiz_customuser' AND column_name='first_name') THEN
        ALTER TABLE app_quiz_customuser ADD COLUMN first_name VARCHAR(30);
    END IF;
END $$;

-- Добавить столбец last_name, если он не существует
DO $$
BEGIN
    IF NOT EXISTS (SELECT 1 FROM information_schema.columns WHERE table_name='app_quiz_customuser' AND column_name='last_name') THEN
        ALTER TABLE app_quiz_customuser ADD COLUMN last_name VARCHAR(150);
    END IF;
END $$;

-- Добавить столбец date_joined, если он не существует
DO $$
BEGIN
    IF NOT EXISTS (SELECT 1 FROM information_schema.columns WHERE table_name='app_quiz_customuser' AND column_name='date_joined') THEN
        ALTER TABLE app_quiz_customuser ADD COLUMN date_joined TIMESTAMP WITH TIME ZONE DEFAULT NOW();
    END IF;
END $$;

-- Изменить столбец created_at, если он существует
DO $$
BEGIN
    IF EXISTS (SELECT 1 FROM information_schema.columns WHERE table_name='app_quiz_customuser' AND column_name='created_at') THEN
        ALTER TABLE app_quiz_customuser ALTER COLUMN created_at DROP NOT NULL;
    END IF;
END $$;

TRUNCATE TABLE app_quiz_roomparticipant RESTART IDENTITY CASCADE;


TRUNCATE TABLE app_quiz_question RESTART IDENTITY CASCADE;

INSERT INTO app_quiz_question (text, options, correct_answer, answer_time, theme, created_at)
VALUES
    -- Вопросы про спорт
    ('Какой спортсмен выиграл наибольшее количество олимпийских медалей?', 'Майкл Фелпс,Усейн Болт,Лариса Латынина,Карл Льюис', 'Майкл Фелпс', 10, 'Спорт', NOW()),
    ('Кто является лучшим бомбардиром чемпионатов мира по футболу?', 'Пеле,Роналдо,Мираслав Клозе,Лионель Месси', 'Мираслав Клозе', 15, 'Спорт', NOW()),
    ('В каком году были проведены первые зимние Олимпийские игры?', '1924,1932,1948,1952', '1924', 10, 'Спорт', NOW()),
    ('Какая страна выиграла чемпионат мира по футболу 2018 года?', 'Бразилия,Франция,Германия,Аргентина', 'Франция', 10, 'Спорт', NOW()),
    
    -- Вопросы про историю
    ('Кто был первым президентом США?', 'Авраам Линкольн,Джордж Вашингтон,Томас Джефферсон,Бенжамин Франклин', 'Джордж Вашингтон', 15, 'История', NOW()),
    ('Когда была подписана Декларация независимости США?', '1776,1789,1799,1804', '1776', 15, 'История', NOW()),
    ('Какая страна была центром Римской империи?', 'Греция,Турция,Италия,Франция', 'Италия', 15, 'История', NOW()),
    ('Кто был последним фараоном Древнего Египта?', 'Рамсес II,Клеопатра,Тутанхамон,Ахмес I', 'Клеопатра', 15, 'История', NOW());
