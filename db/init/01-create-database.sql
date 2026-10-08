-- Runs once via the db-init service. Idempotent.
IF DB_ID(N'$(DB_NAME)') IS NULL
BEGIN
    CREATE DATABASE [$(DB_NAME)];
END
GO
USE [$(DB_NAME)];
GO
PRINT 'Database $(DB_NAME) ready.';
