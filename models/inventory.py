from datetime import datetime
import decimal
import uuid
from imports import db

class InventoryItem(db.Model):
    id = db.Column(db.Integer(), primary_key=True, autoincrement=True)
    name = db.Column(db.String(100))
    category = db.Column(db.String(100))
    price = db.Column(db.Float)
    last_updated_dt = db.Column(db.DateTime, default=datetime.now())
    
    def save(self):
        db.session.add(self)
        db.session.commit()

    def to_dict(self):
        return {
            'id': self.id,
            'name': self.name,
            'category': self.category,
            'price': self.price,
            'last_updated_dt': self.last_updated_dt.strftime('%Y-%m-%d %H:%M:%S') 
        }
    
    @classmethod
    def update_inventory_log(cls, name, category, price, last_updated_dt):
        db.session.query(cls).filter(
            cls.name==name).update(dict(category=category, price=price, last_updated_dt=last_updated_dt))
        db.session.commit() 

    @classmethod
    def find_by_name(cls, name: str) -> "InventoryItem":
        return cls.query.filter_by(name=name).first()
    
    @classmethod
    def insert_inventory_log(cls, name, category, price):
        new_item = cls(name=name, category=category, price=decimal.Decimal(price))
        new_item.save()
        return new_item
    
    @classmethod
    def get_inventory_in_date_range(cls, dt_from, dt_to):
        return cls.query.filter(
            cls.last_updated_dt >= dt_from,
            cls.last_updated_dt <= dt_to
        ).all()
    
    @classmethod
    def aggregate_by_category(cls, category):
        if category != 'all':
            query = db.session.query(
                cls.category,
                db.func.sum(cls.price).label('total_price'),
                db.func.count(cls.id).label('count')
            ).filter(cls.category == category)
        else:
            query = db.session.query(
                cls.category,
                db.func.sum(cls.price).label('total_price'),
                db.func.count(cls.id).label('count')
            )

        return query.group_by(cls.category).all()