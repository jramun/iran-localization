create table village
(
    id                serial
        primary key,
    name              varchar,
    key               varchar,
    local_id          varchar,
    region_local_id   varchar,
    county_local_id   varchar,
    province_local_id varchar,
    code_rec          varchar,
    region_id         integer not null
        references region
);

alter table village
    owner to localization;

