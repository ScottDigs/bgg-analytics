# Board Game Geeks Analytics Project
Sample project for fun using BGG review data from [Kaggle's BoardGameGeek Reviews](https://www.kaggle.com/datasets/jvanelteren/boardgamegeek-reviews)


# Setup

## Get Kaggle Data
Run the following bash command to setup the local data directories:
```bash
mkdir .data .data/ingest .data/ingest/game_info .data/ingest/games .data/ingest/reviews
```

Download the Kaggle data from [BoardGameGeek Reviews](https://www.kaggle.com/datasets/jvanelteren/boardgamegeek-reviews). At the time of this project, there is a `games_detailed_info.csv` file, which should be moved to `.data/ingest/game_info`. There are two game files `2020-08-19.csv` and `2022-01-08.csv` which need to be moved to `data/ingest/games`. There are two review files `bgg-15m-reviews.csv` and `bgg-19m-reviews.csv` which need to be moved to `.data/ingest/reviews`.


## Python
Run the following:
```bash
pip install -r requirements.txt
```

## Spark Container

In the project directory, run the following:
```bash
docker-compose up --build -d
```

Note, if updating Python `requirements.txt` after building, then...
stop the container:
```bash
docker-compose down
```

rebuild the container:
```bash
docker-compose build
```
Restart the container:
```bash
docker-compose up -d
```