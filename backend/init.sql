-- init.sql
ALTER TABLE app_quiz_customuser ADD COLUMN username VARCHAR(150);
ALTER TABLE app_quiz_customuser ADD COLUMN first_name VARCHAR(30);
ALTER TABLE app_quiz_customuser ADD COLUMN last_name VARCHAR(150);
ALTER TABLE app_quiz_customuser ADD COLUMN date_joined TIMESTAMP WITH TIME ZONE DEFAULT NOW();
ALTER TABLE app_quiz_customuser ALTER COLUMN created_at DROP NOT NULL;
