create table little_village
(
    id                serial
        primary key,
    name              varchar,
    key               varchar,
    local_id          varchar,
    village_local_id  varchar,
    region_local_id   varchar,
    county_local_id   varchar,
    province_local_id varchar,
    code_rec          varchar,
    diag              varchar,
    village_id        integer not null
        references village
);

alter table little_village
    owner to localization;

