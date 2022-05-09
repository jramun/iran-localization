from sqlalchemy.orm import Session

from model import Province, County, Region, Village, LittleVillage


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

    def findProvince(self, key) -> Province:
        self.open()
        object = self.session.query(Province).filter_by(key=key).first()
        self.commit()
        return object

    def addProvince(self, province) -> Province:
        self.open()
        object = self.session.query(Province).filter_by(key=province.key).first()
        if object is None:
            self.session.add(province)
            result = province
        else:
            result = object
        self.commit()
        return result

    def findCounty(self, key) -> County:
        self.open()
        object = self.session.query(County).filter_by(key=key).first()
        self.commit()
        return object

    def addCounty(self, county) -> County:
        self.open()
        object = self.session.query(County).filter_by(key=county.key).first()
        if object is None:
            self.session.add(county)
            result = county
        else:
            result = object
        self.commit()
        return result

    def findRegion(self, key) -> Region:
        self.open()
        object = self.session.query(Region).filter_by(key=key).first()
        self.commit()
        return object

    def addRegion(self, region) -> Region:
        self.open()
        object = self.session.query(Region).filter_by(key=region.key).first()
        if object is None:
            self.session.add(region)
            result = region
        else:
            result = object
        self.commit()
        return result

    def addVillage(self, village) -> Village:
        self.open()
        object = self.session.query(Village).filter_by(key=village.key).first()
        if object is None:
            self.session.add(village)
            result = village
        else:
            result = object
        self.commit()
        return result

    def findVillage(self, key) -> Village:
        self.open()
        object = self.session.query(Village).filter_by(key=key).first()
        self.commit()
        return object

    def addLittleVillage(self, littleVillage) -> LittleVillage:
        self.open()
        object = self.session.query(LittleVillage).filter_by(key=littleVillage.key).first()
        if object is None:
            self.session.add(littleVillage)
            result = littleVillage
        else:
            result = object
        self.commit()
        return result

    def findLittleVillage(self, key) -> LittleVillage:
        self.open()
        object = self.session.query(LittleVillage).filter_by(key=key).first()
        self.commit()
        return object
