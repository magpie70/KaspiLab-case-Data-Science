CREATE VIEW V_NOTPROCESSED  AS
SELECT  dat.key_id AS "Ключ", 
		inf.index_1 AS "Индекс биржи", 
        inf.region_1 AS "Страна, где находится биржа",
        COUNT(dat.index_1) AS "Количество строк"
FROM data_csv dat
	 LEFT JOIN processed_csv proc ON proc.key_id = dat.key_id
     LEFT JOIN info_csv inf ON inf.index_1 = dat.index_1
     WHERE proc.key_id IS NULL
group by dat.index_1
