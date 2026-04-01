def greet(name: str) -> str:
    """Generate a greeting message.
    
    Args:
        name: The name of the person to greet
        
    Returns:
        A greeting message
    """
    return f"Hello, {name}!"

def main() -> None:
    """Main entry point for the hello program."""
    print(greet("World"))

if __name__ == "__main__":
    main()
