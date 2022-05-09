create table province
(
    id       serial
        primary key,
    name     varchar,
    key      varchar,
    local_id varchar,
    code_rec varchar
);

alter table province
    owner to localization;

