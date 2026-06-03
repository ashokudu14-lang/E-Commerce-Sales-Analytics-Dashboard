-- Sales by Category
SELECT Category, SUM(Sales) AS TotalSales
FROM sales
GROUP BY Category;

-- Profit by Category
SELECT Category, SUM(Profit) AS TotalProfit
FROM sales
GROUP BY Category;

-- Regional Performance
SELECT Region, SUM(Sales) AS TotalSales, SUM(Profit) AS TotalProfit
FROM sales
GROUP BY Region;
