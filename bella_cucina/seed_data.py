from app import app, db, User, Dish, Order, OrderItem, Booking
from datetime import datetime, timedelta


def seed_database():
    with app.app_context():
        db.drop_all()
        db.create_all()

        # Тестові користувачі
        user1 = User(username='ivan_petrenko', email='ivan@example.com')
        user1.set_password('password123')
        db.session.add(user1)

        user2 = User(username='olena_kovalenko', email='olena@example.com')
        user2.set_password('password123')
        db.session.add(user2)

        # Страви меню
        dishes = [
            Dish(
                name='Брускета аль Помодоро',
                description='Підсмажений хліб зі свіжими помідорами, часником, базиліком та оливковою олією',
                price=12.99,
                category='appetizers',
                image_url='https://images.unsplash.com/photo-1572695157366-5e585ab2b69f?w=600&q=80'
            ),
            Dish(
                name='Кальмарі Фрітті',
                description='Хрусткі кільця кальмара у фритюрі з лимоном та соусом марінара',
                price=14.99,
                category='appetizers',
                image_url='https://images.unsplash.com/photo-1599487488170-d11ec9c172f0?w=600&q=80'
            ),
            Dish(
                name='Спагеті Карбонара',
                description='Класична римська паста з яйцями, панчетою та сиром Пекоріно Романо',
                price=16.99,
                category='main',
                image_url='https://images.unsplash.com/photo-1612874742237-6526221588e3?w=600&q=80'
            ),
            Dish(
                name='Лазанья Болоньєзе',
                description='Шари пасти з м\'ясним соусом болоньєзе та ніжним бешамелем',
                price=18.99,
                category='main',
                image_url='https://images.unsplash.com/photo-1574894709920-11b28e7367e3?w=600&q=80'
            ),
            Dish(
                name='Оссо Буко',
                description='Тушковані телячі голяшки з овочами та білим вином по-міланськи',
                price=28.99,
                category='main',
                image_url='https://images.unsplash.com/photo-1544025162-d76694265947?w=600&q=80'
            ),
            Dish(
                name='Різото з грибами',
                description='Вершкове різото з лісовими грибами та трюфельною олією',
                price=19.99,
                category='main',
                image_url='https://images.unsplash.com/photo-1476124369491-e7addf5db371?w=600&q=80'
            ),
            Dish(
                name='Тірамісу',
                description='Класичний італійський десерт із маскарпоне, просочений еспресо та лікером',
                price=8.99,
                category='desserts',
                image_url='https://images.unsplash.com/photo-1571877227200-a0d98ea607e9?w=600&q=80'
            ),
            Dish(
                name='Панна Котта',
                description='Ніжний ванільний вершковий крем із соусом із лісових ягід',
                price=7.99,
                category='desserts',
                image_url='https://images.unsplash.com/photo-1488477181946-6428a0291777?w=600&q=80'
            ),
            Dish(
                name='Еспресо',
                description='Міцна італійська кава з насиченим ароматом та оксамитовою пінкою',
                price=3.99,
                category='drinks',
                image_url='https://images.unsplash.com/photo-1510591509098-f4fdc6d0ff04?w=600&q=80'
            ),
            Dish(
                name='Просекко',
                description='Італійське ігристе вино з делікатними фруктовими нотками',
                price=9.99,
                category='drinks',
                image_url='https://images.unsplash.com/photo-1558618666-fcd25c85cd64?w=600&q=80'
            ),
        ]
        db.session.add_all(dishes)
        db.session.commit()

        # Тестове замовлення: 2x Карбонара (16.99) + 1x Тірамісу (8.99) = 42.97
        order1 = Order(user_id=user1.id, total_price=42.97, status='confirmed')
        db.session.add(order1)
        db.session.flush()

        item1 = OrderItem(order_id=order1.id, dish_id=dishes[2].id, quantity=2, price=16.99)
        item2 = OrderItem(order_id=order1.id, dish_id=dishes[6].id, quantity=1, price=8.99)
        db.session.add_all([item1, item2])

        # Тестове бронювання
        booking1 = Booking(
            user_id=user2.id,
            booking_date=datetime.utcnow() + timedelta(days=7),
            guests=4,
            status='confirmed',
            notes='Бажано столик біля вікна'
        )
        db.session.add(booking1)

        db.session.commit()
        print('База даних успішно заповнена!')


if __name__ == '__main__':
    seed_database()