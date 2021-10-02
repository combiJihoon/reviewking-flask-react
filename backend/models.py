from app import db


class Restaurants(db.Model):
    __tablename__ = "restaurants"

    id = db.Column(db.Integer, nullable=False, primary_key=True, autoincrement=True)
    name = db.Column(db.String(100), nullable=True)
    res_type = db.Column(db.String(50), nullable=True)
    integrated_rating = db.Column(db.Float, nullable=True)
    longitude_x = db.Column(db.String(100), nullable=True)  # 정확한 값이 필요하므로 String으로 저장
    latitude_y = db.Column(db.String(100), nullable=True)  # 정확한 값이 필요하므로 String으로 저장
    category_id = db.Column(db.Integer, db.ForeignKey("categories.id"), nullable=False)

    categories = db.relationship("Categories", backref=db.backref("restaurants_set"))


class Reviews(db.Model):
    __tablename__ = "reviews"

    id = db.Column(db.Integer, nullable=False, primary_key=True, autoincrement=True)
    name = db.Column(db.String(100), nullable=True)
    date = db.Column(db.DateTime, nullable=True)
    rating = db.Column(db.Float, nullable=True)
    content = db.Column(db.Text(), nullable=True)
    platform = db.Column(db.String(30), nullable=False)
    restaurant_id = db.Column(
        db.Integer, db.ForeignKey("restaurants.id", ondelete="CASCADE"), nullable=False
    )

    restaurants = db.relationship("Restaurants", backref=db.backref("reviews_set"))


class Menus(db.Model):
    __tablename__ = "menus"

    id = db.Column(db.Integer, nullable=False, primary_key=True, autoincrement=True)
    name = db.Column(db.String(100), nullable=False)
    img_path = db.Column(db.String(200), nullable=True)
    category_id = db.Column(db.Integer, db.ForeignKey("categories.id"), nullable=False)
    restaurant_id = db.Column(
        db.Integer, db.ForeignKey("restaurants.id", ondelete="CASCADE"), nullable=False
    )

    restaurants = db.relationship("Restaurants", backref=db.backref("menus_set"))
    categories = db.relationship("Categories", backref=db.backref("menus_set"))


class Analysis(db.Model):
    __tablename__ = "analysis"

    id = db.Column(db.Integer(), nullable=False, primary_key=True, autoincrement=True)
    filename = db.Column(db.String(200), nullable=True)
    platform = db.Column(db.String(30), nullable=False)

    restaurant_id = db.Column(
        db.Integer, db.ForeignKey("restaurants.id", ondelete="CASCADE"), nullable=False
    )

    restaurants = db.relationship("Restaurants", backref=db.backref("analysis_set"))


class TotalRating(db.Model):
    __tablename__ = "total_rating"

    id = db.Column(db.Integer(), nullable=False, primary_key=True, autoincrement=True)
    kakao = db.Column(db.Float, nullable=True)
    naver = db.Column(db.Float, nullable=True)
    sikshin = db.Column(db.Float, nullable=True)
    mango = db.Column(db.Float, nullable=True)

    restaurant_id = db.Column(
        db.Integer, db.ForeignKey("restaurants.id", ondelete="CASCADE"), nullable=False
    )

    restaurants = db.relationship("Restaurants", backref=db.backref("total_rating_set"))


class Categories(db.Model):
    __tablename__ = "categories"

    id = db.Column(db.Integer(), nullable=False, primary_key=True, autoincrement=True)
    category = db.Column(db.String(100), nullable=True)


class Users(db.Model):
    __tablename__ = "users"

    id = db.Column(db.Integer(), nullable=False, primary_key=True, autoincrement=True)
    email = db.Column(db.String(150), nullable=False)
    password = db.Column(db.String(150), nullable=False)
    name = db.Column(db.String(30), nullable=False)

    def __init__(self, email, password, name):
        self.email = email
        self.password = password
        self.name = name
