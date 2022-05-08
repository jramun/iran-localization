from sqlalchemy.orm import Session

from model import Province, County, Area, Village, LittleVillage


def replaceProvince(source, target):
    source.name = target.name
    source.code_rec = target.code_rec
    return source


def replaceCounty(source, target):
    source.name = target.name
    source.code_rec = target.code_rec
    return source


def replaceArea(source, target):
    source.name = target.name
    source.code_rec = target.code_rec
    return source


def replaceVillage(source, target):
    source.name = target.name
    source.code_rec = target.code_rec
    return source


def replaceLittleVillage(source, target):
    source.name = target.name
    source.code_rec = target.code_rec
    source.diag = target.diag
    return source


class Repository:
    def __init__(self, engine):
        self.session = None
        self.engine = engine

    def open(self):
        self.session = Session(self.engine)

    def commit(self):
        self.session.commit()
        self.session.flush()
        self.session.close()

    def findProvince(self, localId) -> Province:
        self.open()
        object = self.session.query(Province).filter_by(local_id=localId).first()
        return object

    def addProvince(self, province) -> Province:
        self.open()
        object = self.session.query(Province).filter_by(local_id=province.local_id).first()
        if object is None:
            self.session.add(province)
            result = province
        else:
            result = object
        self.commit()
        return result

    def updateProvince(self, province) -> Province:
        self.open()
        object = self.session.query(Province).filter_by(local_id=province.local_id).first()
        if object is not None:
            result = self.session.add(replaceProvince(object, province))
        else:
            result = self.session.add(province)
        self.commit()
        return result

    def findCounty(self, localId) -> County:
        self.open()
        object = self.session.query(County).filter_by(local_id=localId).first()
        self.commit()
        return object

    def addCounty(self, county) -> County:
        self.open()
        object = self.session.query(County).filter_by(local_id=county.local_id).first()
        if object is None:
            self.session.add(county)
            result = county
        else:
            result = object
        self.commit()
        return result

    def updateCounty(self, county) -> County:
        self.open()
        object = self.session.query(County).filter_by(local_id=county.local_id).first()
        if object is not None:
            result = self.session.add(replaceCounty(object, county))
        else:
            result = self.session.add(county)
        self.commit()
        return result

    def findArea(self, localId) -> Area:
        self.open()
        object = self.session.query(Area).filter_by(local_id=localId).first()
        self.commit()
        return object

    def addArea(self, area) -> Area:
        self.open()
        object = self.session.query(Area).filter_by(local_id=area.local_id).first()
        if object is None:
            self.session.add(area)
            result = area
        else:
            result = object
        self.commit()
        return result

    def updateArea(self, area) -> Area:
        self.open()
        object = self.session.query(Area).filter_by(local_id=area.local_id).first()
        if object is not None:
            result = self.session.add(replaceArea(object, area))
        else:
            result = self.session.add(area)
        self.commit()
        return result

    def addVillage(self, village) -> Village:
        self.open()
        object = self.session.query(Village).filter_by(local_id=village.local_id).first()
        if object is None:
            self.session.add(village)
            result = village
        else:
            result = object
        self.commit()
        return result

    def findVillage(self, localId) -> Village:
        self.open()
        object = self.session.query(Village).filter_by(local_id=localId).first()
        self.commit()
        return object

    def updateVillage(self, village) -> Village:
        self.open()
        object = self.session.query(Village).filter_by(local_id=village.local_id).first()
        if object is not None:
            result = self.session.add(replaceVillage(object, village))
        else:
            result = self.session.add(village)
        self.commit()
        return result

    def addLittleVillage(self, littleVillage) -> LittleVillage:
        self.open()
        object = self.session.query(LittleVillage).filter_by(local_id=littleVillage.local_id).first()
        if object is None:
            self.session.add(littleVillage)
            result = littleVillage
        else:
            result = object
        self.commit()
        return result

    def updateLittleVillage(self, littleVillage) -> LittleVillage:
        self.open()
        object = self.session.query(LittleVillage).filter_by(local_id=littleVillage.local_id).first()
        if object is not None:
            result = self.session.add(replaceLittleVillage(object, littleVillage))
        else:
            result = self.session.add(littleVillage)
        self.commit()
        return result

    def findLittleVillage(self, localId) -> LittleVillage:
        self.open()
        object = self.session.query(LittleVillage).filter_by(local_id=localId).first()
        self.commit()
        return object
