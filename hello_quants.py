import numpy as np
import pandas as pd

def main():
    print("🚀 QuantsプロジェクトのPython環境が正常に起動しました！")
    
    # 簡単なダミーデータ（株価のイメージ）を作成
    dates = pd.date_range("20240101", periods=5)
    prices = np.array([100, 102, 101, 105, 108])
    
    # データをPandasのDataFrame（表形式）にまとめる
    df = pd.DataFrame(prices, index=dates, columns=["Price"])
    
    print("\n📊 サンプルデータ（直近5日間の価格推移）:")
    print(df)
    
    print("\n📈 基本統計量:")
    print(f"平均価格: {df['Price'].mean()}")
    print(f"最大価格: {df['Price'].max()}")

if __name__ == "__main__":
    main()
