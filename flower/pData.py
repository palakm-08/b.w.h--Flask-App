from flower import app, db
from flower.models import products

items = [
    products(p_name='Lily', price=30, image='images/lily.jpg', desc='Elegant white bloom'),
    products(p_name='Sunflower', price=100, image='images/sunflower.jpg', desc='Bright summer delight'),
    products(p_name='Rose', price=20, image='images/rose.jpg', desc='Classic romantic flower'),
    products(p_name='Daisy', price=50, image='images/daisy.jpg', desc='Simple cheerful bloom'),
    products(p_name='Tulip', price=100, image='images/tulip.jpg', desc='Elegant springtime bloom'),
    products(p_name='Iris', price=50, image='images/iris.jpg', desc='Graceful flower with rich symbolism'),
    products(p_name='Freesia', price=80, image='images/freesia.jpg', desc='Sweet-scented delicate flower'),
    products(p_name='Peony', price=200, image='images/peony.jpg', desc='Lush and luxurious blossom'),
    products(p_name='Gerbera', price=75, image='images/gerbera.jpg', desc='Bright and cheerful daisy flower'),
    products(p_name='Orchid', price=100, image='images/orchid.jpg', desc='Exotic and sophisticated bloom'),
    products(p_name='Carnation', price=200, image='images/carnation.jpg', desc='Long-lasting ruffled flower'),
    products(p_name='Lavender', price=40, image='images/lavender.jpg', desc='Fragrant calming purple flower'),
    products(p_name='Chrysanthemum', price=100, image='images/chrysanthemum.jpg', desc='Classic full-bodied flower'),
    products(p_name='Plumeria', price=50, image='images/plumeria.jpg', desc='Soft tropical fragrant bloom'),
    products(p_name='Hibiscus', price=508, image='images/hibiscus.jpg', desc='Tropical bold vibrant flower')
]

with app.app_context():
    db.session.add_all(items)
    db.session.commit()
