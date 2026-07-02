-- Landing table for ingested CSV rows, before any transform/metrics are applied.
CREATE TABLE IF NOT EXISTS raw_events (
    event_time TIMESTAMP,
    user_id BIGINT,
    event_name VARCHAR,
    category VARCHAR,
    amount DOUBLE
);
