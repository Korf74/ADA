SELECT ActionGeo_CountryCode, MonthYear  ,EventRootCode ,Count(NumArticles) as Nb_Events, SUM(NumArticles) as Sum_Articles
FROM [gdelt-bq:full.events] 
WHERE ( ActionGeo_CountryCode IN ('AF','SY','IZ','MX', 'PK')) AND 
      (EventRootCode == "18" OR EventRootCode == "19" OR EventRootCode  == "20") AND 
      (Year > 1999 AND Year  < 2017)
GROUP BY ActionGeo_CountryCode, MonthYear  , EventRootCode
ORDER BY Sum_Articles Desc