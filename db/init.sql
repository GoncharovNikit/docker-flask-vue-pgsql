CREATE TABLE IF NOT EXISTS users (
    id SERIAL PRIMARY KEY,
    email VARCHAR(128) NOT NULL UNIQUE,
    password VARCHAR(128) NOT NULL,
    is_admin BOOLEAN NOT NULL DEFAULT(FALSE)
);

INSERT INTO users(email, password, is_admin) VALUES
('admin@gmail.com', sha256('admin123'), TRUE),
('admin100@gmail.com', sha256('admin123'), TRUE)
ON CONFLICT(email) DO NOTHING;