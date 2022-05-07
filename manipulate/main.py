import pandas
from sqlalchemy.orm import Session

import model
from model import Province, County, Area, Village, LittleVillage
from repository import Repository

k_p_local_id = "OSTAN"
k_p_name = "نام استان"
k_co_local_id = "SHAHRESTAN"
k_co_name = "نام شهرستان"
k_a_local_id = "BAKHSH"
k_a_name = "نام بخش"
k_v_local_id = "SHRDEH"
k_v_name = "نام دهستان"
k_lv_local_id = "BLKABD"
k_code_rec = "CODEREC"
k_lv_diag = "DIAG"
k_name = "NAME"
sheet = 'فایل تقسیمات کشوری 99'
session = None
repository = None


def handler():
    data = pandas.read_excel('data/GEO99.xlsx', sheet_name=sheet,
                             usecols=[k_name, k_p_local_id, k_p_name, k_co_local_id, k_co_name, k_a_local_id, k_a_name,
                                      k_v_local_id, k_v_name, k_lv_local_id, k_lv_diag, k_code_rec])
    dic = data.to_dict(orient='records')
    for item in dic:
        if is_little_village(item) is True:
            addLittleVillage(item)
            continue
        if is_village(item) is True:
            addVillage(item)
            continue
        if is_area(item) is True:
            addArea(item)
            continue
        if is_county(item) is True:
            addCounty(item)
            continue
        if is_province(item) is True:
            addProvince(item)
            continue

    session.commit()
    session.flush()
    session.close()
    return dic


def addLittleVillage(item) -> LittleVillage:
    province = getProvince(item)
    province = repository.addProvince(province)
    county = getCounty(item)
    county.province = province
    county = repository.addCounty(county)
    area = getArea(item)
    area.county = county
    area = repository.addArea(area)
    village = getVillage(item)
    village.area = area
    village = repository.addVillage(village)
    littleVillage = getLittleVillage(item)
    littleVillage.village = village
    littleVillage = repository.addLittleVillage(littleVillage)
    return littleVillage


def addVillage(item) -> Village:
    province = getProvince(item)
    province = repository.addProvince(province)
    county = getCounty(item)
    county.province = province
    county = repository.addCounty(county)
    area = getArea(item)
    area.county = county
    area = repository.addArea(area)
    village = getVillage(item)
    village.area = area
    village = repository.addVillage(village)
    return village


def addArea(item) -> Area:
    province = getProvince(item)
    province = repository.addProvince(province)
    county = getCounty(item)
    county.province = province
    county = repository.addCounty(county)
    area = getArea(item)
    area.county = county
    area = repository.addArea(area)
    return area


def addCounty(item) -> County:
    province = getProvince(item)
    province = repository.addProvince(province)
    county = getCounty(item)
    county.province = province
    county = repository.addCounty(county)
    return county


def addProvince(item) -> Province:
    province = getProvince(item)
    province = repository.addProvince(province)
    return province


# region make model

def getProvince(item) -> Province:
    return Province(name=item[k_p_name],
                    local_id=str(item[k_p_local_id]),
                    code_rec=item[k_code_rec])


def getCounty(item) -> County:
    return County(name=item[k_co_name],
                  local_id=str(item[k_co_local_id]),
                  code_rec=item[k_code_rec])


def getArea(item) -> Area:
    return Area(name=item[k_a_name],
                local_id=str(item[k_a_local_id]),
                code_rec=item[k_code_rec])


def getVillage(item) -> Village:
    return Village(name=item[k_v_name],
                   local_id=str(item[k_v_local_id]),
                   code_rec=item[k_code_rec])


def getLittleVillage(item) -> LittleVillage:
    return LittleVillage(name=item[k_name],
                         local_id=str(item[k_lv_local_id]),
                         diag=item[k_lv_diag],
                         code_rec=item[k_code_rec])


# endregion

# region validation
def is_little_village(item):
    if str(item[k_lv_local_id]).isspace():
        return False
    return True


def is_village(item):
    if str(item[k_v_local_id]).isspace():
        return False
    return True


def is_area(item):
    if str(item[k_a_local_id]).isspace():
        return False
    return True


def is_county(item):
    if str(item[k_co_local_id]).isspace():
        return False
    return True


def is_province(item):
    if str(item[k_p_local_id]).isspace():
        return False
    return True


# endregion


if __name__ == '__main__':
    session = Session(model.engine())
    repository = Repository(session)
    values = handler()
