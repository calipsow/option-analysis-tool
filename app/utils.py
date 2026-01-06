import pathlib
import os
from datetime import datetime, timedelta
import time
# import curl_cffi
import yfinance as yf
import pandas as pd
import numpy as np

from typing import Optional, List, Any

# setup local cache.
cache_path = pathlib.Path(__file__).parent / 'cache'
if os.path.exists(cache_path) is False: cache_path.mkdir()
yf.set_tz_cache_location(str(cache_path))

outfile = "REPORT.md"
data_dir = pathlib.Path(__file__).parent / 'data'
data_dir.mkdir(exist_ok=True)

def log_print(*args: Any, sep: str = ' ', end: str = '\n', **kwargs) -> None:
    """
    Print wrapper that logs messages to data/REPORT.md and prints to console.
    
    Args:
        *args: Variable length argument list to print
        sep: String inserted between values, default is a space
        end: String appended after the last value, default is a newline
        **kwargs: Additional keyword arguments passed to print()
    """

    
    # Define the report file path
    report_file = data_dir / outfile
    
    # Convert all arguments to strings and join them
    message = sep.join(str(arg) for arg in args)
    
    # Append the message to the markdown file
    with open(report_file, 'a', encoding='utf-8') as f: f.write(message + '\n\n')
    
    # Print to console normally
    print(*args, sep=sep, end=end, **kwargs)

def get_log_print(out=outfile):
    global outfile
    outfile = out
    with open(data_dir / outfile, mode="w", encoding="utf-8") as o: o.write('')
    return log_print

