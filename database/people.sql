CREATE EXTENSION IF NOT EXISTS "uuid-ossp";

CREATE TABLE IF NOT EXISTS people (
    uid UUID NOT NULL DEFAULT uuid_generate_v4(),
    active BOOLEAN NOT NULL DEFAULT true,
    first_name VARCHAR(250) NOT NULL,
    middle_name VARCHAR(250),
    last_name VARCHAR(250) NOT NULL,
    personal_email VARCHAR(250),
    cuny_email VARCHAR(250),
    preferred_email VARCHAR(4) CHECK (preferred_email IN ('cuny', 'personal')), -- to indicate preference explicitly
    discord VARCHAR(250),
    emplid VARCHAR(250) NOT NULL,
    PRIMARY KEY (uid)
