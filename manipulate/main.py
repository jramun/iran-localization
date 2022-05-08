import pandas
from sqlalchemy.orm import Session

import model
from model import Province, County, Area, Village, LittleVillage
from repository import Repository

# region keys
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
# endregion
repository = None
engine = None


def handler():
    data = pandas.read_excel('data/GEO99.xlsx', sheet_name=sheet,
                             usecols=[k_name, k_p_local_id, k_p_name, k_co_local_id, k_co_name, k_a_local_id, k_a_name,
                                      k_v_local_id, k_v_name, k_lv_local_id, k_lv_diag, k_code_rec])
    dic = data.to_dict(orient='records')
    counter = 0
    for item in dic:
        counter += 1
        if is_little_village(item) is True:
            print(counter, 'Little village ', item)
            addLittleVillage(item)
            continue
        if is_village(item) is True:
            print(counter, 'Village ', item)
            addVillage(item)
            continue
        if is_area(item) is True:
            print(counter, 'Area ', item)
            addArea(item)
            continue
        if is_county(item) is True:
            print(counter, 'County ', item)
            addCounty(item)
            continue
        if is_province(item) is True:
            print(counter, 'Province ', item)
            addProvince(item)
            continue
    return dic


def addLittleVillage(item) -> LittleVillage:
    repository = Repository(engine)
    province = Province(name=item[k_p_name],
                        local_id=str(item[k_p_local_id]))
    province = repository.addProvince(province)
    county = County(name=item[k_co_name],
                    local_id=str(item[k_co_local_id]))
    county.province = province
    county = repository.addCounty(county)
    area = Area(name=item[k_a_name],
                local_id=str(item[k_a_local_id]))
    area.county = county
    area = repository.addArea(area)
    village = Village(name=item[k_v_name],
                      local_id=str(item[k_v_local_id]))
    village.area = area
    village = repository.addVillage(village)
    littleVillage = LittleVillage(name=item[k_name],
                                  local_id=str(item[k_lv_local_id]),
                                  code_rec=item[k_code_rec],
                                  diag=item[k_lv_diag])
    littleVillage.village = village
    littleVillage = repository.updateLittleVillage(littleVillage)
    return littleVillage


def addVillage(item) -> Village:
    repository = Repository(engine)
    province = Province(name=item[k_p_name],
                        local_id=str(item[k_p_local_id]))
    province = repository.addProvince(province)
    county = County(name=item[k_co_name],
                    local_id=str(item[k_co_local_id]))
    county.province = province
    county = repository.addCounty(county)
    area = Area(name=item[k_a_name],
                local_id=str(item[k_a_local_id]))
    area.county = county
    area = repository.addArea(area)
    village = Village(name=item[k_name],
                      local_id=str(item[k_v_local_id]),
                      code_rec=item[k_code_rec])
    village.area = area
    village = repository.updateVillage(village)
    return village


def addArea(item) -> Area:
    repository = Repository(engine)
    province = Province(name=item[k_p_name],
                        local_id=str(item[k_p_local_id]))
    province = repository.addProvince(province)
    county = County(name=item[k_co_name],
                    local_id=str(item[k_co_local_id]))
    county.province = province
    county = repository.addCounty(county)
    area = Area(name=item[k_name],
                local_id=str(item[k_a_local_id]),
                code_rec=item[k_code_rec])
    area.county = county
    area = repository.updateArea(area)
    return area


def addCounty(item) -> County:
    repository = Repository(engine)
    province = Province(name=item[k_p_name],
                        local_id=str(item[k_p_local_id]))
    province = repository.addProvince(province)
    county = County(name=item[k_name],
                    local_id=str(item[k_co_local_id]),
                    code_rec=item[k_code_rec])
    county.province = province
    county = repository.updateCounty(county)
    return county


def addProvince(item) -> Province:
    repository = Repository(engine)
    province = Province(name=item[k_name],
                        local_id=str(item[k_p_local_id]),
                        code_rec=item[k_code_rec])
    province = repository.updateProvince(province)
    return province


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

    engine = model.engine()
    values = handler()
