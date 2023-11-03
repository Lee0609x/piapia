CREATE TABLE app_user (
	id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
	name TEXT NOT NULL,
	username TEXT NOT NULL,
	userpass TEXT NOT NULL
);
INSERT INTO app_user (name, username, userpass) VALUES ('管理员', 'admin', 'admin');