-- SQL Script to add the 'departments' table to the 'companydb' database

CREATE TABLE IF NOT EXISTS departments (
    department_id INT AUTO_INCREMENT PRIMARY KEY,  -- Unique identifier for each department
    department_name VARCHAR(255) NOT NULL,         -- Name of the department (cannot be NULL)
    location VARCHAR(255)                         -- Location of the department (optional)
);

-- Optional: Insert some sample data (if needed)
INSERT INTO departments (department_name, location)
VALUES
    ('HR', 'New York'),
    ('Engineering', 'San Francisco'),
    ('Marketing', 'Chicago');
