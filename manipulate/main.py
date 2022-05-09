import pandas
from sqlalchemy.orm import Session

import model
from model import Province, County, Region, Village, LittleVillage
from repository import Repository

# region keys
k_p_local_id = "OSTAN"
k_p_name = "نام استان"
k_co_local_id = "SHAHRESTAN"
k_co_name = "نام شهرستان"
k_r_local_id = "BAKHSH"
k_r_name = "نام بخش"
k_v_local_id = "SHRDEH"
k_v_name = "نام دهستان"
k_lv_local_id = "BLKABD"
k_code_rec = "CODEREC"
k_lv_diag = "DIAG"
k_name = "NAME"
sheet = 'فایل تقسیمات کشوری 99'
# endregion
repository = None
engine = None
littleVillages = {}
villages = {}
areas = {}
counties = {}
provinces = {}


def handler():
    data = pandas.read_excel('data/GEO99.xlsx', sheet_name=sheet,
                             usecols=[k_name, k_p_local_id, k_p_name, k_co_local_id, k_co_name, k_r_local_id, k_r_name,
                                      k_v_local_id, k_v_name, k_lv_local_id, k_lv_diag, k_code_rec])
    dic = data.to_dict(orient='records')
    for item in dic:
        if isLittleVillage(item) is True:
            addLittleVillage(item)
            continue
        if isVillage(item) is True:
            addVillage(item)
            continue
        if isRegion(item) is True:
            addRegion(item)
            continue
        if isCounty(item) is True:
            addCounty(item)
            continue
        if isProvince(item) is True:
            addProvince(item)
            continue
    for key in provinces:
        print(provinces[key])
        insertProvince(provinces[key])
    for key in counties:
        insertCounty(counties[key])
    for key in areas:
        insertRegion(areas[key])
    for key in villages:
        insertVillage(villages[key])
    for key in littleVillages:
        insertLittleVillage(littleVillages[key])

    return dic


# region add to dictionary


def addProvince(item) -> Province:
    province = Province(name=item[k_name],
                        local_id=str(item[k_p_local_id]),
                        code_rec=item[k_code_rec])
    province.key = province.local_id
    provinces[province.key] = province
    return province


def addCounty(item) -> County:
    county = County(name=item[k_name],
                    local_id=str(item[k_co_local_id]),
                    province_local_id=str(item[k_p_local_id]),
                    code_rec=item[k_code_rec])
    county.key = county.province_local_id + "-" + county.local_id
    counties[county.key] = county
    return county


def addRegion(item) -> Region:
    area = Region(name=item[k_name],
                  local_id=str(item[k_r_local_id]),
                  county_local_id=str(item[k_co_local_id]),
                  province_local_id=str(item[k_p_local_id]),
                  code_rec=item[k_code_rec])
    area.key = area.province_local_id + "-" + area.county_local_id + "-" + area.local_id
    areas[area.key] = area
    return area


def addVillage(item) -> Village:
    village = Village(name=item[k_name],
                      local_id=str(item[k_v_local_id]),
                      region_local_id=str(item[k_r_local_id]),
                      county_local_id=str(item[k_co_local_id]),
                      province_local_id=str(item[k_p_local_id]),
                      code_rec=item[k_code_rec])
    village.key = village.province_local_id + "-" + village.county_local_id + "-" + village.region_local_id + "-" + village.local_id
    villages[village.key] = village
    return village


def addLittleVillage(item) -> LittleVillage:
    littleVillage = LittleVillage(name=item[k_name],
                                  local_id=str(item[k_lv_local_id]),
                                  diag=str(item[k_lv_diag]),
                                  village_local_id=str(item[k_v_local_id]),
                                  region_local_id=str(item[k_r_local_id]),
                                  county_local_id=str(item[k_co_local_id]),
                                  province_local_id=str(item[k_p_local_id]),
                                  code_rec=item[k_code_rec])
    littleVillage.key = littleVillage.province_local_id + "-" + littleVillage.county_local_id + "-" + littleVillage.region_local_id + "-" + littleVillage.village_local_id + "-" + littleVillage.local_id
    littleVillages[littleVillage.key] = littleVillage
    return littleVillage


# endregion

# region insert orm

def insertProvince(province) -> Province:
    repository = Repository(engine)
    province = repository.addProvince(province)
    return province


def insertCounty(county) -> County:
    repository = Repository(engine)
    key = county.province_local_id
    p = repository.findProvince(key)
    county.province = p
    county = repository.addCounty(county)
    return county


def insertRegion(region) -> Region:
    repository = Repository(engine)
    key = region.province_local_id + "-" + region.county_local_id
    c = repository.findCounty(key)
    region.county = c
    region = repository.addRegion(region)
    return region


def insertVillage(village) -> Village:
    repository = Repository(engine)
    key = village.province_local_id + "-" + village.county_local_id + "-" + village.region_local_id
    a = repository.findRegion(key)
    village.region = a
    village = repository.addVillage(village)
    return village


def insertLittleVillage(littleVillage) -> LittleVillage:
    repository = Repository(engine)
    key = littleVillage.province_local_id + "-" + littleVillage.county_local_id + "-" + littleVillage.region_local_id + "-" + littleVillage.village_local_id
    v = repository.findVillage(key)
    littleVillage.village = v
    littleVillage = repository.addLittleVillage(littleVillage)
    return littleVillage


# endregion

# region validation
def isLittleVillage(item):
    if str(item[k_lv_local_id]).isspace():
        return False
    return True


def isVillage(item):
    if str(item[k_v_local_id]).isspace():
        return False
    return True


def isRegion(item):
    if str(item[k_r_local_id]).isspace():
        return False
    return True


def isCounty(item):
    if str(item[k_co_local_id]).isspace():
        return False
    return True


def isProvince(item):
    if str(item[k_p_local_id]).isspace():
        return False
    return True


# endregion


if __name__ == '__main__':
    engine = model.engine()
    values = handler()
