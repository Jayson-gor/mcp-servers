from fastmcp import FastMCP

mcp = FastMCP(name="Calculator")

@mcp.tool()
def multiply(a: float, b: float) -> float:
    """Multiply two numbers."""
    return a * b

@mcp.tool(
    name="add",
    description="Add two numbers.",
    tags={"math", "arithmetic"},
)
def add_numbers(x: float, y: float) -> float:
    return x + y

@mcp.tool()
def subtract(a: float, b: float) -> float:
    """Subtract b from a."""
    return a - b

@mcp.tool()
def divide(a: float, b: float) -> float:
    """Divide a by b."""
    if b == 0:
        raise ValueError("Cannot divide by zero.")
    return a / b

if __name__ == "__main__":
    mcp.run()  # STDIO by default