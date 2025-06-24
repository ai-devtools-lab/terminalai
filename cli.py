import typer
import openai
import os

cli = typer.Typer()
openai.api_key = os.getenv("OPENAI_API_KEY")

@cli.command()
def run(prompt: str):
    """Generate a shell command from a natural language prompt."""
    query = f"Translate the following instruction into a shell command:\n\n{prompt}"
    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[{"role": "user", "content": query}],
        temperature=0.2,
        max_tokens=100
    )
    command = response.choices[0].message.content.strip()
    typer.echo(f"\n💡 Suggested Command:\n{command}")

if __name__ == "__main__":
    cli()
