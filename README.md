#### Invoice Agent Graph

<p>
This is a simple invoice agent that uses LangGraph to extract information from invoices and save it to a database.
</p>

### Setup
`uv init invoice_agent_graph`

### Add required libraries
`uv add fastapi sqlalchemy alembic pydantic pydantic-settings langchain langchain-community langchain-openai langchain-langgraph pypdf`
`uv sync`

### initialize albemic
`uv run alembic init alembic`

### create albemic versions
`uv run alembic revision --autogenerate -m "create_invoice_records_table"`
<p> This reads from the src/invoice_agent_graph/db/invoice_record.py</p>

### Migrate database
<p>First Create version </p>
`uv run alembic revision --autogenerate -m "create invoice_records table"`

<p>Now Migrate</p>
`uv run alembic upgrade head`