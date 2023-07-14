import typer
from appgallery_spy.crawl import crawl

app = typer.Typer()


@app.command()
def crawl(app_id: str):
    typer.echo("Crawling the appgallery..")
    crawl(app_id)


if __name__ == "__main__":
    app()