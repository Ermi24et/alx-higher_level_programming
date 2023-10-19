-- a script that creates the table id_not_null on your MYSQL server

CRATE TABLE IF NOT EXISTS id_not_null(
	id INT DEFAULT 1,
	name VARCHAR(256)
);
