from fastapi import FastAPI, HTTPException
from fastmcp import FastMCP

app = FastAPI(title="Calculator API")

@app.post("/multiply")
def multiply_numbers(a: float, b: float):
    """Multiply two numbers and return the result."""
    return {"result": a * b}

@app.post("/add")
def add_numbers(a: float, b: float):
    """Add two numbers and return the result."""
    return {"result": a + b}

@app.post("/subtract")
def subtract_numbers(a: float, b: float):
    """Subtract b from a and return the result."""
    return {"result": a - b}

@app.post("/divide")
def divide_numbers(a: float, b: float):
    """Divide a by b and return the result."""
    if b == 0:
        raise HTTPException(status_code=400, detail="Cannot divide by zero.")
    return {"result": a / b}

mcp = FastMCP.from_fastapi(app=app, name="Calculator MCP")

if __name__ == "__main__":
    mcp.run(transport="http", host="localhost", port=8002)