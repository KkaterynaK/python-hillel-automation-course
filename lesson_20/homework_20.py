-- Створення таблиць
CREATE TABLE categories (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL
);
CREATE TABLE products (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    description TEXT,
    price REAL NOT NULL,
    category_id INTEGER,
    FOREIGN KEY (category_id) REFERENCES categories (id)
);


-- Наповнення таблиць даними
INSERT INTO categories (name) VALUES
    ('Ноутбуки'),
    ('Смартфони'),
    ('Аксесуари');
INSERT INTO products (name, description, price, category_id) VALUES
    ('MacBook Air', 'Ноутбук Apple 13"', 42000, 1),
    ('Lenovo ThinkPad', 'Робочий ноутбук', 35000, 1),
    ('iPhone 15', 'Смартфон Apple', 48000, 2),
    ('Samsung Galaxy S24', 'Смартфон Samsung', 39000, 2),
    ('Навушники JBL', 'Бездротові навушники', 2500, 3),
    ('Чохол для телефону', 'Силіконовий чохол', 300, 3);

    
-- JOIN-запит: продукти та назви їх категорій
SELECT products.name, products.price, categories.name AS category
FROM products
JOIN categories ON products.category_id = categories.id;


-- Результат JOIN-запиту:
-- name                price    category
-- ------------------  -------  ---------
-- MacBook Air         42000.0  Ноутбуки
-- Lenovo ThinkPad     35000.0  Ноутбуки
-- iPhone 15           48000.0  Смартфони
-- Samsung Galaxy S24  39000.0  Смартфони
-- Навушники JBL       2500.0   Аксесуари
-- Чохол для телефону  300.0    Аксесуари
