CREATE TABLE IF NOT EXISTS people (
    uid UUID NOT NULL DEFAULT PRIMARY KEY uuid_generate_v4(),
    active boolean NOT NULL DEFAULT true,
    first_name VARCHAR(250) NOT NULL ,
    middle_name VARCHAR(250) ,
    last_name VARCHAR(250) NOT NULL,
    personal_email VARCHAR(250) ,
    cuny_email VARCHAR(250),
    preferred_email boolean, /* boolean to indicate personal or cuny email contact preferrence */
    discord VARCHAR(250),
    emplid VARCHAR(250) NOT NULL
)