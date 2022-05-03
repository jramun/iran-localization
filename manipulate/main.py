import pandas

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


def read():
    sheet = 'فایل تقسیمات کشوری 99'
    data = pandas.read_excel('data/GEO99.xlsx', sheet_name=sheet,
                             usecols=[k_name, k_p_local_id, k_p_name, k_co_local_id, k_co_name, k_a_local_id, k_a_name,
                                      k_v_local_id, k_v_name, k_lv_local_id, k_lv_diag])
    dic = data.to_dict(orient='records')
    # for item in dic:

    return dic


def is_little_village(item):
    if item[k_lv_local_id].isspace():
        return False
    return True


def is_village(item):
    if item[k_v_local_id].isspace():
        return False
    return True


def is_area(item):
    if item[k_a_local_id].isspace():
        return False
    return True


def is_county(item):
    if item[k_co_local_id].isspace():
        return False
    return True


def is_province(item):
    if item[k_p_local_id].isspace():
        return False
    return True


if __name__ == '__main__':
    values = read()


class Province:
    def __init__(self, id, local_id, name, code_rec):
        self.id = id
        self.local_id = local_id
        self.name = name
        self.code_rec = code_rec


class County:
    def __init__(self, id, local_id, name, code_rec, province_id):
        self.id = id
        self.local_id = local_id
        self.name = name
        self.code_rec = code_rec
        self.province_id = province_id


class Area:
    def __init__(self, id, local_id, name, code_rec, county_id):
        self.id = id
        self.local_id = local_id
        self.name = name
        self.code_rec = code_rec
        self.county_id = county_id


class Village:
    def __init__(self, id, local_id, name, code_rec, area_id):
        self.id = id
        self.local_id = local_id
        self.name = name
        self.area_id = area_id
        self.code_rec = code_rec


class LittleVillage:
    def __init__(self, id, local_id, name, code_rec, village_id):
        self.id = id
        self.local_id = local_id
        self.name = name
        self.village_id = village_id
        self.code_rec = code_rec
