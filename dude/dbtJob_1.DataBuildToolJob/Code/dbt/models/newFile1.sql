{{
  config(
    materialized='table'
  )
}}

-- Example: use ref() to select from an upstream model
-- select * from {{ ref('upstream_model') }}

select 'Hello, World!' as greeting