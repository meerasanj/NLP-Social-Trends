import pandas as pd


def loadDataset(path: str):
    #TODO: Implement loading csv
    # Load dataset
    # Remove unwanted columns?
    pass

def combineColumns(df: pd.DataFrame, processedDF: pd.DataFrame, rawCols: list, processedCols: list):
    #TODO: Implement combining columns
    # Combine selected columns from raw + processed data
    pass

def insertModelOutputs(dframe: pd.DataFrame, sentiments, confidence, topics):
    #TODO: Implement model output insertion
    #Insert model outputs into the dataframe
    pass

def exportProcessedData(df: pd.DataFrame, outputPath="placeholder"):
    #TODO: Implement export
    # Save final processed data to a finished csv
    # To then be loaded by GUI files
    pass