def clean_stock_dataframe(
    df: pd.DataFrame, 
    ticker: Optional[str] = None,
    remove_repaired: bool = True,
    min_volume_threshold: int = 1000,
    price_columns: List[str] = ['Open', 'High', 'Low', 'Close'],
    fill_method: str = 'forward'
) -> pd.DataFrame:
    """
    Clean a multi-index stock DataFrame from yfinance.
    
    Args:
        df: DataFrame with MultiIndex columns (Price metrics, Ticker symbols)
        ticker: Specific ticker to extract (if None, uses first available ticker)
        remove_repaired: Whether to remove rows where 'Repaired?' is True
        min_volume_threshold: Minimum volume threshold (rows below this are removed)
        price_columns: List of price columns to validate
        fill_method: Method for filling missing values ('forward', 'backward', 'interpolate', 'drop')
    
    Returns:
        Cleaned DataFrame with single-level column index
        
    Raises:
        ValueError: If DataFrame structure is invalid or ticker not found
    """
    
    if df.empty:
        raise ValueError("DataFrame is empty")
    
    # Make a copy to avoid modifying original
    df_clean = df.copy()
    
    # Handle MultiIndex columns
    if isinstance(df_clean.columns, pd.MultiIndex):
        print("Detected MultiIndex columns, flattening...")
        
        # Get available tickers from second level
        available_tickers = df_clean.columns.get_level_values(1).unique().tolist()
        print(f"Available tickers: {available_tickers}")
        
        # Select ticker
        if ticker is None:
            ticker = available_tickers[0]
            print(f"No ticker specified, using: {ticker}")
        elif ticker not in available_tickers:
            raise ValueError(f"Ticker '{ticker}' not found. Available: {available_tickers}")
        
        # Extract single ticker data by selecting second level of MultiIndex
        df_clean = df_clean.xs(ticker, level=1, axis=1)
        print(f"Extracted data for ticker: {ticker}")
    
    # Ensure we have the expected columns
    expected_columns = price_columns + ['Volume']
    if remove_repaired and 'Repaired?' not in df_clean.columns:
        print("Warning: 'Repaired?' column not found, skipping repair filter")
        remove_repaired = False
    
    missing_columns = [col for col in expected_columns if col not in df_clean.columns]
    if missing_columns:
        print(f"Warning: Missing columns: {missing_columns}")
    
    print(f"DataFrame shape before cleaning: {df_clean.shape}")
    
    # 1. Remove repaired data if requested
    if remove_repaired and 'Repaired?' in df_clean.columns:
        initial_rows = len(df_clean)
        df_clean = df_clean[df_clean['Repaired?'] == False].copy()
        removed_repaired = initial_rows - len(df_clean)
        if removed_repaired > 0:
            print(f"Removed {removed_repaired} repaired rows")
        
        # Drop the Repaired? column after filtering
        df_clean = df_clean.drop('Repaired?', axis=1)
    
    # 2. Filter by volume threshold
    if 'Volume' in df_clean.columns:
        initial_rows = len(df_clean)
        df_clean = df_clean[df_clean['Volume'] >= min_volume_threshold].copy()
        removed_volume = initial_rows - len(df_clean)
        if removed_volume > 0:
            print(f"Removed {removed_volume} rows with volume < {min_volume_threshold}")
    
    # 3. Remove rows where all price columns are NaN or zero
    price_cols_present = [col for col in price_columns if col in df_clean.columns]
    if price_cols_present:
        initial_rows = len(df_clean)
        
        # Remove rows where all price columns are NaN
        df_clean = df_clean.dropna(subset=price_cols_present, how='all') # type: ignore
        
        # Remove rows where all price columns are zero
        price_zero_mask = (df_clean[price_cols_present] <= 0).all(axis=1)
        df_clean = df_clean[~price_zero_mask].copy()
        
        removed_invalid = initial_rows - len(df_clean)
        if removed_invalid > 0:
            print(f"Removed {removed_invalid} rows with invalid price data")
    
    # 4. Validate price relationships (High >= Low, etc.)
    if all(col in df_clean.columns for col in ['High', 'Low', 'Open', 'Close']):
        initial_rows = len(df_clean)
        
        # Remove rows where High < Low (impossible)
        invalid_high_low = df_clean['High'] < df_clean['Low']
        df_clean = df_clean[~invalid_high_low].copy()
        
        # Remove rows where prices are outside High-Low range
        invalid_open = (df_clean['Open'] > df_clean['High']) | (df_clean['Open'] < df_clean['Low'])
        invalid_close = (df_clean['Close'] > df_clean['High']) | (df_clean['Close'] < df_clean['Low'])
        
        df_clean = df_clean[~(invalid_open | invalid_close)].copy()
        
        removed_invalid_prices = initial_rows - len(df_clean)
        if removed_invalid_prices > 0:
            print(f"Removed {removed_invalid_prices} rows with invalid price relationships")
    
    # 5. Handle remaining missing values
    if df_clean.isnull().any().any():
        missing_count = df_clean.isnull().sum().sum() # type: ignore # ignore
        print(f"Handling {missing_count} missing values using method: {fill_method}")
        
        if fill_method == 'forward':
            df_clean = df_clean.fillna(method='ffill') # type: ignore # ignore
        elif fill_method == 'backward':
            df_clean = df_clean.fillna(method='bfill') # type: ignore # ignore
        elif fill_method == 'interpolate':
            # Only interpolate numeric columns
            numeric_cols = df_clean.select_dtypes(include=[np.number]).columns
            df_clean[numeric_cols] = df_clean[numeric_cols].interpolate()
        elif fill_method == 'drop':
            df_clean = df_clean.dropna()
        else:
            print(f"Unknown fill_method: {fill_method}, using forward fill")
            df_clean = df_clean.fillna(method='ffill') # type: ignore # ignore
    
    # 6. Remove any remaining rows with NaN values
    initial_rows = len(df_clean)
    df_clean = df_clean.dropna()
    removed_nan = initial_rows - len(df_clean)
    if removed_nan > 0:
        print(f"Removed {removed_nan} rows with remaining NaN values")
    
    # 7. Ensure data types are correct
    numeric_columns = ['Open', 'High', 'Low', 'Close', 'Volume']
    for col in numeric_columns:
        if col in df_clean.columns:
            df_clean[col] = pd.to_numeric(df_clean[col], errors='coerce')
    
    # 8. Sort by date index
    if isinstance(df_clean.index, pd.DatetimeIndex):
        df_clean = df_clean.sort_index()
    
    print(f"DataFrame shape after cleaning: {df_clean.shape}")
    print(f"Date range: {df_clean.index.min()} to {df_clean.index.max()}")
    
    # 9. Final validation summary
    if len(df_clean) == 0:
        raise ValueError("All data was removed during cleaning process")
    
    print("\nCleaning Summary:")
    print(f"- Final dataset: {len(df_clean)} rows")
    print(f"- Columns: {list(df_clean.columns)}")
    print(f"- Date range: {df_clean.index.min().date()} to {df_clean.index.max().date()}")
    
    if 'Volume' in df_clean.columns:
        print(f"- Average volume: {df_clean['Volume'].mean():,.0f}")
    
    return df_clean # type: ignore # ignore

