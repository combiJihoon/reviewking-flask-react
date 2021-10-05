import csv
from app import create_app
from app import db
from models import Categories, Restaurants, Reviews, TotalRating

app = create_app()
app.app_context().push()


def categories():
    if Categories.query.first() is None:
        with app.app_context():
            with open(
                f"./dataset/restaurant_categories.csv", "r", encoding="utf8"
            ) as data:
                reader = csv.DictReader(data, delimiter=",")
                categories = set([lines["category"] for lines in reader])
            categories = list(categories)
            for category in categories:
                category_data = Categories(category=category)
                db.session.add(category_data)
                db.session.commit()
            db.create_all(app=app)


# 음식점과 위치, 업종, 데이터 넣기
def restaurants():
    if Restaurants.query.first() is None:
        with app.app_context():
            with open(
                f"./dataset/restaurant_categories.csv", "r", encoding="utf8"
            ) as data:
                reader = csv.DictReader(data, delimiter="|")
                for lines in reader:
                    name = lines["name"]
                    latitude_x = lines["lat"]
                    longitude_y = lines["lon"]
                    category = lines["category"]
                    img_url = lines["img_url"]

                    category_id = (
                        Categories.query.filter_by(category=category).first().id
                    )

                    restaurant = Restaurants(
                        name=name,
                        longitude_x=longitude_x,
                        latitude_y=latitude_y,
                        img_url=img_url,
                        category_id=category_id,
                    )

                    db.session.add(restaurant)
                    db.session.commit()
            db.create_all(app=app)


# 플랫폼별 크롤링한 리뷰 넣기
def reviews():
    if Reviews.query.first() is None:
        with app.app_context():
            with open(f"./dataset/reviews.csv", "r", encoding="utf8") as data:
                reader = csv.DictReader(data, delimiter="|")
                for lines in reader:
                    name = lines["name"]
                    platform = lines["platform"]
                    date = lines["date"].replace(".", "-")
                    rating = float(lines["rating"])
                    content = lines["content"]

                    restaurant = Restaurants.query.filter_by(name=name).first()
                    if restaurant:
                        restaurant_id = restaurant.id

                        reviews = Reviews(
                            platform=platform,
                            name=name,
                            date=date,
                            rating=rating,
                            content=content,
                            restaurant_id=restaurant_id,
                        )
                        db.session.add(reviews)
                        db.session.commit()
            db.create_all(app=app)


# 플랫폼별 총 평점 넣기
def total_rating():
    if TotalRating.query.first() is None:
        with app.app_context():
            with open(f"./dataset/total_rating.csv", "r", encoding="utf8") as data:
                reader = csv.DictReader(data, delimiter="|")
                for lines in reader:
                    name = lines["name"]
                    naver = lines["naver"]
                    kakao = lines["kakao"]
                    mango = lines["mango"]
                    siksin = lines["siksin"]

                    integrated_rating_list = [naver, kakao, mango, siksin]
                    arr = [
                        rating
                        for rating in integrated_rating_list
                        if rating is not None
                    ]
                    integrated_rating = sum(arr)

                    restaurant_id = Restaurants.query.filter_by(name=name).first().id
                    total_rating = TotalRating(
                        naver=naver,
                        kakao=kakao,
                        mango=mango,
                        sikshin=sikshin,
                        integrated_rating=integrated_rating,
                        restaurant_id=restaurant_id,
                    )

                    db.session.add(total_rating)
                    db.session.commit()
            db.create_all(app=app)


# 메뉴 데이터 넣기
def menus():
    if Menus.query.first() is None:
        with app.app_context():
            with open(f"./dataset/menus.csv", "r", encoding="utf8") as data:
                reader = csv.DictReader(data, delimiter="|")
                for lines in reader:
                    name = lines["name"]
                    properties = lines["properties"]

                    restaurant_id = Restaurants.query.filter_by(name=name).first().id
                    category_id = (
                        Restaurants.query.filter_by(restaurant_id=restaurant_id)
                        .first()
                        .id
                    )

                    menu = Menus(
                        name=name,
                        properties=properties,
                        restaurant_id=restaurant_id,
                        category_id=category_id,
                    )

                    db.session.add(menu)
                    db.session.commit()
            db.create_all(app=app)


if __name__ == "__main__":
    categories()
    reviews()
    total_rating()
    menus()
