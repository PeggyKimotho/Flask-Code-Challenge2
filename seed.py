from random import choice as rc
from app import app, db
from models import Hero, Power, HeroPower

# Define your data
powers_data = [
    {"name": "super strength", "description": "gives the wielder super-human strengths"},
    {"name": "flight", "description": "gives the wielder the ability to fly through the skies at supersonic speed"},
    # Add more powers here
]

heroes_data = [
    {"name": "Kamala Khan", "super_name": "Ms. Marvel"},
    {"name": "Doreen Green", "super_name": "Squirrel Girl"},
    {"name": "Gwen Stacy", "super_name": "Spider-Gwen"},
    {"name": "Janet Van Dyne", "super_name": "The Wasp"},
    {"name": "Wanda Maximoff", "super_name": "Scarlet Witch"},
    {"name": "Carol Danvers", "super_name": "Captain Marvel"},
    {"name": "Jean Grey", "super_name": "Dark Phoenix"},
    {"name": "Ororo Munroe", "super_name": "Storm"},
    {"name": "Kitty Pryde", "super_name": "Shadowcat"},
    {"name": "Elektra Natchios", "super_name": "Elektra"}
]

strengths = ["Strong", "Weak", "Average"]

def seed_data():
    with app.app_context():
        try:
            # Deleting existing data
            HeroPower.query.delete()
            Power.query.delete()
            Hero.query.delete()

            # Seeding powers
            for power_info in powers_data:
                power = Power(**power_info)
                db.session.add(power)

            db.session.commit()
            print("🦸‍♀️ Seeded powers...")

            # Seeding heroes
            for hero_info in heroes_data:
                hero = Hero(**hero_info)
                db.session.add(hero)

            db.session.commit()
            print("🦸‍♀️ Seeded heroes...")

            # Adding powers to heroes
            all_heroes = Hero.query.all()
            all_powers = Power.query.all()

            for hero in all_heroes:
                for _ in range(rc([1, 2, 3])):
                    power = rc(all_powers)
                    strength = rc(strengths)
                    hero_power = HeroPower(hero=hero, power=power, strength=strength)
                    db.session.add(hero_power)

            db.session.commit()
            print("🦸‍♀️ Added powers to heroes...")
        
        except Exception as e:
            print(f"An error occurred: {str(e)}")
            db.session.rollback()
        
        finally:
            db.session.close()

if __name__ == '__main__':
    seed_data()
    print("🦸‍♀️ Done seeding!")