def days_until(date_string: str) -> float:
    """
    Calculate total days from now to the given date.
    If the date is in the past, return 0.0.

    :param date_string: Date string in format YYYY-MM-DD
    :return: Number of days as float
    """
    try:
        # Parse the input date string
        target_date = datetime.strptime(date_string, "%Y-%m-%d")
    except ValueError:
        print(date_string)
        raise ValueError("Date string must be in format YYYY-MM-DD")

    now = datetime.now()

    # Calculate difference in days (float)
    delta_days = (target_date - now).total_seconds() / 86400.0  # seconds to days

    return delta_days if delta_days > 0 else 0.0

def get_future_date(days: int | float) -> datetime:
    """
    Calculate a future (or past) datetime based on the current datetime plus the given number of days.
    
    Args:
        days: Number of days to add to the current datetime (can be negative for past dates)
    
    Returns:
        datetime: The calculated datetime object
    """
    return datetime.now() + timedelta(days=days)

class StockTicker:
    def __init__(self, ticker: str):
        print(f'setup stock ticker instance for: {ticker}')
        self._ticker =  yf.Ticker(ticker=ticker)
        self._stock_options = None
        self._price_history = None
        self._earnings = None
    
    def get_price_history(self, start: str = "2020-01-01"):
        if self._price_history is not None: return self._price_history

        end_date = datetime.now().strftime("%Y-%m-%d")
        print(f'{self._ticker.ticker} prices from {start} - {end_date} 1 day interval')
        
        price_history = yf.download(self._ticker.ticker, start=start, end=end_date, interval="1d", repair=True)
        if price_history is None: raise Exception(f'no price history available for {self._ticker.ticker}')
        
        self._price_history = clean_stock_dataframe(price_history)
        return self._price_history
    
    def get_stock_options(self):
        if self._stock_options is not None: return self._stock_options
        print('loading stock options for: ', self._ticker.ticker)

        option_expiration_dates = self._ticker.options
        stock_options: list[tuple[pd.DataFrame, float]] = []

        for expiration_date in list(option_expiration_dates):
            stock_option = self._ticker.option_chain(date=expiration_date)
            stock_options.append((stock_option[0], days_until(expiration_date)))
            time.sleep(1)

        self._stock_options = stock_options
        return self._stock_options
        
    def get_stock_earnings(self):
        if self._earnings is not None: return self._earnings
        print('loading stock earnings for: ', self._ticker.ticker)

        earnings_dates = self._ticker.get_earnings_dates()
        if earnings_dates is None: raise ValueError('Can not load earning for stock ticker: ', self._ticker.ticker)
        self._earnings = earnings_dates
        return self._earnings
    
    def get_ticker(self): return self._ticker

# print(StockTicker('MBG.DE').get_ticker().get_info())
# print(StockTicker('MBG.DE').get_ticker()._download_options())

