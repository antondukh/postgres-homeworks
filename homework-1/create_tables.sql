CREATE TABLE employees
(
	employee_id varchar(50) PRIMARY KEY NOT NULL,
	first_name varchar(50) NOT NULL,
	last_name varchar(50) NOT NULL,
	title varchar(50) NOT NULL,
	birth_date varchar(50) NOT NULL,
	notes text
);

CREATE TABLE customers
(
	customer_id varchar(50) PRIMARY KEY NOT NULL,
	company_name varchar(50) NOT NULL,
	contact_name varchar(50) NOT NULL
);

CREATE TABLE orders
(
	order_id varchar(50) PRIMARY KEY NOT NULL,
	customer_id varchar(50) NOT NULL,
	employee_id varchar(50) NOT NULL,
	order_date varchar(50) NOT NULL,
	ship_city varchar(50) NOT NULL
);