-- noinspection SqlNoDataSourceInspection
SELECT
-- trazendo os estados para filtrar em relação a eles
t2.descUF,
-- média
avg(Receita) AS avgReceita,
-- mediana
median(Receita) AS medianReceita,
-- primeiro e terceito quartil
percentile(Receita, 0.25) AS Quartil1Receita,
percentile(Receita, 0.75) AS Quartil3Receita,
-- variancia
var_pop(Receita) AS varReceita,
-- desvio padrão
stddev_pop(Receita) AS stdReceita,
-- amplitude
max(Receita) - min(Receita) AS amplitudeReceita,

avg(Frequencia) AS avgFrequencia,
median(Frequencia) AS medianFrequencia,
percentile(Frequencia, 0.25) AS Quartil1Frequencia,
percentile(Frequencia, 0.75) AS Quartil3Frequencia

FROM sandbox.teomewhy.vendedores_fv AS t1

LEFT JOIN silver.olist.vendedor AS t2
ON t1.idVendedor = t2.idVendedor

GROUP BY ALL
