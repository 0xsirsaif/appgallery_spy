import typer

from appgallery_spy.crawl import crawl as appgallery_crawl

app = typer.Typer()


@app.command()
def crawl(app_id: str, limit: int = 3):
    typer.echo("Crawling the appgallery..")
    appgallery_crawl(app_id, scroll_limit=limit)


if __name__ == "__main__":
    app()
