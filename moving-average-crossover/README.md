# Moving Average Crossover Strategy

## 📈 Summary

A trend-following strategy based on the crossover of two Simple Moving Averages (SMA).

- **Short SMA (50-day)**
- **Long SMA (200-day)**

A **Golden Cross** occurs when the short SMA crosses above the long SMA → **Buy signal**.  
A **Death Cross** occurs when the short SMA crosses below the long SMA → **Sell signal**.

---

## 🧮 Formula

$$
\text{SMA}_n(t) = \frac{1}{n} \sum_{i=0}^{n-1} P(t - i)
$$

Where:
- \( P(t) \) is the price at time \( t \)
- \( n \) is the window size (e.g., 50, 200)

---

## 🧠 Status

✅ Strategy implemented  
❌ Signal generation  
❌ Backtesting  
❌ Performance metrics

---

## 🛠️ How to Run

```bash
python3 strategy.py