CREATE UNLOGGED TABLE IF NOT EXISTS "quotes" (
    "id" SERIAL PRIMARY KEY,
    "author" VARCHAR(100) NULL,
    "quote" VARCHAR(1024) NOT NULL
);

DELETE FROM "quotes";

INSERT INTO "quotes" ("quote", "author")
VALUES 
    ('Do or do not. There is no try.', 'Yoda'),
    ('It''s okay to have a bad day', NULL),
    ('If you''re going through hell, keep going.', 'Winston Churchill');
