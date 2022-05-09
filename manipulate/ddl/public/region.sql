create table region
(
    id                serial
        primary key,
    name              varchar,
    key               varchar,
    local_id          varchar,
    county_local_id   varchar,
    province_local_id varchar,
    code_rec          varchar,
    county_id         integer not null
        references county
);

alter table region
    owner to localization;

