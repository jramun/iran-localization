from model import Province, County, Area, Village, LittleVillage


class Repository:
    def __init__(self, session):
        self.session = session

    def addProvince(self, province) -> Province:
        object = self.session.query(Province).filter_by(local_id=province.local_id).first()
        if object is None:
            self.session.add(province)
            return province
        else:
            return object

    def addCounty(self, county) -> County:
        object = self.session.query(County).filter_by(local_id=county.local_id).first()
        if object is None:
            self.session.add(county)
            return county
        else:
            return object

    def addArea(self, area) -> Area:
        object = self.session.query(Area).filter_by(local_id=area.local_id).first()
        if object is None:
            self.session.add(area)
            return area
        else:
            return object

    def addVillage(self, village) -> Village:
        object = self.session.query(Village).filter_by(local_id=village.local_id).first()
        if object is None:
            self.session.add(village)
            return village
        else:
            return object

    def addLittleVillage(self, littleVillage) -> LittleVillage:
        object = self.session.query(LittleVillage).filter_by(local_id=littleVillage.local_id).first()
        if object is None:
            self.session.add(littleVillage)
            return littleVillage
        else:
            return object
