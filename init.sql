CREATE DATABASE IF NOT EXISTS `demo-site-django`;
CREATE USER IF NOT EXISTS 'service_user'@'%' IDENTIFIED BY 'password123';
GRANT ALL PRIVILEGES ON `demo-site-django`.* TO 'service_user'@'%';
FLUSH PRIVILEGES;
