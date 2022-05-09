create table county
(
    id                serial
        primary key,
    name              varchar,
    key               varchar,
    local_id          varchar,
    province_local_id varchar,
    code_rec          varchar,
    province_id       integer not null
        references province
);

alter table county
    owner to localization;

