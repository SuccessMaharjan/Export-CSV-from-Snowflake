-- models/create_snowflake_db_and_schema.sql

{% set database_name = var('database_name') %}
{% set schema_name = var('schema_name') %}

-- Create database if it doesn't exist
create database if not exists {{ database_name }};

-- Create schema if not exists
create schema if not exists {{ database_name }}.{{ schema_name }};
