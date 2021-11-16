CREATE VIEW V_PROCESSED  AS
SELECT  inf.region_1 AS "Страна, где находится биржа",
		inf.index_1 AS "Индекс биржи",
        MONTHNAME(proc.date_1) AS "Месяц" ,
        YEAR(proc.date_1) AS "Год",
        MAX(proc.open_1) AS "Максимальная цена в момент даты открытия",
        MIN(proc.low_1) AS "Минимальная цена во время для торговли",
        inf.currency_1 AS "Валюта",
        inf.exchange_1 AS "Название биржи"
FROM processed_csv proc
	    INNER JOIN info_csv inf ON inf.index_1=proc.index_1
GROUP BY proc.index_1, YEAR(proc.date_1), MONTH(proc.date_1)