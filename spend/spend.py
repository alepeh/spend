import click
import pandas
import os

@click.group()
def cli():
    pass

@cli.command()
def list():
    df = getDataFrame()
    print(df)

@cli.command()
@click.argument('datum')
@click.argument('bezeichnung')
@click.argument('betrag')
@click.argument('kategorie')
def add(datum, bezeichnung, betrag, kategorie):
    df = convertToDataframe(datum, bezeichnung, betrag, kategorie)
    save(df)
    print(df)

@cli.command()
def report():
    df = getDataFrame()
    df.groupby(df["Datum"].dt.month)['Betrag'].sum()
    print(df.groupby(df["Datum"].dt.month)['Betrag'].sum())



def convertToDataframe(datum, bezeichnung, betrag, kategorie) -> pandas.DataFrame:
    list_row = {"Datum": [datum], "Bezeichnung" : [bezeichnung], "Betrag" : [betrag], "Kategorie" : [kategorie]}
    df = pandas.DataFrame(data=list_row)
    return df


def read():
    return open(getPath(), "r", encoding="utf-8")


def getDataFrame() -> pandas.DataFrame:
    df = pandas.read_csv(read(), delimiter=";", parse_dates=['Datum'])
    convert_dict = {'Betrag': float}
    df = df.astype(convert_dict)
    return df


def save(df: pandas.DataFrame):
    df.to_csv(getPath(), index=False, sep=";", mode='a', header=not os.path.exists(getPath()))


def getPath():
    home = os.path.expanduser('~')
    return home + "/nas/drive/todotxt/spend.csv"

if __name__ == '__main__':
    cli()