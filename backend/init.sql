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
