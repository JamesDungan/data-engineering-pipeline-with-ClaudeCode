CREATE TABLE IF NOT EXISTS raw_events (
    event_time TIMESTAMP,
    user_id BIGINT,
    event_name VARCHAR,
    category VARCHAR,
    amount DOUBLE
);
