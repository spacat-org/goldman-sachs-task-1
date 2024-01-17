CREATE TABLE loan_approval_status (
    id UUID PRIMARY KEY,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    name VARCHAR(255),
    status VARCHAR(20),
    type VARCHAR(50)
);